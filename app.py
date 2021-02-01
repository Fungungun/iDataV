from flask import Flask, render_template
app = Flask(__name__, template_folder="F:\\projects\\iDataV", static_folder="/")

@app.route('/')
def homepage():
    return render_template("test.html")

@app.route('/')
def testApi():
    return "Hello Cross Domain"

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)