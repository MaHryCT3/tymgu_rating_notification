from typing import Protocol


class MessageFormatter(Protocol):
    """Протокол для  реалцизации форматера для сообщения
    Args:
        position: Позиция в рейтинге
    """

    def __init__(self, new_position: str, old_position: str, *args, **kwargs):
        raise NotImplementedError

    def formatter(self):
        """Интерефейс для форматирования текста сообщения"""

class MarkDownFormatter:
    """MarkDown форматер можно использовать в телеграм сообщение"""

    def __init__(self, new_position: str, old_position = None):
        self.new_position = new_position
        self.old_position = old_position

    def formatter(self):
        message = self._format_message()
        return message

    def _format_message(self):
        return self.new_position


def format_message(_MessageFormatter: MessageFormatter):
    return _MessageFormatter.formatter()