class Participant(object):
    def __init__(self, id):
        self._id = id
        return

    @property
    def id(self):
        return self._id
