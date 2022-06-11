from flask import Flask, redirect
from flask import url_for
from flask import render_template

app = Flask (__name__)

@app.route('/')
def goHome ():
    return redirect('/home')

@app.route('/home')
def homePage ():
    return render_template('homePage.html')

@app.route('/contact')
def contact ():
    return render_template('contactUs.html')

@app.route('/hobbies')
def MyHobbies ():
    user_info = 'shacham'
    hobbies = ('watch TV', 'Read books', 'Diving', 'Sleeping')
    shows = ('greys anatomy', 'station 19', 'blacklist', 'the office')
    return render_template('assignment3_1.html',
                           my_hobbies=hobbies,
                           user_info=user_info,
                           my_shows=shows)


    return render_template('assignment3_1.html')

@app.route('/forms')
def MyForms ():
    return render_template('assignment3_2.html')

if __name__ == '__main__':
    app.run(debug=True)

