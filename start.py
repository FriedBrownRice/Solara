from flask import Flask, render_template, request, jsonify
import json, os
app = Flask(__name__)

def deleteNode(s):
	print s;


@app.route('/')
def index():
	return render_template('index.html');

@app.route('/test', methods=['POST'])
def operations():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	DATA_ROOT = SITE_ROOT+"/data/"
	FILE_NAME = request.form['name']+'.json'
	if request.form['operation'] == 'nav':
		print 1
		DATA_ROOT+='nav.json'
	elif request.form['operation'] == 'createT':
		DATA_ROOT+=FILE_NAME
	elif request.form['operation'] == 'delNode':
		deleteNode('aaa');
		return 'successfully delete'
	elif request.form['operation'] == 'dive':
		DATA_ROOT+="ChildrenOf"+FILE_NAME
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
		SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
		DATA_ROOT = SITE_ROOT+"/data/addNode.json";
		with open(DATA_ROOT) as f:
			data = json.load(f);
			data['hasParent'] = request.form['hasParent']
		return jsonify(data);
	elif request.form['operation']=='update':
		return 'successfully update';
	elif request.form['operation']=='dive':
		data = json.loads(request.form['data']);
		print data['eleID'];
		ret = {
				'eleID':data['eleID'],
				'options':[
					{'name':'China','id':1},
					{'name':'USA','id':2},
					{'name':'Russia','id':3}
				],
				'value':-1
		}
		return jsonify(ret);
	elif request.form['operation']=='insertNode':
		return jsonify(['new data',123]);








