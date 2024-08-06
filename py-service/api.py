from typing import Union
import uvicorn
from fastapi import FastAPI
import requests
class Api:
    def __init__(self, port=5000, address="0.0.0.0"):
        self.port = port
        self.address = address
        self.routs = {
            "default": "/",
            "upload": "/upload",
        }
        self.app = FastAPI()
        self.router()

    def router(self):
        @self.app.get(self.routs["default"])
        def default():
            r = requests.get("https://ifconfig.me/ip")
            return {
                "Your IP is": r.text 
            }
        
    def run(self):
        uvicorn.run(self.app, host=self.address, port=self.port)