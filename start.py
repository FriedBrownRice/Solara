from flask import Flask, render_template, request, jsonify
import json, os
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html');

@app.route('/test', methods=['POST'])
def operations():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open(SITE_ROOT+'/data/nav.json') as file:
		data = json.load(file);
	# print data
	return jsonify(data);
