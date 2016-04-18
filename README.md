iq_suite
============
<img src="https://raw.githubusercontent.com/xaratustrah/iq_suite/master/rsrc/icon.png" width="128">

Collection of code for working with offline complex valued time series data ([inphase and quadrature](https://en.wikipedia.org/wiki/In-phase_and_quadrature_components) or IQ Data) with numpy written in Python. 

![iq_suite](https://raw.githubusercontent.com/xaratustrah/iq_suite/master/rsrc/screenshot.png)

These data are usually results of measurements of quantities in physical experiments in fundamental research or other related fields in science and engineering. These data are usually a result of radio frequency data acquisition systems involving one of the many methods of analog or digital [Hilbert transformation](https://en.wikipedia.org/wiki/Hilbert_transform) for the creation of [analytic signals](https://en.wikipedia.org/wiki/Analytic_signal), which in turn are easily processed in further stages. Applications include particle and fundamental physics, astrophysics, [software defined radio](https://en.wikipedia.org/wiki/Software-defined_radio) and many more.

While the GUI program offers a limited graphical interface to visually inspect the data, the advanced usage allows direct programing using the class file and tools within own scrips or iPython Notebook sessions. The suite offers a extendible structure for adding further methods e.g. in spectral analysis or non-linear time series analysis.

## Code Components

### IQBase class
This class covers all required parameters to handle time domain IQ data and their representation in frequency domain. Cuts, slices etc. are also available. Also a set of windowing functions are available.

### iqtools
Is a collection of commandline tools and additional functions that uses the IQBase class as main data type but additionally offers tools for plotting and accessing the data. Stand alone operation is also possible using
command line arguments.

### iqgui
This is a GUI written using the Qt5 bindings for quick showing of the spectrogram plots for visual analysis or inspection.

## Supported file formats

#### [Tektronix<sup>&reg;</sup>](http://www.tek.com) binary file formats \*.IQT and \*.TIQ

Data format from different generations of real time spectrum analyzers.

#### [National Instruments<sup>&trade;</sup>](http://www.ni.com) \*.TDMS

Data format used in NI's [LabView<sup>&trade;</sup>](http://www.ni.com/labview/). Based on the python library [pyTDMS](http://sourceforge.net/projects/pytdms/) by [Floris van Vugt](http://www.florisvanvugt.com).

#### TCAP \*.DAT files
TCAP file format form the older HP E1430A systems. In this case, the header information is stored in a TXT file, while the data file is stored in blocks of 2GB sequentially. More information can be found in [this PhD thesis](http://www.worldcat.org/oclc/76566695).

#### Audio file \*.WAV

This data format is mostly useful for software defined radio applications. Left and right channels are treated as real and imaginary components respectively, file duration and sampling rate are determined automatically. Memory map is activated to avoid the whole file will be loaded in memory.

#### raw binary \*.BIN, ASCII \*.CSV and \*.TXT 

The binary files begin with a 32-bit integer for sampling rate, followed by a 32-bit float for the center frequency. The rest of the file contains real and imaginary parts each as a 32-bit floats. File size is automatically calculated. All data are little endian. The ASCII files are tab or space separated values with real and imaginary on every line. These data will later be treated as 32-bit floating point numbers. Lines beginning with # are considered as comments and are ignored. Here also the first line contains the a 32-bit integer for sampling rate, followed by a 32-bit float for the center frequency. Such files are used as a result of synthesis signals. For example you can create a synthetic signal like the following: 

    from iqtools import *
    freq = 400 # in Hz
    center = 0 # in Hz
    fs = 10000 # samples per second
    duration = 3 # seconds
    t, x = make_test_signal(freq, fs, duration, nharm=3, noise=False)
    xbar, phase = make_analytical(x)
    write_signal_as_binary('test_signal.bin', xbar, fs, center)
    write_signal_as_ascii('test_signal.bin', xbar, fs, center)

The resulting file can be read by library, or by using **iqgui**.

## Installation and usage

#### Usage under Linux and OSX

Runtime usage without compilation under Linux and OSX is pretty straight forward. Use **pip** to install missing libraries.

#### Building GUI Binary under windows

More general info on installation under Win can be found on this [gist](https://gist.github.com/xaratustrah/4efc5001f1bbcce47e02e2343ba29b87). Additionally following packages where installed using **pip**:

    matplotlib (1.5.1)
    pyTDMS (0.0.3)
    spectrum (0.6.1)

Note that in the current version of the `spectrum`, the file `mtm.py` needs a patch. Replace the following line:

	p = os.path.abspath(os.path.dirname(__file__))

with:

	if hasattr(sys, 'frozen'):
		p = os.path.abspath(os.path.dirname(sys.executable))
	else:
		p = os.path.abspath(os.path.dirname(__file__))
	
then perform the compilation. Note there is also a ready made package for spectrum that can be found [here](https://anaconda.org/carlkl/spectrum).

#### Building OSX App

More general info on installation under OSX can be found on this [gist](https://gist.github.com/xaratustrah/4f1ddb54b94386b4e8c311b905f03396). You also need the packages mentioned above. After making sure the run time version stars without any problems, you may like to build an app. You need to use `py2app`:

    python setup_osx.py py2app
    
Still I encountered a couple of errors which I describe here. I needed to modify this file:

    /opt/local/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/py2app/recipes/pyopengl.py

open it and change `file` to `open`. The after consulting [this post](http://stackoverflow.com/a/32750895/5177935) this file needed to be changed:

    /opt/local/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/macholib/dyld.py

where each instance of `loader_path` was changed to `loader`.


## Acknowledgements
I am thankful to [carlkl](https://github.com/carlkl) for his valuable help in making a stand alone binary under MS Windows and also for fruitful discussions and suggestions.
