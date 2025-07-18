#!/usr/bin/python3
"""
Flask app to display items from a JSON file using Jinja2 templating
"""

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/items")
def show_items():
    try:
        with open("items.json", "r") as file:
            data = json.load(file)
            items = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items = []

    return render_template("items.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)
