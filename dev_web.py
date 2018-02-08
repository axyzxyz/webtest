# coding=utf-8
from wsgiref.simple_server import make_server


def index():
    return ['<h1>hello index! 你好呀</h1>'.encode('gbk')]


def web():
    return ['<h1>hello web! 你好呀 web</h1>'.encode('gbk')]


url = [
    ('index', index),
    ('web', web)
]

url_parttern = dict(url)


def runserver(request, start_response):
    start_response('502 OK', [('Content-Type', 'text/html')])
    path = request.get('PATH_INFO').lstrip('/')
    # return ['<h1>hello index! 你好呀</h1>'.encode()]
    if path and url_parttern.get(path):
        return url_parttern.get(path)()
    return [x.encode()+'</br>'.encode() for x in url_parttern.keys()]


if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 80, runserver)
    print('Server httpd is starting...')
    httpd.serve_forever()
