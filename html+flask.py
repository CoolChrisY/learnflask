from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    some_variable="Chris"
    return render_template('basic.html',my_variable=some_variable)

if __name__ == '__main__':
    app.run(debug=True)
