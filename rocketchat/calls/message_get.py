# -*- coding: utf-8 -*-
# Part of Modoolar. See LICENSE file for full copyright and licensing details.

from rocketchat.calls.base import RocketChatBase

import logging
logger = logging.getLogger(__name__)

class GetMessages(RocketChatBase):
    endpoint = "/api/rooms/{room_id}/messages"

    def build_endpoint(self, **kwargs):
        return self.endpoint.format(
            room_id=kwargs.get("room_id")
        )

    def post_response(self, result):
        messages = []

        try:
            _messages = result.get("messages")

            for message in _messages:
                message_dict = {}
                message_dict["content"] = message.get("msg")
                message_dict["id"] = message.get("_id")
                message_dict["user_id"] = message.get("u").get("_id")
                messages.append(message_dict)

        except Exception as e:
            logger.error(
                "Exception in fetching public rooms {e}".format(
                    e=e
                ),
                exc_info=True
            )
        return messages