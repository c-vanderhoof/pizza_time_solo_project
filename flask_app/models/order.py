from flask_app.config.mysqlconnection import connectToMySQL


class Order:
    db_name = "test_pizza_db"

    def __init__(self,data):
        self.id = data['id'],
        self.customer_id = data['customer_id'],
        self.created_at = data['created_at']
        self.pizza_id = data['pizza_id'],

    @classmethod
    def get_by_customer_id(cls,data):
        query = "select * from orders where customer_id = %(customer_id)s"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def join_pizza(cls):
        query = "select * from orders join pizzas on pizzas.id = orders.pizza_id"
        return connectToMySQL(cls.db_name).query_db(query)

    @classmethod
    def join_sides(cls):
        query= "select* from orders join sides on sides.id = orders.side_id"
        return connectToMySQL(cls.db_name).query_db(query)

    @classmethod
    def get_by_id(cls,data):
        query = "select * from orders where id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM orders WHERE id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def save(cls,data):
        query = "insert into orders (customer_id, pizza_id) values (%(customer_id)s, %(pizza_id)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def join_order_by_customer_id(cls,data):
        query = "select * from orders join customers on customers.id = orders.customer_id where customers.id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query,data)


# not validating orders because there is no form to validate, all data included in this table should have already been validated.



