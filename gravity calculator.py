# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a pyqt5 app with the following attributes:
# - use an App/Window class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function or custom method
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed. 
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 2 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        #set up the app layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(100, 100, 300, 200)

        # make widgets
        self.title = QLabel("Universal Gravity Calculator: ")
        self.grid.addWidget(self.title, 1, 1, 1, 1)

        self.comment = QLabel("All values must be non-zero numbers, not letters or symbols")
        self.grid.addWidget(self.comment, 6, 1, 1, 1)

        self.mass1_label = QLabel("Mass 1(Kg): ")
        self.grid.addWidget(self.mass1_label, 2, 1, 1, 1)

        self.mass1_value = QLineEdit()
        self.grid.addWidget(self.mass1_value, 2, 2, 1, 1)

        self.mass2_label = QLabel("Mass 2(Kg): ")
        self.grid.addWidget(self.mass2_label, 3, 1, 1, 1)

        self.mass2_value = QLineEdit()
        self.grid.addWidget(self.mass2_value, 3, 2, 1, 1)

        self.radius_label = QLabel("Radius(m): ")
        self.grid.addWidget(self.radius_label, 4, 1, 1, 1)

        self.radius_value = QLineEdit()
        self.grid.addWidget(self.radius_value, 4, 2, 1, 1)

        self.calc_button = QPushButton("Calculate")
        self.grid.addWidget(self.calc_button, 5, 1, 1, 2)

        self.answer_value = QLabel("0")
        self.grid.addWidget(self.answer_value, 5, 3, 1, 1)

        # Signals and Slots
        self.calc_button.clicked.connect(self.gravity_calc)

        #style
        style_sheet = "gravity_calc_style.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())


        self.show()
    def gravity_calc(self):
        mass1 = float(self.mass1_value.text())
        mass2 = float(self.mass2_value.text())
        radius = float(self.radius_value.text())
        if mass1 or mass2 or radius == "0":
            self.mass1_value = QLineEdit()
            self.grid.addWidget(self.mass1_value, 2, 2, 1, 1)
            self.mass2_value = QLineEdit()
            self.grid.addWidget(self.mass2_value, 3, 2, 1, 1)
            self.radius_value = QLineEdit()
            self.grid.addWidget(self.radius_value, 4, 2, 1, 1)
        gravity = (6.67e-11) * (mass1 * mass2) / radius **2
        self.answer_value.setText(str(gravity))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())