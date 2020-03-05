from student1 import Student
import tkinter as tk
from tkinter import *
from tkinter import messagebox

if __name__ == "__main__":
    stu = Student('Student Information Database')
    accName = NONE
    accId = NONE
    accYear = NONE
    accCourse = NONE
    idEntry = NONE
    nameEntry = NONE
    courseEntry = NONE
    yearEntry = NONE
    login_accId = NONE
    loginUser_accId = NONE
    loginUser_accName = NONE
    loginUser_accYear = NONE
    loginUser_accCourse = NONE
    window3 = NONE
    window = NONE
    login_idEntry = NONE
    idEdit = NONE

    def login_Details():
        window5 = Tk()
        window5.geometry("300x330+500+200")
        idInfo = login_accId.get()

        Label(window5, text='Account Details: ', font=(
            'Helvetica', '12'), fg='blue').place(x=20, y=20)
        Label(window5, text=f"I.d Number: {stu.getAccount(idInfo).Idnum}", font=(
            'Helvetica', '12'), fg="blue").place(x=75, y=60)
        Label(window5, text=f"Name: {stu.getAccount(idInfo).name}", font=(
            'Helvetica', '12'), fg="blue").place(x=75, y=90)
        Label(window5,  text=f"Year Level: {stu.getAccount(idInfo).yearLvl}", font=(
            'Helvetica', '12'), fg="blue").place(x=75, y=120)
        Label(window5, text=f"Course: {stu.getAccount(idInfo).course}", font=(
            'Helvetica', '12'), fg="blue").place(x=75, y=150)
        Button(window5, text='Quit', padx=40,
               pady=20, fg="blue", font=('Helvetica', '12'), command=window5.destroy).place(x=80, y=200)

    def login_Delete():
        idInfo = login_accId.get()
        answer = messagebox.askyesno(
            "Hey jude", "Are you sure you want to delete this account?")
        if answer == 1:
            stu.deleteAccount(idInfo)
        else:
            return 0
        messagebox.showinfo(
            "Hey jude!", "Quit all windows and Restart the system after deleting")

    def userEdit():
        global idEdit
        idInfo = login_accId.get()
        idEdit = loginUser_accId.get()
        stu.editIdNumber(idInfo, idEdit)
        nameEdit = loginUser_accName.get()
        stu.editAccountName(idInfo, nameEdit)
        yearEdit = loginUser_accYear.get()
        stu.editYearLvl(idInfo, yearEdit)
        courseEdit = loginUser_accCourse.get()
        stu.editCourse(idInfo, courseEdit)
        stu.save()
        Label(window3, text="Account succecsfully edited",
              font=('Helvetica', '10'), fg='green').place(x=120, y=200)
        login_idEntry.delete(0, END)
        login_idEntry.insert(1, idEdit)

    def login_Edit():
        global window3
        window3 = Toplevel()
        window3.geometry("400x350+500+200")
        global loginUser_accId
        global loginUser_accName
        global loginUser_accYear
        global loginUser_accCourse
        loginUser_accId = StringVar()
        loginUser_accName = StringVar()
        loginUser_accYear = StringVar()
        loginUser_accCourse = StringVar()
        idInfo = login_accId.get()

        Label(window3, text='Current Details', font=(
            'Helvetica', '12'), fg='blue').place(x=35, y=20)

        Label(window3, text="I.d Number", font=(
            'Helvetica', '12'), fg="blue").place(x=35, y=60)
        idEntry = Entry(window3, width=30,
                        textvariable=loginUser_accId, fg='red')
        idEntry.insert(1, stu.getAccount(idInfo).Idnum)
        idEntry.place(x=130, y=60)
        Label(window3, text="Name", font=(
            'Helvetica', '12'), fg="blue").place(x=35, y=90)
        nameEntry = Entry(window3, width=30,
                          textvariable=loginUser_accName, fg='red')
        nameEntry.insert(1, stu.getAccount(idInfo).name)
        nameEntry.place(x=130, y=90)
        Label(window3,  text="Year Level", font=(
            'Helvetica', '12'), fg="blue").place(x=35, y=120)
        yearEntry = Entry(window3, width=30,
                          textvariable=loginUser_accYear, fg='red')
        yearEntry.insert(1, stu.getAccount(idInfo).yearLvl)
        yearEntry.place(x=130, y=120)
        Label(window3, text="Course", font=(
            'Helvetica', '12'), fg="blue").place(x=35, y=150)
        courseEntry = Entry(window3, width=30,
                            textvariable=loginUser_accCourse, fg='red')
        courseEntry.insert(1, stu.getAccount(idInfo).course)
        courseEntry.place(x=130, y=150)
        Button(window3, text='Edit', padx=40,
               pady=20, fg="blue", font=('Helvetica', '12'), command=userEdit).place(x=50, y=250)
        Button(window3, text='Quit', padx=50,
               pady=20, fg="blue", font=('Helvetica', '12'), command=window3.destroy).place(x=200, y=250)

    def logInWin():
        idInfo = login_accId.get()
        if not stu.getAccount(idInfo):
            messagebox.showinfo(
                "Hey jude!", "This account doesnt exist")
            login_idEntry.delete(0, END)
            nameEntry.delete(0, END)
            return 0
        window2 = Toplevel()
        window2.geometry("400x420+500+200")
        Label(window2, text='Options', font=(
            'Helvetica', '12'), fg='blue').place(x=50, y=20)
        Button(window2, text='Edit account', padx=40,
               pady=20, fg="blue", font=('Helvetica', '12'), command=login_Edit).place(x=110, y=60)
        Button(window2, text='Account details', padx=30,
               pady=20, fg="blue", font=('Helvetica', '12'), command=login_Details).place(x=110, y=140)
        Button(window2, text='Delete this account', padx=17,
               pady=20, fg="blue", font=('Helvetica', '12'), command=login_Delete).place(x=110, y=220)
        Button(window2, text='Quit', padx=70,
               pady=20, fg="blue", font=('Helvetica', '12'), command=window2.destroy).place(x=110, y=300)

    def signInUser():
        idInfo = accId.get()
        if not stu.checkAccount(idInfo):
            messagebox.showinfo(
                "Hey jude!", "Account number has already taken")
        else:
            messagebox.showinfo(
                "Hey jude!", "Account sucessfully created")
            nameInfo = accName.get()
            yearInfo = accYear.get()
            courseInfo = accCourse.get()
            stu.createAccount(idInfo, nameInfo, yearInfo, courseInfo)
        stu.save()
        idEntry.delete(0, END)
        nameEntry.delete(0, END)
        yearEntry.delete(0, END)
        courseEntry.delete(0, END)

    def signInWin():
        global window
        window = Toplevel()
        window.geometry("400x350+500+200")
        global accName
        global accId
        global accYear
        global accCourse
        global idEntry
        global yearEntry
        global courseEntry
        global nameEntry
        accName = StringVar()
        accId = StringVar()
        accYear = StringVar()
        accCourse = StringVar()

        Label(window, text='Create a account', font=(
            'Helvetica', '12'), fg='blue').place(x=130, y=20)
        Label(window, text="I.d Number", font=(
            'Helvetica', '12'), fg="blue").place(x=35, y=60)
        idEntry = Entry(window, textvariable=accId, width=30)
        idEntry.place(x=130, y=60)
        Label(window, text="Name", font=(
            'Helvetica', '12'), fg="blue").place(x=35, y=90)
        nameEntry = Entry(window, textvariable=accName, width=30)
        nameEntry.place(x=130, y=90)
        Label(window,  text="Year Level", font=(
            'Helvetica', '12'), fg="blue").place(x=35, y=120)
        yearEntry = Entry(window, textvariable=accYear, width=30)
        yearEntry.place(x=130, y=120)
        Label(window, text="Course", font=(
            'Helvetica', '12'), fg="blue").place(x=35, y=150)
        courseEntry = Entry(window, textvariable=accCourse, width=30)
        courseEntry.place(x=130, y=150)
        Button(window, text='Submit', padx=40,
               pady=20, fg="blue", font=('Helvetica', '12'), command=signInUser).place(x=50, y=250)
        Button(window, text='Quit', padx=50,
               pady=20, fg="blue", font=('Helvetica', '12'), command=window.destroy).place(x=200, y=250)

    def mainWin():
        root = Tk()
        root.geometry("500x300+500+200")
        root.title("nevermind")
        global login_accId
        global login_idEntry
        global nameEntry
        login_accId = StringVar()

        Label(root, text='Welcome to, Student Information System', font=('Helvetica', '12')).pack(
            fill=tk.X, padx=30, pady=10)
        Button(root, text='Sign in', padx=50,
                          pady=20, fg="blue", font=('Helvetica', '12'), command=signInWin).place(x=30, y=60)
        Button(root, text='Quit', padx=60,
               pady=20, fg="blue", font=('Helvetica', '12'), command=root.destroy).place(x=30, y=150)
        Label(root, text="Name", font=(
            'Helvetica', '12'), fg="blue").place(x=350, y=50)
        nameEntry = Entry(root, width=30)
        nameEntry.place(x=280, y=80)
        Label(root, text="I.d number", font=(
            'Helvetica', '12'), fg="blue").place(x=340, y=130)
        login_idEntry = Entry(root, textvariable=login_accId,
                              width=30)
        login_idEntry.place(x=280, y=160)
        audrey = Button(root, text='Log in', padx=40,
                        pady=20, fg="blue", command=logInWin, font=('Helvetica', '12')).place(x=300, y=200)

        root.mainloop()

mainWin()
