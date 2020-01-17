import bottle
app=bottle.Bottle()
@app.error(404)
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
@app.route('/verify',method='post')
def verifypage():
    u=bottle.request.forms.get('uname')
    p=bottle.request.forms.get('pw')
    if not(u=='abc' and p=='xyz'):
        return 'login failed'
    else:
        bottle.TEMPLATE_PATH.append(r'C:\Users\lab365\Desktop\python\bin')
        import sqlite3
        con=sqlite3.connect('mydb.sqlite3')
        cur=con.cursor()
        cur.execute('SELECT * FROM LOGDATA')
        result=cur.fetchall()
        return bottle.template('report.tpl',res=result)
@app.route('/download/<filename>')
def staticfile(filename):
    return bottle.static_file(root=r'C:\Users\lab365\Desktop\python\bin',filename=filename)
@app.route('/empid/<eid:int>')
def empid(eid):
    D={'name':'abc','empid':eid}
    return D
@app.route('/nameid/<nid:re:[a-z0-9]+>')
def nameid(nid):
    return str(nid)
@app.route('/logdata')
def logdata():
    return bottle.redirect('/login')
@app.route('/passwords')
def passwords():
    return bottle.abort(201,'access denied')
app.run(host='192.168.3.232',port=8080)
