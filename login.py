########################################
#            Login Window?             #
########################################
import tkinter as tk
import SQLWrapper, Main
from PIL import ImageTk, Image

window = tk.Tk()
window.title('Many Menus')
window.minsize(600, 700)
window.maxsize(600,700)
window.configure(bg = '#6FA8DD')

def submit(event = None):
  # call check valid for valid login
  # if not valid add new label asking for new password
  print(user_entry.get())
  print(pass_entry.get())
  #valid = validate_password(dbfile, user_entry.get(), pass_entry.get())
  user_entry.delete(0, tk.END)
  pass_entry.delete(0, tk.END)

#allows enter key to call submit function
window.bind('<Return>', submit)

def user_create():
  #move to create user page
  pass


def res_create():
  #move to create restaurant page.
  pass


#text box labels
user_label = tk.Label(window, text = 'Username: ', bg = '#6FA8DD')
pass_label = tk.Label(window, text = 'Password: ', bg = '#6FA8DD')

#buttons
login = tk.Button(window, text = 'Login', width = 8, height = 2, command = submit)
create_user = tk.Button(window, text = 'Create new user account', wraplength = 100, justify = tk.CENTER, width = 14, height = 3, command = user_create)
create_res = tk.Button(window, text = 'Create new restaurant account', wraplength = 100, justify = tk.CENTER, width = 14, height = 3, command = res_create)

#text boxes
user_entry = tk.Entry(window, width = 35, relief = tk.GROOVE)
pass_entry = tk.Entry(window, width = 35, relief = tk.GROOVE)

#Many Menus logo
load = Image.open('many_menus.png').resize((326, 212), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = tk.Label(image = render, borderwidth = 3, bg = 'black')


img.place(relx = .5, rely = .02, anchor = tk.N)
user_label.place(relx = .3, rely = .4, anchor = tk.N)
pass_label.place(relx = .299, rely = .45, anchor = tk.N)

user_entry.place(relx = .55, rely = .403, anchor = tk.N)
pass_entry.place(relx = .55, rely = .452, anchor = tk.N)

login.place(relx = .5, rely = .5, anchor = tk.N)
create_res.place(relx = .65, rely = .6, anchor = tk.N)
create_user.place(relx = .35, rely = .6, anchor = tk.N)

window.mainloop()