from turtle import title
from plyer import notification
#Notification Code
def Notification():
    notification.notify(
        title = "Drink a Cup ",
        message = "Please stop working take five minutes rest and work",
        app_icon = r"photo.ico",
        timeout = 5
    )

Notification()