from flask import Flask, url_for, render_template, abort, send_file, request, redirect

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/static/secret.txt')
def ssrf():
	abort(403)



@app.route("/image")
def image():
	image_file = request.args.get('image', '')
	return send_file(f"{image_file}")
  
  
  
  
app.run()
