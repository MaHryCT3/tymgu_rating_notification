from exceptions import *
from formatter import format_message, MarkDownFormatter
from notification import send_notification, TelegramNotification
from rating import TymGyRating
from settings import get_settings, get_settings_dict
from dotenv import load_dotenv

load_dotenv(".env")

#TODO: Сделать датакласс для настроек

def main():
    settings = get_settings_dict()
    rating = TymGyRating(settings.get("UID"), settings.get("page_id"))
    new_position = rating.get_rating_position()
    message = format_message(MarkDownFormatter(new_position, settings.get("last_position")))
    send_notification(TelegramNotification(message))


if __name__ == "__main__":
    main() # TODO: Добавить обработку всех ошибок, с тектом что нужно возможно нужно сделать для их исправления
    
