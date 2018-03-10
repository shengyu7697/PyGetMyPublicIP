#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from getpublicip import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(480, 240)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # SIGNAL & SLOT
        self.pushButton.clicked.connect(self.getPublicIP)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Get Public IP GUI", None))
        self.pushButton.setText(_translate("Form", "Get !!!", None))

    def getPublicIP(self):
        self.pushButton.setEnabled(False)
        self.pushButton.setText(_translate("Form", "Processing...", None))

        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText('%s (https://myip.com.tw)' % getMyPublicIP1())
        app.processEvents()
        self.plainTextEdit.appendPlainText('%s (https://www.rus.net.tw/myip.php)' % getMyPublicIP2())
        app.processEvents()
        self.plainTextEdit.appendPlainText('%s (https://api.ipify.org)' % getMyPublicIP3())
        app.processEvents()
        self.plainTextEdit.appendPlainText('%s (https://whatismyipaddress.com)' % getMyPublicIP4())

        self.pushButton.setEnabled(True)
        self.pushButton.setText(_translate("Form", "Get !!!", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
