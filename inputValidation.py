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