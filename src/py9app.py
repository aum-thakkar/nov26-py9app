from flask import Flask, jsonify
import socket
import time

app = Flask(__name__)


@app.route('/api/v1/info')
def info():
  return jsonify({
    "time": time.ctime(),
    "hostname": socket.gethostname(),
    "env": "dev",
    "message": "Hi Pranav!"

  })  


@app.route('/api/v1/healthz')
def healthz():
  return jsonify({
    "status": "up"

  }) 


if __name__ == '__main__':
  app.run("0.0.0.0")