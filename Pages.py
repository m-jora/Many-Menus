class RestaurantCreateAccount:
    def __init__(self):
        return

class CustomerCreateAccount:
    def __init__(self):
        return

class RestaurantUpdateInfo:
    def __init__(self):
        return

class RestaurantUpdateInventory:
    def __init__(self):
        return

class RestaurantUpdateMenu:
    def __init__(self):
        return

class UpdateUserInfo:
    def __init__(self):
        return

class Login:
    def __init__(self):
        return


class Browse:
    def __init__(self):
        return 
 

# Purpose: Validates a password for a given user
def validate_password(database_file, username, entered_password):
    actualPassword = SQLWrapper.get_password_for_user(database_file, username)

    if(actualPassword != entered_password):
        return False
    else:
        return True
