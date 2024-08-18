from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class Product(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(200), nullable=False)
   price = db.Column(db.Numeric(10, 2), nullable=False)
   description = db.Column(db.Text, nullable=False)
   image_filename = db.Column(db.String(120), nullable=True)
   is_sold_out = db.Column(db.Boolean, default=False)

class Appoinment(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   product_id = db.Column(db.Integer , db.ForeignKey('product.id'), nullable=False)
   user_name = db.Column(db.String(100), nullable=False)
   appoinment_date = db.Column(db.DateTime, nullable=False)
   product = db.relationship('Product', backref=db.backref('appoinments', lazy=True))
