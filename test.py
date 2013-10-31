#!flask/bin/python
from nose import *
from nose.tools import *
from rest_server import app

class TestAPI:

	def check_content_type(headers):
		assert_equals(headers['Content-Type'], 'application/json')

	@classmethod
	def setup_class(cl):

		messages = [
			{
				'id': 1,
				'sender': u'Peter',
				'message': u'Hey, how this work?',
				'timestamp': datetime.now(),
				'read': False
			},
			{
				'id': 2,
				'sender': u'John',
				'message': u'Just write stuff',
				'timestamp': datetime.now(),
				'read': False
			}
		]



	@classmethod
	def teardown_class(cl):
		print("teardown_class(): After everything in the class")

	def setup(self):
		print("setup(): before each method")
		self.app = app.test_client()

	def teardown(self):
		print("teardown(): after each method")

	def test_empty_messages(self):
		response = self.app.get('/messages/api/message/all')

		check_content_type(request.headers)

		assert_true

	def test_equals_fail(self):
		print("This is an assert_equals method failing")
		assert_equals(2+0, 4)

	def test_true(self):
		print("This is an assert_true method")
		assert_true(False)


