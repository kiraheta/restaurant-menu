from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    """Returns all restaurants"""
    return "This page will show all my restaurants"

@app.route('/restaurant/new')
def newRestaurant():
    """Creates a new restaurant"""
    return "This page will be for making a new restaurant"

@app.route('/restaurant/restaurant_id/edit')
def editRestaurant():
    """Edits a restaurant"""
    return "This page will be for editing restaurants"

@app.route('/restaurant/restaurant_id/delete')
def deleteRestaurant():
    """Deletes a restaurant"""
    return "This page will be for deleting restaurants"

@app.route('/restaurant/restaurant_id')
@app.route('/restaurant/restaurant_id/menu')
def showMenu():
    """Returns a restaurant's menu"""
    return "This page is the menu for a restaurant"

@app.route('/restaurant/restaurant_id/menu/new')
def newMenuItem():
    """Creates a new restaurant menu item"""
    return "This page is for making a new restaurant menu item"

@app.route('/restaurant/restaurant_id/menu/menu_id/edit')
def editMenuItem():
    """Edits a new restaurant menu item"""
    return "This page is for editing a restaurant menu item"

@app.route('/restaurant/restaurant_id/menu/menu_id/delete')
def deleteMenuItem():
    """Delete a new restaurant menu item"""
    return "This page is for deleting a restaurant menu item"


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port = 5000)
