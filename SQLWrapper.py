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
            CREATE TABLE IF NOT EXISTS Restaurant (
                State TEXT NOT NULL,
                City TEXT NOT NULL,
                StreetAddress TEXT NOT NULL,
                Password TEXT NOT NULL,
                Username TEXT PRIMARY KEY,
                StoreName TEXT NOT NULL,
                PhoneNumber TEXT NOT NULL
            )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS MenuUpdate (
                LastUpdated TEXT PRIMARY KEY,
                MenuID TEXT,
                RestaurantUsername TEXT,
                FOREIGN KEY(RestaurantUsername) REFERENCES Username(Restaurant)
            )""")        

        create_table(database, """
            CREATE TABLE IF NOT EXISTS Menu(
                MenuID TEXT PRIMARY KEY,
                RestaurantUsername TEXT,
                FOREIGN KEY(RestaurantUsername) REFERENCES RestaurantUsername(Restaurant)
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
                Password TEXT NOT NULL,
                Birthday TEXT NOT NULL,
                Age TEXT NOT NULL
            )""")

        create_table(database, """
            CREATE TABLE IF NOT EXISTS CustomerLocations(
                Username TEXT PRIMARY KEY,
                City TEXT NOT NULL,
                State TEXT NOT NULL,
                FOREIGN KEY(Username) REFERENCES Username(Restaurant)
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
                ID TEXT PRIMARY KEY,
                CaloriesPerServing INTEGER,
                Name TEXT,
                Price TEXT
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
                FOREIGN KEY(RestaurantUsername) REFERENCES RestaurantUsername(Restaurant)
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

    sqlCommand = '''INSERT INTO Customer(Username,Password,Name,Birthday,Age) VALUES (?,?,?,?,?)'''

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

    sqlCommand = '''INSERT INTO Food(ID, CaloriesPerServing, Name, Price, QuanitityInStock, InStock) VALUES (?,?,?,?,?,?)'''

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

###################################################################
# End of insert functions                                         #
###################################################################


###################################################################
# The following functions are SQL commands for deleting data in   #
# the various tables of our database. Not all data is deletable.  #
# We will not allow users to delete their accounts.               #
###################################################################

def delete_food(database_file, FoodID):
    conn = sqlite3.connect(database_file)

    sqlCommand = '''DELETE FROM Food WHERE ID=?'''
    curr = conn.cursor

    curr.execute(sqlCommand, (FoodID,))
    conn.commit()

# Where DietName is the PK of the Diet table
def delete_diet(database_file, DietName):
    conn = sqlite3.connect(database_file)

    sqlCommand = 'DELETE FROM Diet WHERE DietName=?'
    curr = conn.cursor()

    curr.execute(sqlCommand, (DietName,))
    conn.commit()

def delete_customer_location(database_file, customerLocationsID):
    conn = sqlite3.connect(database_file)

    sqlCommand = 'DELTE FROM CustomerLocations WHERE customerLocationsID=?'

    curr = conn.cursor()

    curr.execute(sqlCommand, (customerLocationsID,))
    conn.commit()


###################################################################
# End of delete functions                                         #
###################################################################

initialize_database("testDatabase.db")
