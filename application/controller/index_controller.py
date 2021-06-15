from application import app
from flask import render_template, request
from application.model.dao.product_dao import ProductDAO

product = ProductDAO()
product_list = product.findAll()
cart_list = product.addCart()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', product_list=product_list, cart_list=cart_list)

@app.route("/products", methods=['GET'])
def products():
    return render_template('product.html', product_list = product_list)

@app.route('/insert/<int:id>')
def insert(id:int):
    for product in product_list:
        if id == product._id:
            cart_list.append(product)
        return render_template('index.html', cart_list=cart_list)

@app.route('/remove/<int:id>')
def remove(id:int):
    for product in cart_list:
        if id == product._id:
            cart_list.remove(product)
        return render_template('index.html', cart_list=cart_list)