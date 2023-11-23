from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QHeaderView

class UserData(QWidget):
    def __init__(self, parent):
        super().__init__()
        parent.setGeometry(50, 50, 250, 750)
        self.createWidgets(parent)

    def createWidgets(self, parent):
        layout = QVBoxLayout()
        
        self.header = QLabel('Welcom, displayed below is all saved login credentials for your apps and sites')

        self.view = QTableWidget()
        self.view.setColumnCount(3)
        self.view.setHorizontalHeaderLabels(['App', 'User Name', 'Password'])

        for i in range(0, 3): # loop sets all columns to equal sizes of 175
            self.view.setColumnWidth(i, 225)

        self.addCredsBtn = QPushButton('Add New Credentials')
        self.editCredBtn = QPushButton('Edit')

        layout.addWidget(self.header)
        layout.addWidget(self.view)
        layout.addWidget(self.addCredsBtn)
        layout.addWidget(self.editCredBtn)

        w = QWidget()
        w.setLayout(layout)
        parent.setCentralWidget(w)