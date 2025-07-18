#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Function to read from JSON
def read_json():
    with open("products.json", "r") as f:
        return json.load(f)

# Function to read from CSV
def read_csv():
    products = []
    with open("products.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products

# Function to read from SQLite
def read_sql():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })
    return products

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)
    error = None
    data = []

    try:
        if source == "json":
            data = read_json()
        elif source == "csv":
            data = read_csv()
        elif source == "sql":
            data = read_sql()
        else:
            error = "Wrong source"
            return render_template("product_display.html", error=error)

        if product_id is not None:
            filtered = [p for p in data if p["id"] == product_id]
            if not filtered:
                error = "Product not found"
                return render_template("product_display.html", error=error)
            data = filtered

    except Exception as e:
        error = f"An error occurred: {str(e)}"
        return render_template("product_display.html", error=error)

    return render_template("product_display.html", products=data)
