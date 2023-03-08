from frontend_model.shopModel import *


def getProducts():
    products = getProductsModel()
    return products


def getBrands():
    return getBrandsModel()

def getPrices(Select):
    return getPricesModel(Select)


def getColors():
    return getColorsModel()

def getCategories():
    return getCategoriesModel()