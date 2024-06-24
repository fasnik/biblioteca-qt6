# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterCheckOutQWAwxQ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_RegisterChechOut(object):
    def setupUi(self, RegisterChechOut):
        if not RegisterChechOut.objectName():
            RegisterChechOut.setObjectName(u"RegisterChechOut")
        RegisterChechOut.resize(498, 367)
        self.centralWidget = QWidget(RegisterChechOut)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setGeometry(QRect(0, 0, 491, 361))
        self.mainWidget = QVBoxLayout(self.centralWidget)
        self.mainWidget.setObjectName(u"mainWidget")
        self.name_lbl = QLabel(self.centralWidget)
        self.name_lbl.setObjectName(u"name_lbl")

        self.mainWidget.addWidget(self.name_lbl)

        self.lineEdit = QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.mainWidget.addWidget(self.lineEdit)

        self.telephone_lbl = QLabel(self.centralWidget)
        self.telephone_lbl.setObjectName(u"telephone_lbl")

        self.mainWidget.addWidget(self.telephone_lbl)

        self.lineEdit_2 = QLineEdit(self.centralWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.mainWidget.addWidget(self.lineEdit_2)

        self.email_lbl = QLabel(self.centralWidget)
        self.email_lbl.setObjectName(u"email_lbl")

        self.mainWidget.addWidget(self.email_lbl)

        self.lineEdit_3 = QLineEdit(self.centralWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.mainWidget.addWidget(self.lineEdit_3)

        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")

        self.mainWidget.addWidget(self.label)

        self.lineEdit_4 = QLineEdit(self.centralWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.mainWidget.addWidget(self.lineEdit_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainWidget.addItem(self.verticalSpacer)

        self.confirm = QPushButton(self.centralWidget)
        self.confirm.setObjectName(u"confirm")

        self.mainWidget.addWidget(self.confirm)

        self.clear = QPushButton(self.centralWidget)
        self.clear.setObjectName(u"clear")

        self.mainWidget.addWidget(self.clear)

#if QT_CONFIG(shortcut)
        self.name_lbl.setBuddy(self.lineEdit)
        self.telephone_lbl.setBuddy(self.lineEdit_2)
        self.email_lbl.setBuddy(self.lineEdit_3)
        self.label.setBuddy(self.lineEdit_4)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(RegisterChechOut)

        QMetaObject.connectSlotsByName(RegisterChechOut)
    # setupUi

    def retranslateUi(self, RegisterChechOut):
        RegisterChechOut.setWindowTitle(QCoreApplication.translate("RegisterChechOut", u"Form", None))
        self.name_lbl.setText(QCoreApplication.translate("RegisterChechOut", u"Pessoa", None))
        self.telephone_lbl.setText(QCoreApplication.translate("RegisterChechOut", u"Livro", None))
        self.email_lbl.setText(QCoreApplication.translate("RegisterChechOut", u"Data do Empr\u00e9stimo", None))
        self.label.setText(QCoreApplication.translate("RegisterChechOut", u"Data de Devolu\u00e7\u00e3o", None))
        self.confirm.setText(QCoreApplication.translate("RegisterChechOut", u"Registrar", None))
        self.clear.setText(QCoreApplication.translate("RegisterChechOut", u"Cancelar", None))
    # retranslateUi

