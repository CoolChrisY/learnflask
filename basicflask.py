from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "<h1>It Works for ChrisTofu!</h1>"

@app.route('/information')
def info():
    return "<h1>Chris is cool!</h1>"

@app.route('/person/<name>')
def puppy(name):
    return "<h1>100th letter: {}</h1>".format(name[100])

if __name__ == '__main__':
    app.run(debug=True)
