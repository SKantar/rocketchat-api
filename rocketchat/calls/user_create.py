# -*- coding: utf-8 -*-
# Part of Modoolar. See LICENSE file for full copyright and licensing details.

from rocketchat.calls.base import PostMixin, RocketChatBase


class CreateUser(PostMixin, RocketChatBase):
    endpoint = "/api/v1/users.create"

    def build_endpoint(self, **kwargs):
        return self.endpoint

    def build_payload(self, **kwargs):
        return kwargs
