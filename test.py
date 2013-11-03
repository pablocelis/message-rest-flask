from nose import *
from nose.tools import *
from rest_server import app
from datetime import datetime

from flask import json

class TestAPI:


	@classmethod
	def setup_class(self):

		self.app = app.test_client()

	@classmethod
	def teardown_class(self):
		print("teardown_class(): After everything in the class")

	def setup(self):
		print("setup(): before each method")
		
	def teardown(self):
		print("teardown(): after each method")

	def get_message(self, index):
		response = self.app.get('/messages/api/message/'+str(index))

		eq_(response.headers['Content-Type'], 'application/json')
		eq_(response.status_code,200)

		body = json.loads(response.data)
		message = body['messages']
		eq_(message['id'],index)
		eq_(message['read'], True)

		return message


	def create_message(self, message):
		response = self.app.post('/messages/api/message',
								data = json.dumps(message),
								content_type='application/json')

		eq_(response.headers['Content-Type'], 'application/json')
		eq_(response.status_code,201)

		body = json.loads(response.data)
		message_recv = body['message']
		eq_(message_recv['sender'], message['sender'])

		# Retreive the last message and test that is the message created
		last_message = self.get_message(message_recv['id'])
		eq_(last_message['sender'], message['sender'])

		return message_recv
		

	def test_create_messages(self):
		message = {
				'sender': 'Ray',
				'message': 'testing the api'
				}

		self.create_message(message)

	def test_get_message(self):
		self.get_message(1)

	def test_edit_message(self):
		response = self.app.put('messages/api/message/3',
								data = json.dumps({'message':u'content edited'}),
								content_type='application/json')

		eq_(response.headers['Content-Type'], 'application/json')
		eq_(response.status_code,200)

		body = json.loads(response.data)
		message = body['message']
		eq_(message['sender'], 'Ray')
		eq_(message['message'], 'content edited')

	def test_delete_message(self):
		message = {
			'sender':'Paul',
			'message': 'this will be deleted'
		}
		message_recv = self.create_message(message)

		response = self.app.delete('messages/api/message/' + str(message_recv['id']))

		eq_(response.headers['Content-Type'], 'application/json')
		eq_(response.status_code,200)

		body = json.loads(response.data)
		assert_true(body['deleted'])





