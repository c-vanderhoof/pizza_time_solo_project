from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Pizza:
    db_name = "test_pizza_db"
    
    def __init__(self,data):
        self.id = data["id"],
        self.name = data["name"],
        self.size = data["size"],
        self.crust = data["crust"],
        self.price = data["price"],
        self.toppings = data["toppings"]

    @classmethod
    def save(cls,data):
        query = "insert into pizzas (size, crust, toppings,) \
            values (%(size)s, %(crust)s, %(toppings)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def join_order(cls):
        query = "select * from pizzas join orders on orders.id = pizzas.order_id"
        return connectToMySQL(cls.db_name).query_db(query)

    @classmethod
    def get_all_toppings(cls,data):
        query= "select toppings from pizzas"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "update pizzas set crust=%(crust)s, size=%(size)s, toppings=%(toppings)s where id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query,data)


