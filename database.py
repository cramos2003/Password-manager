import sys
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class Database(QSqlDatabase, QSqlQuery):
    def __init__(self):
        super().__init__()
        self.makeConnection()
        if not self.connection.open():
            print('error connecting to database')
            sys.exit(1)
        self.createTables()

    def makeConnection(self):
        self.connection = QSqlDatabase.addDatabase('QSQLITE')
        self.connection.setDatabaseName('credentials.sqlite')
        con = self.connection.open()
        if not self.connection.open():
            return False
        else:
            return True

    def createTables(self):
        createTableQuery = QSqlQuery()
        executed = createTableQuery.exec(
            """
                CREATE TABLE credentials(
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    app VARCHAR(255) NOT NULL,
                    username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    active INTEGER NOT NULL
                )
            """
        )

    def insertQuery(self, app, user, pwd):
        # sql for inserting to the credentials table
        query = QSqlQuery()
        query.exec(
            f"""
                INSERT INTO credentials (app, username, password, active)
                VALUES ('{app}', '{user}', '{pwd}', 1)
            """
        )

    def setInactiveQuery(self, app, user, pwd): 
        # sql to change if a credential is being used
        # if no id was passed then execute query based on app, user, and pwd
        query = QSqlQuery()
        query.exec(
                f"""
                    UPDATE credentials SET active = 0
                    WHERE app = '{app}' AND username = '{user}'
                    AND password = '{pwd}' AND active = 1
                """
            )

    def replaceQuery(self, prevapp, prevuser, prevpwd, newapp, newuser, newpwd):
        # sql for replacing an element from the credentials table
        query = QSqlQuery()
        query.exec(
            f"""
                UPDATE credentials SET app = '{newapp}', username = '{newuser}',
                password = '{newpwd}', active = 1
                WHERE app = '{prevapp}' AND username = '{prevuser}' 
                AND password = '{prevpwd}'
            """
        )

    def queryActive(self):
        # sql for selecting ony active elements form the credentials table
        # Loads index of each elemnt for retrieving values
        idIndex, appIndex, userIndex, pwdIndex = range(4)
        # 1 = active or true
        # 0 = inactive or false
        query = QSqlQuery()
        query.exec(
            """
                SELECT * FROM credentials WHERE active = 1
            """
        )
        data = dict()
        while query.next():
            id = query.value(idIndex)
            credentials = {
                'appname':query.value(appIndex),
                'username':query.value(userIndex),
                'password':query.value(pwdIndex)
            }
            data.update({id : credentials})
        return data

    def queryAll(self):
        # sql for selecting all elements from the credentials table
        # Loads index to each of each element to retrieve data
        idIndex, appIndex, userIndex, pwdIndex = range(4)
        query = QSqlQuery()
        query.exec(
            """
                SELECT * FROM credentials
            """
        )
        # Loads values to variable to store and return dictionary values
        data = dict()
        while query.next():
            id = query.value(idIndex)
            credentials = {
                'appname':query.value(appIndex),
                'username':query.value(userIndex),
                'password':query.value(pwdIndex)
            }
            data.update({id : credentials})
        return data