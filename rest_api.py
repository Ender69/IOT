from flask import Flask, url_for
from flask import Response
app = Flask(__name__)
# pour utiliser les méthodes GET PUT etc
#curl -X PATCH http://127.0.0.1:5000/echo

#curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/messages -d '{"message":"Hello Data"}'

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid
	
@app.route('/analysis/<filename>')
def analysis(filename):
    x = pd.DataFrame(np.random.randn(20, 5))
    return render_template("analysis.html", name=filename, data=x.to_html())

@app.route('/_get_current_user')
def get_current_user():
    return jsonify(username=g.user.username,
                   email=g.user.email,
                   id=g.user.id)

@app.route('/messages', methods = ['POST','GET'])
def get_messages():
	if request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

@app.route('/hello', methods = ['GET'])
def api_hello():
	data = {
		'hello'  : 'world',
		'number' : 3
	}
	js = json.dumps(data)
	resp = Response(js, status=200, mimetype='application/json')
	resp.headers['Link'] = 'http://luisrei.com'
	return resp
#{
#    "username": "admin",
#    "email": "admin@localhost",
#    "id": 42
#}

if __name__ == '__main__':
    app.run(host='192.168.1.48')