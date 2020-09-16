# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resultado.ui'
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


class Ui_Resultado(object):
    def setupUi(self, Resultado):
        if not Resultado.objectName():
            Resultado.setObjectName(u"Resultado")
        Resultado.resize(836, 191)
        self.centralwidget = QWidget(Resultado)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(730, 140, 80, 25))
        self.txtResultado = QTextEdit(self.centralwidget)
        self.txtResultado.setObjectName(u"txtResultado")
        self.txtResultado.setEnabled(True)
        self.txtResultado.setGeometry(QRect(10, 10, 811, 111))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtResultado.sizePolicy().hasHeightForWidth())
        self.txtResultado.setSizePolicy(sizePolicy)
        self.txtResultado.setMinimumSize(QSize(811, 111))
        self.txtResultado.setMaximumSize(QSize(811, 111))
        Resultado.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Resultado)
        self.statusbar.setObjectName(u"statusbar")
        Resultado.setStatusBar(self.statusbar)

        self.retranslateUi(Resultado)
        self.pushButton.clicked.connect(Resultado.cerrar)

        QMetaObject.connectSlotsByName(Resultado)
    # setupUi

    def retranslateUi(self, Resultado):
        Resultado.setWindowTitle(QCoreApplication.translate("Resultado", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("Resultado", u"Cerrar", None))
    # retranslateUi

