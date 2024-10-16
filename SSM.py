import subprocess
import random
import time
# Для файловой системы
import os
from os.path import abspath
# Skype
from skpy import Skype
# DB
import sqlite3 as sq
# QT
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QIcon

connection = sq.connect('skype_users.db') # тут подключайте базу данных
cursor = connection.cursor()


# ПОДКЛЮЧАЮСЬ К ЧАТ БОТУ
slogin = Skype("Ваша почта", "Ваш пароль") # тут вставляйте данные учетки скайп

class SSM(object):

    def setupUi(self, Form):

        # Параметры окна приложения
        Form.setObjectName("Form")
        Form.resize(230, 404)
        Form.setMinimumSize(QtCore.QSize(230, 404))
        Form.setMaximumSize(QtCore.QSize(230, 404))
        Form.setBaseSize(QtCore.QSize(207, 404))

        # НАЗВАНИЕ ПРОГРАММЫ
        self.name_programm = QtWidgets.QLabel(parent=Form)
        self.name_programm.setGeometry(QtCore.QRect(10, 10, 211, 31))
        self.name_programm.setObjectName("name_programm")

        # Кому отпарвляем
        self.whom_label = QtWidgets.QLabel(parent=Form)
        self.whom_label.setGeometry(QtCore.QRect(10, 80, 34, 21))
        self.whom_label.setObjectName("whom_label")

        # label "Тип сообщения
        self.type_label = QtWidgets.QLabel(parent=Form)
        self.type_label.setGeometry(QtCore.QRect(10, 50, 31, 16))
        self.type_label.setObjectName("type_label")

        # label "СООБЩЕНИЕ"
        self.message_label = QtWidgets.QLabel(parent=Form)
        self.message_label.setGeometry(QtCore.QRect(10, 110, 211, 20))
        self.message_label.setObjectName("message_label")


        # Кнопка "Отправить"
        self.send_pushButton = QtWidgets.QPushButton(parent=Form)
        self.send_pushButton.setGeometry(QtCore.QRect(10, 370, 211, 21))
        self.send_pushButton.setObjectName("send_pushButton")
        self.send_pushButton.clicked.connect(self.Button_Send)

        # Пишу сообщение
        self.message_textEdit = QtWidgets.QTextEdit(parent=Form)
        self.message_textEdit.setGeometry(QtCore.QRect(10, 140, 211, 190))
        self.message_textEdit.setObjectName("message_textEdit")

        # Кому отправляем сообщение
        self.whom_comboBox = QtWidgets.QComboBox(parent=Form)
        self.whom_comboBox.setGeometry(QtCore.QRect(50, 80, 171, 22))
        self.whom_comboBox.setObjectName("whom_comboBox")
        self.whom_comboBox.addItem("")
        self.whom_comboBox.addItem("")
        self.whom_comboBox.addItem("")
        self.whom_comboBox.addItem("")
        self.whom_comboBox.addItem("")

        # Какой тип сообщения
        self.tupe_comboBox = QtWidgets.QComboBox(parent=Form)
        self.tupe_comboBox.setGeometry(QtCore.QRect(50, 50, 171, 22))
        self.tupe_comboBox.setObjectName("tupe_comboBox")
        self.tupe_comboBox.addItem("")
        self.tupe_comboBox.addItem("")

        # Кнопка отправки файла
        self.filesend_pushButton = QtWidgets.QPushButton(parent=Form)
        self.filesend_pushButton.setGeometry(QtCore.QRect(10, 340, 211, 23))
        self.filesend_pushButton.setObjectName("filesend_pushButton")
        self.filesend_pushButton.clicked.connect(self.Button_Send_File)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):


        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SSM"))
        self.name_programm.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Рассылка Skype</span></p></body></html>"))
        self.whom_label.setText(_translate("Form", "КОМУ"))
        self.type_label.setText(_translate("Form", "ТИП"))
        self.message_label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">СООБЩЕНИЕ</span></p></body></html>"))


        self.tupe_comboBox.setItemText(0, _translate("Form", "СРОЧНО!"))
        self.tupe_comboBox.setItemText(1, _translate("Form", "ВОПРОС?"))

        self.whom_comboBox.setItemText(0, _translate("Form", "ТЕСТОВАЯ ТАБЛИЦА 1"))
        self.whom_comboBox.setItemText(1, _translate("Form", "ТЕСТОВАЯ ТАБЛИЦА 2"))
        self.whom_comboBox.setItemText(2, _translate("Form", "ТЕСТОВАЯ ТАБЛИЦА 3"))
        self.whom_comboBox.setItemText(3, _translate("Form", "ТЕСТОВАЯ ТАБЛИЦА 4"))
        self.whom_comboBox.setItemText(4, _translate("Form", "ТЕСТОВАЯ ТАБЛИЦА 5"))

        self.filesend_pushButton.setText(_translate("Form", "ПРИЛОЖИТЬ ФАЙЛЫ"))

        self.send_pushButton.setText(_translate("Form", "ОТПРАВИТЬ "))

    # Щелкаем на кнопку и открываем доступ к папке для загрузки
    def Button_Send_File(self):

        dir_path = "../Trash_can"
        self.absolute_path = abspath(dir_path)

        if os.path.exists(self.absolute_path):
            subprocess.Popen(['explorer', self.absolute_path])
        else:
            print("Path doesn't exist.")


    # Последнее что нужно будет щелкнуть
    def Button_Send(self):

        self.tupe_comboBox.currentText() # КАКОЙ ТИП СООБЩЕНИЯ
        self.whom_comboBox.currentText() # КОМУ ОТПРАВЛЯЕТСЯ СООБЩЕНИЕ
        self.message_textEdit.toPlainText() # КАКОЕ СООБЩЕНИЕ НАПИСАНО
        self.path = self.absolute_path # ПУТЬ К ПАПКЕ

        # Вьюжен баз данных на основе выбора к пользователя
        x = self.whom_comboBox.currentText()

        # Тут может быть несколько таблиц из базы данных по вашему желанию
        if x == "ТЕСТОВАЯ ТАБЛИЦА 1":
            y = "SELECT login_skype test_group_table_1"
        if x == "ТЕСТОВАЯ ТАБЛИЦА 2":
            y = "SELECT login_skype FROM test_group_table_2"
        if x == "ТЕСТОВАЯ ТАБЛИЦА 3":
            y = "SELECT login_skype FROM test_group_table_3"
        if x == "ТЕСТОВАЯ ТАБЛИЦА 4":
            y = "SELECT login_skype FROM test_group_table_4"
        if x == "ТЕСТОВАЯ ТАБЛИЦА 5":
            y = "SELECT login_skype FROM test_group_table_5"

        # Выбираем всех пользователей
        cursor.execute(y)
        users = cursor.fetchall()
        count = 0

        # Выводим результаты
        for user in users:

            user = str(*user)
            timer = random.randint(4, 7)
            print("\nЧерез", timer, 'секунд сообщение отправится', user)
            time.sleep(timer) # таймер для того чтобы не забанили

            contact = slogin.contacts[user]
            print('\nСообщение отправляется: ', contact, '\n')
            count += 1

            contact.chat.sendMsg(self.tupe_comboBox.currentText())
            contact.chat.sendMsg(self.whom_comboBox.currentText())
            contact.chat.sendMsg(self.message_textEdit.toPlainText())

            # Отправляем все в файле
            for file in os.listdir(self.absolute_path):
                full_path = os.path.join(self.absolute_path, file)
                if os.path.isfile(full_path):
                    contact.chat.sendFile(open(self.absolute_path + '/' + file, "rb"), file)

            cursor.execute(y)
            records = cursor.fetchall()

            print('СООБЩЕНИЕ ОТПРАВИЛОСЬ: ', count, "/", len(records))

            if count == len(records):
                print("\nРАССЫЛКА ДЛЯ", x, "ЗАКОНЧИЛАСЬ")

        # Удаляем все папки в файле
        for file in os.listdir(self.absolute_path):
            full_path = os.path.join(self.absolute_path, file)
            if os.path.isfile(full_path):
                os.remove(os.path.join(self.absolute_path, file))

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Тут я ставлю свою иконку
    icon = QIcon("kot.ico")
    app.setWindowIcon(icon)

    Form = QtWidgets.QWidget()
    ui = SSM()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())