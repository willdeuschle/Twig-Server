from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults
from medium_parser import simplify
import json

def simple_app(environ, start_response):
    setup_testing_defaults(environ)
    medium_url = environ['QUERY_STRING']

    status = '200 OK'
    headers=[('Content-type', 'application/json'), ('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Headers', 'Content-Type')]

    start_response(status, headers)
    ret = {}
    if environ['REQUEST_METHOD'] == 'GET':
        (title, article_body) = simplify(medium_url)
        # ret = ["%s: %s\n" % (key, value)
               # for key, value in environ.iteritems()]
        ret = json.dumps({'title': title, 'article_body': article_body})
    return ret

httpd = make_server('', 8000, simple_app)
print "Serving HTTP on port 8000..."

# Respond to requests until process is killed
httpd.serve_forever()

