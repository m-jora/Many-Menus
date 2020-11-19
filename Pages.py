import SQLWrapper as SQLWrapper
import tkinter as tk
from PIL import ImageTk, Image


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Login)
        self.title("Many Menus")
        self.minsize(600,700)
        self.maxsize(600,700)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)

        if(self._frame is not None):
            self._frame.destroy()

        self._frame = new_frame
        self._frame.pack(fill= 'both', expand = True)

# Page not done. This is a sample for everyone to use to know how to interact with the other pages
class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # tk.Tk.Title(self, 'Login')
        # self.tk.Title("Login")
        #tk.Label(self, text = "This is the start page.").pack()
        def submit(event = None):
            print(user_entry.get())
            print(pass_entry.get())

            #valid = validate_password(dbfile, user_entry.get(), pass_entry.get())

            user_entry.delete(0, tk.END)
            pass_entry.delete(0, tk.END)
        
        self.bind('<Return>', submit)
        self.configure(bg = '#6FA8DD')



        #text box labels
        user_label = tk.Label(self, text = 'Username: ', bg = '#6FA8DD')
        pass_label = tk.Label(self, text = 'Password: ', bg = '#6FA8DD')

        #buttons
        login = tk.Button(self, text = 'Login', width = 8, height = 2, command = submit)
        create_user = tk.Button(self, text = 'Create new user account', wraplength = 100, justify = tk.CENTER, width = 14, height = 3, command = lambda: master.switch_frame(CustomerCreateAccount))
        create_res = tk.Button(self, text = 'Create new restaurant account', wraplength = 100, justify = tk.CENTER, width = 14, height = 3, command = lambda: master.switch_frame(RestaurantCreateAccount))

        #text boxes
        user_entry = tk.Entry(self, width = 35, relief = tk.GROOVE)
        pass_entry = tk.Entry(self, width = 35, relief = tk.GROOVE)

        #Many Menus logo
        load = Image.open('many_menus.png').resize((326, 212), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')


        img.place(relx = .5, rely = .02, anchor = tk.N)
        user_label.place(relx = .3, rely = .4, anchor = tk.N)
        pass_label.place(relx = .299, rely = .45, anchor = tk.N)

        user_entry.place(relx = .55, rely = .403, anchor = tk.N)
        pass_entry.place(relx = .55, rely = .452, anchor = tk.N)

        login.place(relx = .5, rely = .5, anchor = tk.N)
        create_res.place(relx = .65, rely = .6, anchor = tk.N)
        create_user.place(relx = .35, rely = .6, anchor = tk.N)


        # This is an example of how we will transfer control from one page to another
        '''tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(RestaurantCreateAccount)).pack()'''

class RestaurantCreateAccount(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text = "This is the restaurant create account page.").place(anchor = tk.N)

class CustomerCreateAccount(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text = "This is the customer create account page.").place(anchor = tk.N)

class RestaurantUpdateInfo(tk.Frame):
    def __init__(self, master):
        return

class RestaurantUpdateInventory(tk.Frame):
    def __init__(self, master):
        return

class RestaurantUpdateMenu(tk.Frame):
    def __init__(self, master):
        return

class UpdateUserInfo(tk.Frame):
    def __init__(self, master):
        return

class Browse(tk.Frame):
    def __init__(self, master):
        return


# Purpose: Validates a password for a given user
def validate_password(database_file, username, entered_password):
    actualPassword = SQLWrapper.get_password_for_user(database_file, username)

    if(actualPassword != entered_password):
        return False
    else:
        return True

    
app = Application()
app.mainloop()
