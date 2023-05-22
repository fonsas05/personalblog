from flask import Flask, render_template, request

app = Flask(__name__)

# define all you pages here
@app.route("/")
def index():
   return render_template("index.html")

@app.route("/page2", methods=['GET', 'POST'])
def page2():
   # either its a gget request (USER WANTS WEBSITE PAGE)

   if request.method == 'GET':
      return render_template("page2.html", number=0, thing="ass")
   
   # or its a POST request (USER SUBMITTED FORM)
   if request.method == "POST":
      user_number = request.form['user_number']
      user_thing = request.form['user_thing']
      return render_template("page2.html", number=user_number, thing=user_thing)

   

# BS python stuff you have to do
if __name__ == '__main__':
   app.run()