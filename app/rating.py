import requests
import json
from exceptions import CantGetRating, UIDNotFound

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

class TymGyRating:
    """Класс для получения рейтинга из заданных параметров
    
    Args:
        UID: str - Снилс или какой то уид, по которому нужно искать аббитуирента
        page_id: str - айди рейтинга, надеюсь в readme будет инструкция как его найти
    Raises:
        CantGetRating - Произошла какая то ошибка с запросом, возможно неверные параметры или просто напросто апи умерло
        UIDNotFound - По уиду не было найдено в данном page_id аббитуирента
    """

    def __init__(self, UID: str, page_id: str):
        """"""
        self._UID = UID
        self._api_url = "https://ratings.utmn.ru/api/rating/"
        self._api_query = self._build_query(page_id)

        self._session = requests.Session()
        self._session.headers.update(user_agent)

    def _build_query(self, page_id) -> set:
        query = {"action": "ratingdata", "pageid": page_id}
        return query

    def get_rating_position(self) -> int:
        """Возвращает номер позиции в рейтинге"""
        rating = self.get_rating()
        position = self._get_position(rating)
        if position == 0:
            raise UIDNotFound
        return position
    
    def get_rating(self) -> dict:
        try:
            rating = self._session.get(url=self._api_url, params=self._api_query)
        except requests.RequestException:
            raise CantGetRating
        else:
            return self._get_json_from_response(rating)

    def _get_json_from_response(self, response: requests.Response) -> dict:
        try:
            decoded_data = response.text.encode().decode("utf-8-sig")
        except Exception:
            raise CantGetRating
        else:
            return json.loads(decoded_data)
    
    def _get_position(self, rating: dict) -> int:
        abiturients: list[dict] = rating["#value"].get("Abiturients")
        for index, abiturient in enumerate(abiturients):
            if abiturient.get("FIO") == self._UID:
                return index + 1
        else:
            return 0