# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1967, 1451)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upperWidget = QtWidgets.QWidget(self.centralwidget)
        self.upperWidget.setObjectName("upperWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.upperWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.statusLabel = QtWidgets.QLabel(self.upperWidget)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout.addWidget(self.statusLabel, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.upperWidget)
        self.midWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.midWidget.sizePolicy().hasHeightForWidth())
        self.midWidget.setSizePolicy(sizePolicy)
        self.midWidget.setObjectName("midWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.midWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startButton = QtWidgets.QPushButton(self.midWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.loadState = QtWidgets.QPushButton(self.midWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadState.sizePolicy().hasHeightForWidth())
        self.loadState.setSizePolicy(sizePolicy)
        self.loadState.setObjectName("loadState")
        self.horizontalLayout.addWidget(self.loadState)
        self.InitParameters = QtWidgets.QPushButton(self.midWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InitParameters.sizePolicy().hasHeightForWidth())
        self.InitParameters.setSizePolicy(sizePolicy)
        self.InitParameters.setObjectName("InitParameters")
        self.horizontalLayout.addWidget(self.InitParameters)
        self.verticalLayout.addWidget(self.midWidget)
        self.bottonWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottonWidget.sizePolicy().hasHeightForWidth())
        self.bottonWidget.setSizePolicy(sizePolicy)
        self.bottonWidget.setObjectName("bottonWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottonWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.resetState = QtWidgets.QPushButton(self.bottonWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetState.sizePolicy().hasHeightForWidth())
        self.resetState.setSizePolicy(sizePolicy)
        self.resetState.setObjectName("resetState")
        self.horizontalLayout_2.addWidget(self.resetState)
        self.stateLabel = QtWidgets.QLabel(self.bottonWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stateLabel.sizePolicy().hasHeightForWidth())
        self.stateLabel.setSizePolicy(sizePolicy)
        self.stateLabel.setObjectName("stateLabel")
        self.horizontalLayout_2.addWidget(self.stateLabel)
        self.verticalLayout.addWidget(self.bottonWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1967, 34))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Save_state = QtWidgets.QAction(MainWindow)
        self.action_Save_state.setObjectName("action_Save_state")
        self.action_Load_State = QtWidgets.QAction(MainWindow)
        self.action_Load_State.setObjectName("action_Load_State")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.menu_File.addAction(self.action_Save_state)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inverse Reinforcement Learning Tool"))
        self.statusLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Welcome to Reinforcement Learning tool App. </span></p><p><span style=\" font-size:11pt;\">Press &quot;Set starting settings&quot; to initialize the model or &quot;Load checkpoint&quot; to restore last work checkpoint. </span></p><p><span style=\" font-size:11pt;\">Press &quot;Reset loaded checkpoint&quot; to reset the previous loaded checkpoint.</span></p><p><span style=\" font-size:11pt;\">Finally press &quot;Start&quot; to begin work.</span></p><p><br/></p><p><span style=\" font-family:\'inherit\'; font-size:11pt; color:#222222;\">If the model is initialized or loaded, wait for the red text to turn green before press &quot;Start&quot; button.</span></p><p><br/></p></body></html>"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.loadState.setText(_translate("MainWindow", "Load Checkpoint"))
        self.InitParameters.setText(_translate("MainWindow", "Set starting settings"))
        self.resetState.setText(_translate("MainWindow", "Reset model"))
        self.stateLabel.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ff0000;\">MODEL NOT LOAD OR INITIALIZE</span></p></body></html>"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.action_Save_state.setText(_translate("MainWindow", "&Save State"))
        self.action_Load_State.setText(_translate("MainWindow", "&Load State"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.action_About.setText(_translate("MainWindow", "&About"))
