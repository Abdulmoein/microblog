import datetime
import os
from flask import Flask, render_template, request
from pymongo import MongoClient
# from dotenv import load_dotenv

# load_dotenv()


def create_app():
    app = Flask(__name__)

    # client = MongoClient(os.getenv('MONGODB_URI'))

    # app.db = client.microblog

    entries = [ 
    ]
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/home', methods=['GET', 'POST'])
    def home():
        # print([e for e in app.db.entries.find({})])
        if request.method == 'POST':
            entry_title = request.form.get('title')
            entry_content = request.form.get('content')
            formatted_date = datetime.datetime.today().strftime('%Y-%m-%d')
            entries.append((entry_title, entry_content, formatted_date))
            # app.db.entries.insert_one({'title': entry_title, 'content': entry_content, 'date': formatted_date}) # save in our mongodb cloud
        
        entries_with_date = [
            (
                entry[0], # when we receive the data it's not a list of tiples it's a courcer object like a list of dictionary that is mean if ineed to access for a value i must use eachlist['key'] to i can get a value
                entry[1],
                entry[2],
                datetime.datetime.strptime(entry['date'], '%Y-%m-%d').strftime('%b-%d')
                
            )
            for entry in entries_with_date 
        ]
        
    # make a loop inside the object docs i mean
    
        return render_template('home.html', entries = entries_with_date)
    return app

