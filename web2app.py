from flask import *
import json
import os
app = Flask(__name__)
items = []
@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html',to=name)
 

@app.route("/")
def index():
    return render_template('index.html',to=name)

@app.route('/add_todo')
def add_todo():
    item = request.arg.get("Item")
    dd=request.args.get("date")
    answer=item + "<br>" + dd
    Items.append(item)
    return answer
    return redirect("http://localhost:5000/",code=302)
    
@app.route('/get_todos')
def get_todos():
    resp=Respose(json.dumps(getlist))
    resp.header['Content-Type']='application/json'
    return resp

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0')

    
