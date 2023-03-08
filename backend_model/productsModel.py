# Done in array instead of dictionaries to portray the differences between dictionaries and arrays
# Database tuples are normally received in an array
productList = [['1', 'Ware Hamster Cage Set', 'Ware', 'This Ware Hamster cage Includes Free Water Bottle, Exercise Wheel, Food Dish & Hamster Hide-Out Large Hamster Cage Measures'         , 'Enclosures', '60', '5', 'HamsterCage.png', 'Teal'],
               ['2', 'Higgins Sunburst Gourmet Blend', 'Higgins', 'This Higgins Sunburst Gourmet Food Mix Is For Hamsters And Gerbils .'       , 'Food', '10', '15', 'HamsterFood.png', 'N/A'],
               ['3', 'Clear Run-About Exercise Ball', 'Kaytee', 'This Kaytee 5" Clear Run-About Exercise Ball Is For Pet Dwarf Hamsters & Mice.'         , 'Toys', '4', '6', 'HamsterToy.png', 'Other'],
               ['4', 'DomeTop Bird Cage', 'WA&E', 'This DomeTop Bird Cage Has Bird Proof Front Door & Feeder Door Lock With A Slide-Out Grill & Tray For Easy Cleaning.'               , 'Enclosures', '525', '2', 'BirdCage.jpg', 'White'],
               ['5', 'Higgins Sunburst Gourmet Food Mix', 'Higgins', 'This Higgins Sunburst Gourmet Food Mix is filled with all the necessary vitamins for your pet.'              , 'Food', '9', '15', 'BirdFood.jpg', 'N/A'],
               ['6', 'Cage Swing Toy', 'Kaytee', 'This Cage Swing Toy is guaranteed to keep your parrot occupied for hours'               , 'Toys', '6', '6', 'BirdToy.jpg', 'Wood'],
               ['7', 'Tetra Aquatic Turtle Deluxe Tank', 'Tetra', 'This Tetra Aquatic Turtle Deluxe Tank Of 20 Gallons, Includes Filters And Heating Lamps'         , 'Enclosures', '50', '2', 'TurtleTank.jpg', 'N/A'],
               ['8', 'Tetra USA Reptomin', 'Tetra', 'Tetra USA Reptomin Contains high-quality proteins and essential amino acids topPromote healthy growth'            , 'Food', '10', '15', 'TurtleFood.jpg', 'N/A'],
               ['9', 'Turtle/Tortoise Treat Ball Toy', 'Tirifer', 'The tortoise feeder ball toy is great for feeding your turtle kinds of food, such as fresh vegetables and fruit. It is healthier and fresher for your turtle to keep treats off the floor. ', 'Toys', '13', '6', 'TurtleToy.jpg', 'Blue'],
               ['10', 'ZENY Plastic Dog House', 'Zeny', 'Water resistant dog kennel for Dogs, for outside use and resistant to all types of weathers'              , 'Enclosures', '81', '3', 'DogHouse.jpg', 'Blue'],
               ['11', 'Purina ONE Dry Dog Food, Chicken & Rice Formula', 'Purina', 'Purina ONE chicken and rice dog food offers a microbiome balance and a SmartBlend of high-quality ingredients, including prebiotic fiber for dogs, to help your pal live up to his full potential '                , 'Food', '25', '15', 'DogFood.jpg', 'N/A'],
               ['12', 'Crinkle Duck Dog Toy', 'Best Pet Supplies', 'This dog crinkle toys no stuffing ducks provide your four-legged best friend with an interactive chew toy that makes noise, keeps them engaged, and is gentler on teeth, gums, and dental health '                      , 'Toys', '6', '6', 'DogToyDuck.jpg', 'Yellow'],
               ['13', 'Cat Tree Tower', 'Zeny', ' This ZENY cat tree is made from highly durable particleboard wood, wrapped with soft flannelette finish to keep your cats warmed and cozy.'              , 'Enclosures', '60', '3', 'CatHouse.jpg', 'Grey'],
               ['14', 'Natural Dry Cat Food', 'Purina', 'Its a Natural Dry Cat Food Blended With Real Salmon', 'Food', '7', '15', 'CatFood.jpg', 'N/A'],
               ['15', ' Cat Wand Toy', 'MeoHui', 'This is a two piece retractable Cat Wand Toy and 9 piece Cat Feather addon', 'Toys', '12', '6', 'CatToys.jpg', 'Other'],
               ['16', 'Aqueon Aquarium Fish Tank', 'Aqueon', 'This is a 10 galon Aqueon Aquarium Fish Tank Starter Kit with LED Lighting', 'Enclosures', '85', '3', 'FishTank.jpg', 'N/A'],
               ['17', 'Min Tropical Flakes Fish Food', 'Tetra', 'TetraMin(R) Tropical Flakes continue to offer a complete diet with a clear water formula thats easier to digest, leaving less waste in the tank.', 'Food', '8', '15', 'FishFood.jpg', 'N/A'],
               ['18', 'Fish Tanks Plants and Caves decorations', 'Aqueon', 'This is an aquarium fish tank with plastic plants and cave rock decorations decor set of 7 pieces', 'Toys', '10', '6', 'FishToy.jpg', 'Other']]


def getProductsModel():
    return productList


# Find the specific product given the ID, found in element 0 of the sub-arrays
def getsingleproductmodel(prodID):
    for product in productList:
        if product[0] == prodID:
            return product

Loop = True
def Addproducts(name, price, stock, colors, desc, brand, category, image):
    global Loop

    while Loop:
        new_item = [str(len(productList) + 1), name, brand, desc, category, str(price), str(stock), image, colors]
        productList.append(new_item)
        Loop = False
