import sqlite3
from sqlite3 import Error

# Purpose: Connects to an existing database file
# @param db_file: an existing database file to connect to
def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

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

        # Creates menu update table
        # Foreign key references to 
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

initialize_database("testDatabase.db")


