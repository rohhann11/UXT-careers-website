from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

JOBS = [{'id':1,
    'title': 'Data analyst',
    'location': 'Bengaluru',
    'salary': '4LPA'
}, {'id':2,
    'title': 'Data scientist',
    'location': 'Delhi',
    'salary': '10LPA'
}, {'id':3,
    'title': 'Frontend developer',
    'location': 'Hyderabad',
    'salary': '6LPA'
}]


@app.route('/')
def hello_world():
  return render_template('index.html', jobs=JOBS)

@app.route('/api/<id>')
def joson(id):
  return jsonify(JOBS[id])

if __name__ == '__main__':
  app.run(debug=True)
