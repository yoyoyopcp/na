import cgi
from flask import Flask, request
from flaskext.xmlrpc import XMLRPCHandler, Fault

app = Flask(__name__)

handler = XMLRPCHandler('api')
handler.connect(app, '/RPC2')

@app.before_request
def log_request_info():
    app.logger.info('Headers: %s', request.headers)
    app.logger.info('Body: %s', request.get_data())
    pass

@handler.register_function('purenetwork.list')
def pure_network_list(*args, **kwargs):
    return []


@handler.register_function('purearray.list')
def pure_array_list(*args, **kwargs):
    return [{'array_name': 'trashy', 'management_address': 'localhost',
	    'revision': '201909102318+ed5f1a6', 'version': '99.9.9',
	    'id': '84de4d02-f435-497f-9b9c-b1a33f16b991'}]

app.run()
