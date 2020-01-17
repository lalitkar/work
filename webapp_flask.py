import flask
app=flask.Flask('myapp')
@app.errorhandler(404)
def errorpage(err):
    return 'page under construction'
#app.run(host='192.168.3.232',port=8080)
@app.route('/')
def indexpage():
    return 'welcome'
@app.route('/about')
def aboutpage():
    return '<b> this is about</b>'
@app.route('/login')
def loginpage():
    return '''<form action='/verify' method='post'>
                username:<input type='text' name='uname'/><br/>
                password:<input type='password' name='pw'/><br/>
                <input type='submit' value='login'/>
                </form>'''
@app.route('/verify',methods=['post'])
def verifypage():
    u=flask.request.form.get('uname')
    p=flask.request.form.get('pw')
    if not(u=='abc' and p=='xyz'):
        return 'login failed'
    else:
        import sqlite3
        con=sqlite3.connect('mydb.sqlite3')
        cur=con.cursor()
        cur.execute('SELECT * FROM LOGDATA')
        result=cur.fetchall()
        return flask.render_template('report.html',res=result)
@app.route('/download/<filename>')
def staticfile(filename):
    return flask.send_from_directory(directory=r'C:\Users\lab365\Desktop\python\bin',filename=filename)
@app.route('/empid/<int:eid>')
def empid(eid):
    D={'name':'abc','empid':eid}
    return D
@app.route('/logdata')
def logdata():
    return flask.redirect('/login')
@app.route('/passwords')
def passwords():
    return flask.abort(201,'access denied')
app.run(host='192.168.3.232',port=8080)
