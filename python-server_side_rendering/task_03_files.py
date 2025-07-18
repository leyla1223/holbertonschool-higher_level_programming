#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def load_json_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def load_csv_data(filename):
    products = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        try:
            products = load_json_data('products.json')
        except FileNotFoundError:
            return render_template("product_display.html", error="JSON file not found", products=None)
    elif source == 'csv':
        try:
            products = load_csv_data('products.csv')
        except FileNotFoundError:
            return render_template("product_display.html", error="CSV file not found", products=None)
    else:
        return render_template("product_display.html", error="Wrong source", products=None)

    # Filter by id if provided
    if product_id is not None:
        products = [p for p in products if p["id"] == product_id]
        if not products:
            return render_template("product_display.html", error="Product not found", products=None)

    return render_template("product_display.html", products=products, error=None)


if __name__ == "__main__":
    app.run(debug=True)
