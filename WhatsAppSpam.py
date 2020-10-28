from tkinter import *
from tkinter.filedialog import askopenfilename
from selenium import webdriver


root = Tk()
root.title('WhatsApp Spam')
root.geometry('600x500')

driver = webdriver.Chrome('C:/webdrivers/chromedriver.exe')
driver.maximize_window()
driver.get('https://web.whatsapp.com/')


def via_self():
    self_win_1 = Toplevel()
    self_win_1.title('Via_Self')
    self_win_1.geometry('600x500')

    def submit():
        name = name_var.get()
        msg = msg_var.get()
        count = count_var.get()

        user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
        user.click()
        msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

        for index in range(count):
            msg_box.send_keys(msg)
            driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
            print(index)
        print("success")
        self_win_1.destroy()

    name_var = StringVar()
    msg_var = StringVar()
    count_var = IntVar()

    Label(self_win_1, text='Name: ').place(x=10, y=20)
    Entry(self_win_1, textvariable=name_var).place(x=50, y=20)

    Label(self_win_1, text='Name: ').place(x=10, y=50)
    Entry(self_win_1, textvariable=msg_var).place(x=50, y=50)

    Label(self_win_1, text='Name: ').place(x=10, y=100)
    Entry(self_win_1, textvariable=count_var).place(x=50, y=100)

    Button(self_win_1, text='Spam', command=submit).place(x=10, y=150)
    self_win_1.mainloop()


def via_file():
    self_win_2 = Toplevel()
    self_win_2.title('Via_file')
    self_win_2.geometry('600x500')
    file = askopenfilename(initialdir="/", title="Select file",
                           filetypes=(("text files", "*.txt"), ("all files", "*.*")))

    def submit():
        words = open(file, "r")
        list_words = words.read().split()
        name = name_var.get()

        user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
        user.click()
        msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

        for i in list_words:
            msg = i
            msg_box.send_keys(msg)
            driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
        print("success")
        self_win_2.destroy()

    name_var = StringVar()
    Label(self_win_2, text=file).place(x=0, y=0)

    Label(self_win_2, text='Name: ').place(x=10, y=20)
    Entry(self_win_2, textvariable=name_var).place(x=50, y=20)

    Button(self_win_2, text='Spam', command=submit).place(x=10, y=150)
    self_win_2.mainloop()


def destroy():
    driver.close()
    exit()


button_1 = Button(root, text='Self', command=via_self).place(x=20, y=30)
button_2 = Button(root, text='File', command=via_file).place(x=80, y=30)
button_3 = Button(root, text='Quit', command=destroy).place(x=120, y=30)

root.mainloop()
