import csv


class Account:

    def __init__(self, Idnum, name, yearLvl, course):
        self.Idnum = Idnum
        self.name = name
        self.yearLvl = yearLvl
        self.course = course

    def editId(self, accId):
        self.Idnum = accId
        return 1

    def editName(self, accName):
        self.name = accName
        return 1

    def editYearLvl(self, accYearLvl):
        self.yearLvl = accYearLvl
        return 1

    def editCourse(self, accCourse):
        self.course = accCourse
        return 1


class Student:

    def __init__(self, sysName):
        self.sysName = sysName
        self.numOfStudent = 0
        self.accounts = []

        with open('turno.csv', 'r') as a:
            db = csv.reader(a)
            next(db)
            for row in db:
                self.createAccount(row[0], row[1], row[2], row[3])

    def checkAccount(self, account_Idnumber):
        for account in self.accounts:
            if account.Idnum == account_Idnumber:
                return 0
        return 1

    def createAccount(self, account_Idnumber, account_Name, account_YearLvl, account_Course):
        newAccount = Account(account_Idnumber, account_Name,
                             account_YearLvl, account_Course)
        if not self.checkAccount(account_Idnumber):
            print('bad')
            return 0
        self.accounts.append(newAccount)
        self.numOfStudent += 1
        print("nice")
        return 1

    def getAccount(self, account_Idnumber):
        for account in self.accounts:
            if account.Idnum == account_Idnumber:
                return account
        return 0

    def editIdNumber(self, account_Idnumber, account_Id):
        account = self.getAccount(account_Idnumber)
        if account:
            if account.editId(account_Id):
                return 1
        return 0
        print('bad')
        return 0

    def editAccountName(self, account_Idnumber, account_Name):
        account = self.getAccount(account_Idnumber)
        if account:
            if account.editName(account_Name):
                return 1
        return 0
        print('bad')
        return 0

    def editYearLvl(self, account_Idnumber, account_YearLvl):
        account = self.getAccount(account_Idnumber)
        if account:
            if account.editYearLvl(account_YearLvl):
                return 1
        return 0
        print('bad')
        return 0

    def editCourse(self, account_Idnumber, account_Course):
        account = self.getAccount(account_Idnumber)
        if account:
            if account.editCourse(account_Course):
                return 1
        return 0
        print('bad')
        return 0

    def deleteAccount(self, account_Idnumber):
        with open("turno.csv", 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if not account_Idnumber in line.split(',')[0]:
                    f.write(line)
            f.truncate()

    def save(self):
        with open('turno.csv', 'w', newline='') as a:
            db = csv.writer(a)
            db.writerow([self.sysName])
            for account in self.accounts:
                db.writerow([account.Idnum, account.name,
                             account.yearLvl, account.course])
