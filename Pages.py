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
                valid = validate_res_password('ManyMenus.db', user_entry.get(), pass_entry.get())

                if not valid:
                    invalid = tk.Label(self, text = 'Invalid username / Password')
                    invalid.place(relx = .5, rely = .76, anchor = tk.N)
                    invalid.after(3000, invalid.destroy)
                
                else:
                    global res_name
                    global user_name
                    user_name = user_entry.get()
                    res_name = SQLWrapper.get_restaurant_name('ManyMenus.db', user_entry.get())[0][0]
                    master.switch_frame(RestaurantUpdateMenu)
        
            elif not res_account.get() and user_account.get():
                valid = validate_password('ManyMenus.db', user_entry.get(), pass_entry.get())

                if not valid:
                    invalid = tk.Label(self, text = 'Invalid username / password')
                    invalid.place(relx = .5, rely = .76, anchor = tk.N)
                    invalid.after(3000, invalid.destroy)

                else:
                    user_name = user_entry.get()
                    master.switch_frame(Browse)
            
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
                SQLWrapper.create_restaurant('ManyMenus.db', (state_entry.get(), city_entry.get(), street_entry.get(), pass_entry.get(), user_entry.get(), store_entry.get(), phone_entry.get()))
            
            except:
               invalid = tk.Label(self, text = 'Invalid Field')
               invalid.place(relx = .5, rely = .9, anchor = tk.N) 
               invalid.after(3000, invalid.destroy)
               return
            
            global res_name
            res_name = store_entry.get()
            global user_name
            user_name = user_entry.get()
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
                SQLWrapper.create_customer('ManyMenus.db', (user_entry.get(), name_entry.get(), pass_entry.get(), birthday, age))
            
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
        store_name = res_name
        global user_name
        user = user_name


        def submit(password, state, city, street, user, store, phone):
            try:
                SQLWrapper.update_restaurant_info('ManyMenus.db', (state, city, street, password, store, phone, user))

            except:

                invalid = tk.Label(self, text = 'Invalid Field')
                invalid.place(relx = .5, rely = .6, anchor = tk.N)
                invalid.after(3000, invalid.destroy)
                return

            valid = tk.Label(self, text = 'Changes Saved')
            valid.place(relx = .5, rely = .6, anchor = tk.N)
            valid.after(3000, valid.destroy)

        # Text labels
        rest_name = tk.Label(self, text = store_name, bg = '#6FA8DD', font = ('helvetica', 11))
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

        ing_frame = tk.Frame(self, bg = '#6FA8DD', bd = 2)
        restaurant_id = SQLWrapper.get_restaurant_id('ManyMenus.db', res_name)

        #def save_amount(i):
        '''
        def remove_ingredient(i, frame, name, restaurant_id):
            invalid = False
            try:
                SQLWrapper.delete_food('ManyMenus.db', name, restaurant_id)
            except:
                invalid = tk.Label(frame, text = 'Invalid Field')
                invalid.grid(row = 7+i, column = 0, columnspan = 2)
                invalid.after(3000, invalid.destroy)
                invalid = True
            if not invalid:
                list_ingredients(frame, restaurant_id)

        def get_ingredient_to_remove(i, frame, add_ing_b, remove_ing_b, restaurant_id):
            # destroy add new ingredient button
            add_ing_b.grid_forget()
            remove_ing_b.grid_forget()
            # get food name
            name_label = tk.Label(frame, text = "Name of ingredient to remove:", bg = '#6FA8DD', font = ('helvetica', 8))
            name_label.grid(row = 3+i, column = 0, pady = 3)
            name_entry = tk.Entry(frame, relief = tk.GROOVE, width = 25)
            name_entry.grid(row = 3+i, column = 1, pady = 3)
            submit_ing = tk.Button(frame, text = 'Finish removing', height = 1, width = 10, command = lambda: remove_ingredient(i, frame, name_entry.get(), restaurant_id))
            submit_ing.grid(row = 4+i, column = 0, columnspan = 2, pady = 3)
        '''
        def add_ingredient(i, frame, calories, restaurant_id, name, quantity):
            invalid = False
            if len(calories) == 0 or len(name) == 0 or len(quantity) == 0:
                invalid = tk.Label(frame, text = 'Invalid Field')
                invalid.grid(row = 7+i, column = 0, columnspan = 2)
                invalid.after(3000, invalid.destroy)
                invalid = True
            if not invalid:
                try:
                    SQLWrapper.create_food('ManyMenus.db', (calories, restaurant_id, restaurant_id, name, '0', quantity, True))
                except:
                    invalid = tk.Label(frame, text = 'Invalid Field')
                    invalid.grid(row = 7+i, column = 0, columnspan = 2)
                    invalid.after(3000, invalid.destroy)
                    invalid = True
            if not invalid:
                list_ingredients(frame, restaurant_id)
        
        def get_ingredient(i, frame, add_ing_b, restaurant_id):
            # destroy add new ingredient button
            add_ing_b.grid_forget()
            #remove_ing_b.grid_forget()
            # create entry boxes and labels
            name_label = tk.Label(frame, text = "Ingredient name:", bg = '#6FA8DD', font = ('helvetica', 8))
            name_label.grid(row = 3+i, column = 0, pady = 3)
            name_entry = tk.Entry(frame, relief = tk.GROOVE, width = 25)
            name_entry.grid(row = 3+i, column = 1, pady = 3)
            calories_label = tk.Label(frame, text = "Calories per serving:", bg = '#6FA8DD', font = ('helvetica', 8))
            calories_label.grid(row = 4+i, column = 0, pady = 3)
            calories_entry = tk.Entry(frame, relief = tk.GROOVE, width = 10)
            calories_entry.grid(row = 4+i, column = 1, pady = 3)
            quantity_label = tk.Label(frame, text = "Quantity:", bg = '#6FA8DD', font = ('helvetica', 8))
            quantity_label.grid(row = 5+i, column = 0, pady = 3)
            quantity_entry = tk.Entry(frame, relief = tk.GROOVE, width = 10)
            quantity_entry.grid(row = 5+i, column = 1, pady = 3)
            submit_ing = tk.Button(frame, text = 'Finish adding', height = 1, width = 10, command = lambda: add_ingredient(i, frame, calories_entry.get(), restaurant_id, name_entry.get(), quantity_entry.get()))
            submit_ing.grid(row = 6+i, column = 0, columnspan = 2, pady = 3)
        
        def list_ingredients(frame, restaurant_id):
            # forget everything in the frame
            frame.destroy()
            ing_frame = tk.Frame(self, bg = '#6FA8DD', bd = 2)
            # get the ingredients and place them
            ingredients = SQLWrapper.get_food_in_inventory('ManyMenus.db', restaurant_id)
            i = 0
            for ing in ingredients:
                ingredient_name_label = tk.Label(ing_frame, text = ing[1], bg = '#6FA8DD', font = ('helvetica', 11, 'bold'))
                ingredient_name_label.grid(row = 0+i, column = 0, columnspan = 2)

                amount_label = tk.Label(ing_frame, text = 'Amount:', bg = '#6FA8DD', font = ('helvetica', 9))
                amount_label.grid(row = 1+i, column = 0)

                ing_amount_label = tk.Label(ing_frame, text = ing[2], bg = '#6FA8DD', font = ('helvetica', 9))
                ing_amount_label.grid(row = 1+i, column = 1)

                calorie_label = tk.Label(ing_frame, text = 'Calories per serving:', bg = '#6FA8DD', font = ('helvetica', 9))
                calorie_label.grid(row = 2+i, column = 0)

                ing_calorie_label = tk.Label(ing_frame, text = ing[3], bg = '#6FA8DD', font = ('helvetica', 9))
                ing_calorie_label.grid(row = 2+i, column = 1)

                #save_amount = tk.Button(ing_frame, text = 'save amount', height = 1, width = 11)
                #save_amount.grid(row = 0+i, column = 0)

                i += 3
            add_ing = tk.Button(ing_frame, text = 'Add new ingredient', height = 1, width = 15, command = lambda: get_ingredient(i, ing_frame, add_ing, restaurant_id))
            #remove_ing = tk.Button(ing_frame, text = 'Remove', height = 1, width = 11, command = lambda: get_ingredient_to_remove(i, ing_frame, add_ing, remove_ing, restaurant_id))
            add_ing.grid(row = 3+i, column = 0, columnspan = 2)
            #remove_ing.grid(row = 3+i, column = 1)
            ing_frame.place(relx = .5, rely = .3, anchor = tk.N)
        
        # text labels
        res_name_label = tk.Label(self, text = res_name, bg = '#6FA8DD', font = ('helvetica', 11))
        title_label = tk.Label(self, text = 'Update Inventory', bg = '#6FA8DD', font = ('helvetica', 14, 'bold'))
        
        # text box
        #enter_amount = tk.Entry(self, relief = tk.GROOVE, width = 35)

        # Many Menus Logo
        load = Image.open(resource_path('many_menus.png')).resize((163, 106), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')

        # buttons
        update_info = tk.Button(self, text = 'Update Info', height = 2, width = 13, command = lambda: master.switch_frame(RestaurantUpdateInfo))
        update_menu = tk.Button(self, text = 'Update Menu', height = 2, width = 13, command = lambda: master.switch_frame(RestaurantUpdateMenu))
        
        #update_amount = tk.Button(self, text = 'update amount', height = 1, width = 12) 

        # display image, restaurant name, title, change page buttons
        img.place(relx = .05, rely = .02)
        res_name_label.place(relx = .5, rely = .08, anchor = tk.N)
        title_label.place(relx = .5, rely = .2, anchor = tk.N)
        update_info.place(relx = .8, rely = .03, anchor = tk.N)
        update_menu.place(relx = .8, rely = .1, anchor = tk.N)

        #id_label = tk.Label(self, text = restaurant_id)
        #id_label.place(relx = .5, rely = .3, anchor = tk.N)

        # display table (ingredient name, remove, amount label, amount, update amount button)
        ing_frame.place(relx = .5, rely = .3, anchor = tk.N)
        list_ingredients(ing_frame, restaurant_id)

        return

class RestaurantUpdateMenu(tk.Frame):
    def __init__(self, master):
        # main frame
        tk.Frame.__init__(self, master)
        self.configure(bg = '#6FA8DD')

        global res_name

        menu_frame = tk.Frame(self, bg = '#6FA8DD', bd = 2)
        restaurant_id = SQLWrapper.get_restaurant_id('ManyMenus.db', res_name)

        def add_new_dish(i, frame, name, price, restaurant_id):
            invalid = False
            if len(name) == 0 or len(price) == 0:
                invalid = tk.Label(frame, text = 'Invalid Field')
                invalid.grid(row = 7+i, column = 0, columnspan = 2)
                invalid.after(3000, invalid.destroy)
                invalid = True
            if not invalid:
                try:
                    SQLWrapper.create_dish('ManyMenus.db', (name, restaurant_id, price))
                except:
                    invalid = tk.Label(frame, text = 'Invalid Field')
                    invalid.grid(row = 7+i, column = 0, columnspan = 2)
                    invalid.after(3000, invalid.destroy)
                    invalid = True
            if not invalid:
                list_dishes(frame, restaurant_id)

        def get_new_dish(i, frame, add_dish_b, add_ing_b, restaurant_id):
            add_dish_b.grid_forget()
            for b in add_ing_b:
                b.grid_forget()
            # create entry boxes and labels
            name_label = tk.Label(frame, text = "Dish name:", bg = '#6FA8DD', font = ('helvetica', 8))
            name_label.grid(row = 3+i, column = 0, pady = 3)
            name_entry = tk.Entry(frame, relief = tk.GROOVE, width = 25)
            name_entry.grid(row = 3+i, column = 1, pady = 3)
            price_label = tk.Label(frame, text = "Price:", bg = '#6FA8DD', font = ('helvetica', 8))
            price_label.grid(row = 4+i, column = 0, pady = 3)
            price_entry = tk.Entry(frame, relief = tk.GROOVE, width = 10)
            price_entry.grid(row = 4+i, column = 1, pady = 3)
            submit_ing = tk.Button(frame, text = 'Finish adding', height = 1, width = 10, command = lambda: add_new_dish(i, frame, name_entry.get(), price_entry.get(), restaurant_id))
            submit_ing.grid(row = 5+i, column = 0, columnspan = 2, pady = 3)
        
        def add_ingredient(i, frame, name, quantity, restaurant_id, dish_id):
            invalid = False
            if len(name) == 0 or len(quantity) == 0:
                invalid = tk.Label(frame, text = 'Invalid Field')
                invalid.grid(row = 7+i, column = 0, columnspan = 2)
                invalid.after(3000, invalid.destroy)
                invalid = True
            if not invalid:
                inventory_ing = SQLWrapper.get_food_in_inventory('ManyMenus.db', restaurant_id)
                in_inventory = False
                for ing in inventory_ing:
                    if name == ing[1]:
                        in_inventory = True
                        cal = ing[3]
                if in_inventory:
                    try:
                        SQLWrapper.create_dish_foods('ManyMenus.db', (dish_id, name, quantity, cal))
                    except:
                        invalid = tk.Label(frame, text = 'Invalid Field')
                        invalid.grid(row = 7+i, column = 0, columnspan = 2)
                        invalid.after(3000, invalid.destroy)
                        invalid = True
                else:
                    invalid = tk.Label(frame, text = 'Ingredient not in inventory')
                    invalid.grid(row = 7+i, column = 0, columnspan = 2)
                    invalid.after(3000, invalid.destroy)
                    invalid = True
                list_dishes(frame, restaurant_id)

        def get_ingredient(i, frame, add_dish_b, add_ing_b, restaurant_id, dish_id):
            add_dish_b.grid_forget()
            for b in add_ing_b:
                b.grid_forget()
            # create entry boxes and labels
            name_label = tk.Label(frame, text = "Ingredient name:", bg = '#6FA8DD', font = ('helvetica', 8))
            name_label.grid(row = 3+i, column = 0, pady = 3)
            name_entry = tk.Entry(frame, relief = tk.GROOVE, width = 25)
            name_entry.grid(row = 3+i, column = 1, pady = 3)
            quantity_label = tk.Label(frame, text = "Quantity in dish:", bg = '#6FA8DD', font = ('helvetica', 8))
            quantity_label.grid(row = 4+i, column = 0, pady = 3)
            quantity_entry = tk.Entry(frame, relief = tk.GROOVE, width = 10)
            quantity_entry.grid(row = 4+i, column = 1, pady = 3)
            submit_ing = tk.Button(frame, text = 'Finish adding', height = 1, width = 10, command = lambda: add_ingredient(i, frame, name_entry.get(), quantity_entry.get(), restaurant_id, dish_id))
            submit_ing.grid(row = 5+i, column = 0, columnspan = 2, pady = 3)

        
        def list_dishes(frame, restaurant_id):
            frame.destroy()
            menu_frame = tk.Frame(self, bg = '#6FA8DD', bd = 2)
            dishes = SQLWrapper.get_dishes_for_menu('ManyMenus.db', restaurant_id)
            add_ing = []
            i = 0
            j = 0
            for dish in dishes:
                dish_name_label = tk.Label(menu_frame, text = dish[0], bg = '#6FA8DD', font = ('helvetica', 11, 'bold'))
                dish_name_label.grid(row = 0+i, column = 0, pady = 2)
                
                price_label = tk.Label(menu_frame, text = '$' + dish[1], bg = '#6FA8DD', font = ('helvetica', 11))
                price_label.grid(row = 0+i, column = 1, pady = 2)

                dish_id = SQLWrapper.get_dish_id('ManyMenus.db', restaurant_id, dish[0])
                ingredients = SQLWrapper.get_food_for_dish('ManyMenus.db', dish_id)

                for ing in ingredients:
                    ingredient_name_label = tk.Label(menu_frame, text = ing[0], bg = '#6FA8DD', font = ('helvetica', 9, 'bold'))
                    ingredient_name_label.grid(row = 1+i, column = 0, pady = 1, sticky = tk.W)

                    calories_label = tk.Label(menu_frame, text = 'Calories per serving:', bg = '#6FA8DD', font = ('helvetica', 8))
                    calories_label.grid(row = 2+i, column = 0, pady = 1, sticky = tk.W)
                    calories_amount_label = tk.Label(menu_frame, text = ing[1], bg = '#6FA8DD', font = ('helvetica', 8))
                    calories_amount_label.grid(row = 2+i, column = 1, pady = 1, sticky = tk.E)

                    quantity_label = tk.Label(menu_frame, text = 'Quantity in dish:', bg = '#6FA8DD', font = ('helvetica', 8))
                    quantity_label.grid(row = 3+i, column = 0, pady = 1, sticky = tk.W)
                    quantity_amount_label = tk.Label(menu_frame, text = ing[2], bg = '#6FA8DD', font = ('helvetica', 8))
                    quantity_amount_label.grid(row = 3+i, column = 1, pady = 1, sticky = tk.E)
                    
                    i += 3
                add_ing.append(tk.Button(menu_frame, text = 'Add ingredient', height = 1, width = 14, command = lambda did=dish_id: get_ingredient(i, menu_frame, add_dish, add_ing, restaurant_id, did)))
                add_ing[j].grid(row = 1+i, column = 0, columnspan = 2, pady = 2)
                i += 2
                j += 1
                
            #remove_ingredient = (tk.Button(menu_frame, text = 'Remove', height = 1, width = 8, font = ('helvetica', 8))
            #remove_ingredient.grid(row = 1+i, column = 2)
            #remove_dish = tk.Button(menu_frame, text = 'Remove dish', height = 1, width = 8, font = ('helvetica', 8))
            #remove_dish.grid(row = 0+i, column = 2)
            add_dish = tk.Button(menu_frame, text = 'Add new dish', height = 2, width = 14, command = lambda: get_new_dish(i, menu_frame, add_dish, add_ing, restaurant_id))
            add_dish.grid(row = 5+i, column = 0, columnspan = 2, pady = 5)
            menu_frame.place(relx = .5, rely = .3, anchor = tk.N)

        # text labels
        res_name_label = tk.Label(self, text = res_name, bg = '#6FA8DD', font = ('helvetica', 11))
        title_label = tk.Label(self, text = 'Update Menu', bg = '#6FA8DD', font = ('helvetica', 14, 'bold'))
        
        # buttons
        update_info = tk.Button(self, text = 'Update Info', height = 2, width = 13, command = lambda: master.switch_frame(RestaurantUpdateInfo))
        update_inv = tk.Button(self, text = 'Update Inventory', height = 2, width = 13, command = lambda: master.switch_frame(RestaurantUpdateInventory))

        # Many Menus Logo
        load = Image.open(resource_path('many_menus.png')).resize((163, 106), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')

        # display image, restaurant name, title, change page buttons
        img.place(relx = .05, rely = .02)
        res_name_label.place(relx = .5, rely = .08, anchor = tk.N)
        title_label.place(relx = .5, rely = .2, anchor = tk.N)
        update_info.place(relx = .8, rely = .03, anchor = tk.N)
        update_inv.place(relx = .8, rely = .1, anchor = tk.N)

        list_dishes(menu_frame, restaurant_id)

        return

class UpdateUserInfo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg = '#6FA8DD')

        self.loca_default = .34
        self.diet_default = .64

        global user_name
        user = user_name


        def get_diet():
            self.new_diet.after(0, self.new_diet.destroy)
            self.delete_diet.after(0, self.delete_diet.destroy)
            self.names = tk.Label(self, text = 'Diet, Calorie Limit', bg = '#6FA8DD')
            self.diet_n = tk.Entry(self, relief = tk.GROOVE, width = 19)
            self.limit_n = tk.Entry(self, relief = tk.GROOVE, width = 4)
            self.submit = tk.Button(self, text = 'Submit', command = lambda: add_diet(self.diet_n.get(), self.limit_n.get()))
            
            self.names.place(relx = .5, rely = self.diet_default + .03, anchor = tk.N)
            self.diet_n.place(relx = .47, rely = self.diet_default, anchor = tk.N)
            self.limit_n.place(relx = .6, rely = self.diet_default, anchor = tk.N)
            self.submit.place(relx = .5, rely = self.diet_default + .07, anchor = tk.N)


        def add_diet(diet, limit):
            invalid = False
            try:
                SQLWrapper.create_diet('ManyMenus.db', (diet, user, limit))
            
            except:
                invalid = tk.Label(self, text = 'Invalid Field')
                invalid.place(relx = .3, rely = self.loca_default + .2)
                invalid.after(3000, invalid.destroy)
                self.loca_default -= .05
                invalid = True

            self.diet_n.after(0, self.diet_n.destroy)
            self.limit_n.after(0, self.limit_n.destroy)
            self.names.after(0, self.names.destroy)
            self.submit.after(0, self.submit.destroy)

            self.diet_default += .05
            self.new_diet = tk.Button(self, text = 'Add New Diet', command = get_diet)
            self.new_diet.place(relx = .5, rely = self.diet_default, anchor = tk.N)

            self.delete_diet = tk.Button(self, text = 'Delete Diet', command = get_diet2)
            self.delete_diet.place(relx = .5, rely = self.diet_default + .1, anchor = tk.N)

            if not invalid:
                diets = SQLWrapper.get_diet_for_user('ManyMenus.db', user)

                D = tk.Label(self, text  = diets[-1][0] + ' ' + str(diets [-1][1]), bg = '#6FA8DD')
                D.place(relx = .5, rely = self.diet_default - .05, anchor = tk.N)
                

        def get_location():
            self.new_location.after(0, self.new_location.destroy)
            self.names = tk.Label(self, text = 'City, State', bg = '#6FA8DD')
            self.city_n = tk.Entry(self, relief = tk.GROOVE, width = 19)
            self.state_n = tk.Entry(self, relief = tk.GROOVE, width = 4)
            self.submit = tk.Button(self, text = 'Submit', command = lambda: add_location(self.city_n.get(), self.state_n.get()))
            
            self.names.place(relx = .5, rely = self.loca_default + .03, anchor = tk.N)
            self.state_n.place(relx = .6, rely = self.loca_default, anchor = tk.N)
            self.city_n.place(relx = .47, rely = self.loca_default, anchor = tk.N)
            self.submit.place(relx = .5, rely = self.loca_default + .07, anchor = tk.N)


        def add_location(city, state):
            invalid = False
            try:
                SQLWrapper.create_customer_locations('ManyMenus.db', (user, city, state))
            
            except:
                invalid = tk.Label(self, text = 'Invalid Field')
                invalid.place(relx = .3, rely = self.loca_default + .2)
                invalid.after(3000, invalid.destroy)
                self.loca_default -= .05
                invalid = True

            self.state_n.after(0, self.state_n.destroy)
            self.city_n.after(0, self.city_n.destroy)
            self.names.after(0, self.names.destroy)
            self.submit.after(0, self.submit.destroy)

            self.loca_default += .05
            self.new_location = tk.Button(self, text = 'Add New location', command = get_location)
            self.new_location.place(relx = .5, rely = self.loca_default, anchor = tk.N)

            if not invalid:
                locations = SQLWrapper.get_customer_locations('ManyMenus.db', user)

                L = tk.Label(self, text  = locations[-1][0] + ', ' + locations [-1][1], bg = '#6FA8DD')
                L.place(relx = .5, rely = self.loca_default - .05, anchor = tk.N)


        def get_diet2():
            self.delete_diet.after(0, self.delete_diet.destroy)
            self.names = tk.Label(self, text = 'Enter Diet Name', bg = '#6FA8DD')
            self.diet = tk.Entry(self, relief = tk.GROOVE, width = 19)
            self.submit = tk.Button(self, text = 'Delete', command = lambda: remove_diet(self.diet.get()))

            self.names.place(relx = .5, rely = self.diet_default + .13, anchor = tk.N)
            self.diet.place(relx = .5, rely = self.diet_default + .1, anchor = tk.N)
            self.submit.place(relx = .5, rely = self.diet_default + .16, anchor = tk.N)


        def remove_diet(diet_name):
            invalid = False
            try:
                SQLWrapper.delete_diet('ManyMenus.db', (diet_name))

            except:
                invalid = tk.Label(self, text = 'Invalid Field')
                invalid.place(relx = .3, rely = self.diet_default + .2)
                invalid = True

            self.names.after(0, self.names.destroy)
            self.diet.after(0, self.diet.destroy)
            self.submit.after(0, self.submit.destroy)

            if not invalid:
                master.switch_frame(UpdateUserInfo)


        # text labels
        user_label = tk.Label(self, text = user, bg = '#6FA8DD', font = ('helvetica', 11))
        title = tk.Label(self, text = 'Update Info', bg = '#6FA8DD', font = ('helvetica', 14, 'bold'))
        fav_locations = tk.Label(self, text = 'Favorite Locations', bg = '#6FA8DD', font = ('helvetica', 11, 'bold'))
        diets_label = tk.Label(self, text = 'Diet', bg = '#6FA8DD', font = ('helvetica', 11, 'bold'))


        # add loop for adding in labels for diet and locations?
        locations = SQLWrapper.get_customer_locations('ManyMenus.db', user)
        diet = SQLWrapper.get_diet_for_user('ManyMenus.db', user)
        
        for place in locations:
            L = tk.Label(self, text = place[0] + ', ' + place[1], bg = '#6FA8DD')
            L.place(relx = .5, rely = self.loca_default, anchor = tk.N)
            self.loca_default += .04

        for diets in diet:
            D = tk.Label(self, text = diets[0] + ' ' + str(diets[1]), bg = '#6FA8DD')
            D.place(relx = .5, rely = self.diet_default, anchor = tk.N)
            self.diet_default += .04

        # button
        back = tk.Button(self, text = 'Back to Browse', height = 2, command = lambda: master.switch_frame(Browse))
        self.new_location = tk.Button(self, text = 'Add New location', command = get_location)
        self.new_diet = tk.Button(self, text = 'Add new Diet', command = get_diet)
        self.delete_diet = tk.Button(self, text = 'Delete Diet', command = get_diet2)


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
        self.new_location.place(relx = .5, rely = self.loca_default, anchor = tk.N)
        self.new_diet.place(relx = .5, rely = self.diet_default, anchor = tk.N)
        self.delete_diet.place(relx = .5, rely = self.diet_default + .1, anchor = tk.N)
        return

class Browse(tk.Frame):
    def __init__(self, master):
        # main frame
        tk.Frame.__init__(self, master)
        self.configure(bg = '#6FA8DD')
        # search bar and check box frame
        top_frame = tk.Frame(self, bg = '#6FA8DD', bd = 9, height = 20, width = 70)
        # frame to hold restaurant lists
        bottom_frame = tk.Frame(self, bg = '#6FA8DD', bd = 2)

        global user_name
        
        # should be called by search, given the restaurants needed to print
        #def print_results():

        # make this func the command for search_button when complete
        def search(search_var, search_type):
            #if len(search_var.get()) == 0:
                # print 'nothing was entered in the search bar'
            #elif not search_type.get():
                # print 'please select what you are searching for'
            #elif search_type.get() == 'loc':
                # print matching locations
            if search_type.get() == 'res':
                # print matching restaurants
                restaurants = SQLWrapper.get_restaurants_with_name('ManyMenus.db', search_var)
                frames = []
                i = 0
                for restaurant in restaurants:
                    # add a frame
                    frames.append(tk.Frame(bottom_frame, bg = '#6FA8DD', bd = 2))
                    # first row
                    res_name = tk.Label(frames[i], text = search_var, bg = '#6FA8DD', font = ('helvetica', 10, 'bold'))
                    res_name.grid(row = 0, column = 0, sticky = tk.W, pady = 5)
                    see_more = tk.Button(frames[i], text = 'see more', bg = '#6FA8DD', font = ('helvetica', 11))
                    see_more.grid(row = 0, column = 1, sticky = tk.E, pady = 5)
                    like_res = tk.Button(frames[i], text = 'like', bg = '#6FA8DD', font = ('helvetica', 11))
                    like_res.grid(row = 0, column = 2, sticky = tk.E, pady = 5)
                    # list the menu items
                    menus = SQLWrapper.get_menu('ManyMenus.db', restaurant[0])
                    for menu in menus:
                        dishes = SQLWrapper.get_dishes_for_menu('ManyMenus.db', menu[0])
                        j = 0
                        for dish in dishes:
                            dish_name = tk.Label(frames[i], text = dish[0], bg = '#6FA8DD', font = ('helvetica', 11))
                            dish_name.grid(row = j, column = 0, columnspan = 2, sticky = tk.W, pady = 5)
                            price = tk.Label(frames[i], text = "$" + dish[1], bg = '#6FA8DD', font = ('helvetica', 11))
                            price.grid(row = j, column = 2, pady = 5)
                            # increment dish placement
                            j += 1
                    # increment frame
                    i += 1

        '''
        def search_fav_loc():
            # print restaurants of the favorite location
            #locations = get_customer_locations('ManyMenus.db', user)

        
        def search_fav_res():
            # print favorite restaurants
        '''

        # text labels
        user_label = tk.Label(self, text = user_name, bg = '#6FA8DD', font = ('helvetica', 11))
        title_label = tk.Label(self, text = 'Browse Menus', bg = '#6FA8DD', font = ('helvetica', 14, 'bold'))
        ingredient = tk.Label(self, text = 'ingredient 1', bg = '#6FA8DD', font = ('helvetica', 11))

        # text box
        search_var = tk.StringVar()
        search_bar = tk.Entry(top_frame, relief = tk.GROOVE, width = 35)

        # buttons
        search_type = tk.StringVar()
        #diet_var = tk. IntVar()
        search_button = tk.Button(top_frame, text = 'Search', bg = '#6FA8DD', font = ('helvetica', 11), command = lambda: search(search_var, search_type))
        update_info = tk.Button(self, text = 'Update Info', bg = '#6FA8DD', font = ('helvetica', 11), command = lambda: master.switch_frame(UpdateUserInfo))
        loc_check = tk.Radiobutton(top_frame, text = 'Search locations (City, State)', variable = search_type, value = 'loc', bg = '#6FA8DD', activebackground = '#6FA8DD')
        res_check = tk.Radiobutton(top_frame, text = 'Search restaurants', variable = search_type, value = 'res', bg = '#6FA8DD', activebackground = '#6FA8DD')
        browse_fav_loc = tk.Button(top_frame, text = 'Browse favorite locations', bg = '#6FA8DD', activebackground = '#6FA8DD')
        browse_fav_res = tk.Button(top_frame, text = 'Browse favorite restaurants', bg = '#6FA8DD', activebackground = '#6FA8DD')
        #diet_check = tk.Checkbutton(top_frame, text = 'Filter by diet', variable = diet_var, bg = '#6FA8DD', activebackground = '#6FA8DD')
        
        see_less = tk.Button(self, text = 'see less', bg = '#6FA8DD', font = ('helvetica', 11))
        #see_last_searched = tk.Button(top_frame, text = 'see last searched', bg = '#6FA8DD', font = ('helvetica', 8))
        

        # Many Menus Logo
        load = Image.open(resource_path('many_menus.png')).resize((163, 106), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = tk.Label(image = self.render, borderwidth = 3, bg = 'black')

        # place image, headers, and switch screen buttons at top
        img.place(relx = .05, rely = .02)
        user_label.place(relx = .5, rely = .08, anchor = tk.N)
        title_label.place(relx = .5, rely = .2, anchor = tk.N)
        update_info.place(relx = .8, rely = .05, anchor = tk.N)

        # place top frame
        # place search bar
        search_bar.grid(row = 0, column = 0, padx = 10)
        search_button.grid(row = 0, column = 1, pady = 10)
        # place check buttons and last searched button
        loc_check.grid(row = 1, column = 0, sticky = tk.W, pady = 5)
        res_check.grid(row = 2, column = 0, sticky = tk.W, pady = 5)
        #diet_check.grid(row = 3, column = 0, sticky = tk.W)
        #see_last_searched.grid(row = 0, column = 2, sticky = tk.E)
        browse_fav_loc.grid(row = 1, column = 1)
        browse_fav_res.grid(row = 2, column = 1)
        top_frame.place(relx = .5, rely = .3, anchor = tk.N)

        '''
        # place bottom frame
        # place list of restaurants and their dishes
        res_name.place(relx = .2, rely = .55, anchor = tk.N)
        see_more.place(relx = .55, rely = .55, anchor = tk.N)
        like_res.place(relx = .8, rely = .55, anchor = tk.N)
        dish.place(relx = .25, rely = .6, anchor = tk.N)
        price.place(relx = .8, rely = .6, anchor = tk.N)
        
        res_name.place(relx = .2, rely = .55, anchor = tk.N)
        see_less.place(relx = .55, rely = .55, anchor = tk.N)
        like_res.place(relx = .8, rely = .55, anchor = tk.N)
        dish.place(relx = .25, rely = .6, anchor = tk.N)
        price.place(relx = .8, rely = .6, anchor = tk.N)

        bottom_frame.place(relx = .4, rely = .6, anchor = tk.N)
        '''

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

SQLWrapper.initialize_database("ManyMenus.db")
app = Application()
app.mainloop()