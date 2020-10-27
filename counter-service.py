from flask import Flask
import boto3
import os


app = Flask(__name__)


def readFile(filename):
    filehandle = open(filename)
    count = int(filehandle.read())
    filehandle.close()
    return count


def updateFile(filename,count):
    count = count
    filehandle = open(filename , "w")
    filehandle.write(str(count))
    filehandle.close()

filename = "count.txt"

@app.route('/counter-service', methods=['GET'])
def GetCounter():
    count = 0
    count = readFile(filename)
    return str(count), 200

@app.route('/counter-service', methods=['POST'])
def PostCounter():
    count = 0
    count = readFile(filename)
    count = int(count) + 1
    updateFile(filename,count)
    return '', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)







