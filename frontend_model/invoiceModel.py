
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False

orderDict = {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibo Puerto Rico, 00614",
    "total": 70.00,
    "payment_method": "Mastercard"
}

#productDict1 = {"1":{
#    "image": 'ruko_f11_pro.jpg',
#    "name": 'F11 Pro',
 #   "brand": 'Ruko',
  #  "price": 399.00,
   # "quantity": 1,
    #"total_price": 399.00
#}}

dictitems1 = {'1': {'name': "Ware Hamster Cage Set", 'price': 60.00, 'quantity': 1, 'total_price': 0,
                  'stock': 5, 'brand': "Ware", 'desc': "This Ware Hamster cage Includes Free Water Bottle, Exercise Wheel, Food Dish & Hamster Hide-Out Large Hamster Cage Measures'",
                  'image': "HamsterCage.png", 'color': "Teal", 'category': "Enclosure"}}

dictitems2 = {'2': {'name': "Higgins Sunburst Gourmet Blend", 'price': 10.00, 'quantity': 1, 'total_price': 0,
                  'stock': 15, 'brand': "Higgins", 'desc': "This Higgins Sunburst Gourmet Food Mix Is For Hamsters And Gerbils.",
                  'image': "HamsterFood.png", 'color': "N/A", 'category': "Food"}}

products = dictitems1
products = MagerDicts(products, dictitems2)


def getOrderModel():
    return orderDict


def getProductsModel():
    return products
