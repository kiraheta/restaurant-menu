from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    """Returns all restaurants"""
    return "This page will show all my restaurants"

@app.route('/restaurants/new')
def newRestaurant():
    """Creates a new restaurant"""
    return "This page will be for making a new restaurant"

@app.route('/restaurants/restaurant_id/edit')
def editRestaurant():
    """Edits a restaurant"""
    return "This page will be for editing restaurants"

@app.route('/restaurants/restaurant_id/delete')
def deleteRestaurant():
    """Deletes a restaurant"""
    return "This page will be for deleting restaurants"


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port = 5000)
