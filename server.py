from flask import Flask, render_template, url_for,request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open ('database.txt', mode = 'a') as database:
		name = data['full name']
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n {name}, {email}, {subject}, {message} ')

def write_to_csv(data):
	with open ('database.csv', mode = 'a', newline = '') as database2:
		name = data['full name']
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,)
		csv_writer.writerow([name,email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_file(data)
			write_to_csv(data)
			print(data)
			return redirect('/thankyou.html')
		except:
			return 'data did not saved in database'

	else:
		return 'something went wrong please try again!'

