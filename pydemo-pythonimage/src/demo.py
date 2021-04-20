from bottle import route, run
from redis import Redis

redis = Redis(host='redis', port=6379)

@route('/')
def home():
    count = redis.incr('hits')
    return f"Hello World! ({count} times..)"

run(host='0.0.0.0', port=8888, debug=True, reloader=True)
