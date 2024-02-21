from win10toast import ToastNotifier
from winotify import Notification, audio
import time


def send_notification_toast(title, message, icon_path, duration=5):
    toaster = ToastNotifier()
    toaster.show_toast(title=title, msg=message, icon_path=icon_path, duration=duration, threaded=True)


def send_notification_notify(app_name, title, message, dur, icon):
    toaster = Notification(app_id=app_name, title=title, msg=message, duration=dur, icon=icon)
    toaster.set_audio(audio.Default, loop=False)
    toaster.show()
