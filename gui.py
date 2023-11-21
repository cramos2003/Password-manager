import os
import sys
import pandas as pd
from PyQt6 import QtCore
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from login import Login
from userData import UserData
from addNewCreds import AddNewCreds
from inputValidation import InputValidation
from fileOperations import FileManipulation, InputFormatting

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
            self.loginScreen.header.setText('Invalid Login, Please Input Correct Credentials')
            return
        
        elif isValid == True:
                self.displayUserData()

        else:
            self.loginScreen.header.setText('An Unexpected Error Occured, Please try again')
            return
        
    def add(self):
        # gather input from form to add new credentials
        siteName, username, pwd = self.addNewCreds.getInputs()

        # sets isValid to true if credentials are valid else false
        isValid = InputValidation.validateNewCredentials(self, siteName, username, pwd)

        # if isValid is false change header to error message and propts user to retry
        if isValid == False:
            self.addNewCreds.header.setText('Not All Textboxes Are Filled, Please Fill Out All Items To Continue')
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
            self.addNewCreds.header.setText('An Unexpected Error Occured, Please Try Again')
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
            self.replaceCreds.header.setText('Not All Inputs Are Filled, Please Fill In Empty ELements')
            return
        
        elif isValid == True:
            # main difference in function opposed to add this operation finds and replaces
            # the credentials within the data file
            FileManipulation.replaceCredentials(self, self.credential[0], self.credential[1],
                                                self.credential[2], site, user, pwd)
            self.displayUserData()
            
        else:
            self.replaceCreds.header.setText('Unexpected Error Occured, Please Try Again')
            return
