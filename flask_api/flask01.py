'''
Goals of the script - Ensure your application has:
    • at least two endpoints
    • at least one of your endpoints should return JSON
    • has ONE additional feature from the following list:
        - one endpoint returns HTML that uses jinja2 logic
        - requires a session value be present in order to get a response
        - writes to/reads from a cookie
        - reads from/writes to a sqlite3 database
'''

from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pepper')
def pepper():
    return render_template('pepper.html')

@app.route('/peach')
def peach():
    return render_template('peach.html')

@app.route('/my_cat', methods=["GET", "POST"])
def my_cat(data={}):
    if request.method == 'POST':
        data = request.form
        return render_template('my_cat.html', cat_info=data)

    return json.dumps({"cat_name": None, "fav_food": None, "fav_hobby": None, "fun_fact": None})

@app.route('/new_cat')
def new_cat():
    return render_template('new_cat.html')

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)