"""_summary_

Returns:
    _type_: _description_
"""
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """
    Sets up a simple Tornado web application with a single route.

    The application listens on port 8888 and responds with "Hello, world"

    when accessed at the root URL ("/").

    Classes:

        MainHandler: Handles GET requests to the root URL.

    Functions:

        make_app: Creates and returns a Tornado web application instance.

    """

    def get(self):
        """
        Handles GET requests to the root URL ("/").

        Writes "Hello, world" in response to GET requests to the root URL.

        """

        self.write("Hello, world")


def make_app():
    """
    Creates and returns a Tornado web application instance.

    The application has a single route ("/") handled by MainHandler,
    which responds with "Hello, world" to GET requests.
    """

    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
