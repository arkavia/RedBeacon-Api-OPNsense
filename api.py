#!/usr/bin/env python
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests


app = Flask(__name__)
CORS(app)

@app.route('/setAlias', methods=['POST'])
def setAlias():
    bodyjson = request.json
    api_key = bodyjson['api_key']
    api_secret = bodyjson['api_secret']
    uuid = bodyjson['uuid']
    url = bodyjson['url']
    alias_obj = bodyjson['alias']
    payload = json.dumps({
        "alias": {
            "enabled": alias_obj['enabled'],
            "name": alias_obj['name']
        }
    })
    # request headers
    headers = {
        'Content-Type': "application/json"
    }
    # request data
    r = requests.post(url,
                      verify=False,
                      headers=headers,
                      data=payload,
                      auth=(api_key, api_secret)
                      )
    if r.status_code == 200:
        response = json.loads(r.text)
        return (response)
    else:
        # default return
        return jsonify(
            response='system error',
            status=500
        )

@app.route('/addAlias', methods=['POST'])
def addAlias():
	bodyjson = request.json
	api_key = bodyjson['api_key']
	api_secret = bodyjson['api_secret']
	url = bodyjson['url']
	alias_obj = bodyjson['alias']
	payload = json.dumps({
        "alias": {
            "enabled": alias_obj['enabled'],
            "name": alias_obj['name'],
            "type": alias_obj['type'],
            "description": alias_obj['description']
        }
    })
    # request headers
	headers = {
        'Content-Type': "application/json"
    }
    # request data
	r = requests.post(url,
                      verify=False,
                      data=payload, headers=headers,
                      auth=(api_key, api_secret)
                      )
	print(r.text)
	if r.status_code == 200:
		response = json.loads(r.text)
		return (response)
	else:
        # default return
		return jsonify(
            response='system error',
            status=500
        )

@app.route('/delAlias', methods=['POST'])
def delAlias():
	bodyjson = request.json
	api_key = bodyjson['api_key']
	api_secret = bodyjson['api_secret']
	uuid = bodyjson['uuid']
	url = bodyjson['url'] + uuid
	payload = json.dumps({})
    # request headers
	headers = {
        'Content-Type': "application/json"
	}
    # request data
	r = requests.post(url,
                      verify=False,
                      headers=headers,
                      data=payload,
                      auth=(api_key, api_secret)
                      )
	if r.status_code == 200:
		response = json.loads(r.text)
		return (response)
	else:
        # default return
		return jsonify(
            response='system error',
            status=500
        )

@app.route('/createAlias', methods=['POST'])
def createAlias():
		
	bodyjson = request.json
	api_key = bodyjson['api_key']
	api_secret = bodyjson['api_secret']
	url = bodyjson['url']
	alias_obj = bodyjson['alias']
	payload = json.dumps({
        "alias": {
            "enabled": alias_obj['enabled'],
            "name": alias_obj['name'],
            "type": alias_obj['type'],
            "description": alias_obj['description'],
            "content": alias_obj['content']
        }
    })
	headers = {
	    'Content-Type': "application/json"
	}
	
	r = requests.post(url,
	                 verify=False,
	                  data=payload,headers=headers,
	                  auth=(api_key, api_secret)
	                  )

	if r.status_code == 200:
	    response = json.loads(r.text)
	    return(response)
	return 3


@app.route('/obtenerAlias', methods=['POST'])
def ontener_alias():
		
	bodyjson = request.json
	api_key = bodyjson['api_key']
	api_secret = bodyjson['api_secret']
	url = bodyjson['url']
	headers = {
	    'Content-Type': "application/json"
	}
	
	r = requests.get(url,
	                 verify=False,headers=headers,
	                  auth=(api_key, api_secret)
	                  )

	if r.status_code == 200:
	    response = json.loads(r.text)
	    return(response)
	return 3
   
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5005)