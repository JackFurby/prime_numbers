from flask import Flask, request, render_template
from prime_numbers import getFactors, primesInRange

app = Flask(__name__)


@app.route('/')
def prime_form():
	return render_template('prime_form.html')


@app.route('/', methods=['POST'])
def prime_post():
	number = int(request.form['number'])
	factors = getFactors(number)
	if len(factors) is 0:
		out = "Prime!"
	else:
		out = str(factors)
	return out


@app.route('/range')
def range_form():
	return render_template('range_form.html')


@app.route('/range', methods=['POST'])
def range_post():
	numberStart = int(request.form['startNumber'])
	numberEnd = int(request.form['endNumber'])
	primes = primesInRange(numberStart, numberEnd)
	if len(primes) is 0:
		out = "No prime numbers in range"
	else:
		out = str(primes)
	return out


if __name__ == "__main__":
	app.run()
