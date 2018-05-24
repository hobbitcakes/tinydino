import urllib
#from bs4 import BeautifulSoup
import json

from flask import Flask, url_for, Response

app = Flask(__name__)

@app.route('/getresponse')
def get_response():
    response = {"ServiceResponse" : "Success!! You have successfully called the GetResponse operation"}
    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')