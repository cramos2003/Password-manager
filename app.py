import sys
import pandas as pd
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from gui import Window
from database import Database

database = Database() # Initializes database

app = QApplication(sys.argv)
app.setStyle('Fusion') # Sets color scheme of application

with open('styles.qss', 'r') as f: # Applys stylesheet to application widgets
    _style = f.read()
    app.setStyleSheet(_style)

GUI = Window()
GUI.show()
app.exec()