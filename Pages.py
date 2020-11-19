import SQLWrapper as SQLWrapper
import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Login)
        self.title("Many Menus")
        self.minsize(600,700)
        self.maxsize(600,700)
        self.configure(bg = '#6FA8DD')

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)

        if(self._frame is not None):
            self._frame.destroy()

        self._frame = new_frame
        self._frame.pack()

# Page not done. This is a sample for everyone to use to know how to interact with the other pages
class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # tk.Tk.Title(self, 'Login')
        # self.tk.Title("Login")
        tk.Label(self, text = "This is the start page.").pack()

        # This is an example of how we will transfer control from one page to another
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(RestaurantCreateAccount)).pack()

class RestaurantCreateAccount(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text = "This is the restaurant create account page.").pack()

class CustomerCreateAccount(tk.Frame):
    def __init__(self, master):
        return

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
