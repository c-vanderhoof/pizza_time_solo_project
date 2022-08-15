from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.order import Order
from flask_app.models.customer import Customer
from flask_app.models.pizza import Pizza


@app.route('/show/order/<int:id>')
def show_order():
    if 'customer_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['customer_id']
    }
    return render_template('home.html', customer=Customer.get_by_id(data), order=Order.join_order_by_customer_id(data))

@app.route('/delete/order/<int:id>')
def delete_order(id):
    if 'customer_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Order.delete(data)
    return redirect('/home')


# customer order relationship will be called by customer_id in session

@app.route('/new/order', methods=['POST'])
def new_order():
    if 'customer_id' not in session:
        return redirect('/logout')
    data = {
        "customer_id": request.form["customer_id"],
        "pizza_id": request.form["pizza_id"],
    }
    Order.save(data)
    return redirect('/order')







