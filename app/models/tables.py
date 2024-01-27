# arquivo tables, responsável pelas tabelas do banco de dados

from app import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    cart = db.relationship("Cart", backref="user")

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True)
    shoe = db.Column(db.String)
    size = db.Column(db.String)
    quantity = db.Column(db.String)
    price = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, shoe, size, quantity, price, user_id):
        self.shoe = shoe
        self.size = size
        self.quantity = quantity
        self.price = price
        self.user_id = user_id