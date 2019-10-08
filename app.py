from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)  # sets up Flask variable

# Tells Flask how to find database
host = os.environ.get("MONGODB_URI","mongodb://localhost:27017/coffee_beans")
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
print (db)
coffee_beans = db.coffee_beans
print(coffee_beans)

if coffee_beans.find_one({'name': 'Arabicus'}):
    print('we not gonna insert those items')
else:
    multi_beans = [{"name":"Arabicus",
                "location":"Latin America",
                "smell":"Chocolate",
                "taste":"Varies by bean"},
                {"name":"Robusta",
                "location":"Africa",
                "smell":"Earthy",
                "taste":"Bitter"},
                {"name":"Liberica",
                "location":"Philippines",
                "smell":"Fruity Aroma",
                "taste":"Smokey, Whole"},
                {"name":"Excelsa",
                "location":"Southeast Asia",
                "smell":"Tart",
                "taste":"Fruity, Tart"}]
    coffee_beans.insert_many(multi_beans) # insert into db 
@app.route('/')
def homepage():
    '''Shows homepage'''
         
    return render_template('index.html', coffee_beans=coffee_beans.find())

@app.route('/new_beans')
def new_beans():
    """Creating new bean form"""
    return render_template('submit-new.html')

@app.route('/beans', methods=['POST'])
def beans_submit():
    '''Displays form to make new bean cart'''
    shopping_beans = {
        'name': request.form.get('name'),
        'location': request.form.get('location'),
        'smell': request.form.get('smell'),
        'taste': request.form.get('taste')
    }
    coffee_beans.insert_one(shopping_beans)
    return redirect(url_for('index'))





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))