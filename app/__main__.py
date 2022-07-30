from exceptions import *
from formatter import format_message, MarkDownFormatter
from notification import send_notification, TelegramNotification, Notification
from rating import TymGyRating
from settings import get_settings, get_settings_dict, set_settings
from dotenv import load_dotenv
from repeater import repeater

load_dotenv(".env")

#TODO: Сделать датакласс для настроек

Notifications = {
    "Telegram": TelegramNotification
}

Formatters = {
    TelegramNotification: MarkDownFormatter 
}

def get_notifications_list():
    notifications_settings: list = get_settings("notifications")
    notifications_list = [value for key, value in Notifications.items() if key in notifications_settings]
    if not notifications_list:
        raise Notifications
    return notifications_list



def run_notification(notifications: list[type[Notification]], rating: TymGyRating):
    new_position = rating.get_rating_position()
    old_position = get_settings("last_position")
    set_settings("last_position", new_position)
    if old_position is None:
        old_position =  new_position
    for notification in notifications:
        message = format_message(Formatters[notification](
            new_position=new_position, old_position=old_position
        ))
        send_notification(notification(message))
    


def main():
    settings = get_settings_dict()
    UID = settings.get("UID")
    page_id = settings.get("page_id")
    rating = TymGyRating(UID=UID, page_id=page_id)
    delay = int(settings.get("repeat_time", 3600))
    notifications_list = get_notifications_list()
    repeater(run_notification, delay, notifications = notifications_list, rating=rating)


if __name__ == "__main__":
    main() # TODO: Добавить обработку всех ошибок, с тектом что нужно возможно нужно сделать для их исправления
    
