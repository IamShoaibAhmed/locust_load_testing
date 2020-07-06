import random
from locust import HttpUser, task, between

class MyUser(HttpUser):
    @task
    def index(self):
        self.client.get("/")
        self.client.get("/web")
    
    
    
    def on_start(self):
        self.client.post("/login", {"username":"foo", "password":"bar"})

    wait_time = between(5, 9)
