from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('hello.html',name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)

