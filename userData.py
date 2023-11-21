from PyQt6.QtWidgets import *

class UserData(QWidget):
    def __init__(self, parent):
        super().__init__()
        parent.setGeometry(50, 50, 250, 750)
        self.createWidgets(parent)

    def createWidgets(self, parent):
        layout = QVBoxLayout()
        
        header = QLabel('Welcom, displayed below is all saved login credentials for your apps and sites')
        self.mainList = QListWidget()
        self.addCredsBtn = QPushButton('Add New Credentials')
        self.editCredBtn = QPushButton('Edit')

        layout.addWidget(header)
        layout.addWidget(self.mainList)
        layout.addWidget(self.addCredsBtn)
        layout.addWidget(self.editCredBtn)

        w = QWidget()
        w.setLayout(layout)
        parent.setCentralWidget(w)