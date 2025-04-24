from flask import Flask, render_template
import requests
from time import sleep

app = Flask(__name__)

def get_quote():
    url = 'https://zenquotes.io/api/random'
    retries = 5
    for i in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data[0]
        except requests.exceptions.RequestException as e:
            print(f"Attempt {i + 1} failed: {e}")
            sleep(2)
    return None

@app.route('/')
def index():
    quote = get_quote()
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)