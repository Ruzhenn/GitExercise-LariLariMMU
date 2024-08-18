from flask import Flask

app = Flask(__name__)

#sample
categories = [
    {'id': 1, 'name': 'Electronics'},
    {'id': 2, 'name': 'Clothing'},
    {'id': 3, 'name': 'Books'}
]

# Route to display the product submission form
@app.route('/submit', methods=['GET', 'POST'])