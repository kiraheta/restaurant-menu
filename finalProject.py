from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


#Connect to Database and create database session
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#Show all restaurants
@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
    """Returns all restaurants"""
    restaurants = session.query(Restaurant).order_by(asc(Restaurant.name))
    return render_template('restaurants.html', restaurants = restaurants)

@app.route('/restaurant/new', methods=['GET','POST'])
def newRestaurant():
    """Creates a new restaurant"""
    if request.method == 'POST':
      newRestaurant = Restaurant(name = request.form['name'])
      session.add(newRestaurant)
      flash('New Restaurant %s Successfully Created' % newRestaurant.name)
      session.commit()
      return redirect(url_for('showRestaurants'))
    else:
      return render_template('newRestaurant.html')

@app.route('/restaurant/restaurant_id/edit')
def editRestaurant():
    """Edits a restaurant"""
    return render_template('editRestaurant.html',restaurant = restaurant)

@app.route('/restaurant/restaurant_id/delete')
def deleteRestaurant():
    """Deletes a restaurant"""
    return render_template('deleteRestaurant.html',restaurant = restaurant)

@app.route('/restaurant/restaurant_id')
@app.route('/restaurant/restaurant_id/menu')
def showMenu():
    """Returns a restaurant's menu"""
    return render_template('menu.html',restaurant = restaurant)




@app.route('/restaurant/<int:restaurant_id>/menu/new', methods = ['GET','POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(
            name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showRestaurants', restaurant_id=restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant_id=restaurant_id)

    # """Creates a new restaurant menu item"""
    # return render_template('newMenuItem.html',restaurant = restaurant)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit',
methods = ['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showRestaurants', restaurant_id=restaurant_id))
    else:
        return render_template(
            'editMenuItem.html', restaurant_id=restaurant_id, menu_id=menu_id,
            item=editedItem)

    # """Edits a new restaurant menu item"""
    # return render_template('editMenuItem.html',restaurant = restaurant)

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showRestaurants', restaurant_id=restaurant_id))
    else:
        return render_template('deleteconfirmation.html', item=itemToDelete)

    # """Delete a new restaurant menu item"""
    # return render_template('deleteMenuItem.html',restaurant = restaurant)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0',port = 5000)
