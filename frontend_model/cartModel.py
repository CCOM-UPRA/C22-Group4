from flask import session

# Dictionary uniter
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


dictitems1 = {'1': {'name': "Ware Hamster Cage Set", 'price': 60.00, 'quantity': 1, 'total_price': 0,
                  'stock': 5, 'brand': "Ware", 'desc': "This Ware Hamster cage Includes Free Water Bottle, Exercise Wheel, Food Dish & Hamster Hide-Out Large Hamster Cage Measures'",
                  'image': "HamsterCage.png", 'color': "Teal", 'category': "Enclosure"}}

dictitems2 = {'2': {'name': "Higgins Sunburst Gourmet Blend", 'price': 10.00, 'quantity': 1, 'total_price': 0,
                  'stock': 15, 'brand': "Higgins", 'desc': "This Higgins Sunburst Gourmet Food Mix Is For Hamsters And Gerbils.",
                  'image': "HamsterFood.png", 'color': "N/A", 'category': "Food"}}

dicts = [dictitems1, dictitems2]
totaltotalprice =0

for d in dicts:
    for key in d:
        d[key]['total_price'] = d[key]['price'] * d[key]['quantity']

def getCartModel():
    # Checking if cart is in session or not and adding the dictionaries to it
    if 'cart' in session:
        session['cart'] = MagerDicts(session['cart'], dictitems1)
    else:
        session['cart'] = dictitems1

    if 'cart' in session:
        session['cart'] = MagerDicts(session['cart'], dictitems2)
    else:
        session['cart'] = dictitems2
    return


def addCartModel():
    # make changes to cart here
    # not in use at the moment
    return


def deleteCartItemModel(select):
    # delete item from cart
    # not in use at the moment
   # list_of_dicts = [dictitems1, dictitems2]
    #del list_of_dicts[int(select)]

    #Quiero que si el carrito es en session y el usuario elije el carrito 1 que se borre
    #Tengo que encontrar una manera de borrar el carrito del dictionario
    #sif 'cart' in session and select == 1:
        #session['cart'] = MagerDicts(session['cart'], dictitems1)

    return



