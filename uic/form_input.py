# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_input.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(458, 600)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_prepare = QPushButton(self.centralwidget)
        self.button_prepare.setObjectName(u"button_prepare")
        self.button_prepare.setGeometry(QRect(20, 490, 321, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 150, 30))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 150, 30))
        self.edit_price = QLineEdit(self.centralwidget)
        self.edit_price.setObjectName(u"edit_price")
        self.edit_price.setGeometry(QRect(180, 60, 250, 30))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 100, 150, 30))
        self.edit_name = QLineEdit(self.centralwidget)
        self.edit_name.setObjectName(u"edit_name")
        self.edit_name.setGeometry(QRect(180, 100, 250, 30))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 150, 30))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 250, 150, 30))
        self.edit_phone = QLineEdit(self.centralwidget)
        self.edit_phone.setObjectName(u"edit_phone")
        self.edit_phone.setGeometry(QRect(180, 250, 250, 30))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 290, 150, 30))
        self.edit_id = QLineEdit(self.centralwidget)
        self.edit_id.setObjectName(u"edit_id")
        self.edit_id.setGeometry(QRect(180, 290, 250, 30))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 330, 150, 30))
        self.edit_name_kefil = QLineEdit(self.centralwidget)
        self.edit_name_kefil.setObjectName(u"edit_name_kefil")
        self.edit_name_kefil.setGeometry(QRect(180, 330, 250, 30))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 370, 150, 30))
        self.edit_kefil_id = QLineEdit(self.centralwidget)
        self.edit_kefil_id.setObjectName(u"edit_kefil_id")
        self.edit_kefil_id.setGeometry(QRect(180, 370, 250, 30))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 410, 150, 30))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 450, 150, 30))
        self.edit_amount = QSpinBox(self.centralwidget)
        self.edit_amount.setObjectName(u"edit_amount")
        self.edit_amount.setGeometry(QRect(180, 450, 250, 30))
        self.edit_amount.setValue(1)
        self.date_month = QComboBox(self.centralwidget)
        self.date_month.addItem("")
        self.date_month.addItem("")
        self.date_month.addItem("")
        self.date_month.addItem("")
        self.date_month.addItem("")
        self.date_month.addItem("")
        self.date_month.addItem("")
        self.date_month.addItem("")
        self.date_month.addItem("")
        self.date_month.addItem("")
        self.date_month.addItem("")
        self.date_month.addItem("")
        self.date_month.setObjectName(u"date_month")
        self.date_month.setGeometry(QRect(230, 20, 121, 30))
        self.date_day = QLineEdit(self.centralwidget)
        self.date_day.setObjectName(u"date_day")
        self.date_day.setGeometry(QRect(180, 21, 41, 30))
        self.date_year = QLineEdit(self.centralwidget)
        self.date_year.setObjectName(u"date_year")
        self.date_year.setGeometry(QRect(360, 20, 71, 30))
        self.date_month_2 = QComboBox(self.centralwidget)
        self.date_month_2.addItem("")
        self.date_month_2.addItem("")
        self.date_month_2.addItem("")
        self.date_month_2.addItem("")
        self.date_month_2.addItem("")
        self.date_month_2.addItem("")
        self.date_month_2.addItem("")
        self.date_month_2.addItem("")
        self.date_month_2.addItem("")
        self.date_month_2.addItem("")
        self.date_month_2.addItem("")
        self.date_month_2.addItem("")
        self.date_month_2.setObjectName(u"date_month_2")
        self.date_month_2.setGeometry(QRect(230, 409, 121, 30))
        self.date_year_2 = QLineEdit(self.centralwidget)
        self.date_year_2.setObjectName(u"date_year_2")
        self.date_year_2.setGeometry(QRect(360, 410, 71, 30))
        self.date_day_2 = QLineEdit(self.centralwidget)
        self.date_day_2.setObjectName(u"date_day_2")
        self.date_day_2.setGeometry(QRect(180, 410, 41, 30))
        self.edit_address = QPlainTextEdit(self.centralwidget)
        self.edit_address.setObjectName(u"edit_address")
        self.edit_address.setGeometry(QRect(180, 140, 250, 101))
        self.button_reset = QPushButton(self.centralwidget)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setGeometry(QRect(350, 490, 81, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 458, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_prepare.setText(QCoreApplication.translate("MainWindow", u"Haz\u0131rla", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00d6deme G\u00fcn\u00fc", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"T\u00fcrk Liras\u0131", None))
        self.edit_price.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0130sim - \u00dcnvan", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Adres", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Telefon Numaras\u0131", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TC Numaras\u0131", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Kefil", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Kefil TC Numaras\u0131", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"D\u00fczenleme Tarihi", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ka\u00e7 Ayl\u0131k", None))
        self.date_month.setItemText(0, QCoreApplication.translate("MainWindow", u"Ocak", None))
        self.date_month.setItemText(1, QCoreApplication.translate("MainWindow", u"\u015eubat", None))
        self.date_month.setItemText(2, QCoreApplication.translate("MainWindow", u"Mart", None))
        self.date_month.setItemText(3, QCoreApplication.translate("MainWindow", u"Nisan", None))
        self.date_month.setItemText(4, QCoreApplication.translate("MainWindow", u"May\u0131s", None))
        self.date_month.setItemText(5, QCoreApplication.translate("MainWindow", u"Haziran", None))
        self.date_month.setItemText(6, QCoreApplication.translate("MainWindow", u"Temmuz", None))
        self.date_month.setItemText(7, QCoreApplication.translate("MainWindow", u"A\u011fustos", None))
        self.date_month.setItemText(8, QCoreApplication.translate("MainWindow", u"Eyl\u00fcl", None))
        self.date_month.setItemText(9, QCoreApplication.translate("MainWindow", u"Ekim", None))
        self.date_month.setItemText(10, QCoreApplication.translate("MainWindow", u"Kas\u0131m", None))
        self.date_month.setItemText(11, QCoreApplication.translate("MainWindow", u"Aral\u0131k", None))

        self.date_day.setText(QCoreApplication.translate("MainWindow", u"01", None))
        self.date_year.setText(QCoreApplication.translate("MainWindow", u"2022", None))
        self.date_month_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Ocak", None))
        self.date_month_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u015eubat", None))
        self.date_month_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Mart", None))
        self.date_month_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Nisan", None))
        self.date_month_2.setItemText(4, QCoreApplication.translate("MainWindow", u"May\u0131s", None))
        self.date_month_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Haziran", None))
        self.date_month_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Temmuz", None))
        self.date_month_2.setItemText(7, QCoreApplication.translate("MainWindow", u"A\u011fustos", None))
        self.date_month_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Eyl\u00fcl", None))
        self.date_month_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Ekim", None))
        self.date_month_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Kas\u0131m", None))
        self.date_month_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Aral\u0131k", None))

        self.date_year_2.setText(QCoreApplication.translate("MainWindow", u"2022", None))
        self.date_day_2.setText(QCoreApplication.translate("MainWindow", u"01", None))
        self.button_reset.setText(QCoreApplication.translate("MainWindow", u"S\u0131f\u0131rla", None))
    # retranslateUi

