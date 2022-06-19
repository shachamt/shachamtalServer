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

@app.route('/assignment3_1')
def MyHobbies ():
    user_info = 'shacham'
    hobbies = ('watch TV', 'Read books', 'Diving', 'Sleeping')
    shows = ('greys anatomy', 'station 19', 'blacklist', 'the office')
    return render_template('assignment3_1.html',
                           my_hobbies=hobbies,
                           user_info=user_info,
                           my_shows=shows)

@app.route('/hobbies')
def assign1 ():
    return redirect('/assignment3_1')


users_dict =  {
    1: {'id':'319002762', 'first_name': 'shacham', 'last_name': 'tal', 'email': 'shachamt@post.bgu.ac.il', 'password': '1234'},
    2: {'id': '313131317', 'first_name': 'aviv', 'last_name': 'menahem', 'email': 'aviv@post.bgu.ac.il', 'password': '8585'},
    3: {'id': '363636369', 'first_name': 'nir', 'last_name': 'yaakov', 'email': 'nirnir@post.bgu.ac.il', 'password': '2222'},
    4: {'id': '258471369', 'first_name': 'adi', 'last_name': 'mizrahi', 'email': 'adimi@post.bgu.ac.il', 'password': '3641'},
    5: {'id': '285236581', 'first_name': 'shir', 'last_name': 'yehezkel', 'email': 'shishir@post.bgu.ac.il','password': '2258'}
}


@app.route('/assignment3_2',methods=['GET','POST'])
def MyForms ():
    if 'user_id' in request.args:
        user_id= request.args['user_id']
        for key in users_dict:
            if user_id.__eq__(users_dict[key]['id']):
                return render_template('assignment3_2.html',
                                       user_id=user_id,
                                       user_email= users_dict[key]['email'],
                                       first_name = users_dict[key]['first_name'],
                                       last_name = users_dict[key]['last_name'])
            else:
                if user_id=='':
                    return render_template('assignment3_2.html',
                                           isEmpty=True,
                                           users_dict=users_dict)
                else:
                    return render_template('assignment3_2.html',
                                       message= 'user not found')

    if request.method == 'POST':
        first_name = request.form ['first_name']
        last_name = request.form ['last_name']
        user_name = request.form ['user_name']
        user_id = request.form ['user_id']
        user_email = request.form ['user_email']
        user_password = request.form ['user_password']
        if ((first_name!='') & (last_name!='') & (user_name!='') & (user_password!='')& (user_id!='')):
                session['user_name'] = user_name
                x=len(users_dict)
                users_dict[x+1]={'id':user_id, 'first_name': first_name, 'last_name': last_name, 'email': user_email, 'password': user_password}
                return render_template('assignment3_2.html',
                                        first_name=first_name,
                                        last_name=last_name,
                                       user_name=user_name,
                                       user_password=user_password,
                                       sessionOn=False
                                       )
    return render_template('assignment3_2.html',
                           users_dict=users_dict)


@app.route('/home')
def homePage ():
    return render_template('homePage.html')

@app.route('/contact')
def contact ():
    return render_template('contactUs.html')

@app.route('/session')
def session_func():
    return jsonify(dict(session))

@app.route('/logOut')
def logOut ():
    session.clear()
    return redirect('/assignment3_2')

if __name__ == '__main__':
    app.run(debug=True)

