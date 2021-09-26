from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def acceptinput():
    a = {}
    inputchr = str(request.args['query'])
    d['output'] = inputchr
    return d

if __name__ == "__main__":
    app.run()
