from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
# from bson.objectid import ObjectId
import os

app = Flask(__name__)


@app.route('/')
def homepage():
    '''Shows homepage'''
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)