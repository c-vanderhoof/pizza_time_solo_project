from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.order import Order
from flask_app.models.customer import Customer
from flask_app.models.pizza import Pizza


@app.route('/new/pizza')
def new_pizza():
    if 'customer_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['customer_id']
    }
    return render_template('custompizza.html', customer=Customer.get_by_id(data))






@app.route('/create/pizza', methods=['POST'])
def create_pizza():
    if 'customer_id' not in session:
        return redirect('/logout')
    data = {
        "size": request.form["size"],
        "crust": request.form["crust"],
        "toppings": request.form["toppings"],
    }
    Pizza.save(data)
    return redirect('/order')

@app.route('/edit/pizza/<int:id>')
def edit_pizza(id):
    if 'customer_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    customer_data = {
        "id": session['customer_id']
    }
    return render_template("custompizza.html", edit=Pizza.get_by_id(data), customer=Customer.get_by_id(customer_data))

@app.route('/update/pizza', methods= ['POST'])
def update_pizza():
    if 'customer_id' not in session:
        return redirect('/logout')
    if not Pizza.validate_pizza(request.form):
        return redirect('/new/pizza')
    data= {
        "size":request.form["size"],
        "crust": request.form["crust"],
        "toppings": request.form["toppings"]
    }
    Pizza.update(data)
    return redirect('/order')

@app.route ('/pizza/<int:id>')
def show_pizza(id):
    if 'customer_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    return render_template("custompizza.html")