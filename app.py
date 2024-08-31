from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Iniciando a aplicação e o banco
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///e-commerce.db'
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)


@app.route('/')
def hello_word():
    return 'Hello word'


if __name__ == "__main__":
    app.run(debug=True)
