class Island(object):
    """
    島。
    """

    def __init__(self, north_len, south_len):
        self._north_edge = [] * north_len
        self._south_edge = [] * south_len
        return

    @property
    def north_edge(self):
        return self._north_edge

    @property
    def south_edge(self):
        return self._south_edge
