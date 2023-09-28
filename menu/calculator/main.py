import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import display

class ExampleApp(QtWidgets.QMainWindow, display.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        self.period.clicked.connect(lambda: self.write_number(self.period.text()))

        self.ravno.clicked.connect(self.results)
        self.but_clear.clicked.connect(self.clear_results)

    def write_number(self, number):
        if self.label.text() == "0":
            self.label.setText(number)
        else:
            self.label.setText(self.label.text() + number)

    def clear_results(self):
        self.label.setText("0")

    def results(self):
        try:
            result = eval(self.label.text())
            self.label.setText("Результат: " + str(result))
            self.label.setFocus()
        except:
            error_box = QMessageBox()
            error_box.setWindowTitle("Ошибка")
            error_box.setIcon(QMessageBox.Warning)
            error_box.setStandardButtons(QMessageBox.Ok)
            error_box.setInformativeText("При выполнении произошла ошибка!")
            error_box.setText("Не удалось вычислить результат.")
            error_box.exec_()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_0:
            self.write_number('0')
        elif key == Qt.Key_1:
            self.write_number('1')
        elif key == Qt.Key_2:
            self.write_number('2')
        elif key == Qt.Key_3:
            self.write_number('3')
        elif key == Qt.Key_4:
            self.write_number('4')
        elif key == Qt.Key_5:
            self.write_number('5')
        elif key == Qt.Key_6:
            self.write_number('6')
        elif key == Qt.Key_7:
            self.write_number('7')
        elif key == Qt.Key_8:
            self.write_number('8')
        elif key == Qt.Key_9:
            self.write_number('9')
        elif key == Qt.Key_Plus:
            self.write_number('+')
        elif key == Qt.Key_Minus:
            self.write_number('-')
        elif key == Qt.Key_Asterisk:
            self.write_number('*')
        elif key == Qt.Key_Slash:
            self.write_number('/')
        elif key == Qt.Key_ParenLeft:
            self.write_number('(')
        elif key == Qt.Key_ParenRight:
            self.write_number(')')
        elif key == Qt.Key_Enter or key == Qt.Key_Return:
            self.results()
        elif key == Qt.Key_Delete or key == Qt.Key_Backspace:
            self.clear_results()
        elif key == Qt.Key_Period:
            self.write_number('.')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()