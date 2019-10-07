from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
# from bson.objectid import ObjectId
import os

app = Flask(__name__)  # sets up Flask variable

# Tells Flask how to find database
# client = MongoClient(host=f'{host}?retryWrites=false')
# db = client.get_default_database()
# playlists = db.playlists


@app.route('/')
def homepage():
    '''Shows homepage'''
    coffee_beans = [
        {'name': 'Arabica', 'location': 'Latin America',
            'smell': 'chocolatey', 'taste': 'varies'},
        {'name': 'Robusta', 'location': 'Africa',
         'smell': 'earthy', 'taste': 'bitter'},
        {'name': 'Liberica', 'location': 'Philippines',
         'smell': 'fruity', 'taste': 'smokey'},
        {'name': 'Arabica', 'location': 'Latin America',
         'smell': 'tart', 'taste': 'tart'}
    ]
    return render_template('homepage.html', coffee_beans=coffee_beans)


if __name__ == '__main__':
    app.run(debug=True)
