from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#sample dummy data hereee
categories = [
    {"id": 1, "name": "Electronics"},
    {"id": 2, "name": "Clothing"},
    {"id": 3, "name": "Books"},
]


#route to display the product submission form (this at main webpage for now only cuz just testing)
@app.route("/", methods=["GET", "POST"])
def submit_product():
    if request.method == "POST":
        #retrieve form data
        title = request.form["title"]
        description = request.form["description"]
        price = request.form["price"]
        quantity = request.form["quantity"]
        condition = request.form["condition"]
        category_id = request.form["category_id"]
        file = request.files["file"]

        #process the form data 
        #juz for demo purposes, we're just printing the data.
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Price: {price}")
        print(f"Quantity: {quantity}")
        print(f"Condition: {condition}")
        print(f"Category ID: {category_id}")
        if file:
            print(f"File name: {file.filename}")

        #redirect a success template after processing (a flash message can be added here later on)
        return redirect(url_for("submit_product"))

    #render the html template with the categories data
    return render_template("submit_product.html", categories=categories)

#for database can use sqlite3 or SQLAlchemy later on


if __name__ == "__main__":
    app.run(debug=True, port=8000)
