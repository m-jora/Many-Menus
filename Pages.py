import SQLWrapper as SQLWrapper
import tkinter as tk
from PIL import ImageTk, Image
import sys
import datetime
 
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Login)
        self.title("Many Menus")
        self.iconbitmap(resource_path('pepper.ico'))
        self.minsize(600,700)
        self.maxsize(600,700)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)

        if(self._frame is not None):
            self._frame.destroy()

        self._frame = new_frame
        self._frame.pack(fill= 'both', expand = True)

class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg = '#6FA8DD')

        def submit(res_account, user_account):

            if res_account.get() and user_account.get():
                invalid = tk.Label(self, text = 'Select only one Checkbox')
                invalid.place(relx = .5, rely = .76, anchor = tk.N)
                invalid.after(3000, invalid.destroy)

            elif res_account.get() and not user_account.get():
                valid = validate_res_password('TestDatabase2.db', user_entry.get(), pass_entry.get())

                if not valid:
                    invalid = tk.Label(self, text = 'Invalid username / Password')
                    invalid.place(relx = .5, rely = .76, anchor = tk.N)
                    invalid.after(3000, invalid.destroy)
                
                else:
                    global res_name
                    res_name = user_entry.get()
                    master.switch_frame(RestaurantUpdateInfo) #RestaurantUpdateMenu
        
            elif not res_account.get() and user_account.get():
                valid = validate_password('TestDatabase2.db', user_entry.get(), pass_entry.get())

                if not valid:
                    invalid = tk.Label(self, text = 'Invalid username / password')
                    invalid.place(relx = .5, rely = .76, anchor = tk.N)
                    invalid.after(3000, invalid.destroy)

                else:
                    global user_name
                    user_name = user_entry.get()
                    master.switch_frame(UpdateUserInfo) # Browse
            
            elif not res_account.get() and not user_account.get():
                invalid = tk.Label(self, text = 'Please select account type')
                invalid.place(relx = .5, rely = .76, anchor = tk.N)
                invalid.after(3000, invalid.destroy)

        user_label = tk.Label(self, text = 'Username: ', bg = '#6FA8DD')
        pass_label = tk.Label(self, text = 'Password: ', bg = '#6FA8DD')
        login_type = tk.Label(self, text = 'Account Type:', bg = '#6FA8DD')

        login = tk.Button(self, text = 'Login', width = 8, height = 2, command = lambda: submit(res_account, user_account))
        create_user = tk.Button(self, text = 'Create new user account', wraplength = 100, justify = tk.CENTER, width = 14, height = 3, command = lambda: master.switch_frame(CustomerCreateAccount)) #UpdateUserInfo
        create_res = tk.Button(self, text = 'Create new restaurant account', wraplength = 100, justify = tk.CENTER, width = 14, height = 3, command = lambda: master.switch_frame(RestaurantCreateAccount)) # RestaurantUpdateInfo

        # Text boxes for user entry
        user_entry = tk.Entry(self, width = 35, relief = tk.GROOVE)
        pass_entry = tk.Entry(self, width = 35, relief = tk.GROOVE, show = '•')

        # Checkbox for account type
        res_account = tk.IntVar()
        user_account = tk.IntVar()
        res_check = tk.Checkbutton(self, text = 'Restaurant', variable = res_account, bg = '#6FA8DD', activebackground = '#6FA8DD')
        user_check = tk.Checkbutton(self, text = 'User', variable = user_account, bg = '#6FA8DD', activebackground = '#6FA8DD')

        # Many Menus logo
        load = Image.open(resource_path("many_menus.png")).resize((326, 212), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')

        # Places items to the GUI
        img.place(relx = .5, rely = .02, anchor = tk.N)
        user_label.place(relx = .3, rely = .4, anchor = tk.N)
        pass_label.place(relx = .299, rely = .45, anchor = tk.N)
        user_entry.place(relx = .55, rely = .403, anchor = tk.N)
        pass_entry.place(relx = .55, rely = .452, anchor = tk.N)
        login_type.place(relx = .311, rely = .5, anchor = tk.N)
        
        res_check.place(relx = .47, rely = .498, anchor = tk.N)
        user_check.place(relx = .63, rely = .498, anchor = tk.N)

        login.place(relx = .5, rely = .57, anchor = tk.N)
        create_res.place(relx = .65, rely = .67, anchor = tk.N)
        create_user.place(relx = .35, rely = .67, anchor = tk.N)


        # This is an example of how we will transfer control from one page to another
        '''tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(RestaurantCreateAccount)).pack()'''

class RestaurantCreateAccount(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg = '#6FA8DD')

        # Submit user account -- check to make sure that the information is valid
        def submit():
            try:
                SQLWrapper.create_restaurant('TestDatabase2.db', (state_entry.get(), city_entry.get(), street_entry.get(), pass_entry.get(), user_entry.get(), store_entry.get(), phone_entry.get()))
            
            except:
               invalid = tk.Label(self, text = 'Invalid Field')
               invalid.place(relx = .5, rely = .9, anchor = tk.N) 
               invalid.after(3000, invalid.destroy)
               return
            
            global res_name
            res_name = user_entry.get()
            master.switch_frame(RestaurantUpdateMenu)

        # Labels
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

        finish = tk.Button(self, text = 'Finish creating account', height = 3, command = submit)
        back  = tk.Button(self, text = 'Back to login page', command = lambda: master.switch_frame(Login))

        # Text boxes now
        store_entry = tk.Entry(self, relief = tk.GROOVE, width = 35)
        user_entry = tk.Entry(self, relief = tk.GROOVE, width = 35)
        pass_entry = tk.Entry(self, relief = tk.GROOVE, width = 35, show = '•')
        street_entry = tk.Entry(self, relief = tk.GROOVE, width = 33)
        city_entry = tk.Entry(self, relief = tk.GROOVE, width = 19)
        state_entry = tk.Entry(self, relief = tk.GROOVE, width = 4)
        phone_entry = tk.Entry(self, relief = tk.GROOVE, width = 32)

        # Many Menus Logo
        load = Image.open(resource_path('many_menus.png')).resize((326, 212), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')

        # Placing things
        img.place(relx = .5, rely = .02, anchor = tk.N)
        title.place(relx = .5, rely = .34, anchor = tk.N)
        
        # Store name thingssss
        storename_label.place(relx = .32, rely = .4, anchor = tk.N)
        store_entry.place(relx = .58, rely = .403, anchor = tk.N)

        # All items that have to do with username
        user_label.place(relx = .31, rely = .443, anchor = tk.N)
        user_entry.place(relx = .58, rely = .446, anchor = tk.N)
        user_info.place(relx = .52, rely = .478, anchor = tk.N)

        # All items for the password
        pass_label.place(relx = .31, rely = .513, anchor = tk.N)
        pass_entry.place(relx = .58, rely = .516, anchor = tk.N)
        pass_info.place(relx = .52, rely = .548, anchor = tk.N)

        # All items for the street 
        street_label.place(relx = .33, rely = .583, anchor = tk.N)
        street_entry.place(relx = .61, rely = .586, anchor = tk.N)

        # All items for city
        city_label.place(relx = .258, rely = .627, anchor = tk.N)
        city_entry.place(relx = .4, rely = .628 , anchor = tk.N)

        # All items for state
        state_label.place(relx = .56, rely = .627, anchor = tk.N)
        state_entry.place(relx = .623, rely = .628, anchor = tk.N)
        state_ex.place(relx = .692, rely = .627, anchor = tk.N)

        # All items for phone number
        phone_label.place(relx = .33, rely = .673, anchor = tk.N)
        phone_entry.place(relx = .6, rely = .676, anchor = tk.N)
        phone_ex.place(relx = .5, rely = .707, anchor = tk.N)

        # Buttons
        finish.place(relx = .5, rely = .753, anchor = tk.N)
        back.place(relx = .5, rely = .843, anchor = tk.N)


class CustomerCreateAccount(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg = '#6FA8DD')

        def submit():
            birthday = birthday_entry1.get() + '/' + birthday_entry2.get() + '/' + birthday_entry3.get()
            age = datetime.datetime.now().year - int(birthday_entry3.get())

            try:
                SQLWrapper.create_customer('TestDatabase2.db', (user_entry.get(), name_entry.get(), pass_entry.get(), birthday, age))
            
            except:
               invalid = tk.Label(self, text = 'Invalid Field')
               invalid.place(relx = .5, rely = .79, anchor = tk.N) 
               invalid.after(3000, invalid.destroy)
               return

            global user_name
            user_name = user_entry.get()
            master.switch_frame(Browse)

        # lables for this screen
        title = tk.Label(self, text = 'Create User Account', bg = '#6FA8DD', font = ('helvetica', 14, 'bold'))
        username_label = tk.Label(self, text = 'Enter username:', bg = '#6FA8DD')
        user_info = tk.Label(self, text = '(Username must be at least 6 characters)', bg = '#6FA8DD')
        pass_label = tk.Label(self, text = 'Enter password:', bg = '#6FA8DD')
        pass_info = tk.Label(self, text = '(Password must be at least 8 characters)', bg = '#6FA8DD')
        name_label = tk.Label(self, text = 'Enter name:', bg = '#6FA8DD')
        birthday_label = tk.Label(self, text = 'Enter Birthday:', bg = '#6FA8DD')
        birthday_info = tk.Label(self, text = '(MM/DD/YYYY)', bg = '#6FA8DD')
        slash1 = tk.Label(self, text = '/', bg = '#6FA8DD')
        slash2 = tk.Label(self, text = '/', bg = '#6FA8DD')
        
        # Text boxes
        user_entry = tk.Entry(self, relief = tk.GROOVE, width = 35)
        pass_entry = tk.Entry(self, relief = tk.GROOVE, width = 35, show = '•')
        name_entry = tk.Entry(self, relief = tk.GROOVE, width = 35)
        birthday_entry1 = tk.Entry(self, relief = tk.GROOVE, width = 4)
        birthday_entry2 = tk.Entry(self, relief = tk.GROOVE, width = 4)
        birthday_entry3 = tk.Entry(self, relief = tk.GROOVE, width = 4)

        # Buttons
        create = tk.Button(self, text = 'Finish Creating Account', height = 3, command = submit)
        back = tk.Button(self, text = 'Back to login page', command = lambda: master.switch_frame(Login))

        # Many Menus Logo
        load = Image.open(resource_path('many_menus.png')).resize((326, 212), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')

        # placing logo and title
        img.place(relx = .5, rely = .02, anchor = tk.N)
        title.place(relx = .5, rely = .34, anchor = tk.N)

        # All items that have to do with username
        username_label.place(relx = .31, rely = .4, anchor = tk.N)
        user_entry.place(relx = .58, rely = .403, anchor = tk.N)
        user_info.place(relx = .52, rely = .435, anchor = tk.N)

        # All items for the password
        pass_label.place(relx = .308, rely = .47, anchor = tk.N)
        pass_entry.place(relx = .58, rely = .473, anchor = tk.N)
        pass_info.place(relx = .52, rely = .505, anchor = tk.N)

        # All items for name
        name_label.place(relx = .29, rely = .54, anchor = tk.N)
        name_entry.place(relx = .58, rely = .543, anchor = tk.N)

        # All itms for birthday
        birthday_label.place(relx = .3, rely = .584, anchor = tk.N)
        birthday_entry1.place(relx = .424, rely = .587, anchor = tk.N)
        slash1.place(relx = .464, rely = .587, anchor = tk.N)
        birthday_entry2.place(relx = .504, rely = .587, anchor = tk.N)
        slash2.place(relx = .544, rely = .587, anchor = tk.N)
        birthday_entry3.place(relx = .584, rely = .587, anchor = tk.N)
        birthday_info.place(relx = .69, rely = .587, anchor = tk.N)


        # Buttons
        create.place(relx = .5, rely = .65, anchor = tk.N)
        back.place(relx = .5, rely = .74, anchor = tk.N)


class RestaurantUpdateInfo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg = '#6FA8DD')

        global res_name
        user = res_name

        def submit(password, state, city, street, user, store, phone):
            #try:
            SQLWrapper.update_restaurant_info('TestDatabase2.db', (state, city, street, password, store, phone))

            #except:
            #    invalid = tk.Label(self, text = 'Invalid Field')
            #    invalid.place(relx = .5, rely = .6, anchor = tk.N)
            #    invalid.after(3000, invalid.destroy)
            #    return

        # Text labels
        rest_name = tk.Label(self, text = res_name, bg = '#6FA8DD', font = ('helvetica', 11))
        title = tk.Label(self, text = 'Restaurant Info', bg = '#6FA8DD', font = ('helvetica', 14, 'bold'))
        name_label = tk.Label(self, text = 'Restaurant Name:', bg = '#6FA8DD')
        address_label = tk.Label(self, text = 'Restaurant Address:', bg = '#6FA8DD')
        city_label = tk.Label(self, text = 'City:', bg = '#6FA8DD')
        state_label = tk.Label(self, text = 'State:', bg = '#6FA8DD')
        phone_label = tk.Label(self, text = 'Phone number:', bg = '#6FA8DD')
        pass_label = tk.Label(self, text = 'New Password:', bg = '#6FA8DD')

        # Buttons
        update_menu = tk.Button(self, text = 'Update Menu', height = 2, width = 13, command = lambda: master.switch_frame(RestaurantUpdateMenu))
        update_inven = tk.Button(self, text = 'Update Inventory', height = 2, command = lambda: master.switch_frame(RestaurantUpdateInventory))
        save = tk.Button(self, text = 'Save changes', height = 2, command = lambda: submit(pass_entry.get(), state_entry.get(), city_entry.get(), address_entry.get(), user, name_entry.get(), phone_entry.get()))


        # Text boxes
        name_entry = tk.Entry(self, relief = tk.GROOVE, width = 35)
        address_entry = tk.Entry(self, relief = tk.GROOVE, width = 35)
        city_entry = tk.Entry(self, relief = tk.GROOVE, width = 19)
        state_entry = tk.Entry(self, relief = tk.GROOVE, width = 4)
        phone_entry = tk.Entry(self, relief = tk.GROOVE, width = 35)
        pass_entry = tk.Entry(self, relief = tk.GROOVE, width = 35, show = '•')

        # Many Menus Logo
        load = Image.open(resource_path('many_menus.png')).resize((163, 106), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')

        # Placing logo, title, update buttons
        img.place(relx = .05, rely = .02)
        rest_name.place(relx = .5, rely = .08, anchor = tk.N)
        title.place(relx = .5, rely = .2, anchor = tk.N)
        update_menu.place(relx = .8, rely = .03, anchor = tk.N)
        update_inven.place(relx = .8, rely = .1, anchor = tk.N)


        # Restaurant name stuff
        name_label.place(relx = .3, rely = .26, anchor = tk.N)
        name_entry.place(relx = .6, rely = .263, anchor = tk.N)

        # Address stuff
        address_label.place(relx = .305, rely = .306, anchor = tk.N)
        address_entry.place(relx = .6, rely = .309, anchor = tk.N)
        
        city_label.place(relx = .24, rely = .352, anchor = tk.N)
        city_entry.place(relx = .4, rely = .352, anchor = tk.N)
        
        state_label.place(relx = .58, rely = .352, anchor = tk.N)
        state_entry.place(relx = .67, rely = .352, anchor = tk.N)


        # phone number
        phone_label.place(relx = .29, rely = .398, anchor = tk.N)
        phone_entry.place(relx = .6, rely = .398, anchor = tk.N)


        # password
        pass_label.place(relx = .29, rely = .444, anchor = tk.N)
        pass_entry.place(relx = .6, rely = .444, anchor = tk.N)


        # save button
        save.place(relx = .5, rely = .52, anchor = tk.N)

        return

class RestaurantUpdateInventory(tk.Frame):
    def __init__(self, master):
        # main frame
        tk.Frame.__init__(self, master)
        self.configure(bg = '#6FA8DD')

        global res_name
        user = res_name

        #def save_amount():
        
        #def remove():
        
        #def add_new_ingredient():
        
        # text labels
        res_name_label = tk.Label(self, text = res_name, bg = '#6FA8DD', font = ('helvetica', 11))
        title_label = tk.Label(self, text = 'Update Inventory', bg = '#6FA8DD', font = ('helvetica', 14, 'bold'))
        amount_label = tk.Label(self, text = 'Amount: ', bg = '#6FA8DD', font = ('helvetica', 11))
        ingredient_name_label = tk.Label(self, text = 'ingre 1', bg = '#6FA8DD', font = ('helvetica', 11, 'bold'))
        ingredient_amount_label = tk.Label(self, text = '1 oz', bg = '#6FA8DD', font = ('helvetica', 11))

        # text box
        enter_amount = tk.Entry(self, relief = tk.GROOVE, width = 35)

        # Many Menus Logo
        load = Image.open(resource_path('many_menus.png')).resize((163, 106), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')

        # buttons
        update_info = tk.button(self, text = 'Update Info', height = 2, width = 13)
        update_menu = tk.button(self, text = 'Update Menu', height = 2, width = 13)
        remove_ingredient = tk.Button(self, text = 'remove', height = 1, width = 12)
        # command is save amount
        save_amount = tk.Button(self, text = 'save amount', height = 1, width = 12) 
        # opens text box to type in new amount
        update_amount = tk.Button(self, text = 'update amount', height = 1, width = 12) 
        add_new_ingredient = tk.Button(self, text = 'Add new ingredient', height = 1, width = 13)

        # display image, restaurant name, title, change page buttons
        img.place(relx = .05, rely = .02)
        res_name_label.place(relx = .5, rely = .08, anchor = tk.N)
        title_label.place(relx = .5, rely = .2, anchor = tk.N)
        update_info.place(relx = .8, rely = .03, anchor = tk.N)
        update_menu.place(relx = .8, rely = .1, anchor = tk.N)

        # display table (ingredient name, remove, amount label, amount, update amount button)
        ingredient_name_label.place(relx = .2, rely = .4, anchor = tk.N)
        remove_ingredient.place(relx = .3, rely = .4, anchor = tk.N)
        amount_label.place(relx = .2, rely = .45, anchor = tk.N)
        ingredient_amount_label.place(relx = .25, rely = .45, anchor = tk.N)
        save_amount.place(relx = .3, rely = .45, anchor = tk.N)
        add_new_ingredient.place(relx = .2, rely = .5, anchor = tk.N)

        return

class RestaurantUpdateMenu(tk.Frame):
    def __init__(self, master):

        # Many Menus Logo
        load = Image.open(resource_path('many_menus.png')).resize((163, 106), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')

        return

class UpdateUserInfo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg = '#6FA8DD')

        loca_default = .34
        diet_default = .64

        global user_name
        user = user_name

        def get_diet():
            pass

        def add_diet():
            pass

        def get_location():
            pass

        def add_location():
            pass

        # text labels
        user_label = tk.Label(self, text = user, bg = '#6FA8DD', font = ('helvetica', 11))
        title = tk.Label(self, text = 'Update Info', bg = '#6FA8DD', font = ('helvetica', 14, 'bold'))
        fav_locations = tk.Label(self, text = 'Favorite Locations', bg = '#6FA8DD', font = ('helvetica', 11, 'bold'))
        diets_label = tk.Label(self, text = 'Diet', bg = '#6FA8DD', font = ('helvetica', 11, 'bold'))


        # add loop for adding in labels for diet and locations?
        locations = SQLWrapper.get_customer_locations('TestDatabase2.db', user)
        diet = SQLWrapper.get_diet_for_user('TestDatabase2.db', user)
        print(locations)
        print(diet)


        # button
        back = tk.Button(self, text = 'Back to Browse', height = 2, command = lambda: master.switch_frame(Browse))
        new_location = tk.Button(self, text = 'Add New location', command = get_location)
        new_diet = tk.Button(self, text = 'Add new Diet', command = get_diet)


        # Many Menus Logo
        load = Image.open(resource_path('many_menus.png')).resize((163, 106), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')


        # placing logo, title, back button
        img.place(relx = .05, rely = .02)
        user_label.place(relx = .5, rely = .08, anchor = tk.N)
        title.place(relx = .5, rely = .2, anchor = tk.N)
        back.place(relx = .8, rely = .05, anchor = tk.N)


        # sub titles sections
        fav_locations.place(relx = .5, rely = .3, anchor = tk.N)
        diets_label.place(relx = .5, rely = .6, anchor = tk.N)


        # add button place
        # shift these based on locaitons and diets
        new_location.place(relx = .5, rely = loca_default, anchor = tk.N)
        new_diet.place(relx = .5, rely = diet_default, anchor = tk.N)
        return

class Browse(tk.Frame):
    def __init__(self, master):

        # Many Menus Logo
        load = Image.open(resource_path('many_menus.png')).resize((163, 106), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')

        return

# Purpose: Validates a password for a given user
def validate_password(database_file, username, entered_password):
    actualPassword = SQLWrapper.get_password_for_user(database_file, username)

    if(actualPassword != entered_password):
        return False
    else:
        return True

def validate_res_password(database_file, username, entered_password):
    actualPassword = SQLWrapper.get_password_for_restaurant_username(database_file, username)

    if actualPassword != entered_password:
        return False
    else:
        return True

SQLWrapper.initialize_database("testDatabase2.db")
app = Application()
app.mainloop()