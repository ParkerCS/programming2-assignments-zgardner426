import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.equation = ""
        #layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(10, 10, 300, 500)

        #widgets
        self.answer = QLabel("0")
        self.grid.addWidget(self.answer, 1, 1, 1, 5)

        self.button_ac = QPushButton("AC")
        self.grid.addWidget(self.button_ac, 2, 1, 1, 1)

        self.button_plus_minus = QPushButton("+/-")
        self.grid.addWidget(self.button_plus_minus, 2, 2, 1, 1)

        self.button_percent = QPushButton("%")
        self.grid.addWidget(self.button_percent, 2, 3, 1, 1)

        self.button_division = QPushButton("/")
        self.grid.addWidget(self.button_division, 2, 4, 1, 1)

        self.button7 = QPushButton("7")
        self.grid.addWidget(self.button7, 3, 1, 1, 1)

        self.button8 = QPushButton("8")
        self.grid.addWidget(self.button8, 3, 2, 1, 1)

        self.button9 = QPushButton("9")
        self.grid.addWidget(self.button9, 3, 3, 1, 1)

        self.button_multiplication = QPushButton("x")
        self.grid.addWidget(self.button_multiplication, 3, 4, 1, 1)

        self.button4 = QPushButton("4")
        self.grid.addWidget(self.button4, 4, 1, 1, 1)

        self.button5 = QPushButton("5")
        self.grid.addWidget(self.button5, 4, 2, 1, 1)

        self.button6 = QPushButton("6")
        self.grid.addWidget(self.button6, 4, 3, 1, 1)

        self.button_minus = QPushButton("-")
        self.grid.addWidget(self.button_minus, 4, 4, 1, 1)

        self.button1 = QPushButton("1")
        self.grid.addWidget(self.button1, 5, 1, 1, 1)

        self.button2 = QPushButton("2")
        self.grid.addWidget(self.button2, 5, 2, 1, 1)

        self.button3 = QPushButton("3")
        self.grid.addWidget(self.button3, 5, 3, 1, 1)

        self.button_adition = QPushButton("+")
        self.grid.addWidget(self.button_adition, 5, 4, 1, 1)

        self.button0 = QPushButton("0")
        self.grid.addWidget(self.button0, 6, 1, 1, 2)

        self.button_point = QPushButton(".")
        self.grid.addWidget(self.button_point, 6, 3, 1, 1)

        self.button_equal = QPushButton("=")
        self.grid.addWidget(self.button_equal, 6, 4, 1, 1)


        #signals and slots
        self.button1.clicked.connect(lambda: self.concat("1"))
        self.button2.clicked.connect(lambda: self.concat("2"))
        self.button_adition.clicked.connect(lambda: self.concat(" + "))
        self.button0.clicked.connect(lambda: self.concat("0"))
        self.button_point.clicked.connect(lambda: self.concat("."))
        self.button3.clicked.connect(lambda: self.concat("3"))
        self.button_minus.clicked.connect(lambda: self.concat(" - "))
        self.button6.clicked.connect(lambda: self.concat("6"))
        self.button5.clicked.connect(lambda: self.concat("5"))
        self.button4.clicked.connect(lambda: self.concat("4"))
        self.button_multiplication.clicked.connect(lambda: self.concat(" * "))
        self.button9.clicked.connect(lambda: self.concat("9"))
        self.button8.clicked.connect(lambda: self.concat("8"))
        self.button7.clicked.connect(lambda: self.concat("7"))
        self.button_division.clicked.connect(lambda: self.concat(" / "))
        self.button_equal.clicked.connect(self.equation_eval)
        self.button_equal.setObjectName("equal")
        self.button_ac.clicked.connect(self.all_clear)
        self.button_percent.clicked.connect(self.percent)


        #style
        style_sheet = "calc_style.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())
        #draw
        self.show()

    def concat(self, value):
        self.equation += value
        self.answer.setText(self.equation)

    def equation_eval(self):
        self.answer.setText(str(eval(self.equation)))

    def all_clear(self):
        self.equation = " "
        self.answer.setText(self.equation)

    def percent(self):
        self.answer.setText(str(eval(self.equation) * .01))
    # i don't know why this won't work and have no idea where to start on the +/- thing

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())