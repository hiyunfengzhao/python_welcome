import tkinter as tk
from tkinter import messagebox
import pickle
# create a window
window = tk.Tk()
window.title('Welcome to xxx')
window.geometry('450x300')

# welcome image
canvas = tk.Canvas(window, height=100, width=400)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')


# user information label
tk.Label(window, text='User name: ').place(x=50,y=150)
tk.Label(window, text='Password: ').place(x=50, y=190)

# initialize default value
var_user_name = tk.StringVar()
var_user_name.set('example@gmail.com')
var_user_pass = tk.StringVar()

# entry box
entry_user_name = tk.Entry(window, textvariable=var_user_name)
entry_user_name.place(x=160,y=150)
entry_user_pass = tk.Entry(window, textvariable=var_user_pass, show='*')
entry_user_pass.place(x=160,y=190)

# function

def user_login():
    user_name = var_user_name.get()
    user_pass = var_user_pass.get()
    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    
    if user_name in usrs_info:
        if user_pass == usrs_info[user_name]:
            tk.messagebox.showinfo(message='Welcome ' + user_name)
        else:
            tk.messagebox.showerror(message='Password incorrect / User not found')
    else:
        is_sign_up = tk.messagebox.askyesno('You have not signed up, do you want to sign up?')
        
        if is_sign_up:
            user_sign_up()



def user_sign_up():
    window_sign_up = tk.Toplevel(window)

# button
btn_login = tk.Button(window, text='Login',command=user_login)
btn_login.place(x=100,y=230)
btn_sign_up = tk.Button(window,text='Sign up',command=user_sign_up)
btn_sign_up.place(x=200,y=230)

# refresh window
window.mainloop()
