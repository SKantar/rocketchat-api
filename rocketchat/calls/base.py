# -*- coding: utf-8 -*-
# Part of Modoolar. See LICENSE file for full copyright and licensing details.

import logging
import pprint
import requests
import json

logger = logging.getLogger(__name__)

class RocketChatBase(object):
    settings = None
    endpoint = None
    headers = {}
    method = "get"
    auth_token = None
    auth_user_id = None

    def __init__(self, settings=None, *args, **kwargs):
        self.settings = settings

        # Prepare for a call by fetching an Auth Token
        self.set_auth_token()
        self.set_auth_headers()

    def set_auth_token(self):

        url = "{domain}/api/login".format(
            domain=self.settings["domain"]
        )

        response = requests.post(
            url,
            {
                "user": self.settings["username"],
                "password": self.settings["password"]
            }
        )

        self.auth_token = response.json()["data"]["authToken"]
        self.auth_user_id = response.json()["data"]["userId"]

    def set_auth_headers(self):
        self.headers["X-Auth-Token"] = self.auth_token
        self.headers["X-User-Id"] = self.auth_user_id

    def logoff(self):
        url = "{domain}/api/logout".format(
            domain=self.settings["domain"]
        )
        requests.get(url, headers=self.headers)

    def post_response(self, result):
        return result

    def build_endpoint(self, **kwargs):
        """
        Build the endpoint for the user given some **kwargs
        from the initial calling.
        :return:
        """

        raise NotImplementedError()

    def build_payload(self, **kwargs):
        """
        Build a payload dict that will be passed directly to the
        endpoint.  If you need to pass this as plain text or whatever
        you"ll need to the dumping here.

        :return:
        """

        return None

    def raise_for_status(self, result):
        from requests.exceptions import HTTPError
        """Raises stored :class:`HTTPError`, if one occurred."""
        if 500 <= result.status_code < 600:
            raise HTTPError('%s Server Error: %s' % (result.status_code, result.reason), response=self)


    def call(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """

        timeout = kwargs.get("timeout", None)

        url = "{domain}{endpoint}".format(
            domain=self.settings["domain"],
            endpoint=self.build_endpoint(**kwargs)
        )

        result = requests.request(
            method=self.method,
            url=url,
            data=json.dumps(self.build_payload(**kwargs)),
            headers=self.headers, timeout=timeout
        )

        request_data = {
            "url": url,
            "method": self.method,
            "payload": self.build_payload(**kwargs),
            "headers": self.headers,
        }

        logger.debug("API Request - {request}".format(
            request=pprint.pformat(request_data)
        ))

        self.logoff()
        try:
            self.raise_for_status(result)

            logger.debug("API Response - {data}".format(
                data=pprint.pformat(result.json())
            ))

            return self.post_response(result.json())

        except Exception as e:
            logger.error(
                "RESTful {classname} call failed. {message}".format(
                    classname=self.__class__.__name__, message=e
                ),
                exc_info=True
            )
            raise e


class PostMixin(object):
    method = "post"
