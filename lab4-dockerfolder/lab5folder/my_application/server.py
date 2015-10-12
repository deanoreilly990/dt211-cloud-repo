from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "hello dean "
@app.route('/user/<username>')
def show_user_profile(username)
	return 'User %s' %username
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)

