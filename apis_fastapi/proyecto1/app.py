"""_summary_

    Working with FastAPI
    
    Example: Basic API

"""

from fastapi import FastAPI
import uvicorn

# allows to create an instance of FastAPI
app: FastAPI = FastAPI()

# allows to create a route


@app.get("/home")
# will be executed each time a user visits the URL path specified by the @app.get() decorator, in this case the "/home" path
def index() -> dict:
    """ 
    This path operation returns a message saying that the API is working
    """
    return {"message": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
