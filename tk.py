import tkinter as tk
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
var_user_pass = tk.StringVar()
var_user_name.set('example@gmail.com')
# entry box
entry_user_name = tk.Entry(window, textvariable=var_user_name)
entry_user_name.place(x=160,y=150)
entry_user_pass = tk.Entry(window, textvariable=var_user_pass, show='*')
entry_user_pass.place(x=160,y=190)

# function

def user_login():
    pass
def user_sign_up():
    pass

# button
btn_login = tk.Button(window, text='Login',command='user_login')
btn_login.place(x=100,y=230)
btn_sign_up = tk.Button(window,text='Sign up',command='user_sign_up')
btn_sign_up.place(x=200,y=230)

# refresh window
window.mainloop()
