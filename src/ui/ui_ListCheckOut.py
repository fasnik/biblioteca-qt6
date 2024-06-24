# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListCheckOutZEjfqg.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QHeaderView, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_ListCheckOut(object):
    def setupUi(self, ListCheckOut):
        if not ListCheckOut.objectName():
            ListCheckOut.setObjectName(u"ListCheckOut")
        ListCheckOut.resize(561, 371)
        ListCheckOut.setAutoFillBackground(False)
        ListCheckOut.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.centralWidget = QWidget(ListCheckOut)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setGeometry(QRect(0, 0, 561, 371))
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.busca = QLineEdit(self.centralWidget)
        self.busca.setObjectName(u"busca")
        self.busca.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.busca)

        self.pesquisar = QPushButton(self.centralWidget)
        self.pesquisar.setObjectName(u"pesquisar")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.pesquisar.setIcon(icon)
        self.pesquisar.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.pesquisar)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.mainWidget = QTableView(self.centralWidget)
        self.mainWidget.setObjectName(u"mainWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"arial"])
        self.mainWidget.setFont(font)
        self.mainWidget.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.mainWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
#if QT_CONFIG(statustip)
        self.mainWidget.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.mainWidget.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.mainWidget.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.mainWidget.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.mainWidget.setStyleSheet(u"")
        self.mainWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.mainWidget.setAutoScroll(False)
        self.mainWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.mainWidget.setTabKeyNavigation(False)
        self.mainWidget.setProperty("showDropIndicator", False)
        self.mainWidget.setDragDropOverwriteMode(False)
        self.mainWidget.setAlternatingRowColors(True)
        self.mainWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.mainWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.mainWidget.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.mainWidget.setSortingEnabled(True)
        self.mainWidget.horizontalHeader().setStretchLastSection(True)
        self.mainWidget.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_2.addWidget(self.mainWidget)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(ListCheckOut)
        self.busca.returnPressed.connect(self.pesquisar.click)

        self.pesquisar.setDefault(False)


        QMetaObject.connectSlotsByName(ListCheckOut)
    # setupUi

    def retranslateUi(self, ListCheckOut):
        ListCheckOut.setWindowTitle(QCoreApplication.translate("ListCheckOut", u"Empr\u00e9stimos", None))
        self.busca.setPlaceholderText(QCoreApplication.translate("ListCheckOut", u"Buscar", None))
        self.pesquisar.setText(QCoreApplication.translate("ListCheckOut", u"Pesquisar", None))
    # retranslateUi

