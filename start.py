from flask import Flask, render_template, request, jsonify
import json, os
app = Flask(__name__)

def deleteNode(s):
	print s;

def addNode(dic):
	return {'id':1001};

@app.route('/')
def index():
	return render_template('index.html');

@app.route('/test', methods=['POST'])
def operations():

	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	DATA_ROOT = SITE_ROOT+"/data/"
	if request.form['operation'] == 'nav':
		DATA_ROOT+='nav.json'
	elif request.form['operation'] == 'createT':
		DATA_ROOT+='table.json'
	elif request.form['operation'] == 'delNode':
		deleteNode('aaa');
		return 'successfully delete'
	elif request.form['operation'] == 'dive':
		DATA_ROOT+='childrenT.json'
	elif request.form['operation'] == 'edit':
		DATA_ROOT+='editor.json'
	with open(DATA_ROOT) as file:
		data = json.load(file);
	# print data
	return jsonify(data);

@app.route('/upload',methods=['POST'])
def oper():
	if request.form['operation']=='delete':
		return 'successfully delete';
	elif request.form['operation']=='addNode':
		return jsonify(addNode(request.form['attrs']));
	elif request.form['operation']=='update':
		return 1