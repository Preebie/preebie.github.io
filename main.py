from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify, make_response



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/aboutme.html', methods=['GET', 'POST'])
def aboutme():
    return render_template('aboutme.html')

@app.route('/contactme.html', methods=['GET', 'POST'])
def contactme():
    return render_template('contactme.html')


if __name__ == "__main__":
    app.run(debug=True)