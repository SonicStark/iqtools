#!/usr/bin/env python

"""
Collection of tools for dealing with IQ data. This code converts data in TIQ
format and extracts the data in numpy format

xaratustrah oct-2014
            mar-2015
"""

import os, argparse
from pprint import pprint
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt
import numpy as np
import logging as log
from scipy.signal import hilbert
from scipy.io import wavfile
from pylab import psd


verbose = False


def make_signal(f, fs, l=1, nharm=0, noise=True):
    """Make a sine signal with/without noise."""

    t = np.arange(0, l, 1 / fs)
    x = np.zeros(len(t))
    for i in range(nharm + 2):
        x += np.sin(2 * np.pi * i * f * t)

    if noise:
        x += np.random.normal(0, 1, len(t))
    return t, x


def make_analytical(x):
    """Make an analytical signal from the real signal"""

    yy = hilbert(x)
    ii = np.real(yy)
    qq = np.imag(yy)
    x_bar = np.vectorize(complex)(ii, qq)
    ins_ph = np.angle(x_bar) * 180 / np.pi
    return x_bar, ins_ph


def plot_hilbert(x_bar):
    """Show Hilbert plot."""

    plt.plot(np.real(x_bar), np.imag(x_bar))
    plt.grid(True)
    plt.xlabel('Real Part')
    plt.ylabel('Imag. Part')


def channel_power_dbm(f, p_avg):
    """ Return total power in band in dBm
    Input: average power in Watts
    """
    return get_dbm(np.trapz(p_avg, x=f))


def get_fft_50(x, fs, c, plot=False, filename=''):
    """ Plots the fft of a power signal."""

    n = x.size
    ts = 1.0 / fs
    f = np.fft.fftfreq(n, ts) + c
    v_peak_iq = np.fft.fft(x) / n
    v_rms = abs(v_peak_iq) / np.sqrt(2)
    p_avg = v_rms ** 2 / 50
    p_avg_dbm = 10 * np.log10(p_avg * 1000)
    if plot:
        plt.savefig(filename + '.pdf')
        plt.plot(f, p_avg_dbm, '.')
        plt.xlabel("Frequency [Hz]")
        plt.title(filename)
        plt.ylabel("Power Spectral Density [dBm/Hz]")
        plt.grid(True)
    return f, v_peak_iq, p_avg

def get_fft_1(x, fs, c, plot=False, filename=''):
    """ Plots the fft of a power signal."""

    n = x.size
    ts = 1.0 / fs
    f = np.fft.fftfreq(n, ts) + c
    v_peak_iq = np.fft.fft(x) / n
    v_rms = abs(v_peak_iq) / np.sqrt(2)
    p_avg = v_rms ** 2 / 1
    p_avg_dbm = 10 * np.log10(p_avg * 1000)
    if plot:
        plt.savefig(filename + '.pdf')
        plt.plot(f, p_avg_dbm, '.')
        plt.xlabel("Frequency [Hz]")
        plt.title(filename)
        plt.ylabel("Power Spectral Density [dBm/Hz]")
        plt.grid(True)
    return f, v_peak_iq, p_avg

def plot_pwelch(x, fs, filename='', plot=False):
    p_avg, f = psd(x, NFFT=1024, Fs=fs, noverlap=0)
    plt.xlabel("Frequency [Hz]")
    plt.title(filename)
    plt.ylabel("Power Spectral Density [dB/Hz]")
    plt.grid(True)
    if plot:
        plt.savefig(filename + '.pdf')
    return f, p_avg


def filename_wo_ext(filename):
    """Extracts the filename base"""

    return os.path.splitext(filename)[0]


def save_header(filename, ba):
    """Saves the header byte array into a txt tile."""

    with open(filename + '.xml', 'wb') as f3:
        f3.write(ba)
    log.info("Header saved in an xml file.")


def save_data(filename, dic):
    """Saves the dictionary to a numpy file."""

    np.save(filename + '.npy', dic)


def save_audio(filename, afs, na):
    """ Save the singal as an audio wave """

    wavfile.write(filename_wo_ext(filename) + '.wav', afs, abs(na))


def get_dbm(watt):
    return 10 * np.log10(watt * 1000)


def get_watt(dbm):
    return 10 ** (dbm / 10) / 1000


def read_result_csv(filename):
    p = np.genfromtxt(filename, skip_header=63)
    with open(filename) as f:
        cont = f.readlines()
    for l in cont:
        l = l.split(',')
        if 'Frequency' in l and len (l) == 3:
            center = float(l[1])
        if 'XStart' in l and len (l) == 3:
            start = float(l[1])
        if 'XStop' in l and len (l) == 3:
            stop = float(l[1])
    f = np.linspace(start - center, stop - center, len(p))
    return f, p

def read_data_csv(filename):
    """Reads the CSV data export from the instrument
    """
    data = np.genfromtxt(filename, skip_header=10, delimiter=",")
    data = np.ravel(data).view(dtype='c16')  # has one dimension more, should use ravel
    return data


def read_tiq(filename, nframes=10, lframes=1024, sframes=1):
    """Process the tiq input file.
    Following information are extracted, except Data offset, all other are stored in the dic

    AcquisitionBandwidth
    Frequency
    File name
    Data I and Q [Unit is Volt]
    Data_offset
    DateTime
    NumberSamples
    Resolution Bandwidth
    RFAttenuation (it is already considered in the data scaling, no need to use this value, only for info)
    Sampling Frequency
    Span
    Voltage Scaling
    """

    filesize = os.path.getsize(filename)
    log.info("File size is {} bytes.".format(filesize))

    with open(filename) as f:
        line = f.readline()
    data_offset = int(line.split("\"")[1])

    with open(filename, 'rb') as f:
        ba = f.read(data_offset)

    xml_tree_root = et.fromstring(ba)

    for elem in xml_tree_root.iter(tag='{http://www.tektronix.com}AcquisitionBandwidth'):
        acq_bw = float(elem.text)
    for elem in xml_tree_root.iter(tag='{http://www.tektronix.com}Frequency'):
        center = float(elem.text)
    for elem in xml_tree_root.iter(tag='{http://www.tektronix.com}DateTime'):
        date_time = str(elem.text)
    for elem in xml_tree_root.iter(tag='{http://www.tektronix.com}NumberSamples'):
        number_samples = str(elem.text)
    for elem in xml_tree_root.iter('NumericParameter'):
        if 'name' in elem.attrib and elem.attrib['name'] == 'Resolution Bandwidth' and elem.attrib['pid'] == 'rbw':
            rbw = float(elem.find('Value').text)
    for elem in xml_tree_root.iter(tag='{http://www.tektronix.com}RFAttenuation'):
        rf_att = float(elem.text)
    for elem in xml_tree_root.iter(tag='{http://www.tektronix.com}SamplingFrequency'):
        fs = float(elem.text)
    for elem in xml_tree_root.iter('NumericParameter'):
        if 'name' in elem.attrib and elem.attrib['name'] == 'Span' and elem.attrib['pid'] == 'globalrange':
            span = float(elem.find('Value').text)
    for elem in xml_tree_root.iter(tag='{http://www.tektronix.com}Scaling'):
        scale = float(elem.text)

    log.info("Center {0} Hz, span {1} Hz, sampling frequency {2} scale factor {3}.".format(center, span, fs, scale))
    log.info("Header size {} bytes.".format(data_offset))

    log.info("Proceeding to read binary section, 32bit (4 byte) little endian.")
    total_nbytes = 8 * nframes * lframes  # 8 comes from 2 times 4 byte integer for I and Q
    start_nbytes = 8 * (sframes - 1 ) * lframes
    nframes_tot = int((filesize - data_offset) / 8 / lframes)
    log.info("Total number of frames: {0} = {1}s".format(nframes_tot, (filesize - data_offset) / 8 / fs))
    log.info("Frame length: {0} data points = {1}s".format(lframes, lframes / fs))
    log.info("Frame offset: {0} = {1}s".format(sframes, start_nbytes / fs))
    log.info("Reading {0} frames = {1}s.".format(nframes, total_nbytes / fs))

    head = ba

    with open(filename, 'rb') as f:
        f.seek(data_offset + start_nbytes)
        ba = f.read(total_nbytes)

    # return a numpy array of little endian 8 byte floats (known as doubles)
    ar = np.fromstring(ba, dtype='<i4')  # little endian 4 byte ints.
    ar = ar * scale  # Scale to retreive value in Volts. Augmented assigment does not work here.
    ar = ar.view(dtype='c16')  # reinterpret the bytes as a 16 byte complex number, which consists of 2 doubles.

    log.info("Output complex array has a size of {}.".format(ar.size))
    dict_local = {'center': center, 'number_samples': number_samples, 'fs': fs, 'lframes': lframes, 'data': ar,
                  'nframes_tot': nframes_tot, 'DataTime': date_time, 'rf_att': rf_att, 'span': span, 'acq_bw': acq_bw,
                  'file_name': filename, 'rbw': rbw}

    # in order to read you may use: data = x.item()['data'] or data = x[()]['data'] other wise you get 0-d error
    return dict_local, head


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="Name of the input file.")
    parser.add_argument("-l", "--lframes", nargs='?', type=int, const=1024, default=1024,
                        help="Length of frames, default is 1024.")
    parser.add_argument("-n", "--nframes", nargs='?', type=int, const=10, default=10,
                        help="Number of frames, default is 10.")
    parser.add_argument("-s", "--sframes", nargs='?', type=int, const=1, default=1,
                        help="Starting frame, default is 1.")
    parser.add_argument("-d", "--dic", help="Print dictionary to screen.", action="store_true")
    parser.add_argument("-f", "--fft", help="Plot FFT to file.", action="store_true")
    parser.add_argument("-p", "--psd", help="Plot PSD to file.", action="store_true")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    parser.add_argument("-x", "--xml", help="Write XML header to file.", action="store_true")
    parser.add_argument("-y", "--npy", help="Write dic to NPY file.", action="store_true")

    args = parser.parse_args()
    if args.verbose:
        log.basicConfig(level=log.DEBUG)
        verbose = True

    log.info("File {} passed for processing.".format(args.filename))

    dic, header = read_tiq(args.filename, args.nframes, args.lframes, args.sframes)

    if args.fft:
        log.info('Generating FFT plot.')
        plot_fft(dic['data'], dic['fs'], dic['center'], filename_wo_ext(args.filename) + '_fft', True)

    if args.psd:
        log.info('Generating PSD plot.')
        plot_pwelch(dic['data'], dic['fs'], filename_wo_ext(args.filename) + '_psd', True)

    if args.xml:
        log.info('Saving header into xml file.')
        save_header(filename_wo_ext(args.filename), header)

    if args.npy:
        log.info('Saving data dictionary in numpy format.')
        save_data(filename_wo_ext(args.filename), dic)

    if args.dic:
        log.info('Printing dictionary on the screen.')
        pprint(dic)
    print(dic['data'])
