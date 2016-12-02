# -*- coding: utf-8 -*-
# Part of Modoolar. See LICENSE file for full copyright and licensing details.

import logging

from rocketchat.calls.base import PostMixin, RocketChatBase

logger = logging.getLogger(__name__)


class CreateChannel(PostMixin, RocketChatBase):
    endpoint = "/api/v1/channels.create"

    def build_endpoint(self, **kwargs):
        return self.endpoint

    def build_payload(self, **kwargs):
        return {"name" : kwargs.get("name")}