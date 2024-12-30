from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get data from the form
        student_name = request.form['name']
        student_roll = request.form['roll_no']
        student_city = request.form['city']
        # Do something with the input, e.g., print it or process it
        print(f"User input: {student_name}")
        return f"Received input: {student_name}, {student_roll}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
