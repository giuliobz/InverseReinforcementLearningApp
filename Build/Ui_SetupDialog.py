# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetupDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetupModel(object):
    def setupUi(self, SetupModel):
        SetupModel.setObjectName("SetupModel")
        SetupModel.resize(952, 494)
        SetupModel.setLayoutDirection(QtCore.Qt.LeftToRight)
        SetupModel.setAutoFillBackground(False)
        self.formLayout = QtWidgets.QFormLayout(SetupModel)
        self.formLayout.setObjectName("formLayout")
        self.env = QtWidgets.QLabel(SetupModel)
        self.env.setObjectName("env")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.env)
        self.minigrid_env = QtWidgets.QComboBox(SetupModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minigrid_env.sizePolicy().hasHeightForWidth())
        self.minigrid_env.setSizePolicy(sizePolicy)
        self.minigrid_env.setObjectName("minigrid_env")
        self.minigrid_env.addItem("")
        self.minigrid_env.addItem("")
        self.minigrid_env.addItem("")
        self.minigrid_env.addItem("")
        self.minigrid_env.addItem("")
        self.minigrid_env.addItem("")
        self.minigrid_env.addItem("")
        self.minigrid_env.addItem("")
        self.minigrid_env.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.minigrid_env)
        self.episode_len = QtWidgets.QLabel(SetupModel)
        self.episode_len.setObjectName("episode_len")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.episode_len)
        self.episode_len_line = QtWidgets.QLineEdit(SetupModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.episode_len_line.sizePolicy().hasHeightForWidth())
        self.episode_len_line.setSizePolicy(sizePolicy)
        self.episode_len_line.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.episode_len_line.setText("")
        self.episode_len_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.episode_len_line.setObjectName("episode_len_line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.episode_len_line)
        self.lr = QtWidgets.QLabel(SetupModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lr.sizePolicy().hasHeightForWidth())
        self.lr.setSizePolicy(sizePolicy)
        self.lr.setObjectName("lr")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lr)
        self.lr_line = QtWidgets.QLineEdit(SetupModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lr_line.sizePolicy().hasHeightForWidth())
        self.lr_line.setSizePolicy(sizePolicy)
        self.lr_line.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lr_line.setText("")
        self.lr_line.setMaxLength(32762)
        self.lr_line.setFrame(True)
        self.lr_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lr_line.setClearButtonEnabled(False)
        self.lr_line.setObjectName("lr_line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lr_line)
        self.clips_len = QtWidgets.QLabel(SetupModel)
        self.clips_len.setObjectName("clips_len")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.clips_len)
        self.clips_len_line = QtWidgets.QLineEdit(SetupModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clips_len_line.sizePolicy().hasHeightForWidth())
        self.clips_len_line.setSizePolicy(sizePolicy)
        self.clips_len_line.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.clips_len_line.setText("")
        self.clips_len_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.clips_len_line.setObjectName("clips_len_line")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.clips_len_line)
        self.episodes = QtWidgets.QLabel(SetupModel)
        self.episodes.setObjectName("episodes")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.episodes)
        self.episodes_line = QtWidgets.QLineEdit(SetupModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.episodes_line.sizePolicy().hasHeightForWidth())
        self.episodes_line.setSizePolicy(sizePolicy)
        self.episodes_line.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.episodes_line.setText("")
        self.episodes_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.episodes_line.setObjectName("episodes_line")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.episodes_line)
        self.K = QtWidgets.QLabel(SetupModel)
        self.K.setObjectName("K")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.K)
        self.K_line = QtWidgets.QLineEdit(SetupModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.K_line.sizePolicy().hasHeightForWidth())
        self.K_line.setSizePolicy(sizePolicy)
        self.K_line.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.K_line.setText("")
        self.K_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.K_line.setObjectName("K_line")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.K_line)
        self.label = QtWidgets.QLabel(SetupModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.ok_button = QtWidgets.QDialogButtonBox(SetupModel)
        self.ok_button.setOrientation(QtCore.Qt.Horizontal)
        self.ok_button.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.ok_button.setObjectName("ok_button")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.ok_button)
        self.defaultButton = QtWidgets.QPushButton(SetupModel)
        self.defaultButton.setObjectName("defaultButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.defaultButton)
        self.n_annotations = QtWidgets.QLabel(SetupModel)
        self.n_annotations.setObjectName("n_annotations")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.n_annotations)
        self.n_annotation_line = QtWidgets.QLineEdit(SetupModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_annotation_line.sizePolicy().hasHeightForWidth())
        self.n_annotation_line.setSizePolicy(sizePolicy)
        self.n_annotation_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.n_annotation_line.setObjectName("n_annotation_line")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.n_annotation_line)

        self.retranslateUi(SetupModel)
        self.ok_button.accepted.connect(SetupModel.accept)
        self.ok_button.rejected.connect(SetupModel.reject)
        QtCore.QMetaObject.connectSlotsByName(SetupModel)

    def retranslateUi(self, SetupModel):
        _translate = QtCore.QCoreApplication.translate
        SetupModel.setWindowTitle(_translate("SetupModel", "Setup RL Model"))
        self.env.setText(_translate("SetupModel", "Minigrid env. name"))
        self.minigrid_env.setItemText(0, _translate("SetupModel", "-- none --"))
        self.minigrid_env.setItemText(1, _translate("SetupModel", "MiniGrid-Empty-6x6-v0"))
        self.minigrid_env.setItemText(2, _translate("SetupModel", "MiniGrid-Empty-16x16-v0"))
        self.minigrid_env.setItemText(3, _translate("SetupModel", "MiniGrid-FourRooms-v0"))
        self.minigrid_env.setItemText(4, _translate("SetupModel", "MiniGrid-MultiRoom-N6-v0"))
        self.minigrid_env.setItemText(5, _translate("SetupModel", "MiniGrid-DoorKey-6x6-v0"))
        self.minigrid_env.setItemText(6, _translate("SetupModel", "MiniGrid-DoorKey-16x16-v0"))
        self.minigrid_env.setItemText(7, _translate("SetupModel", "MiniGrid-Dynamic-Obstacle-6x6-v0"))
        self.minigrid_env.setItemText(8, _translate("SetupModel", "MiniGrid-Dynamic-Obstacle-16x16-v0"))
        self.episode_len.setText(_translate("SetupModel", "Trajectory length(Episode length):"))
        self.lr.setText(_translate("SetupModel", "Learning Rate : "))
        self.clips_len.setText(_translate("SetupModel", "Clips length : "))
        self.episodes.setText(_translate("SetupModel", "Train policy Period (Episodes):"))
        self.K.setText(_translate("SetupModel", "Reward Model mini-batch:"))
        self.label.setText(_translate("SetupModel", "<html><head/><body><p>To understand the parameters please see the documentations in the site.</p></body></html>"))
        self.defaultButton.setText(_translate("SetupModel", "Default parameters"))
        self.n_annotations.setText(_translate("SetupModel", "Number of annotations:"))
