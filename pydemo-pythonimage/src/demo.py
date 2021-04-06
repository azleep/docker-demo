from bottle import route, run

@route('/')
def home():
    return "Hello Zug!"

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
