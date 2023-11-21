from PyQt6.QtWidgets import *

class Login(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.createWidgets(parent)
        parent.setGeometry(150, 150, 250, 250)

    def createWidgets(self, parent):
        layout = QVBoxLayout()

        self.header = QLabel("Log In To View Saved Credentials")
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