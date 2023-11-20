import os
import sys
import pandas as pd
from PyQt6 import QtCore
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager GUI")
        self.displayLogin()

    def displayLogin(self):
        self.setWindowTitle('Login')
        self.loginScreen = Login(self)
        self.loginScreen.loginBtn.clicked.connect(self.logIn)

    def displayUserData(self):
        self.setWindowTitle('User Logged In')
        self.userData = UserData(self)
        self.userData.addCredsBtn.clicked.connect(self.displayAddCreds)
        self.userData.editCredBtn.clicked.connect(self.editCreds)

        # these 2 lines retrieve and display data file contents within the list widget 
        # to display all user credentials
        df = FileManipulation.retrieveFileItems(self)
        self.userData.mainList.addItems(df)

    def displayAddCreds(self):
        self.setWindowTitle('Add Credentials')
        self.addNewCreds = AddNewCreds(self)
        self.addNewCreds.submitCreds.clicked.connect(self.add)
        self.addNewCreds.backBtn.clicked.connect(self.displayUserData)

    def displayReplaceCreds(self):
        self.setWindowTitle('Replace Existing Credentials')
        self.replaceCreds = AddNewCreds(self)
        self.replaceCreds.submitCreds.clicked.connect(self.confirmEdit)
        self.replaceCreds.backBtn.clicked.connect(self.displayUserData)

    def logIn(self):
        # grab inputs from textboxes
        user, pwd = self.loginScreen.getInputs()

        # must validate login credentials are valid
        isValid = InputValidation.validate(self, user, pwd)
        if isValid == False:
            self.loginScreen.header.setText('Invalid Login Credentials Were Input Please Input Correct Credentials')
            return
        
        elif isValid == True:
                self.displayUserData()

        else:
            return
        
    def add(self):
        # gather input from form to add new credentials
        siteName, username, pwd = self.addNewCreds.getInputs()

        # sets isValid to true if credentials are valid else false
        isValid = InputValidation.validateNewCredentials(self, siteName, username, pwd)

        # if isValid is false change header to error message and propts user to retry
        if isValid == False:
            self.addNewCreds.header.setText('Something Went Wrong, Please Fill All Input Elements')
            return
        # if isValid is true then input is saved to data file and displays user data screen with
        # updated file contents
        elif isValid == True:
            # add user inputs to file if valid
            FileManipulation.saveItems(self, siteName, username, pwd)
            self.displayUserData()
        
        # stops funciton call due to other unexpected error with isValid not returning a true or
        # false value
        else:
            return

    def editCreds(self):
        # gets clicked list item for user to edit credentials for
        self.credential = self.userData.mainList.currentItem().text()

        # sections out credential to have only site user and password 
        self.credential = InputFormatting.formatCredentials(self, self.credential)

        self.displayReplaceCreds()

        # sets input fields to previous credential values to be updated or changed
        self.replaceCreds.websiteInput.setText(self.credential[0])
        self.replaceCreds.unInput.setText(self.credential[1])
        self.replaceCreds.pwdInput.setText(self.credential[2])

    def confirmEdit(self):
        # pretty much the same as the add function inside the Window class (aka. add function above)
        site, user, pwd = self.replaceCreds.getInputs()
        
        isValid = InputValidation.validateNewCredentials(self, site, user, pwd)

        if isValid == False:
            self.replaceCreds.header.setText('Something Went Wrong, Please Fill All Input Elements')
            return
        
        elif isValid == True:
            # main difference in function opposed to add this operation finds and replaces
            # the credentials within the data file
            FileManipulation.replaceCredentials(self, self.credential[0], self.credential[1],
                                                self.credential[2], site, user, pwd)
            self.displayUserData()
            
        else:
            return

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

class UserData(QWidget):
    def __init__(self, parent):
        super().__init__()
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

class AddNewCreds(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.createWidgets(parent)

    def createWidgets(self, parent):
        layout = QVBoxLayout()

        self.header = QLabel('Please Enter New Credentials With The Belo Inputs')
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

class InputValidation():
    def validate(self, username, password):
        USR = 'Christian'
        PWD = 'Password101'

        # if log in credentials match then return true else return false
        if username == USR and password == PWD:
            return True
        else:
            return False
        
    def validateNewCredentials(self, site, username, password):
        # if any input is empty then return false if they aren't empty return true
        if site == '' or username == '' or password == '':
            return False
        else:
            return True

class FileManipulation():
    def saveItems(self, site, username, password):
        df = pd.DataFrame(
            {
                'Website':[site],
                'Username':[username],
                'Password':[password]
            }
        )
        df.to_csv(file, mode='a', index=False, header=False)

    def retrieveFileItems(self):
        df = pd.read_csv(file)
        
        # converts to list of strings to return to display to list widget item within UserData class
        df = FileManipulation.convertFileData(self, df)
        return df
    
    def convertFileData(self, df):
        # converts dataframe df to list of strings formatted to display to list widget item 
        # inside UserData class
        items = list()
        sites = df['Website'].to_list()
        unames = df['Username'].to_list()
        pwds = df['Password'].to_list()

        for i in range(0, len(sites)):
            items.append(f'{sites[i]}\n\t{unames[i]}\n\t{pwds[i]}')
        return items
    
    def replaceCredentials(self, pSite, pUser, pPwd, nSite, nUser, nPwd):
        fileDf = pd.read_csv(file)

        # finds row with previous credentials and replaces it with new credentials
        fileDf.loc[(fileDf['Website'] == pSite) & (fileDf['Username'] == pUser) & (fileDf['Password'] == pPwd)] = [nSite, nUser, nPwd]
        fileDf.to_csv(file, mode='w', index=False, header=True)

class InputFormatting():
    def formatCredentials(self, credentials):
        # splits credentials to return list with [sitename, username, password] without whitespace
        credentials = credentials.split("\n")
        credentials[1] = credentials[1].strip()
        credentials[2] = credentials[2].strip()
        return credentials
    
# CODEBLOCK WILL CONNECT OR CREATE A CSV FILE IN PLACE OF A DATABASE FOR NOW
file = 'pwdData.csv'

# if file path exists then print path otherwise create dataframe to create pwdData.csv file and format it
if os.path.exists(file) == True:
    print(f'Path To: {file}, exists')
else:
    print(f'Path To: {file}, doesnt exist. File Is being created')
    df = pd.DataFrame(
        {
            'Website':[],
            'Username':[],
            'Password':[]
        }
    )
    df.to_csv(file, index=False)

app = QApplication(sys.argv)
GUI = Window()
GUI.show()
app.exec()