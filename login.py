from PyQt6.QtWidgets import *

class Login(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.createWidgets(parent)

    def createWidgets(self, parent):
        layout = QVBoxLayout()

        self.header = QLabel("Welcome, Please Enter Login Credentials To View Saved Logins")
        self.unInput = QLineEdit()
        self.unInput.setPlaceholderText('UserName')
        self.pwdInput = QLineEdit()
        self.pwdInput.setPlaceholderText('Password')
        self.loginBtn = QPushButton('Login')

        layout.addWidget(self.header)
        layout.addWidget(self.unInput)
        layout.addWidget(self.pwdInput)
        layout.addWidget(self.loginBtn)

        w = QWidget()
        w.setLayout(layout)
        parent.setCentralWidget(w)

    def getInputs(self):
        un = self.unInput.text()
        pwd = self.pwdInput.text()

        # sets header as an error message if credentials are left empty
        if un == '' or pwd == '':
            self.header.setText('Something Went Wrong, Please Re-enter Login Credentials')
        return un, pwd