from flask import Flask , render_template ,request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='nishi'
app.config['MYSQL_PASSWORD']='samridhi@1'
app.config['MYSQL_DB']='flask'

mysql=MySQL(app)

#for new users
@app.route("/form")
def login():
    return render_template("login.html")

@app.route("/login" , methods =['POST'])
def form():
    if request.method=='POST':
        name=request.form['login']
        pwd=request.form['pwd']
        cursor=mysql.connection.cursor()
        cursor.execute('''INSERT INTO info(name,pwd) values(%s,%s)''',(name,pwd))
        mysql.connection.commit()
        cursor.close()
        return render_template("success.html")
    
if __name__=="__main":
    app.run(debug=True)
