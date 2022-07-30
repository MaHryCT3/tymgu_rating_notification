from typing import Protocol

BigNumbers = {
    0: "0️⃣",
    1: "1️⃣",
    2: "2️⃣",
    3: "3️⃣",
    4: "4️⃣",
    5: "5️⃣",
    6: "6️⃣",
    7: "7️⃣",
    8: "8️⃣",
    9: "9️⃣",
}


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

    def __init__(self, new_position: int, old_position = None):
        self.new_position = new_position
        self.old_position = old_position
        self.new_position_smile = self.new_position
        self.old_position_smile = self.old_position
        self._reformat_numbers()

    def formatter(self):
        message = self._format_message()
        return message

    def _format_message(self):
        if self.old_position is None:
            return (f"🐣*Позиция в рейтинге \- * __{self.new_position_smile}__")
        else:
            if self.old_position == self.new_position:
                return(f"👀*Ты все еще на * __{self.new_position_smile}__ *месте\. *")
            if self.new_position > self.old_position:
                return(f"👺*Ты спустился вниз\! * ~{self.old_position_smile}~ \-\> __{self.new_position_smile}__ ")
            if self.new_position < self.old_position:
                return (f"🥳🥳*Сам бог велел, ты теперь не  на* ~{self.old_position_smile}~*, а на *__{self.new_position_smile}__🎀")
    
    def _reformat_numbers(self):
        self.new_position_smile = self._reformat_positions(self.new_position)
        self.old_position_smile = self._reformat_positions(self.old_position)

    def _reformat_positions(self, positions: int) -> str:
        new_number = ""
        for number in str(positions):
            new_number += BigNumbers.get(int(number), number)
        return new_number
        

def format_message(_MessageFormatter: MessageFormatter):
    return _MessageFormatter.formatter()