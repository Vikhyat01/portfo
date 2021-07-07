from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<string:pagename>")
def html_page(pagename):
    return render_template(pagename)


def write_to_file(data):
    with open("./venv/database.txt", mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open("./venv/database.csv", mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csvwriter = csv.writer(database2, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect("thankyou.html")
    else:
        return "Something wrong,Try again!!"
