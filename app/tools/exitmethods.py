#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Добавляем методы для подтверждения закрытия диалоговых окон
"""
from PyQt5.QtWidgets import QDialog, QMessageBox

class Dialog(QDialog):

    def closeEvent(self, evnt):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle('Уведомление')
        msg_box.setText('Данные не сохранятся')
        msg_box.setStandardButtons(
            QMessageBox.Yes | QMessageBox.Cancel
        )
        buttonY = msg_box.button(QMessageBox.Yes)
        buttonY.setText('Выйти')
        buttonN = msg_box.button(QMessageBox.Cancel)
        buttonN.setText('Отмена')
        msg_box.exec_()

        if msg_box.clickedButton() == buttonY:
            QDialog.closeEvent(self, evnt)
        elif msg_box.clickedButton() == buttonN:
            evnt.ignore()

    def accept(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle('Уведомление')
        msg_box.setText('Подтвердить ввод данных')
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = msg_box.button(QMessageBox.Yes)
        buttonY.setText('Да')
        buttonN = msg_box.button(QMessageBox.No)
        buttonN.setText('Нет')
        msg_box.exec_()

        if msg_box.clickedButton() == buttonY:
            QDialog.accept(self)
            return True
        else:
            return False