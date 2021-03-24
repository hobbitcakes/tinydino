import urllib
#from bs4 import BeautifulSoup
import json

from flask import Flask, url_for, Response, request


#----------------------
#   Load Dinosaur info
#______________________

trilobite = { "name" : "Trilobite", "Kingdom" : "Animalia", "period" : "Cambrian", "discovered" : "1698"}
ankylosaurus = { "name" : "Ankylosaurus", "Kingdom" : "Animalia", "period" : "Cretaceous", "discovered" : "1908"}

dinosaurs = [trilobite, ankylosaurus]


app = Flask(__name__)

#--------------------------
#    Basic testing services
#__________________________

@app.route('/GetResponse')
def get_response():
    response = {"ServiceResponse" : "Success!! You have successfully called the GetResponse operation"}
    return json.dumps(response)

@app.route('/GetNextInteger/<int:integer>')
def get_next_integer(integer):
    next_int = int(integer) + 1
    response = {"ServiceResponse" : next_int}
    return json.dumps(response)

@app.route('/GetAllCaps/<notcaps>')
def get_all_caps(notcaps):
    response = {"ServiceResponse" : notcaps.upper()}
    return json.dumps(response)

@app.route('/headers')
def get_headers():
    headers_dict = {}
    for key, value in request.headers.items():
        headers_dict[key] = value
    return json.dumps(headers_dict)


#--------------------
#    Dinosaurs
#____________________

@app.route('/version')
def version():
    version = {"version" : "trilobite"}
    return json.dumps(version)


@app.route('/<dino>', methods=['GET', 'PUT'])
def tinydino(dino):
    '''Return the json for a dinosuar or create a new one'''
    for dinosaur in dinosaurs:
        if dino.lower() in dinosaur['name'].lower():
            return json.dumps(dinosaur)


@app.route('/dinosaur', methods=['GET', 'POST'])
def dinosuar():
    if request.method == 'GET':
        'trilobite'
    elif request.method == 'POST':
        'Need to do something with this...'
    return "triolobite"





if __name__ == '__main__':
    app.run(host='0.0.0.0')
