from wsgiref.simple_server import make_server


def hello(environ, start_response):
    start_response("200 OK",
        [("Content-type", "text/plain;charset=utf-8")])

    return [b"Hello, world"]


httpd = make_server('', 8080, hello)
httpd.serve_forever()