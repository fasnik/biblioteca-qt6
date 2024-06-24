# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BibliotecaMainWindowLnyYRg.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_BibliotecaApp(object):
    def setupUi(self, BibliotecaApp):
        if not BibliotecaApp.objectName():
            BibliotecaApp.setObjectName(u"BibliotecaApp")
        BibliotecaApp.setEnabled(True)
        BibliotecaApp.resize(771, 572)
        self.actionAddUser = QAction(BibliotecaApp)
        self.actionAddUser.setObjectName(u"actionAddUser")
        self.actionAddUser.setCheckable(False)
        self.actionQueryUser = QAction(BibliotecaApp)
        self.actionQueryUser.setObjectName(u"actionQueryUser")
        self.actionQueryUser.setCheckable(False)
        self.actionAddPublicacao = QAction(BibliotecaApp)
        self.actionAddPublicacao.setObjectName(u"actionAddPublicacao")
        self.actionAddPublicacao.setCheckable(False)
        self.actionQueryPublicacao = QAction(BibliotecaApp)
        self.actionQueryPublicacao.setObjectName(u"actionQueryPublicacao")
        self.actionQueryPublicacao.setCheckable(False)
        self.actionregisterCheckOut = QAction(BibliotecaApp)
        self.actionregisterCheckOut.setObjectName(u"actionregisterCheckOut")
        self.actionregisterDevolucao = QAction(BibliotecaApp)
        self.actionregisterDevolucao.setObjectName(u"actionregisterDevolucao")
        self.centralwidget = QWidget(BibliotecaApp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setStyleSheet(u"centralwidget{\n"
"qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))\n"
"}")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 771, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.welcome = QLabel(self.verticalLayoutWidget)
        self.welcome.setObjectName(u"welcome")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome.sizePolicy().hasHeightForWidth())
        self.welcome.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(36)
        self.welcome.setFont(font)
        self.welcome.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.welcome)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        BibliotecaApp.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(BibliotecaApp)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 771, 19))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menuUsuarios = QMenu(self.menubar)
        self.menuUsuarios.setObjectName(u"menuUsuarios")
        self.menuPublicacoes = QMenu(self.menubar)
        self.menuPublicacoes.setObjectName(u"menuPublicacoes")
        self.menuEmprestimos = QMenu(self.menubar)
        self.menuEmprestimos.setObjectName(u"menuEmprestimos")
        BibliotecaApp.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(BibliotecaApp)
        self.statusbar.setObjectName(u"statusbar")
        BibliotecaApp.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuUsuarios.menuAction())
        self.menubar.addAction(self.menuPublicacoes.menuAction())
        self.menubar.addAction(self.menuEmprestimos.menuAction())
        self.menuUsuarios.addAction(self.actionAddUser)
        self.menuUsuarios.addAction(self.actionQueryUser)
        self.menuPublicacoes.addAction(self.actionAddPublicacao)
        self.menuPublicacoes.addAction(self.actionQueryPublicacao)
        self.menuEmprestimos.addAction(self.actionregisterCheckOut)
        self.menuEmprestimos.addAction(self.actionregisterDevolucao)

        self.retranslateUi(BibliotecaApp)

        QMetaObject.connectSlotsByName(BibliotecaApp)
    # setupUi

    def retranslateUi(self, BibliotecaApp):
        BibliotecaApp.setWindowTitle(QCoreApplication.translate("BibliotecaApp", u"Biblioteca Escola X", None))
        self.actionAddUser.setText(QCoreApplication.translate("BibliotecaApp", u"Adicionar Usu\u00e1rio", None))
        self.actionQueryUser.setText(QCoreApplication.translate("BibliotecaApp", u"Consultar Usu\u00e1rio", None))
        self.actionAddPublicacao.setText(QCoreApplication.translate("BibliotecaApp", u"Adicionar Publica\u00e7\u00e3o", None))
        self.actionQueryPublicacao.setText(QCoreApplication.translate("BibliotecaApp", u"Consultar Publica\u00e7\u00e3o", None))
        self.actionregisterCheckOut.setText(QCoreApplication.translate("BibliotecaApp", u"Registrar Empr\u00e9stimo", None))
        self.actionregisterDevolucao.setText(QCoreApplication.translate("BibliotecaApp", u"Fazer Devolu\u00e7\u00e3o", None))
        self.welcome.setText(QCoreApplication.translate("BibliotecaApp", u"Biblioteca App", None))
        self.menuUsuarios.setTitle(QCoreApplication.translate("BibliotecaApp", u"Usu\u00e1rios", None))
        self.menuPublicacoes.setTitle(QCoreApplication.translate("BibliotecaApp", u"Publica\u00e7\u00f5es", None))
        self.menuEmprestimos.setTitle(QCoreApplication.translate("BibliotecaApp", u"Empr\u00e9stimos", None))
    # retranslateUi

