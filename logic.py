import math

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import *
from gui import *


class logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """Connects when buttons are pressed to their corresponding methods"""
        super().__init__()
        self.setupUi(self)
        self.setMaximumWidth(500)
        self.setMinimumWidth(500)
        self.button_equals.clicked.connect(lambda: self.equals())
        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_on.clicked.connect(lambda: self.on())
        self.button_off.clicked.connect(lambda: self.off())
        self.button_delete.clicked.connect(lambda: self.delete())
        self.button_plus.clicked.connect(lambda: self.add())
        self.button_minus.clicked.connect(lambda: self.subtract())
        self.button_multiply.clicked.connect(lambda: self.multiply())
        self.button_divide.clicked.connect(lambda: self.divide())
        self.button_e.clicked.connect(lambda: self.e())
        self.button_pi.clicked.connect(lambda: self.pi())
        self.button_sqrt.clicked.connect(lambda: self.sqrt())
        self.button_power2.clicked.connect(lambda: self.power())
        self.button1.clicked.connect(lambda: self.one())
        self.button2.clicked.connect(lambda: self.two())
        self.button3.clicked.connect(lambda: self.three())
        self.button4.clicked.connect(lambda: self.four())
        self.button5.clicked.connect(lambda: self.five())
        self.button6.clicked.connect(lambda: self.six())
        self.button7.clicked.connect(lambda: self.seven())
        self.button8.clicked.connect(lambda: self.eight())
        self.button9.clicked.connect(lambda: self.nine())
        self.button0.clicked.connect(lambda: self.zero())
        self.button_negative.clicked.connect(lambda: self.negative())
        self.trajectory_button.clicked.connect(lambda: self.trajectory())
        self.distance_button.clicked.connect(lambda: self.distance())
        self.final_speed_button.clicked.connect(lambda: self.final_speed())
        self.initital_speed_button.clicked.connect(lambda: self.initial_speed())
        self.time_button.clicked.connect(lambda: self.airTime())
        self.height_button.clicked.connect(lambda: self.height())
        self.x_speed_button.clicked.connect(lambda: self.x_speed())

        self.stack = []
        self.result = float(0)

    def fillLine(self) -> None:
        """Shows the stack into the display bar"""
        stack_text = ' '.join(map(str, self.stack))
        self.display.setText(stack_text)

    def x_speed(self) -> None:
        """Calculates the horizontal speed"""
        try:
            self.stack.clear()
            x = float(self.x_input.text().strip())
            air_time = float(self.time_input.text().strip())
            vf = x / air_time
            self.push(vf)
            self.fillLine()
            self.error_message.setText("")
        except ValueError:
            self.error_message.setText("Please enter the distance \n"
                                       "and the air air_time")
            self.error_message.setStyleSheet("color: red")

    def initial_speed(self) -> None:
        """Calculates the initial speed"""
        self.stack.clear()
        try:
            vf = float(self.vf_y_input.text().strip())
            air_time = float(self.time_input.text().strip())
            vo = vf + 9.8 * air_time
            if vo < 0:
                self.push(-vo)
            else:
                self.push(vo)
            self.fillLine()
            self.error_message.setText("")
        except ValueError:
            self.error_message.setText("Please enter the final velocity y \n"
                                       "and the air air_time")
            self.error_message.setStyleSheet("color: red")

    def final_speed(self) -> None:
        """Calculates the final speed"""
        self.stack.clear()
        try:
            vo = float(self.initial_y_input.text().strip())
            air_time = float(self.time_input.text().strip())
            final_velocity = vo - 9.8 * air_time
            if final_velocity < 0:
                self.push(-final_velocity)
            else:
                self.push(final_velocity)
            self.fillLine()
            self.error_message.setText("")
        except ValueError:
            self.error_message.setText("Please enter the initial velocity y\n and the air time")
            self.error_message.setStyleSheet("color: red")

    def distance(self) -> None:
        """calculates the horizontal distance"""
        self.stack.clear()
        try:
            vo = float(self.initial_x_input.text().strip())
            air_time = float(self.time_input.text().strip())
            distance = vo * air_time
            self.push(distance)
            self.fillLine()
            self.error_message.setText("")
        except ValueError:
            self.error_message.setText("To calculate max distance enter the\n initial speed x and the air_time")
            self.error_message.setStyleSheet("color: red")

    def height(self) -> None:
        """Calculates the max vertical"""
        self.stack.clear()
        try:
            air_time = float(self.time_input.text().strip())
            voy = float(self.initial_y_input.text().strip())
            initial_height = float(self.height_input.text().strip())
            height = (voy * air_time) - (.5 * 9.8 * math.pow(air_time, 2)) + initial_height
            if height < 0:
                self.push(-height)
            else:
                self.push(height)
            self.fillLine()
            self.error_message.setText("")
        except ValueError:
            self.error_message.setText("To calculate max height enter the initial speed y,\n"
                                       " the air_time, and the initial height")
            self.error_message.setStyleSheet("color: red")

    def airTime(self) -> None:
        """Calculates the air time for the object"""
        self.stack.clear()
        try:
            voy = float(self.initial_y_input.text().strip())
            launch_angle = float(self.launch_input.text().strip())
            air_time = 2 * voy * math.sin(math.radians(launch_angle)) / 9.8
            self.push(air_time)
            self.fillLine()
            self.error_message.setText("")
        except ValueError:
            self.error_message.setText("Enter the initial speed y,"
                                       "\nand the launch angle")
            self.error_message.setStyleSheet("color: red")

    def trajectory(self) -> None:
        """Opens the trajectory side"""
        self.stack.clear()
        self.setMaximumWidth(1000)
        self.setMinimumWidth(1000)

    def delete(self) -> None:
        """Deletes the most recent addition to the stack"""
        if self.stack:
            item = self.stack.pop()
            if isinstance(item, (int, float)):
                if item >= 10:
                    modified_number = int(item // 10)
                    self.push(modified_number)
                else:
                    self.fillLine()
        self.fillLine()

    def off(self) -> None:
        """Turns the program off"""
        self.clear()
        self.display.setText('Powering off')
        QTimer.singleShot(3000, QApplication.quit)

    def on(self) -> None:
        """turns the program on """
        self.display.setText('Ti-Matt is on')

    def add(self) -> None:
        """adds the addition symbol to the stack"""
        self.stack.append('+')
        self.fillLine()

    def subtract(self) -> None:
        """adds the subtraction symbol to the stack"""
        self.stack.append('-')
        self.fillLine()

    def multiply(self) -> None:
        """adds the multiplication symbol to the stack"""
        self.stack.append('*')
        self.fillLine()

    def divide(self) -> None:
        """adds the division symbol to the stack"""
        self.stack.append('/')
        self.fillLine()

    def pi(self) -> None:
        """adds the pi amount to the stack"""
        self.multiply()
        self.push(math.pi)
        self.fillLine()

    def e(self) -> None:
        """adds the e symbol to the stack"""
        self.multiply()
        self.push(math.e)
        self.fillLine()

    def sqrt(self) -> None:
        """adds the sqrt symbol to the stack"""
        if len(self.stack) == 0:
            self.push(1)
        self.stack.append('√')
        self.fillLine()

    def power(self) -> None:
        """adds the power symbol to the stack"""
        self.stack.append('^')
        self.fillLine()

    def zero(self) -> None:
        """adds the number 0 to the stack"""
        self.push(0)
        self.fillLine()

    def one(self) -> None:
        """adds the number 1 to the stack"""
        self.push(1)
        self.fillLine()

    def two(self) -> None:
        """adds the number 2 to the stack"""
        self.push(2)
        self.fillLine()

    def three(self) -> None:
        """adds the number 3 to the stack"""
        self.push(3)
        self.fillLine()

    def four(self) -> None:
        """adds the number 4 to the stack"""
        self.push(4)
        self.fillLine()

    def five(self) -> None:
        """adds the number 5 to the stack"""
        self.push(5)
        self.fillLine()

    def six(self) -> None:
        """adds the number 6 to the stack"""
        self.push(6)
        self.fillLine()

    def seven(self) -> None:
        """adds the number 7 to the stack"""
        self.push(7)
        self.fillLine()

    def eight(self) -> None:
        """adds the number 8 to the stack"""
        self.push(8)
        self.fillLine()

    def nine(self) -> None:
        """adds the number 9 to the stack"""
        self.push(9)
        self.fillLine()

    def equals(self) -> None:
        """pulls all the numbers from the stack and does the proper math"""
        while len(self.stack) != 1:
            if self.stack.__sizeof__() > 2:
                number1 = self.stack.pop()
                token2 = self.stack.pop()
                number2 = self.stack.pop()
                if token2 == '+':
                    self.result = number2 + number1
                elif token2 == '-':
                    self.result = number2 - number1
                elif token2 == '*':
                    self.result = number2 * number1
                elif token2 == '/':
                    if number1 == 0:
                        self.display.setText("Division by zero")
                        return
                    self.result = number2 / number1
                elif token2 == '√':
                    self.result = number2 * math.sqrt(number1)
                elif token2 == '^':
                    self.result = math.pow(number2, number1)
                self.stack.append(self.result)
            if len(self.stack) == 1:
                self.display.setText(str(self.stack[0]))
            else:
                self.display.setText("Invalid expression")

    def clear(self) -> None:
        """Clears everything from the stack"""
        self.display.setText('')
        self.stack.clear()

    def push(self, number) -> None:
        """adds the number of symbol to the stack"""
        if not self.stack or not isinstance(self.stack[-1], int):
            self.stack.append(number)
        else:
            top_element = self.stack.pop()
            combined_number = top_element * 10 + number
            self.stack.append(combined_number)

    def negative(self) -> None:
        """Makes numbers negative"""
        self.push(-self.stack.pop())
        self.fillLine()
