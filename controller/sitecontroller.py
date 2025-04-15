from json import JSONEncoder
from flask import jsonify,request
from model.spam import Spam, db
import sqlalchemy
import sqlalchemy.orm
from services.spamanalizer import analiz as scanner, analizer

def index():
	return "Flask page"


def spam():
	msg = request.args.get('msg')
	al = Spam.query.all()
	sts = []
	msgs = []
	for i in al:
		sts.append(i.status)
		msgs.append(i.message)
		
	dataFame = []
	dataFame.append({'status':sts})
	dataFame.append({'message':msgs})
	# return jsonify(dataFame)

	scc = analizer(msg,dataFame)
	return jsonify(scc)



def analiz():
	msg = request.args.get("msg")
	if msg and len(msg) > 0:
		scan = scanner(msg)
		if scan:
			return jsonify({'status':'spam'})
		else:
			return jsonify({'status':'not-spam'})
	else:
		return jsonify({'status':'msg required parametr'})