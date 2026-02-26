from flask import Flask, render_template, request
import requests

app = Flask(__name__)
url = "https://d2q2kkuy34.execute-api.eu-north-1.amazonaws.com/user_my"


def get_user_from_aws(username):
    response = requests.get(url, params={"user": username})
    return response.json() if response.status_code == 200 else None

def send_to_aws(username, password):
    payload = {"name": username, "pass": password}
    response = requests.post(url, json=payload)
    return response.status_code

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def handle_submit():
    user_val = request.form.get('username')
    pass_val = request.form.get('password')
    
    status = send_to_aws(user_val, pass_val)
    
    if status in [200, 201]:
        return f"<h1>Success!</h1><p>{user_val} is now in the AWS cloud.</p>"
    else:
        return f"<h1>Error</h1><p>AWS Status: {status}</p>", 400

if __name__ == '__main__':
    app.run(debug=True)