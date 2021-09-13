from pusher_push_notifications import PushNotifications


"""
Notification push with pusher Beams
"""


def push_notify(user_id, title, body):

    push_client = PushNotifications(
        instance_id="bf43c259-1895-47cd-83cf-82461abe58b5",
        secret_key="339532172AF3778E9C25495695A9CBA34269183BFE57B0D5DE2739D5290A0109",
    )
    response = push_client.publish_to_interests(
        interests=[str(user_id)],
        publish_body={
            "apns": {
                "aps": {
                    "alert": title,
                },
            },
            "fcm": {
                "notification": {
                    "title": title,
                    "body": body,
                },
            },
            "web": {
                "notification": {
                    "title": title,
                    "body": body,
                },
            },
        },
    )
    print(response["publishId"])
