import flask
from flask import Flask
from flask import request
app = Flask(__name__)
import redis
from redis import Redis
import json


@app.route('/api/post_reply',methods=['GET', 'POST'])
def api_post_reply():
	board = request.args.get('board');
	articleid = request.args.get('articleid');
	title = request.args.get('title');
	reply = request.args.get('reply');
	data = {
		'board':board,
		'articleid':articleid,
		'title':title,
		'reply':reply,
	}
	jstr = json.dumps(data)
	r = Redis()
	p = r.pubsub()
	p.subscribe('post_reply')
	r.publish('post_reply',jstr)
	return 'success'

if __name__ == '__main__':
	app.run(port=8810,threaded=True)
