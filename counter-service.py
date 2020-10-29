from flask import Flask
import boto3
import os


app = Flask(__name__)

####### read the current value from local file #######
def readFile(filename):
    filehandle = open(filename)
    count = int(filehandle.read())
    filehandle.close()
    return count

####### write the new value to local file #######
def updateFile(filename,count):
    count = count
    filehandle = open(filename , "w")
    filehandle.write(str(count))
    filehandle.close()

filename = "count.txt"
####### GET methods #######
@app.route('/counter-service', methods=['GET'])
def GetCounter():
    count = 0
    count = readFile(filename)
    return str(count), 200
####### POST methods #######
@app.route('/counter-service', methods=['POST'])
def PostCounter():
    count = 0
    count = readFile(filename)
    count = int(count) + 1
    updateFile(filename,count)
    return '', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)







