# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddPublicationQoXbAn.ui'
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

class Ui_AddPublication(object):
    def setupUi(self, AddPublication):
        if not AddPublication.objectName():
            AddPublication.setObjectName(u"AddPublication")
        AddPublication.resize(507, 372)
        self.centralWidget = QWidget(AddPublication)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setGeometry(QRect(0, 0, 491, 361))
        self.mainWidget = QVBoxLayout(self.centralWidget)
        self.mainWidget.setObjectName(u"mainWidget")
        self.name_lbl = QLabel(self.centralWidget)
        self.name_lbl.setObjectName(u"name_lbl")

        self.mainWidget.addWidget(self.name_lbl)

        self.name = QLineEdit(self.centralWidget)
        self.name.setObjectName(u"name")

        self.mainWidget.addWidget(self.name)

        self.year_lbl = QLabel(self.centralWidget)
        self.year_lbl.setObjectName(u"year_lbl")

        self.mainWidget.addWidget(self.year_lbl)

        self.year = QLineEdit(self.centralWidget)
        self.year.setObjectName(u"year")

        self.mainWidget.addWidget(self.year)

        self.autor_lbl = QLabel(self.centralWidget)
        self.autor_lbl.setObjectName(u"autor_lbl")

        self.mainWidget.addWidget(self.autor_lbl)

        self.author = QLineEdit(self.centralWidget)
        self.author.setObjectName(u"author")

        self.mainWidget.addWidget(self.author)

        self.theme_lbl = QLabel(self.centralWidget)
        self.theme_lbl.setObjectName(u"theme_lbl")

        self.mainWidget.addWidget(self.theme_lbl)

        self.theme = QLineEdit(self.centralWidget)
        self.theme.setObjectName(u"theme")

        self.mainWidget.addWidget(self.theme)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainWidget.addItem(self.verticalSpacer)

        self.confirm = QPushButton(self.centralWidget)
        self.confirm.setObjectName(u"confirm")

        self.mainWidget.addWidget(self.confirm)

        self.clear = QPushButton(self.centralWidget)
        self.clear.setObjectName(u"clear")

        self.mainWidget.addWidget(self.clear)

#if QT_CONFIG(shortcut)
        self.name_lbl.setBuddy(self.name)
        self.year_lbl.setBuddy(self.year)
        self.autor_lbl.setBuddy(self.author)
        self.theme_lbl.setBuddy(self.theme)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(AddPublication)

        QMetaObject.connectSlotsByName(AddPublication)
    # setupUi

    def retranslateUi(self, AddPublication):
        AddPublication.setWindowTitle(QCoreApplication.translate("AddPublication", u"Adicionar Publica\u00e7\u00e3o", None))
        self.name_lbl.setText(QCoreApplication.translate("AddPublication", u"Nome", None))
        self.year_lbl.setText(QCoreApplication.translate("AddPublication", u"Ano", None))
        self.autor_lbl.setText(QCoreApplication.translate("AddPublication", u"Autor", None))
        self.theme_lbl.setText(QCoreApplication.translate("AddPublication", u"Tema", None))
        self.confirm.setText(QCoreApplication.translate("AddPublication", u"Adicionar", None))
        self.clear.setText(QCoreApplication.translate("AddPublication", u"Cancelar", None))
    # retranslateUi

