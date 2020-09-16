# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Buscardor(object):
    def setupUi(self, Buscardor):
        if not Buscardor.objectName():
            Buscardor.setObjectName(u"Buscardor")
        Buscardor.resize(416, 139)
        Buscardor.setMinimumSize(QSize(416, 139))
        Buscardor.setMaximumSize(QSize(416, 139))
        self.centralwidget = QWidget(Buscardor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 10, 291, 20))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.lblNombre = QLineEdit(self.centralwidget)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(170, 50, 211, 25))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 50, 111, 17))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 90, 80, 25))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 90, 80, 25))
        Buscardor.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Buscardor)
        self.statusbar.setObjectName(u"statusbar")
        Buscardor.setStatusBar(self.statusbar)

        self.retranslateUi(Buscardor)
        self.pushButton.clicked.connect(Buscardor.buscar)
        self.pushButton_2.clicked.connect(Buscardor.borrar)

        QMetaObject.connectSlotsByName(Buscardor)
    # setupUi

    def retranslateUi(self, Buscardor):
        Buscardor.setWindowTitle(QCoreApplication.translate("Buscardor", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Buscardor", u"Tu propio buscador de archivos", None))
        self.label_2.setText(QCoreApplication.translate("Buscardor", u"Nombre del archivo", None))
        self.pushButton.setText(QCoreApplication.translate("Buscardor", u"Buscar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Buscardor", u"Borrar", None))
    # retranslateUi

