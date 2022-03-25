# import necessary modules
from flask import Flask, request, render_template
from pymongo import MongoClient

# define the mongodb client
client = MongoClient(port=27017)
# define the database to use
db = client.student_data

# define the flask app
app = Flask(__name__)


# define the home page route
@app.route('/')
def hello_world():
    return render_template("index.html")



@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/change')
def change():
    return render_template('change&challenges.html')

@app.route('/happiness')
def happy():
    return render_template('happiness&fun.html')

@app.route('/healthy')
def healthy():
    return render_template('healthyhabits.html')

@app.route('/lettinggo')
def lettinggo():
    return render_template('lettinggo.html')

@app.route('/relationship')
def love():
    return render_template('loverelationships.html')



@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')


# route to get data from html form and insert data into database
@app.route('/data', methods=["GET", "POST"])
def data():
    data = {}
    if request.method == "POST":
        data['Name'] = request.form['name']
        data['Email'] = request.form['email']
        data['Mob'] = request.form['mobile']
        data['Age'] = request.form['age']
        data['DOB'] = request.form['dob']
        # data['Department'] = request.form['department']
        data['Gender'] = request.form['gender']
        data['Address'] = request.form['address']
        data['Pincode'] = request.form['pincode']
        lang = []
        for i in "1234567":
            try:
                if request.form['language' + i] != "":
                    lang.append(request.form['language' + i])
            except Exception as e:
                pass
        data['Language'] = lang
        db.studentData.insert_one(data)

    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=False)