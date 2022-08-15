from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.customer import Customer
from flask_app.models.order import Order
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not Customer.validate_registration(request.form):
        return redirect('/')
    data= {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "address": request.form["address"],
        "city": request.form["city"],
        # "state" : request.form["state"],
        "password": bcrypt.generate_password_hash(request.form["password"])
    }
    id = Customer.save(data)
    session['customer_id'] = id
    return redirect('/home')


@app.route('/update/customer', methods=['POST'])
def update():
    if not Customer.validate_update(request.form):
        return redirect ('/account')
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "address": request.form["address"],
        "city": request.form["city"],
        "state" : request.form["state"]
    }
    id = Customer.save(data)
    session['customer_id'] = id
    return redirect('/account')

@app.route('/login', methods=['POST'])
def login():
    customer = Customer.get_by_email(request.form)

    if not customer:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(customer.password, request.form["password"]):
        flash("Invalid passowrd" "login")
        return redirect('/')
    session['customer_id'] = customer.id
    return redirect('/home')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/account/<int:id>')
def show_account(id):
    if 'customer_id' not in session:
        return redirect('/logout')
    data= {
        'id':session['customer_id']
    }
    return render_template('account.html', customer=Customer.get_by_id(data))

@app.route('/home')
def home():
    if 'customer_id' not in session:
        return redirect('/logout')
    data= {
        'id':session['customer_id']
    }
    return render_template('home.html')