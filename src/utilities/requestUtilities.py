import requests
import json
import logging as logger
import allure
from src.config.hostConfig import API_HOSTS



class RequestsUtilities(object):

    def __init__(self):
        self.base_url = API_HOSTS['staging']
    logger.info("Verifying Status Code in Every Request")

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f'Bad Status code.' \
                                                              f"Expected{self.expected_status_code}, Actual status code: {self.status_code}," \
                                                              f"URL: {self.url}, Response Json: {self.rs_json}"

    logger.info("Post Request for the API")

    @allure.step("Post request")
    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.post(self.url, data=payload, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API Post response:{self.rs_json} ")
        return self.rs_json

    logger.info("Get Request of the API")

    @allure.step("Get request")
    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(self.url, data=payload, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API Get response:{self.rs_json} ")
        return self.rs_json

    logger.info("Put request of the API")

    @allure.step("Put request")
    def put(self, endpoint, payload, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.put(self.url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API Put response:{self.rs_json} ")
        return self.rs_json

    logger.info("Patch request of the API")

    @allure.step("Patch request")
    def patch(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.patch(self.url, data=payload, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API Patch response:{self.rs_json} ")
        return self.rs_json

    logger.info("delete request of the API")

    @allure.step("Delete request")
    def delete(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.delete(self.url, data=payload, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API delete response:{self.rs_json} ")
        return self.rs_json
