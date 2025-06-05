import tkinter as tk
from tkinter import *
import random
from tkinter.ttk import Combobox

import pyperclip
from docutils.nodes import entry
from docutils.utils.math.latex2mathml import letters
from fontTools.misc.eexec import decrypt
from pymsgbox import password
from ttkthemes import ThemedTk
import requests, json





letters = "ABCDEFGHIJKLMNOPQRSTVWXYZabcdefghiJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
makis = "!#$%*&"
characters = "ABCDEFGHIJKLMNOPQRSTVWXYZabcdefghiJKLMNOPQRSTUVWXYZ0123456789!#$%*&"

def decrypt1():
    print("bfvr")
    passw = password_entry.get()
    encrypted_entry.delete(0, END)
    key = -3
    encrpassword = ''
    for i in passw:
        if i in characters:
            pos = characters.index(i)
            newpos = (pos + key) % len(characters)
            encrpassword += characters[newpos]
        else:
            encrpassword += i
    Decrypted_entry.insert(END, encrpassword)

def encrypt1():
    print("bfvr")
    passw = password_entry.get()
    encrypted_entry.delete(0,END)
    key = 3
    encrpassword = ''
    for i in  passw :
        if i in characters:
            pos= characters.index(i)
            newpos = (pos+key) % len(characters)
            encrpassword  += characters[newpos]
        else:
            encrpassword +=i
    encrypted_entry.insert(END, encrpassword)

def generator1():
    get1=choice.get()
    get2= int(teams.get())
    password_entry.delete(0,END)
    password1 = ''



    if get1 == 1:
        print("low")
        for i in range(get2):
            a = random.choice(letters)
            password1 += a
    elif get1 == 2:
        print("mid")
        for i in range(get2):
            a = random.choice(maksi2)
            password1 += a
    elif get1 == 3:
        print("h")
        for i in range(get2):
            a = random.choice(makis3)
            password1 += a
    password_entry.insert(END,password1)

maksi2 = letters+numbers
makis3 = letters+makis+numbers











def copy():
    ent = password_entry.get()
    pyperclip.copy(ent)
    spam = pyperclip.paste()




screen = ThemedTk(theme="equilux") #dimiourgia ouonis
screen.configure(themebg= "equilux")
screen.title("Generator") #titlos

screen.geometry('450x150') #megeuos

choice = IntVar() #metavliti poy pernei akereoys
rb1 = Radiobutton(screen, text="Low" , value= 1 , variable = choice)
rb2 = Radiobutton(screen, text="Medium" , value= 2 , variable = choice)
rb3 = Radiobutton(screen, text="Strong" , value= 3 , variable = choice)


rb1.grid(row= 5 , column= 0)
rb2.grid(row= 5 , column= 1)
rb3.grid(row= 5 , column= 2)


copy_lbl = Button(screen, text= " Copy " , command=copy  )
copy_lbl.grid(row= 0 , column= 4)

Generate_lbl = Button(screen, text= " Generate " , command= generator1  )
Generate_lbl.grid(row= 0 , column= 5)

encrypy_lbl = Button(screen, text= " Encrypt " ,command=encrypt1 )
encrypy_lbl.grid(row= 1 , column= 4)

decrypt_lbl = Button(screen, text= " Decrypt " , command= decrypt1 )
decrypt_lbl.grid(row= 1 , column= 5)


password_btn = Label(screen, text  = "Password")
password_entry = Entry(screen)

password_btn.grid(row=0, column=0)
password_entry.grid(row=0, column=1)

Length_btn = Label(screen, text  = "Length")
Length_btn.grid(row=2, column=0)

teams = Combobox(screen, state='readonly', )
teams['value'] = ('8', '9' , '10' , '11' , '12', '13', '14', '15', '16', '17', '18', '19', '20', '36' ) #tuple
teams.current(0)
teams.grid(row= 2 , column= 1)





encrypted_btn = Label(screen, text  = "Encrypted password")
encrypted_entry = Entry(screen)

encrypted_btn.grid(row=3, column=0)
encrypted_entry.grid(row=3, column=1)




Decrypted_btn = Label(screen, text  = "Decrypted password")
Decrypted_entry = Entry(screen)

Decrypted_btn.grid(row=4, column=0)
Decrypted_entry.grid(row=4, column=1)










screen.mainloop()   #teleutaia entoli