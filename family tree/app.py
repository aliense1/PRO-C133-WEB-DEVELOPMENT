# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Davis Shaju" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    name = "Pr : 1"  
    age = "45"  

    return render_template('father.html',name = name , age = age)

@app.route("/mother")
def mother():
    name = "Pr : 2" 
    age = "45"  

    return render_template('mother.html',name = name , age = age)


@app.route("/friend")
def friend():
    name = "Fr 1" 
    age = "45" 

    return render_template('friend.html',name = name , age = age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
