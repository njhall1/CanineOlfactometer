# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Panel_Auto3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 782)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1131, 741))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 480, 961, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.TargDist_1 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.TargDist_1.setObjectName("TargDist_1")
        self.TargDist_1.addItem("")
        self.TargDist_1.addItem("")
        self.gridLayout.addWidget(self.TargDist_1, 2, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.Odor3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Odor3.setObjectName("Odor3")
        self.gridLayout.addWidget(self.Odor3, 1, 3, 1, 1)
        self.Odor6 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Odor6.setObjectName("Odor6")
        self.gridLayout.addWidget(self.Odor6, 1, 6, 1, 1)
        self.Odor2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Odor2.setObjectName("Odor2")
        self.gridLayout.addWidget(self.Odor2, 1, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)
        self.Odor1 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Odor1.setObjectName("Odor1")
        self.gridLayout.addWidget(self.Odor1, 1, 1, 1, 1)
        self.EditOdorList = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.EditOdorList.setObjectName("EditOdorList")
        self.gridLayout.addWidget(self.EditOdorList, 1, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 5, 1, 1)
        self.Odor4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Odor4.setObjectName("Odor4")
        self.gridLayout.addWidget(self.Odor4, 1, 4, 1, 1)
        self.Odor5 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Odor5.setObjectName("Odor5")
        self.gridLayout.addWidget(self.Odor5, 1, 5, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 4, 1, 1)
        self.TargDist_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.TargDist_5.setObjectName("TargDist_5")
        self.TargDist_5.addItem("")
        self.TargDist_5.addItem("")
        self.gridLayout.addWidget(self.TargDist_5, 2, 5, 1, 1)
        self.TargDist_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.TargDist_4.setObjectName("TargDist_4")
        self.TargDist_4.addItem("")
        self.TargDist_4.addItem("")
        self.gridLayout.addWidget(self.TargDist_4, 2, 4, 1, 1)
        self.TargDist_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.TargDist_3.setObjectName("TargDist_3")
        self.TargDist_3.addItem("")
        self.TargDist_3.addItem("")
        self.TargDist_3.addItem("")
        self.gridLayout.addWidget(self.TargDist_3, 2, 3, 1, 1)
        self.TargDist_6 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.TargDist_6.setObjectName("TargDist_6")
        self.TargDist_6.addItem("")
        self.TargDist_6.addItem("")
        self.gridLayout.addWidget(self.TargDist_6, 2, 6, 1, 1)
        self.TargDist_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.TargDist_2.setObjectName("TargDist_2")
        self.TargDist_2.addItem("")
        self.TargDist_2.addItem("")
        self.TargDist_2.addItem("")
        self.gridLayout.addWidget(self.TargDist_2, 2, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 3, 0, 1, 1)
        self.OdorWeights_1 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.OdorWeights_1.setObjectName("OdorWeights_1")
        self.OdorWeights_1.addItem("")
        self.OdorWeights_1.addItem("")
        self.OdorWeights_1.addItem("")
        self.gridLayout.addWidget(self.OdorWeights_1, 3, 1, 1, 1)
        self.OdorWeights_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.OdorWeights_2.setObjectName("OdorWeights_2")
        self.OdorWeights_2.addItem("")
        self.OdorWeights_2.addItem("")
        self.OdorWeights_2.addItem("")
        self.OdorWeights_2.addItem("")
        self.gridLayout.addWidget(self.OdorWeights_2, 3, 2, 1, 1)
        self.OdorWeights_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.OdorWeights_3.setObjectName("OdorWeights_3")
        self.OdorWeights_3.addItem("")
        self.OdorWeights_3.addItem("")
        self.OdorWeights_3.addItem("")
        self.OdorWeights_3.addItem("")
        self.gridLayout.addWidget(self.OdorWeights_3, 3, 3, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(230, 20, 761, 371))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.AlertTime = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.AlertTime.setProperty("value", 4.0)
        self.AlertTime.setObjectName("AlertTime")
        self.gridLayout_2.addWidget(self.AlertTime, 4, 1, 1, 1)
        self.WaitforCorrect = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.WaitforCorrect.setObjectName("WaitforCorrect")
        self.WaitforCorrect.addItem("")
        self.WaitforCorrect.addItem("")
        self.gridLayout_2.addWidget(self.WaitforCorrect, 1, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 7, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 5, 2, 1, 1)
        self.HandlerBlind = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.HandlerBlind.setObjectName("HandlerBlind")
        self.HandlerBlind.addItem("")
        self.HandlerBlind.addItem("")
        self.gridLayout_2.addWidget(self.HandlerBlind, 13, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)
        self.OdorPrev = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.OdorPrev.setObjectName("OdorPrev")
        self.OdorPrev.addItem("")
        self.OdorPrev.addItem("")
        self.OdorPrev.addItem("")
        self.OdorPrev.addItem("")
        self.OdorPrev.addItem("")
        self.OdorPrev.addItem("")
        self.OdorPrev.addItem("")
        self.OdorPrev.addItem("")
        self.OdorPrev.addItem("")
        self.gridLayout_2.addWidget(self.OdorPrev, 3, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 2, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 3, 0, 1, 1)
        self.Context = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.Context.setObjectName("Context")
        self.Context.addItem("")
        self.Context.addItem("")
        self.gridLayout_2.addWidget(self.Context, 6, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 1, 2, 1, 1)
        self.RunCorrections = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.RunCorrections.setObjectName("RunCorrections")
        self.RunCorrections.addItem("")
        self.RunCorrections.addItem("")
        self.gridLayout_2.addWidget(self.RunCorrections, 2, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 13, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.Notes = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Notes.setObjectName("Notes")
        self.gridLayout_2.addWidget(self.Notes, 13, 3, 1, 1)
        self.ReinforceBlanks = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.ReinforceBlanks.setObjectName("ReinforceBlanks")
        self.ReinforceBlanks.addItem("")
        self.ReinforceBlanks.addItem("")
        self.ReinforceBlanks.addItem("")
        self.ReinforceBlanks.addItem("")
        self.ReinforceBlanks.addItem("")
        self.ReinforceBlanks.addItem("")
        self.ReinforceBlanks.addItem("")
        self.ReinforceBlanks.addItem("")
        self.ReinforceBlanks.addItem("")
        self.ReinforceBlanks.addItem("")
        self.ReinforceBlanks.addItem("")
        self.gridLayout_2.addWidget(self.ReinforceBlanks, 4, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 10, 3, 1, 1)
        self.GenProbes = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.GenProbes.setObjectName("GenProbes")
        self.GenProbes.addItem("")
        self.GenProbes.addItem("")
        self.GenProbes.addItem("")
        self.GenProbes.addItem("")
        self.GenProbes.addItem("")
        self.gridLayout_2.addWidget(self.GenProbes, 7, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 10, 2, 1, 1)
        self.NumberofTrials = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.NumberofTrials.setObjectName("NumberofTrials")
        self.NumberofTrials.addItem("")
        self.NumberofTrials.addItem("")
        self.NumberofTrials.addItem("")
        self.NumberofTrials.addItem("")
        self.NumberofTrials.addItem("")
        self.NumberofTrials.addItem("")
        self.gridLayout_2.addWidget(self.NumberofTrials, 3, 1, 1, 1)
        self.ReinforceTargets = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.ReinforceTargets.setObjectName("ReinforceTargets")
        self.ReinforceTargets.addItem("")
        self.ReinforceTargets.addItem("")
        self.ReinforceTargets.addItem("")
        self.ReinforceTargets.addItem("")
        self.ReinforceTargets.addItem("")
        self.ReinforceTargets.addItem("")
        self.ReinforceTargets.addItem("")
        self.ReinforceTargets.addItem("")
        self.ReinforceTargets.addItem("")
        self.ReinforceTargets.addItem("")
        self.gridLayout_2.addWidget(self.ReinforceTargets, 5, 3, 1, 1)
        self.TrainingLevel = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.TrainingLevel.setObjectName("TrainingLevel")
        self.TrainingLevel.addItem("")
        self.TrainingLevel.addItem("")
        self.TrainingLevel.addItem("")
        self.TrainingLevel.addItem("")
        self.gridLayout_2.addWidget(self.TrainingLevel, 0, 1, 1, 1)
        self.ExperimenterName = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ExperimenterName.setObjectName("ExperimenterName")
        self.gridLayout_2.addWidget(self.ExperimenterName, 2, 1, 1, 1)
        self.DogName = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.DogName.setObjectName("DogName")
        self.gridLayout_2.addWidget(self.DogName, 1, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 13, 2, 1, 1)
        self.DaySession = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.DaySession.setObjectName("DaySession")
        self.gridLayout_2.addWidget(self.DaySession, 10, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 7, 0, 1, 1)
        self.Session = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.Session.setObjectName("Session")
        self.gridLayout_2.addWidget(self.Session, 7, 1, 1, 1)
        self.TrialTime = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.TrialTime.setProperty("value", 45)
        self.TrialTime.setObjectName("TrialTime")
        self.gridLayout_2.addWidget(self.TrialTime, 6, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 6, 0, 1, 1)
        self.AlertTime_2 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.AlertTime_2.setProperty("value", 0.0)
        self.AlertTime_2.setObjectName("AlertTime_2")
        self.gridLayout_2.addWidget(self.AlertTime_2, 5, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_35.setObjectName("label_35")
        self.gridLayout_2.addWidget(self.label_35, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(540, 390, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.Submit = QtWidgets.QPushButton(self.tab)
        self.Submit.setGeometry(QtCore.QRect(570, 620, 96, 28))
        self.Submit.setObjectName("Submit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.trialNumber = QtWidgets.QLCDNumber(self.tab_2)
        self.trialNumber.setGeometry(QtCore.QRect(490, 50, 201, 91))
        self.trialNumber.setObjectName("trialNumber")
        self.infoLabel = QtWidgets.QLabel(self.tab_2)
        self.infoLabel.setGeometry(QtCore.QRect(380, 160, 471, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.infoLabel.setFont(font)
        self.infoLabel.setObjectName("infoLabel")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(70, 360, 391, 171))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(540, 400, 231, 101))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(870, 410, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.Button1 = QtWidgets.QPushButton(self.tab_3)
        self.Button1.setGeometry(QtCore.QRect(70, 330, 161, 171))
        self.Button1.setObjectName("Button1")
        self.Button2 = QtWidgets.QPushButton(self.tab_3)
        self.Button2.setGeometry(QtCore.QRect(410, 330, 161, 171))
        self.Button2.setObjectName("Button2")
        self.Button3 = QtWidgets.QPushButton(self.tab_3)
        self.Button3.setGeometry(QtCore.QRect(720, 330, 161, 171))
        self.Button3.setObjectName("Button3")
        self.Position1 = QtWidgets.QLabel(self.tab_3)
        self.Position1.setGeometry(QtCore.QRect(70, 220, 141, 101))
        self.Position1.setObjectName("Position1")
        self.Position2 = QtWidgets.QLabel(self.tab_3)
        self.Position2.setGeometry(QtCore.QRect(420, 210, 151, 101))
        self.Position2.setObjectName("Position2")
        self.Position3 = QtWidgets.QLabel(self.tab_3)
        self.Position3.setGeometry(QtCore.QRect(740, 210, 181, 101))
        self.Position3.setObjectName("Position3")
        self.trialNumber_2 = QtWidgets.QLCDNumber(self.tab_3)
        self.trialNumber_2.setGeometry(QtCore.QRect(410, 60, 201, 91))
        self.trialNumber_2.setObjectName("trialNumber_2")
        self.Button4 = QtWidgets.QPushButton(self.tab_3)
        self.Button4.setGeometry(QtCore.QRect(430, 560, 201, 51))
        self.Button4.setObjectName("Button4")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_5)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(210, 130, 741, 251))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.NewOdor_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.NewOdor_1.setObjectName("NewOdor_1")
        self.gridLayout_3.addWidget(self.NewOdor_1, 0, 1, 1, 1)
        self.ResetOdors = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.ResetOdors.setObjectName("ResetOdors")
        self.gridLayout_3.addWidget(self.ResetOdors, 6, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 0, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 1, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 4, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 3, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 2, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_34.setObjectName("label_34")
        self.gridLayout_3.addWidget(self.label_34, 5, 0, 1, 1)
        self.NewOdor_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.NewOdor_2.setObjectName("NewOdor_2")
        self.gridLayout_3.addWidget(self.NewOdor_2, 1, 1, 1, 1)
        self.NewOdor_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.NewOdor_3.setObjectName("NewOdor_3")
        self.gridLayout_3.addWidget(self.NewOdor_3, 2, 1, 1, 1)
        self.NewOdor_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.NewOdor_4.setObjectName("NewOdor_4")
        self.gridLayout_3.addWidget(self.NewOdor_4, 3, 1, 1, 1)
        self.NewOdor_5 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.NewOdor_5.setObjectName("NewOdor_5")
        self.gridLayout_3.addWidget(self.NewOdor_5, 4, 1, 1, 1)
        self.NewOdor_6 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.NewOdor_6.setObjectName("NewOdor_6")
        self.gridLayout_3.addWidget(self.NewOdor_6, 5, 1, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1173, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsave_as_default = QtWidgets.QAction(MainWindow)
        self.actionsave_as_default.setObjectName("actionsave_as_default")
        self.actionset_directory = QtWidgets.QAction(MainWindow)
        self.actionset_directory.setObjectName("actionset_directory")
        self.menuFile.addAction(self.actionsave_as_default)
        self.menuFile.addAction(self.actionset_directory)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.TargDist_5.setCurrentIndex(1)
        self.TargDist_4.setCurrentIndex(1)
        self.TargDist_3.setCurrentIndex(2)
        self.TargDist_6.setCurrentIndex(1)
        self.TargDist_2.setCurrentIndex(1)
        self.OdorPrev.setCurrentIndex(2)
        self.ReinforceBlanks.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TargDist_1.setItemText(0, _translate("MainWindow", "Target"))
        self.TargDist_1.setItemText(1, _translate("MainWindow", "Distractor"))
        self.label_28.setText(_translate("MainWindow", "Target or Distractor"))
        self.label_11.setText(_translate("MainWindow", "Valve 3"))
        self.label_10.setText(_translate("MainWindow", "Valve 2"))
        self.label_22.setText(_translate("MainWindow", "Valve 6"))
        self.label_9.setText(_translate("MainWindow", "Valve 1"))
        self.EditOdorList.setText(_translate("MainWindow", "Edit Odor List?"))
        self.label_21.setText(_translate("MainWindow", "Valve 5"))
        self.label_14.setText(_translate("MainWindow", "Valve 4"))
        self.TargDist_5.setItemText(0, _translate("MainWindow", "Distractor"))
        self.TargDist_5.setItemText(1, _translate("MainWindow", "None"))
        self.TargDist_4.setItemText(0, _translate("MainWindow", "Distractor"))
        self.TargDist_4.setItemText(1, _translate("MainWindow", "None"))
        self.TargDist_3.setItemText(0, _translate("MainWindow", "Target"))
        self.TargDist_3.setItemText(1, _translate("MainWindow", "Distractor"))
        self.TargDist_3.setItemText(2, _translate("MainWindow", "None"))
        self.TargDist_6.setItemText(0, _translate("MainWindow", "Distractor"))
        self.TargDist_6.setItemText(1, _translate("MainWindow", "None"))
        self.TargDist_2.setItemText(0, _translate("MainWindow", "Target"))
        self.TargDist_2.setItemText(1, _translate("MainWindow", "Distractor"))
        self.TargDist_2.setItemText(2, _translate("MainWindow", "Probe"))
        self.label_29.setText(_translate("MainWindow", "Weigths"))
        self.OdorWeights_1.setItemText(0, _translate("MainWindow", "1"))
        self.OdorWeights_1.setItemText(1, _translate("MainWindow", "2"))
        self.OdorWeights_1.setItemText(2, _translate("MainWindow", "3"))
        self.OdorWeights_2.setItemText(0, _translate("MainWindow", "0"))
        self.OdorWeights_2.setItemText(1, _translate("MainWindow", "1"))
        self.OdorWeights_2.setItemText(2, _translate("MainWindow", "2"))
        self.OdorWeights_2.setItemText(3, _translate("MainWindow", "3"))
        self.OdorWeights_3.setItemText(0, _translate("MainWindow", "0"))
        self.OdorWeights_3.setItemText(1, _translate("MainWindow", "1"))
        self.OdorWeights_3.setItemText(2, _translate("MainWindow", "2"))
        self.OdorWeights_3.setItemText(3, _translate("MainWindow", "3"))
        self.WaitforCorrect.setItemText(0, _translate("MainWindow", "No"))
        self.WaitforCorrect.setItemText(1, _translate("MainWindow", "Yes"))
        self.label_19.setText(_translate("MainWindow", "N Generalization Trials"))
        self.label_15.setText(_translate("MainWindow", "Reinforce Targets"))
        self.HandlerBlind.setItemText(0, _translate("MainWindow", "Yes"))
        self.HandlerBlind.setItemText(1, _translate("MainWindow", "No"))
        self.label.setText(_translate("MainWindow", "Dog Name"))
        self.label_2.setText(_translate("MainWindow", "Alert Time"))
        self.OdorPrev.setCurrentText(_translate("MainWindow", "0.8"))
        self.OdorPrev.setItemText(0, _translate("MainWindow", "1.0"))
        self.OdorPrev.setItemText(1, _translate("MainWindow", "0.9"))
        self.OdorPrev.setItemText(2, _translate("MainWindow", "0.8"))
        self.OdorPrev.setItemText(3, _translate("MainWindow", "0.7"))
        self.OdorPrev.setItemText(4, _translate("MainWindow", "0.6"))
        self.OdorPrev.setItemText(5, _translate("MainWindow", "0.5"))
        self.OdorPrev.setItemText(6, _translate("MainWindow", "0.4"))
        self.OdorPrev.setItemText(7, _translate("MainWindow", "0.3"))
        self.OdorPrev.setItemText(8, _translate("MainWindow", "0.2"))
        self.label_20.setText(_translate("MainWindow", "Run corrections?"))
        self.label_17.setText(_translate("MainWindow", "Number of Trials"))
        self.Context.setItemText(0, _translate("MainWindow", "Yes"))
        self.Context.setItemText(1, _translate("MainWindow", "No"))
        self.label_5.setText(_translate("MainWindow", "Use Tones"))
        self.label_16.setText(_translate("MainWindow", "Wait for a Correct Response? "))
        self.RunCorrections.setItemText(0, _translate("MainWindow", "No"))
        self.RunCorrections.setItemText(1, _translate("MainWindow", "Yes"))
        self.label_13.setText(_translate("MainWindow", "Reinforce Blanks"))
        self.label_7.setText(_translate("MainWindow", "Experimenter Name"))
        self.label_23.setText(_translate("MainWindow", "Handler Blind"))
        self.label_12.setText(_translate("MainWindow", "Target Odor Frequency"))
        self.label_4.setText(_translate("MainWindow", "Level"))
        self.ReinforceBlanks.setCurrentText(_translate("MainWindow", "1.00"))
        self.ReinforceBlanks.setItemText(0, _translate("MainWindow", "1.00"))
        self.ReinforceBlanks.setItemText(1, _translate("MainWindow", "0.90"))
        self.ReinforceBlanks.setItemText(2, _translate("MainWindow", "0.80"))
        self.ReinforceBlanks.setItemText(3, _translate("MainWindow", "0.70"))
        self.ReinforceBlanks.setItemText(4, _translate("MainWindow", "0.60"))
        self.ReinforceBlanks.setItemText(5, _translate("MainWindow", "0.50"))
        self.ReinforceBlanks.setItemText(6, _translate("MainWindow", "0.40"))
        self.ReinforceBlanks.setItemText(7, _translate("MainWindow", "0.30"))
        self.ReinforceBlanks.setItemText(8, _translate("MainWindow", "0.20"))
        self.ReinforceBlanks.setItemText(9, _translate("MainWindow", "0.10"))
        self.ReinforceBlanks.setItemText(10, _translate("MainWindow", "0.00"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox.setItemText(1, _translate("MainWindow", "No"))
        self.GenProbes.setItemText(0, _translate("MainWindow", "0"))
        self.GenProbes.setItemText(1, _translate("MainWindow", "2"))
        self.GenProbes.setItemText(2, _translate("MainWindow", "4"))
        self.GenProbes.setItemText(3, _translate("MainWindow", "6"))
        self.GenProbes.setItemText(4, _translate("MainWindow", "8"))
        self.label_24.setText(_translate("MainWindow", "Auto Score Alerts"))
        self.NumberofTrials.setCurrentText(_translate("MainWindow", "10"))
        self.NumberofTrials.setItemText(0, _translate("MainWindow", "10"))
        self.NumberofTrials.setItemText(1, _translate("MainWindow", "20"))
        self.NumberofTrials.setItemText(2, _translate("MainWindow", "30"))
        self.NumberofTrials.setItemText(3, _translate("MainWindow", "40"))
        self.NumberofTrials.setItemText(4, _translate("MainWindow", "50"))
        self.NumberofTrials.setItemText(5, _translate("MainWindow", "60"))
        self.ReinforceTargets.setItemText(0, _translate("MainWindow", "1.0"))
        self.ReinforceTargets.setItemText(1, _translate("MainWindow", "0.9"))
        self.ReinforceTargets.setItemText(2, _translate("MainWindow", "0.8"))
        self.ReinforceTargets.setItemText(3, _translate("MainWindow", "0.7"))
        self.ReinforceTargets.setItemText(4, _translate("MainWindow", "0.6"))
        self.ReinforceTargets.setItemText(5, _translate("MainWindow", "0.5"))
        self.ReinforceTargets.setItemText(6, _translate("MainWindow", "0.4"))
        self.ReinforceTargets.setItemText(7, _translate("MainWindow", "0.3"))
        self.ReinforceTargets.setItemText(8, _translate("MainWindow", "0.2"))
        self.ReinforceTargets.setItemText(9, _translate("MainWindow", "0.1"))
        self.TrainingLevel.setItemText(0, _translate("MainWindow", "3AFC"))
        self.TrainingLevel.setItemText(1, _translate("MainWindow", "GoNoGo"))
        self.TrainingLevel.setItemText(2, _translate("MainWindow", "Threshold"))
        self.TrainingLevel.setItemText(3, _translate("MainWindow", "Control"))
        self.label_26.setText(_translate("MainWindow", "Notes"))
        self.label_6.setText(_translate("MainWindow", "Day Session"))
        self.label_3.setText(_translate("MainWindow", "Session"))
        self.label_18.setText(_translate("MainWindow", "Trial Time (s)"))
        self.label_35.setText(_translate("MainWindow", "Add random alert Time"))
        self.label_8.setText(_translate("MainWindow", "Define Odors"))
        self.Submit.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Session Settings"))
        self.infoLabel.setText(_translate("MainWindow", "Updates"))
        self.label_27.setText(_translate("MainWindow", "Manual Score"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Trial Status"))
        self.Button1.setText(_translate("MainWindow", "Response 1"))
        self.Button2.setText(_translate("MainWindow", "Response 2"))
        self.Button3.setText(_translate("MainWindow", "Response 3"))
        self.Position1.setText(_translate("MainWindow", "TextLabel"))
        self.Position2.setText(_translate("MainWindow", "TextLabel"))
        self.Position3.setText(_translate("MainWindow", "TextLabel"))
        self.Button4.setText(_translate("MainWindow", "No Response"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Manual Score"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Session Statistics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Basic Statistics"))
        self.ResetOdors.setText(_translate("MainWindow", "Re-set Odor Names"))
        self.label_25.setText(_translate("MainWindow", "Valve 1"))
        self.label_30.setText(_translate("MainWindow", "Valve 2"))
        self.label_33.setText(_translate("MainWindow", "Valve 5"))
        self.label_32.setText(_translate("MainWindow", "Valve 4"))
        self.label_31.setText(_translate("MainWindow", "Valve 3"))
        self.label_34.setText(_translate("MainWindow", "Valve 6"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Edit Odors"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionsave_as_default.setText(_translate("MainWindow", "save as default"))
        self.actionset_directory.setText(_translate("MainWindow", "set directory"))

