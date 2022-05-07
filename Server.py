import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about-us")
def about():
    return render_template("about.html")
@app.route("/contact-us")
def contact():
    return render_template("contact.html")
@app.route("/works")
def works():
    return render_template("works.html")
@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/thankyou")
def components():
    return render_template("thankyou.html")


def write_to_file(data):
    with open('database.txt', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = db.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        db2.close()


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou')
    else:
        return "Something Went Wrong !"


if __name__ == '__main__':
    app.run(debug=True, port=8000)