from flask import Flask, redirect
from flask import url_for
from datetime import timedelta
from flask import render_template
from flask import request, session, jsonify

app = Flask (__name__)
app.secret_key = '565656'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

@app.route('/')
def goHome ():
    return redirect(url_for('homePage'))

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

users_dict =  {
    'Shacham': 'shachamt@post.bgu.ac.il',
    'Aviv': 'aviv@post.bgu.ac.il',
    'Noy': 'noy@post.bgu.ac.il',
    'Oron': 'Oron@post.bgu.ac.il',
    'Shany': 'shany@post.bgu.ac.il',

}

@app.route('/forms', methods=['GET','POST'])
def MyForms ():
    if 'user_name' in request.args:
        user_name= request.args['user_name']
        if user_name in users_dict:
            return render_template('assignment3_2.html',
                                   user_name=user_name,
                                   user_email= users_dict[user_name])
        else:
            if user_name=='':
                return render_template('assignment3_2.html',
                                       isEmpty=True,
                                       users_dict=users_dict)
            else:
                return render_template('assignment3_2.html',
                                   message= 'user not found')
    if request.method == 'POST':
        userName = request.form ['userName']
        email = request.form ['email']
        nickname = request.form ['nickname']
        if ((userName!='') & (email!='') & (nickname!='')):
                session['nickname'] = nickname
                return render_template('assignment3_2.html',
                                        nickname=nickname,
                                        email=email,
                                       userName=userName)
    return render_template('assignment3_2.html',
                           users_dict=users_dict)

@app.route('/session')
def session_func():
    return jsonify(dict(session))

@app.route('/logOut')
def logOut ():
    session.clear()
    return redirect(url_for('MyForms'))

if __name__ == '__main__':
    app.run(debug=True)

