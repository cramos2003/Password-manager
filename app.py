import os
import sys
import pandas as pd
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from gui import Window
from fileOperations import file

# CODEBLOCK WILL CONNECT OR CREATE A CSV FILE IN PLACE OF A DATABASE FOR NOW

# if file path exists then print path otherwise create dataframe to create pwdData.csv file and format it
if os.path.exists(file) == True:
    pass
else:
    df = pd.DataFrame(
        {
            'Website':[],
            'Username':[],
            'Password':[]
        }
    )
    df.to_csv(file, index=False)

app = QApplication(sys.argv)
app.setStyle('Fusion') # SETS COLOR SCHEME OF APPLICATION
GUI = Window()
GUI.show()
app.exec()