import sqlite3
from sqlite3 import Error

# Purpose: Connects to an existing database file
# @param db_file: an existing database file to connect to
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

# Purpose: Creates a table in a connected database
# @param conn: the database we are connected to
# @param create_table_sql: the sql command string
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


# Purpose: Creates the database for the Many Menus GUI
def initialize_database(database_file):
    
    database = create_connection(database_file)

    with database:
        create_table(database, """
            CREATE TABLE IF NOT EXISTS Restaurant(
                State TEXT NOT NULL,
                City TEXT NOT NULL,
                StreetAddress TEXT NOT NULL,
                Password TEXT NOT NULL ,
                Username TEXT PRIMARY KEY,
                StoreName TEXT NOT NULL,
                PhoneNumber TEXT NOT NULL,
                CHECK(length(Username) >= 6),
                CHECK(length(Password) >= 8),
                CHECK(length(StoreName) >= 4),
                CHECK(length(State) == 2)
            )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS MenuUpdate(
                LastUpdated TEXT PRIMARY KEY,
                MenuID TEXT,
                RestaurantUsername TEXT,
                FOREIGN KEY(RestaurantUsername) REFERENCES Username(Restaurant)
            )""")        

        create_table(database, """
            CREATE TABLE IF NOT EXISTS Menu(
                MenuID TEXT PRIMARY KEY,
                RestaurantUsername TEXT,
                FOREIGN KEY(RestaurantUsername) REFERENCES Username(Restaurant)
            )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS Browse(
                LastBrowsed TEXT PRIMARY KEY,
                CustomerUsername TEXT,
                MenuID TEXT,
                FOREIGN KEY(CustomerUsername) REFERENCES Username(Customer),
                FOREIGN KEY(MenuID) REFERENCES MenuID(Menu)
            )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS Customer(
                Username TEXT PRIMARY KEY,
                Name TEXT NOT NULL,
                Password TEXT NOT NULL,
                Birthday TEXT NOT NULL,
                Age TEXT NOT NULL,
                CHECK(length(Username) >= 6),
                CHECK(length(Password) >= 8)
            )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS CustomerLocations(
                Username TEXT,
                City TEXT NOT NULL,
                State TEXT NOT NULL,
                CustomerLocationsID TEXT PRIMARY KEY,
                FOREIGN KEY(Username) REFERENCES Username(Customer)
            )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS Diet(
                DietName TEXT PRIMARY KEY,
                CustomerUsername TEXT,
                CalorieLimit INTEGER,
                FOREIGN KEY(CustomerUsername) REFERENCES Username(Customer)
            )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS AdhereTo(
                DietName TEXT,
                FoodID TEXT,
                PRIMARY KEY(DietName, FoodID),
                FOREIGN KEY(DietName) REFERENCES DietName(Diet),
                FOREIGN KEY(FoodID) REFERENCES ID(Food)
            )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS DietRestrictedTypes(
                DietName TEXT,
                RestrictedTypeName TEXT PRIMARY KEY,
                FOREIGN KEY(DietName) REFERENCES DietName(Diet)
        )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS Food(
                FoodID TEXT PRIMARY KEY,
                CaloriesPerServing INTEGER,
                MenuID TEXT,
                InventoryID TEXT,
                Name TEXT,
                Price TEXT,
                QuantityInStock INTEGER,
                InStock INTEGER,
                FOREIGN KEY(MenuID) REFERENCES MenuID(Menu),
                FOREIGN KEY(InventoryID) REFERENCES InventoryID(Inventory)
        )""") 

        create_table(database, """
            CREATE TABLE IF NOT EXISTS FoodTypes(
                FoodID TEXT,
                FoodTypeName TEXT,
                FOREIGN KEY(FoodID) REFERENCES FoodID(Food)
        )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS TrackAmount(
                InventoryID TEXT,
                RestaurantUsername TEXT,
                FOREIGN KEY(RestaurantUsername) REFERENCES RestaurantUsername(Restaurant),
                FOREIGN KEY(InventoryID) REFERENCES InventoryID(Inventory)
        )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS Inventory(
                InventoryID TEXT PRIMARY KEY,
                RestaurantUsername TEXT,
                FOREIGN KEY(RestaurantUsername) REFERENCES RestaurantUsername(Restaurant)
        )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS RestaurantUpdate(
                LastUpdated TEXT,
                RestaurantUsername TEXT,
                InventoryID TEXT,
                FOREIGN KEY(RestaurantUsername) REFERENCES RestaurantUsername(Restaurant),
                FOREIGN KEY(InventoryID) REFERENCES InventoryID(Inventory)  
        )""")
   
###################################################################
# The following functions are SQL commands for inserting data     #
# into the various tables of our database                         #
###################################################################

def create_restaurant(database_file, restaurant_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO Restaurant(State,City,StreetAddress,Password,Username,StoreName,PhoneNumber) VALUES (?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sqlCommand, restaurant_data)
    conn.commit()

def create_menu_update(database_file, menu_update_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO MenuUpdate(LastUpdated, MenuID, RestaurantUsername) VALUES (?,?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, menu_update_data)
    conn.commit()

def create_menu(database_file, menu_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO Menu(MenuID,RestaurantUsername) VALUES (?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, menu_data)
    conn.commit()

def create_browse(database_file, browse_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO Browse(LastBrowsed, CustomerUsername, MenuID) VALUES (?,?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, browse_data)
    conn.commit()

def create_customer(database_file, customer_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO Customer(Username,Name,Password,Birthday,Age) VALUES (?,?,?,?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, customer_data)
    conn.commit()

def create_customer_locations(database_file, customer_locations_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO CustomerLocations(Username,City,State,CustomerLocationsID) VALUES (?,?,?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, customer_locations_data)
    conn.commit()

def create_diet(database_file, diet_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO Diet(DietName, CustomerUsername, CalorieLimit) VALUES (?,?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, diet_data)
    conn.commit()

def create_adhere_to(database_file, adhere_to_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO AdhereTo(DietName, FoodID) VALUES (?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, adhere_to_data)
    conn.commit()

def create_diet_restricted_type(database_file, restricted_type_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO DietRestrictedTypes(DietName, RestrictedTypeName) VALUES (?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, restricted_type_data)
    conn.commit()

def create_food(database_file, food_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO Food(FoodID,CaloriesPerServing,MenuID,InventoryID,Name,Price,QuantityInStock,InStock) VALUES (?,?,?,?,?,?,?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, food_data)
    conn.commit()

def create_food_type(database_file, food_type_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO FoodTypes(FoodID, FoodTypeName) VALUES (?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, food_type_data)
    conn.commit()

def create_track_amount(database_file, track_amount_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO TrackAmount(InventoryID, RestaurantUsername) VALUES (?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, track_amount_data)
    conn.commit()

def create_restaurant_update(database_file, restaurant_update_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO RestaurantUpdate(RestaurantUsername, InventoryID) VALUES (?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, restaurant_update_data)
    conn.commit()

def create_inventory(database_file, inventory_data):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''INSERT INTO Inventory(InventoryID, RestaurantUsername) VALUES (?,?)'''

    cur = conn.cursor()
    cur.execute(sqlCommand, inventory_data)
    conn.commit()

###################################################################
# End of insert functions                                         #
###################################################################

###################################################################
# The following functions are SQL commands for deleting data in   #
# the various tables of our database. Not all data is deletable.  #
# We will not allow users to delete their accounts.               #
###################################################################

# @param FoodID: FoodID is the PK of the Food table
def delete_food(database_file, FoodID):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''DELETE FROM Food WHERE FoodID = ?'''
    curr = conn.cursor()

    curr.execute(sqlCommand, (FoodID,))
    conn.commit()

# @param DietName: Dietname is the PK of the Diet table
def delete_diet(database_file, DietName):
    conn = sqlite3.connect(database_file)

    sqlCommand = 'DELETE FROM Diet WHERE DietName = ?'
    curr = conn.cursor()

    curr.execute(sqlCommand, (DietName,))
    conn.commit()

# @param customerLocationsID: customerLocationsID is the PK of CustomerLocation
def delete_customer_location(database_file, customerLocationsID):
    conn = sqlite3.connect(database_file)

    sqlCommand = 'DELETE FROM CustomerLocations WHERE customerLocationsID=?'

    curr = conn.cursor()

    curr.execute(sqlCommand, (customerLocationsID,))
    conn.commit()

# @param MenuID: MenuID is the PK of the Menu table
def delete_menu(database_file, MenuID):
    conn = sqlite3.connect(database_file)

    sqlCommand = 'DELETE FROM Menu WHERE MenuID=?'

    curr = conn.cursor()

    curr.execute(sqlCommand, (MenuID,))
    conn.commit()

###################################################################
# End of delete functions                                         #
###################################################################

###################################################################
# Start of update functions                                       #
###################################################################

# @param updatedRestaurantTuple: the new tuple to insert into the table where we are 
# given the values in this order: State, City, StreetAddress, Password, StoreName, PhoneNumber, and the Username last
def update_restaurant_info(database_file, updated_restaurant_tuple):
    conn = sqlite3.connect(database_file)

    sql = '''UPDATE Restaurant 
                SET State = ?,
                City = ?,
                StreetAddress = ?,
                Password = ?,
                StoreName = ?,
                PhoneNumber =?
            WHERE Username = ?'''

    curr = conn.cursor()
    curr.execute(sql, updated_restaurant_tuple)

    conn.commit()

# @param updated_customer_tuple: the new tuple to insert into the table where we are
# given the values in this order: Name, Password, Birthday, Age, Username
def update_customer_info(database_file, updated_customer_tuple):
    conn = sqlite3.connect(database_file)

    sql = '''UPDATE Customer
                SET Name=?,
                Password=?,
                Birthday=?,
                Age=?
                WHERE Username=?'''

    curr = conn.cursor()
    curr.execute(sql, updated_customer_tuple)

    conn.commit()

# @param updated_food_tuple: the datavalue to replace the previous element
# The format of the updated_food_tuple needs to have this order:
# CaloriesPerServing, Name, Price, QuantityInStock, InStock, FoodID
def update_food(database_file, updated_food_tuple):
    conn = sqlite3.connect(database_file)

    sql = '''UPDATE Food
                SET CaloriesPerServing=?,
                Name=?,
                Price=?,
                QuantityInStock=?,
                InStock=?
            WHERE FoodID = ?'''

    curr = conn.cursor()
    curr.execute(sql, updated_food_tuple)

    conn.commit()

###################################################################
# End of update functions                                         #
###################################################################

###################################################################
# Query functions. These will be used to access information in    #
# the various tables.                                             #
###################################################################

# Purpose: Gets the password for an associated customerusername.
# Will be used to verify a login.
def get_password_for_user(database_file, customer_username):
    conn = sqlite3.connect(database_file)
    
    curr = conn.cursor()
    curr.execute("SELECT Password FROM Customer WHERE Username=?", (customer_username,))

    password = curr.fetchone()

    if(password == None):
        return("USER DOES NOT EXIST")
    else:
        return(password[0])


# Purpose: Gets the basic info about a user
def get_customer_info(database_file, customer_username):
    conn = sqlite3.connect(database_file)

    curr = conn.cursor()
    curr.execute("SELECT Name,Birthday,Age FROM Customer")

    customer_data = curr.fetchone()

    return customer_data

# Purpose: Gets the password for an associated restaurant
def get_password_for_restaurant_username(database_file, restaurant_username):
    conn = sqlite3.connect(database_file)

    curr = conn.cursor()
    curr.execute("SELECT Password FROM Restaurant WHERE Username=?", (restaurant_username,))

    password = curr.fetchone()

    if(password == None):
        return("USER DOES NOT EXIST")
    else:
        return(password[0])

# Purpose: Gets the information about a certain food with a given ID
def get_info_about_food(database_file, food_id):
    conn = sqlite3.connect(database_file)

    curr = conn.cursor()
    curr.execute("SELECT * FROM Food WHERE FoodID=?", (food_id,))

    food_info = curr.fetchone()

    return(food_info)

# Purpose: Gets all the locations associated with a given username
def get_customer_locations(database_file, username):
    conn = sqlite3.connect(database_file)

    curr = conn.cursor()
    curr. execute("SELECT * FROM CustomerLocations WHERE Username=?", (username,))

    customer_location_info = curr.fetchall()

    return(customer_location_info)

# Purpose: Gets the menuID for a certain restaurant with a given username
def get_menu(database_file, restaurant_username):
    conn = sqlite3.connect(database_file)

    curr = conn.cursor()
    curr.execute("SELECT * FROM Menu WHERE RestaurantUsername=?", (restaurant_username,))

    menu_info = curr.fetchall()

    return(menu_info)

# Purpose: Gets all the diets for a given customer username
def get_diet_for_user(database_file, customer_username):
    conn = sqlite3.connect(database_file)

    curr = conn.cursor()
    curr.execute("SELECT * FROM Diet WHERE Username=?", (customer_username,))

    diet_info = curr.fetchall()

    return(diet_info)

# Purpose: Gets all the information for a restaurant with a given username
def get_restaurant_info(database_file, restaurant_username):
    conn = sqlite3.connect(database_file)

    curr = conn.cursor()
    curr.execute("SELECT State, City, StreetAddress, StoreName, PhoneNumber FROM Restaurant WHERE Username=?", (restaurant_username,))

    store_info = curr.fetchall()

    return(store_info)

# Purpose: Gets food that adheres to a certain diet
def get_adhere_to(database_file, diet_name):
    conn = sqlite3.connect(database_file)

    curr = conn.cursor()
    curr.execute("SELECT FoodID FROM AdhereTo WHERE DietName=?", (diet_name,))

    food_for_diet = curr.fetchall()

    return(food_for_diet)

# Purpoes: Gets all the food listed on a menu with the given ID
def get_food_on_menu(database_file, menuID):
    conn = sqlite3.connect(database_file)

    curr = conn.cursor()
    curr.execute("SELECT Name,CaloriesPerServing,Price FROM Food WHERE MenuID=?", (menuID,))

    food_on_menu = curr.fetchall()

    return(food_on_menu)

# Purpose: Gets all the food listed in an inventory with the given ID
def get_food_in_inventory(database_file, inventoryID):
    conn = sqlite3.connect(database_file)

    curr = conn.cursor()
    curr.execute("SELECT Name,QuantityInStock FROM Food WHERE inventoryID=?", (inventoryID,))

    food_in_inventory = curr.fetchall()

    return(food_in_inventory) 

# Purpose: Gets all food in the inventory that have more than zero items
def get_nonempty_food_from_inventory(database_file, inventoryID):
    conn = sqlite3.connect(database_file)

    curr = conn.cursor()
    curr.execute("SELECT Name,QuantityInStock FROM Food WHERE inventoryID=? AND QuantityInStock > 0", (inventoryID,) )

    nonempty_food_in_inventory = curr.fetchall()

    return(nonempty_food_in_inventory)

# Purpose: Gets the number of food items for a given menu
def get_number_of_food_items(database_file, menuID):
    conn = sqlite3.connect(database_file)

    curr = conn.cursor()

    curr.execute("SELECT COUNT(*) as numOfFoods FROM Food WHERE MenuID=?", (menuID,))

    numOfFoods = curr.fetchone()

    return(numOfFoods[0]) # Get the first argument of the tuple

initialize_database("ManyMenus.db")
