# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'synth.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 130, 1011, 571))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_path = QtWidgets.QPushButton(self.tab)
        self.pushButton_path.setGeometry(QtCore.QRect(40, 20, 151, 41))
        self.pushButton_path.setObjectName("pushButton_path")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setGeometry(QtCore.QRect(30, 90, 941, 451))
        self.widget_2.setObjectName("widget_2")
        self.label_sample = QtWidgets.QLabel(self.widget_2)
        self.label_sample.setGeometry(QtCore.QRect(20, 20, 911, 411))
        self.label_sample.setTextFormat(QtCore.Qt.PlainText)
        self.label_sample.setScaledContents(False)
        self.label_sample.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sample.setObjectName("label_sample")
        self.lineEdit_samplepath = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_samplepath.setGeometry(QtCore.QRect(220, 30, 451, 31))
        self.lineEdit_samplepath.setObjectName("lineEdit_samplepath")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_font = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_font.setGeometry(QtCore.QRect(20, 40, 112, 34))
        self.pushButton_font.setObjectName("pushButton_font")
        self.comboBox_font = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_font.setGeometry(QtCore.QRect(140, 40, 161, 31))
        self.comboBox_font.setCurrentText("")
        self.comboBox_font.setObjectName("comboBox_font")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(20, 110, 711, 401))
        self.widget.setObjectName("widget")
        self.pushButton_addfont = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_addfont.setGeometry(QtCore.QRect(330, 40, 112, 34))
        self.pushButton_addfont.setObjectName("pushButton_addfont")
        self.lineEdit_addfont = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_addfont.setGeometry(QtCore.QRect(460, 40, 231, 25))
        self.lineEdit_addfont.setObjectName("lineEdit_addfont")
        self.textEdit_fontlist = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_fontlist.setGeometry(QtCore.QRect(760, 130, 201, 371))
        self.textEdit_fontlist.setObjectName("textEdit_fontlist")
        self.label_font = QtWidgets.QLabel(self.tab_2)
        self.label_font.setGeometry(QtCore.QRect(30, 130, 671, 371))
        self.label_font.setAlignment(QtCore.Qt.AlignCenter)
        self.label_font.setObjectName("label_font")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(760, 100, 68, 19))
        self.label_6.setObjectName("label_6")
        self.pushBotton_clearfont = QtWidgets.QPushButton(self.tab_2)
        self.pushBotton_clearfont.setGeometry(QtCore.QRect(750, 40, 112, 34))
        self.pushBotton_clearfont.setObjectName("pushBotton_clearfont")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_fontsize = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_fontsize.setGeometry(QtCore.QRect(220, 70, 171, 31))
        self.textEdit_fontsize.setObjectName("textEdit_fontsize")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(20, 70, 68, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 68, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 181, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 181, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 181, 41))
        self.label_5.setObjectName("label_5")
        self.textEdit_fontcolor = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_fontcolor.setGeometry(QtCore.QRect(220, 110, 171, 31))
        self.textEdit_fontcolor.setObjectName("textEdit_fontcolor")
        self.textEdit_textnumber = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_textnumber.setGeometry(QtCore.QRect(220, 210, 171, 31))
        self.textEdit_textnumber.setObjectName("textEdit_textnumber")
        self.textEdit_reusenumber = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_reusenumber.setGeometry(QtCore.QRect(220, 170, 171, 31))
        self.textEdit_reusenumber.setObjectName("textEdit_reusenumber")
        self.textEdit_textcontent = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_textcontent.setGeometry(QtCore.QRect(220, 260, 301, 171))
        self.textEdit_textcontent.setObjectName("textEdit_textcontent")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setGeometry(QtCore.QRect(540, 330, 241, 101))
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_textsource = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_textsource.setGeometry(QtCore.QRect(20, 290, 151, 31))
        self.pushButton_textsource.setObjectName("pushButton_textsource")
        self.pushButton_colordialog = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_colordialog.setGeometry(QtCore.QRect(420, 110, 171, 34))
        self.pushButton_colordialog.setObjectName("pushButton_colordialog")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton_data = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_data.setGeometry(QtCore.QRect(30, 40, 171, 51))
        self.pushButton_data.setObjectName("pushButton_data")
        self.pushButton_detectlabel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_detectlabel.setGeometry(QtCore.QRect(250, 40, 261, 51))
        self.pushButton_detectlabel.setObjectName("pushButton_detectlabel")
        self.pushButton_recoglabel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_recoglabel.setGeometry(QtCore.QRect(560, 40, 301, 51))
        self.pushButton_recoglabel.setObjectName("pushButton_recoglabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_path.setText(_translate("MainWindow", "open data path"))
        self.label_sample.setText(_translate("MainWindow", "Sample Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "background preparation"))
        self.pushButton_font.setText(_translate("MainWindow", "choose"))
        self.pushButton_addfont.setText(_translate("MainWindow", "add font"))
        self.label_font.setText(_translate("MainWindow", "Sample Font"))
        self.label_6.setText(_translate("MainWindow", "font list"))
        self.pushBotton_clearfont.setText(_translate("MainWindow", "clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "generate font style"))
        self.label.setText(_translate("MainWindow", "font size"))
        self.label_2.setText(_translate("MainWindow", "font color"))
        self.label_3.setText(_translate("MainWindow", "reuse number per image"))
        self.label_4.setText(_translate("MainWindow", "text number per image"))
        self.label_5.setText(_translate("MainWindow", "text content"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">please enter text with&quot; ;&quot; split , e.g. &quot;test1,test2,test3&quot; ; or you can import an existing text source</span></p></body></html>"))
        self.pushButton_textsource.setText(_translate("MainWindow", "import text source"))
        self.pushButton_colordialog.setText(_translate("MainWindow", "open color palette"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "property setting"))
        self.pushButton_data.setText(_translate("MainWindow", "Generate data"))
        self.pushButton_detectlabel.setText(_translate("MainWindow", "Generate detection label"))
        self.pushButton_recoglabel.setText(_translate("MainWindow", "Generate recognition label"))
