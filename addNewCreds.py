from PyQt6.QtWidgets import *

class AddNewCreds(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.createWidgets(parent)
        parent.setGeometry(150, 150, 250, 500)

    def createWidgets(self, parent):
        layout = QVBoxLayout()

        self.header = QLabel('Please Enter New Credentials Below')
        self.websiteInput = QLineEdit()
        self.websiteInput.setPlaceholderText('Website or app name')
        self.unInput = QLineEdit()
        self.unInput.setPlaceholderText('Username')
        self.pwdInput = QLineEdit()
        self.pwdInput.setPlaceholderText('Password')
        self.submitCreds = QPushButton('Add Credentials')
        self.backBtn = QPushButton('Back')

        layout.addWidget(self.header)
        layout.addWidget(self.websiteInput)
        layout.addWidget(self.unInput)
        layout.addWidget(self.pwdInput)
        layout.addWidget(self.submitCreds)
        layout.addWidget(self.backBtn)

        w = QWidget()
        w.setLayout(layout)
        parent.setCentralWidget(w)

    def getInputs(self):
        siteName = self.websiteInput.text()
        username = self.unInput.text()
        pwd = self.pwdInput.text()
        return siteName, username, pwd