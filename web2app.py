from flask import Flask, render_template
app = Flask(__name__)
items = []

@app.route(/)
def index():
    return render_template('form.html')

@app.route('/add_todo')
def add_todo():
    item = request.arg.get("Item")
    Items.append(item)
    return ",".join(Items)

@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html',to=name)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    
