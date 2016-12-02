# -*- coding: utf-8 -*-
# Part of Modoolar. See LICENSE file for full copyright and licensing details.

from rocketchat.calls.base import PostMixin, RocketChatBase

class UpdateUser(PostMixin, RocketChatBase):
    endpoint = "/api/v1/user.update"

    def set_auth_headers(self):
        super(UpdateUser, self).set_auth_headers()
        self.headers["Content-Type"] = "application/json"

    def build_endpoint(self, **kwargs):
        return self.endpoint

    def build_payload(self, **kwargs):
        return {
            "userId" : kwargs.pop("user_id"),
            "data" : kwargs
        }
