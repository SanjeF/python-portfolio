from flask import Flask, render_template, request, redirect
import os
import csv

app = Flask(__name__)

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(email, subject, message):
    # f = open("database.txt", "a")
    # f.write(email + ", " + subject + ", " + message + "\n")
    # f.close()
    with open('database.txt', mode='a') as database:
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(email, subject, message):
    with open('database.csv', mode='a', newline='') as database2:
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            email = data.get('email')
            subject = request.form['subject']
            message = request.form['message']

            write_to_csv(email, subject, message)
        except:
            return 'did not save to database'

        return redirect('./thankyou.html')
    else:
        return 'something went wrong try again'


# list_of_routes=[
#     "index.html",
#     "works.html",
#     "about.html",
#     "contact.html"
# ]
#
# routes ={}
#
# for i, route in enumerate(list_of_routes):
#     @app.route(f"/{route}", endpoint=f"route_{i}")
#     def dynamic_route(route_name=route):
#         return render_template(route_name)
#     routes[f"function_{i}"] = dynamic_route


