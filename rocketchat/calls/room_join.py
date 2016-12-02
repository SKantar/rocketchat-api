# -*- coding: utf-8 -*-
# Part of Modoolar. See LICENSE file for full copyright and licensing details.

import logging

from rocketchat.calls.base import PostMixin, RocketChatBase

logger = logging.getLogger(__name__)


class JoinRoom(PostMixin, RocketChatBase):
    endpoint = "/api/rooms/{room_id}/join"

    def build_endpoint(self, **kwargs):
        return self.endpoint.format(
            room_id=kwargs.get("room_id")
        )

    def build_payload(self, **kwargs):
        return {}
