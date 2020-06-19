# USING FLASK TO SETUP OUR WEBSITE!
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)  # creating our Flask 'app'
print(__name__)


@app.route('/<string:page_name>')  # Dynamic web pages linked with HTML, CSS, JS
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):       # writing received data to a "database" text file
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):  # writing received data to a "database" text file
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def sumbit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, did not POST, try again!'

# -------------------------------------------------

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'staic'), 'favicon.ico', mimetype='image/.ico')
