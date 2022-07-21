# Set up your imports here!
# import ...
from flask import Flask

app=Flask(__name__)

@app.route('/') # Fill this in!
def index():
    return "<h1>Welcome to my Website!</h1>"
    # Welcome Page
    # Create a generic welcome page.
    pass

@app.route('/puppylatin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    if name[-1] == 'y':
        # name='spotiful'
        name=name.replace("y","iful")
        return "<h1>Puppy Latin: {}</h1>".format(name)
        # return "<h1>Puppy Latin: {}</h1>".format(name=name.replace("y","iful"))
    #    return "<h1>Puppy Latin: {}</h1>".format(name+"iful")
    else:
        return "<h1>Puppy Latin: {}</h1>".format(name+"y")
    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    pass

if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
    pass
