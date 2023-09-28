import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import menu
import subprocess


class ExampleApp(QtWidgets.QMainWindow, menu.Ui_MainWindow):
    def __init__(self):
        self.clear = False
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.b_shah.clicked.connect(self.run_checkers)
        self.b_calculator.clicked.connect(self.run_calculator)

    def run_checkers(self):
        try:
            # Здесь вы указываете команду, которая запустит ваш другой проект
            # Например, если ваш проект находится в файле my_other_project.py:
            subprocess.run(["python3", "GameCheckers/main.py"])

            # Если ваш проект находится в другом файле, замените "my_other_project.py" на соответствующий путьesds
        except Exception as e:
            print(f"Произошла ошибка при выполнении другого проекта: {e}")

    def switch_start_window(self):
        self.stackedWidget.setCurrentIndex(0)

    def run_calculator(self):
        try:
            # Здесь вы указываете команду, которая запустит ваш другой проект
            # Например, если ваш проект находится в файле my_other_project.py:
            subprocess.run(["python3", "calculator/main.py"])

            # Если ваш проект находится в другом файле, замените "my_other_project.py" на соответствующий путьesds
        except Exception as e:
            print(f"Произошла ошибка при выполнении другого проекта: {e}")


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
