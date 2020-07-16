from locust import HttpUser, between, task
import json
import requests
import sys


# from odoo-12 import http, _, exceptions


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)


    
    @task
    def index(self):
        self.client.get("/web/login")
        
    @task
    def about(self):
        self.client.get("/pos/web/#action=pos.ui")

    
