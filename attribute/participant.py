class Participant(object):
    """
    参加者データ
    """

    def __init__(self, id, genre_code):
        self._id = id
        self._genre_code = genre_code
        return

    @property
    def id(self):
        return self._id

    @property
    def genre_code(self):
        return self._genre_code
