from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string', '')
    regex_pattern = request.form.get('regex', '')
    matches = []
    try:
        if regex_pattern:
            matches = re.findall(regex_pattern, test_string)
    except re.error:
        matches = ["Invalid regex pattern"]
    return render_template('index.html', test_string=test_string, regex=regex_pattern, matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form.get('email', '')
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid = bool(re.match(email_regex, email))
    return render_template('index.html', email=email, is_valid=is_valid)

if __name__ == '__main__':
    app.run(debug=True)
