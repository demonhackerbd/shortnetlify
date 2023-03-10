from flask import Flask, request, redirect, render_template
from shortener import Shortener

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        shortener = Shortener()
        short_url = shortener.shorten(url)
        return render_template('result.html', short_url=short_url)
    else:
        return render_template('home.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    shortener = Shortener()
    original_url = shortener.expand(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return "Invalid URL"

if __name__ == '__main__':
    app.run()
