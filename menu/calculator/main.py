import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import display



class ExampleApp(QtWidgets.QMainWindow, display.Ui_MainWindow):
    def __init__(self):
        self.clear = False
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.n0.clicked.connect(lambda: self.write_number(self.n0.text()))
        self.n1.clicked.connect(lambda: self.write_number(self.n1.text()))
        self.n2.clicked.connect(lambda: self.write_number(self.n2.text()))
        self.n3.clicked.connect(lambda: self.write_number(self.n3.text()))
        self.n4.clicked.connect(lambda: self.write_number(self.n4.text()))
        self.n5.clicked.connect(lambda: self.write_number(self.n5.text()))
        self.n6.clicked.connect(lambda: self.write_number(self.n6.text()))
        self.n7.clicked.connect(lambda: self.write_number(self.n7.text()))
        self.n8.clicked.connect(lambda: self.write_number(self.n8.text()))
        self.n9.clicked.connect(lambda: self.write_number(self.n9.text()))
        self.delenie.clicked.connect(lambda: self.write_number(self.delenie.text()))
        self.plus.clicked.connect(lambda: self.write_number(self.plus.text()))
        self.ymnojit.clicked.connect(lambda: self.write_number(self.ymnojit.text()))
        self.minus.clicked.connect(lambda: self.write_number(self.minus.text()))
        self.parenthesis_left.clicked.connect(lambda: self.write_number(self.parenthesis_left.text()))
        self.parenthesis_right.clicked.connect(lambda: self.write_number(self.parenthesis_right.text()))

        self.ravno.clicked.connect(self.results)
        self.but_clear.clicked.connect(self.clear_results)

    def write_number(self, number):
        if self.label.text() == "0":
            self.label.setText(number)
        elif self.clear:
            self.label.setText(number)
            self.clear = False
        else:
            self.label.setText(self.label.text() + number)

    def clear_results(self):
        self.label.setText("0")
    def results(self):
        if not self.clear:
            result = eval(self.label.text())
            self.label.setText("Результат " + str(result))
            self.clear = True
        else:
            error = QMessageBox()

            error.setWindowTitle("Ошибка")
            error.setText("При выполнении произошла ошибка!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.setInformativeText("Два раза не возможно посчитать результат")

            error.exec_()








def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
