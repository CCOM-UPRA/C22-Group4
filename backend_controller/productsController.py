from flask import redirect

from backend_model.productsModel import *

def getProducts():
    products = getProductsModel()
    return products


def getsingleproduct(prodID):
    return getsingleproductmodel(prodID)

def addproductscontroller(name, price, stock, colors, desc, brand, category, image):
    result = Addproducts(name=name, price=price, stock=stock, colors=colors, desc=desc, brand=brand, category=category, image=image)
    if result is 1:
        return redirect("/products")
    else:
        return redirect("/products")
