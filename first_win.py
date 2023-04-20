#тут будут 3 класса, для каждого окна
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from settings import *
class FirstWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.set_ui()


    def set_appear(self):
        self.setWindowTitle(title)
        self.resize(win_width, win_height)

    def set_ui(self):
        hello = QLabel(txt_hello)
        instruction = QLabel(txt_instruction)
        start_btn = QPushButton(txt_next)
        start_btn.setStyleSheet('''width:10px;height:10px''')
        line = QVBoxLayout()
        line.addWidget(hello)
        line.addWidget(instruction)
        line.addWidget(start_btn, alignment= Qt.AlignCenter)
        self.setLayout(line)