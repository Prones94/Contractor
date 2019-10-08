from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)  # sets up Flask variable

# Tells Flask how to find database
host = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/coffee_beans")
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
print(db)
coffee_beans = db.coffee_beans
print(coffee_beans)

if coffee_beans.find_one({'name': 'Arabicus'}):
    print('we not gonna insert those items')
else:
    multi_beans = [{"name": "Arabicus",
                    "location": "Latin America",
                    "smell": "Chocolate",
                    "taste": "Varies by bean"},
                   {"name": "Robusta",
                    "location": "Africa",
                    "smell": "Earthy",
                    "taste": "Bitter"},
                   {"name": "Liberica",
                    "location": "Philippines",
                    "smell": "Fruity Aroma",
                    "taste": "Smokey, Whole"},
                   {"name": "Excelsa",
                    "location": "Southeast Asia",
                    "smell": "Tart",
                    "taste": "Fruity, Tart"}]
    coffee_beans.insert_many(multi_beans)  # insert into db


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
    beaninfo = {
        'name': request.form.get('name'),
        'location': request.form.get('location'),
        'smell': request.form.get('smell'),
        'taste': request.form.get('taste')
    }
    coffee_id = coffee_beans.insert_one(beaninfo).inserted_id
    return redirect(url_for('show_list', coffee_id=coffee_id))


@app.route('/coffee_beans/<beans_id>')
def show_list(beans_id):
    '''Shows individual bean information'''
    new_bean = coffee_beans.find_one({'_id': ObjectId(beans_id)})
    return render_template('show-beans.html', new_bean=new_bean)


@app.route('/coffee_beans/{{bean._id}}/edit')
def edit_info(beans_id):
    '''Shows form to edit information for coffee bean information.'''
    bean_info = coffee_beans.find_one({'_id': ObjectId(beans_id)})
    return render_template('edit-beans.html', bean_info=bean_info)

@app.route('/coffee_beans/<beans_id>',methods=['POST'])
def update_beancart(beans_id):
    '''This will submit the updated cart'''
    new_cart = {
        'name': request.form.get('name'),
        'location': request.form.get('location'),
        'smell': request.form.get('smell'),
        'taste': request.form.get('taste')
    }
    coffee_beans.update_one(
        {'_id':ObjectId(beans_id)},
        {'$set': new_cart})
    return redirect(url_for('homepage', beans_id=beans_id))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
