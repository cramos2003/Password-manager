import pandas as pd

file = 'pwdData.csv'

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