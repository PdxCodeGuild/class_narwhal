from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class ImWindow(QMainWindow):
    def __init__(self):
        super(ImWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Isaac mini Capstone.")
        self.initUI()



    def initUI(self):
         
         self.label = QtWidgets.QLabel(self)
         self.label.setText("Just do it")
         self.label.move(75,75)

         self.b1 = QtWidgets.QPushButton(self)
         self.b1.setText("Push Me")
         self.b1.clicked.connect(self.clicked)


    def clicked(self):
        self.label.setText("You pushed the button")




def window():
        app = QApplication(sys.argv)
        win = ImWindow()
        win.show()
        sys.exit(app.exec_())

window()





