from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/find_nth_largest', methods=['POST'])
def find_nth_largest():
    try:
        # Get user input from the form
        numbers_input = request.form['numbers']
        n = int(request.form['n'])

        # Parse the comma-separated numbers into a list of floats
        numbers = [float(x.strip()) for x in numbers_input.split(',')]

        # Validate inputs
        if n <= 0:
            return render_template('result.html', error="Please enter a positive value for n.")
        if n > len(numbers):
            return render_template('result.html', error=f"n ({n}) cannot be larger than the list size ({len(numbers)}).")
        if not numbers:
            return render_template('result.html', error="Please enter at least one number.")

        # Sort the list in descending order and find the nth largest
        sorted_numbers = sorted(numbers, reverse=True)
        nth_largest = sorted_numbers[n-1]

        return render_template('result.html', result=f"The {n}th largest number is: {nth_largest}", numbers=numbers)
    except ValueError as e:
        return render_template('result.html', error="Invalid input. Please enter numbers separated by commas and a valid integer for n.")

if __name__ == '__main__':
    # For local development only; GAE uses its own server
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)