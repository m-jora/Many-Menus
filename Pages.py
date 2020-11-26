import SQLWrapper as SQLWrapper
import tkinter as tk
from PIL import ImageTk, Image


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Login)
        self.title("Many Menus")
        self.iconbitmap('pepper.ico')
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
        self.configure(bg = '#6FA8DD')

        def submit():
            print(user_entry.get())
            print(pass_entry.get())

            #valid = validate_password('TestDatabase.db', user_entry.get(), pass_entry.get())
            valid = False
            if not valid:
                invalid = tk.Label(self, text = 'Invalid username / Password')
                invalid.place(relx = .5, rely = .7, anchor = tk.N)
                invalid.after(3000, invalid.destroy)


            user_entry.delete(0, tk.END)
            pass_entry.delete(0, tk.END)
        
        
        # text box labels
        user_label = tk.Label(self, text = 'Username: ', bg = '#6FA8DD')
        pass_label = tk.Label(self, text = 'Password: ', bg = '#6FA8DD')

        # buttons
        login = tk.Button(self, text = 'Login', width = 8, height = 2, command = submit)
        create_user = tk.Button(self, text = 'Create new user account', wraplength = 100, justify = tk.CENTER, width = 14, height = 3, command = lambda: master.switch_frame(CustomerCreateAccount))
        create_res = tk.Button(self, text = 'Create new restaurant account', wraplength = 100, justify = tk.CENTER, width = 14, height = 3, command = lambda: master.switch_frame(RestaurantCreateAccount))

        # text boxes
        user_entry = tk.Entry(self, width = 35, relief = tk.GROOVE)
        pass_entry = tk.Entry(self, width = 35, relief = tk.GROOVE, show = '•')

        # Many Menus logo
        load = Image.open('many_menus.png').resize((326, 212), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')

        # placing things
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
        self.configure(bg = '#6FA8DD')
        #tk.Label(self, text = "This is the restaurant create account page.").place(relx = .5, rely = .4, anchor = tk.CENTER)

        # submit user account
        def submit():
            valid = SQLWrapper.create_restaurant('TestDatabase.db', (state_entry.get(), city_entry.get(), street_entry.get(), pass_entry.get(), user_entry.get(), store_entry.get(), phone_entry.get()))
            if valid:
                print('yee haw')
            if not valid:
                invalid = tk.Label(self, text = 'Invalid Field')
                invalid.place(relx = .5, rely = .85, anchor = tk.N)
                invalid.after(3000, invalid.destroy)

        # wayyyyy too many labels for this screen
        title = tk.Label(self, text = 'Create Restaurant Account', bg = '#6FA8DD', font = ('helvetica', 14, 'bold'))
        storename_label = tk.Label(self, text = 'Enter Store name:', bg = '#6FA8DD')
        user_label = tk.Label(self, text = 'Enter username:', bg = '#6FA8DD')
        user_info = tk.Label(self, text = '(Username must be at least 6 characters)', bg = '#6FA8DD')
        pass_label = tk.Label(self, text = 'Enter password:', bg = '#6FA8DD')
        pass_info = tk.Label(self, text = '(Password must be at least 8 characters)', bg = '#6FA8DD')
        street_label = tk.Label(self, text = 'Enter street addresss:', bg = '#6FA8DD')
        city_label = tk.Label(self, text = 'City:', bg = '#6FA8DD')
        state_label = tk.Label(self, text = 'State:', bg = '#6FA8DD')
        state_ex = tk.Label(self, text = '(ex: MO)', bg = '#6FA8DD')
        phone_label = tk.Label(self, text = 'Enter phone number:', bg = '#6FA8DD')
        phone_ex = tk.Label(self, text = '(ex: 123-456-7890)', bg = '#6FA8DD')


        # buttons... only 2 on this screen
        finish = tk.Button(self, text = 'Finish creating account', height = 3, command = submit)
        back  = tk.Button(self, text = 'Back to login page', command = lambda: master.switch_frame(Login))


        # text boxes now... too many once again
        store_entry = tk.Entry(self, relief = tk.GROOVE, width = 35)
        user_entry = tk.Entry(self, relief = tk.GROOVE, width = 35)
        pass_entry = tk.Entry(self, relief = tk.GROOVE, width = 35, show = '•')
        street_entry = tk.Entry(self, relief = tk.GROOVE, width = 33)
        city_entry = tk.Entry(self, relief = tk.GROOVE, width = 19)
        state_entry = tk.Entry(self, relief = tk.GROOVE, width = 4)
        phone_entry = tk.Entry(self, relief = tk.GROOVE, width = 32)


        # Many Menus Logo
        load = Image.open('many_menus.png').resize((326, 212), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')


        # placing things
        img.place(relx = .5, rely = .02, anchor = tk.N)
        title.place(relx = .5, rely = .34, anchor = tk.N)
        
        # store name thingssss
        storename_label.place(relx = .32, rely = .4, anchor = tk.N)
        store_entry.place(relx = .58, rely = .403, anchor = tk.N)

        # all items that have to do with username
        user_label.place(relx = .31, rely = .443, anchor = tk.N)
        user_entry.place(relx = .58, rely = .446, anchor = tk.N)
        user_info.place(relx = .52, rely = .478, anchor = tk.N)

        # all items for the password
        pass_label.place(relx = .31, rely = .513, anchor = tk.N)
        pass_entry.place(relx = .58, rely = .516, anchor = tk.N)
        pass_info.place(relx = .52, rely = .548, anchor = tk.N)

        # all items for the street 
        street_label.place(relx = .33, rely = .583, anchor = tk.N)
        street_entry.place(relx = .61, rely = .586, anchor = tk.N)

        # all items for city
        city_label.place(relx = .258, rely = .627, anchor = tk.N)
        city_entry.place(relx = .4, rely = .628 , anchor = tk.N)

        # all items for state
        state_label.place(relx = .56, rely = .627, anchor = tk.N)
        state_entry.place(relx = .623, rely = .628, anchor = tk.N)
        state_ex.place(relx = .692, rely = .627, anchor = tk.N)

        # all items for phone number
        phone_label.place(relx = .33, rely = .673, anchor = tk.N)
        phone_entry.place(relx = .6, rely = .676, anchor = tk.N)
        phone_ex.place(relx = .5, rely = .707, anchor = tk.N)

        # buttons
        finish.place(relx = .5, rely = .753, anchor = tk.N)
        back.place(relx = .5, rely = .843, anchor = tk.N)


class CustomerCreateAccount(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text = "This is the customer create account page.").place(relx = .3, rely = .3, anchor = tk.CENTER)

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
