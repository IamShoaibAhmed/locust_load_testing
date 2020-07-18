from locust import HttpUser, between, task
import json
import requests
import sys


# from odoo-12 import http, _, exceptions


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        # AUTH_URL = 'http://localhost:8069/web/session/authenticate/'

        headers = {'Content-type': 'application/json'}

        # Remember to configure default db on odoo configuration file(dbfilter = ^db_name$)
        # Authentication credentials
        data = {
            'params': {
                "login": "admin@amarbay.com",
                "password": "123",
                "db": "bay-demo-0711_1"
            }
        }
        self.client.post(
            "/web/session/authenticate",
            data=json.dumps(data),
            headers=headers
        )

    @task
    def index(self):
        self.client.get("/")

    @task(10)
    def post_product_categ(self):
        AUTH_URL = 'https://bayerp.com/web/session/authenticate/'

        headers = {'Content-type': 'application/json'}

        # Remember to configure default db on odoo configuration file(dbfilter = ^db_name$)
        # Authentication credentials
        data = {
            "params": {
                "login": "admin@amarbay.com",
                "password": "123",
                "db": "bay-demo-0711_1"
            }
        }

        # Authenticate user
        res = requests.post(
            AUTH_URL,
            data=json.dumps(data),
            headers=headers
        )

        # Get session_id from the response cookies
        # We are going to use this as our API key
        session_id = res.cookies.get('session_id', '')
        print(session_id)
        #  params = {'session_id': session_id, 'query': '{id, name}'}

        # headers = {'Content-type': 'application/json'}
        data = {
            'params': {
                "data": {
                    "name": "Test category_2"
                }
            }
        }
        self.client.post(
            "/ecom/product_list_temp",
            data=json.dumps(data),
            headers=headers
        )