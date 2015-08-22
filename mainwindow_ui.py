# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Aug 23 00:09:41 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(310, 10, 771, 521))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mplWidget = MatplotLibWidget(self.groupBox_4)
        self.mplWidget.setObjectName("mplWidget")
        self.gridLayout_3.addWidget(self.mplWidget, 0, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 12, 288, 520))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox_nframes = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_nframes.setMaximum(10000)
        self.spinBox_nframes.setProperty("value", 100)
        self.spinBox_nframes.setObjectName("spinBox_nframes")
        self.gridLayout.addWidget(self.spinBox_nframes, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.spinBox_lframes = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_lframes.setMaximum(10000)
        self.spinBox_lframes.setProperty("value", 1024)
        self.spinBox_lframes.setObjectName("spinBox_lframes")
        self.gridLayout.addWidget(self.spinBox_lframes, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.spinBox_sframes = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_sframes.setMaximum(1500)
        self.spinBox_sframes.setProperty("value", 0)
        self.spinBox_sframes.setObjectName("spinBox_sframes")
        self.gridLayout.addWidget(self.spinBox_sframes, 3, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 4, 0, 1, 1)
        self.comboBox_color = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_color.setObjectName("comboBox_color")
        self.gridLayout.addWidget(self.comboBox_color, 4, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_choose_file = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_choose_file.setObjectName("pushButton_choose_file")
        self.verticalLayout.addWidget(self.pushButton_choose_file)
        self.pushButton_replot = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_replot.setObjectName("pushButton_replot")
        self.verticalLayout.addWidget(self.pushButton_replot)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1091, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionReplot = QtWidgets.QAction(MainWindow)
        self.actionReplot.setObjectName("actionReplot")
        self.actionChoose_file = QtWidgets.QAction(MainWindow)
        self.actionChoose_file.setObjectName("actionChoose_file")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionChoose_file)
        self.menuFile.addAction(self.actionReplot)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "barion"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Plot"))
        self.groupBox.setTitle(_translate("MainWindow", "Navigation"))
        self.label_2.setText(_translate("MainWindow", "No. of frames:"))
        self.label_20.setText(_translate("MainWindow", "Length of frames:"))
        self.label_3.setText(_translate("MainWindow", "Starting frame:"))
        self.label_21.setText(_translate("MainWindow", "Color map:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Actions"))
        self.pushButton_choose_file.setText(_translate("MainWindow", "Choose file"))
        self.pushButton_replot.setText(_translate("MainWindow", "Plot"))
        self.groupBox_2.setTitle(_translate("MainWindow", "File Info"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionReplot.setText(_translate("MainWindow", "Replot"))
        self.actionReplot.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionChoose_file.setText(_translate("MainWindow", "Choose file"))
        self.actionChoose_file.setShortcut(_translate("MainWindow", "Ctrl+O"))

from matplotlibwidget import MatplotLibWidget
