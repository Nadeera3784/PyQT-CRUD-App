#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Заводим новых работников
"""
import sys
import os
import employee
import pc
import data
import address
from functions_ import get_or_create
from sqlalchemy import exc
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QMainWindow, QWidget, QTabWidget, QDialog,
                             QPushButton,QToolTip, QAction, QLabel,
                             QLineEdit, QDesktopWidget, QVBoxLayout, QFormLayout,
                             QHBoxLayout, QMessageBox, QFrame, QSplitter, QTextEdit)
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_ui()
        self.display_data()
        self.show()

    def init_ui(self):
        self.set_and_center_the_window(900,900)
        self.setWindowTitle('РАН НИИ')
        self.setWindowIcon(QIcon(r'pics\star.png'))
        
        employee_action = QAction(QIcon(r'pics\employee.png'), 'Employee', self)
        employee_action.triggered.connect(self.add_employee)
        pc_action = QAction(QIcon(r'pics\pc.png'), 'Pc', self)
        pc_action.triggered.connect(self.add_pc)
        adress_action = QAction(QIcon(r'pics\home.png'), 'Adress', self)
        adress_action.triggered.connect(self.add_address)
        refresh_action = QAction(QIcon(r'pics\refresh.png'), 'Refresh', self)
        refresh_action.triggered.connect(self.refresh)
        settings_action = QAction(QIcon(r'pics\settings.png'), 'Settings', self)
        settings_action.triggered.connect(self.settings)
        
        toolbar = self.addToolBar('asdf')
        toolbar.addActions([employee_action, pc_action, adress_action, refresh_action, settings_action])


    def display_data(self):
        test_ = QWidget()
        a = QPushButton('Жми', test_)
        b = QPushButton('Жми', test_)
        c = QPushButton('Жми', test_)
        lay = QVBoxLayout(test_)
        lay.addWidget(a, alignment = Qt.AlignAbsolute)
        lay.addWidget(b)
        lay.addWidget(c)
        tab = QTabWidget()
        tab.addTab(test_, 'Вкладка 1')
        tab.addTab(QLabel('<b>Содержимое вкладки 2</b>'), 'Вкладка 2')
        tab.addTab(QLabel('Содержимое вкладки 3'), 'Вкладка 3')
        self.setCentralWidget(tab)
    
    def add_employee(self):
        session = data.Session()
        try:
            reg_employee_window = employee.RegisterClient(session)
            if reg_pc_window.exec_() == QDialog.Accepted:
                session.commit()
        except exc.IntegrityError:
            session.rollback()
            QMessageBox.critical(self, 'Критическая ошибка', 'Ошибка базы данных. Попробуйте еще раз.')
        else:
            print('Все успешно')
        finally:
            session.close()

    def add_pc(self):
        session = data.Session()
        try:
            reg_pc_window = pc.RegisterPC(session)
            if reg_pc_window.exec_() == QDialog.Accepted:
                session.commit()
        except exc.IntegrityError:
            session.rollback()
            QMessageBox.critical(self, 'Критическая ошибка', 'Ошибка базы данных. Попробуйте еще раз.')
        else:
            print('Все успешно')
        finally:
            session.close()

    def add_address(self):
        session = data.Session()
        try:
            address_window = address.ConfigureAdresses(session)
            if address_window.exec_() == QDialog.Accepted:
                session.commit()
                print("закоммитили")
        except exc.IntegrityError as errmsg:
            print(errmsg)
            session.rollback()
            QMessageBox.critical(self, 'Критическая ошибка', 'Ошибка базы данных. Попробуйте еще раз.')
        else:
            print('Все успешно')
        finally:
            session.close()
    
    def refresh(self):
        self.display_data()

    def settings(self):
        pass

    def set_and_center_the_window(self, x, y):
        """ Задаем окно (x, y), выравниваем по центру экрана """
        self.setFixedSize(x, y)
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())