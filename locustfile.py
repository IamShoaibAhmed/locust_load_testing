import random
from locust import HttpUser, task, between

class MyUser(HttpUser):
    @task
    def index(self):
        self.client.get("/")
        #self.client.get("")
    
    
    
    def on_start(self):
        self.client.post("/web/login", {"username":"admin@amarbay.com", "password":"123"})

    wait_time = between(5, 9)
