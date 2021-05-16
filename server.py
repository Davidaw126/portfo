from flask import Flask,render_template, request
import csv

app = Flask(__name__)
print(__name__)

@app.route('/index.html')
def hello_world():
    return render_template('index.html')

@app.route('/<page_name>')
def page(page_name):
    return render_template(page_name)

@app.route('/submit_form',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return "GG"
        except:
            return "did not save to database"
    else:
        return "something went wrong"


def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=",", quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])