import asyncio
import json
import tornado.web
import tornado.httpclient

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Mensaje desde Tornado")
        
    def post(self):
        self.json_args = json.loads(self.request.body)
        self.write("You wrote " + self.json_args['message'])

class MessageHandler(tornado.web.RequestHandler):
    async def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = await http.fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
        json_result = tornado.escape.json_decode(response.body)
        self.write(f"{json.dumps(json_result)}")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/api/v1/messages", MessageHandler),
    ])
    
async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()
    
if __name__ == "__main__":
    asyncio.run(main())