Rocketchat: API for Chat
=========================

```python
    >>> from rocketchat.api import RocketChatAPI
    >>> api = RocketChatAPI(
            settings={
                'username': username,
                'password': password,
                'domain': url
                }
            )
    >>> api.send_message(message, roomID);
    >>> api.create_channel(name);
    >>> api.get_messages(roomID)
    >>> api.leave_room(roomID)
    >>> api.join_room(roomID)
    >>> api.create_user(
            name="Name",
            email="Email",
            password="Password",
            username="Username",
        )
    >>> api.update_user(
            user_id="userID",
            name="Name"
        )
```

Installation
------------

To install Requests, simply:

```bash
    $ pip install rocketchat
```
Satisfaction, guaranteed.

How to Contribute
-----------------

- Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a `Contributor Friendly` tag for issues that should be ideal for people who are not very familiar with the codebase yet.
- Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
- Write a test which shows that the bug was fixed or that the feature works as expected.
- Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.