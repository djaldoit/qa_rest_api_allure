import requests
import logging
import json
import allure
from curlify import to_curl


def send_request_logger(method, url, **kwargs):
    with allure.step(f'{method} {url}'):
        response = requests.request(method=method, url=url, **kwargs)
        curl = to_curl(response.request)
        logging.info(curl)
        logging.info(f'status code: {response.status_code}')
        allure.attach(body=curl, name='curl', attachment_type=allure.attachment_type.TEXT, extension='txt')

        try:
            allure.attach(body=json.dumps(response.json(), indent=4), name='response',
                          attachment_type=allure.attachment_type.JSON, extension='json')
        except json.JSONDecodeError:
            if response.text:
                allure.attach(body=response.text, name='response',
                              attachment_type=allure.attachment_type.TEXT, extension='txt')
            else:
                allure.attach(body=None, name='response', attachment_type=allure.attachment_type.TEXT, extension='txt')

        return response
