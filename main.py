# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_per.clicked.connect(self.per)
        self.ui.btn_radix.clicked.connect(self.radix)
        self.ui.btn_change.clicked.connect(self.change)
        self.ui.btn_c.clicked.connect(self.c)
        self.ui.btn_0.clicked.connect(self.num0)
        self.ui.btn_1.clicked.connect(self.num1)
        self.ui.btn_2.clicked.connect(self.num2)
        self.ui.btn_3.clicked.connect(self.num3)
        self.ui.btn_4.clicked.connect(self.num4)
        self.ui.btn_5.clicked.connect(self.num5)
        self.ui.btn_6.clicked.connect(self.num6)
        self.ui.btn_7.clicked.connect(self.num7)
        self.ui.btn_8.clicked.connect(self.num8)
        self.ui.btn_9.clicked.connect(self.num9)
        self.setWindowTitle("My Calculator")

    def num0(self):
        self.ui.tb1.setText(self.ui.tb1.text() + "0")

    def num1(self):
        self.ui.tb1.setText(self.ui.tb1.text() + "1")

    def num2(self):
        self.ui.tb1.setText(self.ui.tb1.text() + "2")

    def num3(self):
        self.ui.tb1.setText(self.ui.tb1.text() + "3")

    def num4(self):
        self.ui.tb1.setText(self.ui.tb1.text() + "4")

    def num5(self):
        self.ui.tb1.setText(self.ui.tb1.text() + "5")

    def num6(self):
        self.ui.tb1.setText(self.ui.tb1.text() + "6")

    def num7(self):
        self.ui.tb1.setText(self.ui.tb1.text() + "7")

    def num8(self):
        self.ui.tb1.setText(self.ui.tb1.text() + "8")

    def num9(self):
        self.ui.tb1.setText(self.ui.tb1.text() + "9")

    def radix(self):
        self.ui.tb1.setText(self.ui.tb1.text() + ".")

    def equal(self):
        self.b = float(self.ui.tb1.text())
        if self.op == '+':
            result = self.a + self.b
        elif self.op == '-':
            result = self.a - self.b
        elif self.op == '*':
            result = self.a * self.b
        elif self.op == '/':
            result = self.a / self.b
        elif self.op == '%':
            result = self.a * 0.01
        self.ui.tb1.setText(str(result))

    def sum(self):
        # self.ui.tb1.setText(str(0))
        self.op = '+'
        self.a = int(self.ui.tb1.text())
        self.ui.tb1.clear()

    def sub(self):
        self.op = '-'
        self.a = int(self.ui.tb1.text())
        self.ui.tb1.clear()

    def mul(self):
        self.op = '*'
        self.a = int(self.ui.tb1.text())
        self.ui.tb1.clear()

    def div(self):
        self.op = '/'
        self.a = int(self.ui.tb1.text())
        self.ui.tb1.clear()

    def per(self):
        self.op = '%'
        self.a = int(self.ui.tb1.text())
        self.ui.tb1.clear()

    def c(self):
        self.ui.tb1.clear()

    def change(self):
        self.a = int(self.ui.tb1.text())
        self.a *= -1
        self.ui.tb1.setText(self.a)


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    sys.exit(app.exec_())
