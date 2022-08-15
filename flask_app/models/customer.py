from flask_app.config.mysqlconnection import connectToMySQL
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Customer:
    db_name = "test_pizza_db"
    def __init__(self,data):
        self.id = data['id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        self.address = data['address'],
        self.city = data['city'],
        self.state = data['state'],
        self.password = data['password'],
        self.confirm_pw = data['confirm_pw'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "insert into customers (first_name, last_name, email, address, city, state, password, confirm_pw) \
            values(%(first_name)s,%(last_name)s,%(email)s, %(address)s, %(city)s, %(state)s, %(password)s, %(confirm_pw)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "select * from customers where id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "update customers set first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, address=%(address)s,\
        state=%(state)s, city=%(city)s where id = %(id)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)

    
    @classmethod
    def get_by_email(cls,data):
        query = "select * from customers where email= %(email)s"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_registration(customer):
        is_valid = True
        query = "select * from customers where email = %(email)s"
        results = connectToMySQL(Customer.db_name).query_db(query,customer)
        if len(results)>=1:
            flash("Email is taken", "register")
            is_valid=False
        if not EMAIL_REGEX.match(customer['email']):
            flash("Invalid email address please enter a different one","register")
            is_valid=False
        if len(customer['first_name']) < 3:
            flash("First name must be at least 3 characters","register")
            is_valid= False
        if len(customer['last_name']) < 3:
            flash("Last name must be at least 3 characters","register")
            is_valid= False
        if len(customer['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        if customer['password'] != customer['confirm_pw']:
            flash("Passwords don't match","register")
        return is_valid
