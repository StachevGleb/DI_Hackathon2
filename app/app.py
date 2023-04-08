from paintings_data import retrieve_all_paintings, retrieve_requested_paintings
from flask import Flask, render_template, url_for, redirect


app = Flask(__name__)

cart_items = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/paintings')
def paintings():
    all_paintings = retrieve_all_paintings()
    return render_template('paintings.html', paintings=all_paintings)

@app.route('/paintings/<painting_id>')
def painting(painting_id):
    painting = retrieve_requested_paintings(painting_id)[0]
    print(painting)
    return render_template('paint.html', painting_details=painting)

@app.route('/gallery')
def cart():
    return render_template('cart.html', cart_items=cart_items)

@app.route('/add_painting_to_gallery/<painting_id>')
def add_to_gallery(painting_id):
    painting = retrieve_requested_paintings(painting_id)[0]
    cart_items.append(painting)
    return redirect(url_for('cart'))

@app.route('/delete_painting_from_gallery/<painting_id>')
def delete_from_cart(painting_id):
    for el in cart_items:
        if el['Id'] == painting_id:
            cart_items.pop(cart_items.index(el))
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)