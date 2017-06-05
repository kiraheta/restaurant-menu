from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    """Returns all restaurants"""
    return render_template('restaurants.html',restaurant = restaurant)

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


#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'},
{'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [
{'name':'Cheese Pizza', 'description':'made with fresh cheese',
'price':'$5.99','course' :'Entree', 'id':'1'},
{'name':'Chocolate Cake','description':'made with Dutch Chocolate',
'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad',
'description':'with fresh organic vegetables','price':'$5.99',
'course':'Entree','id':'3'},{'name':'Iced Tea',
'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},
{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach',
'price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese',
'price':'$5.99','course' :'Entree'}


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port = 5000)
