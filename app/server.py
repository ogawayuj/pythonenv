from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.debug = True
    print('http://0.0.0.0:4000/ docker-compose ports')
    app.run(host='0.0.0.0', port=80)
