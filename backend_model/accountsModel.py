dictUser1 = {1: {'c_first_name': "Milena", 'c_last_name': "Ríos",
                'c_email': "milena.rios2@upr.edu", 'c_password': "aghetyeifc",
                'c_phone_number': 7871621782, 'c_status': 'active',
                'c_address_line_1': "Sector Barrios", 'c_address_line_2': "Calle 8 H20", 'c_city': "Hatillo", 'c_state': "Puerto Rico",
                 'c_zipcode': '00612', 'c_card_name': 'Milena Rios', 'c_card_type': 'Visa', 'c_exp_date': '2020-05-04',
                 'c_card_num': 1234123412341234}}

dictUser2 = {2: {'c_first_name': "Reina", 'c_last_name': "López",
                'c_email': "reina.lopez@upr.edu", 'c_password': "p1234567",
                'c_phone_number': 8981821728, 'c_status': 'active',
                'c_address_line_1': "Victor Azul", 'c_address_line_2': "Calle 9 A10", 'c_city': "Arecibo", 'c_state': "Puerto Rico",
                 'c_zipcode': '00610', 'c_card_name': 'Reina Lopez', 'c_card_type': 'Discover', 'c_exp_date': '2022-01-01',
                 'c_card_num': 1234123412341234}}

dictUser3 = {3: {'c_first_name': "Javier", 'c_last_name': "Quiñones",
                'c_email': "javier.quinones3@upr.edu", 'c_password': "pass1234",
                'c_phone_number': 7871231234, 'c_status': 'active',
                'c_address_line_1': "Vista Azulin", 'c_address_line_2': "Calle L11 L13", 'c_city': "Arecibor", 'c_state': "Puerto Ricor",
                 'c_zipcode': '00612', 'c_card_name': 'Javier Quiñones', 'c_card_type': 'Mastercard',
                 'c_exp_date': '2023-01-01', 'c_card_num': 1234123412341234}}

dictUser4 = {4: {'c_first_name': "Luis", 'c_last_name': "Ortega",
                'c_email': "luis@gmail.com", 'c_password': "pass1234",
                'c_phone_number': 7870000000, 'c_status': 'active',
                'c_address_line_1': "Vista", 'c_address_line_2': "Calle L11 L13", 'c_city': "Ciales", 'c_state': "Puerto Rico",
                 'c_zipcode': '00638', 'c_card_name': 'Luis Ortega', 'c_card_type': 'Mastercard',
                 'c_exp_date': '2023-01-01', 'c_card_num': 1234123412341234}}


def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


userList = dictUser1
userList = MagerDicts(userList, dictUser2)
userList = MagerDicts(userList, dictUser3)
userList = MagerDicts(userList, dictUser4)

def adduser():
    dictUser1 = add_user(dictUser1, 5, "Alice", "Smith", "alice@gmail.com", "alicespass", 7877877877, "active",
                         "Vistaaa", "Calle L11 L13", "CIales", "Puerto Rico", "00638",
                         "Alice Smith", "MasterCard", "2232323", 234567890)
    userList = MagerDicts(userList, dictUser5)




# Get all accounts
def getaccountsmodel():
    return userList


# Get the specific account requested
# In this case, we're requesting it via the key
def getaccountmodel(acc):
    acc = int(acc)
    for key, user in userList.items():
        if key == acc:
            return user

