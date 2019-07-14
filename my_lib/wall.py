class Wall(object):
    """
    壁。
    """

    def __init__(self, edge_size):
        self._edge = [0] * edge_size
        return

    @property
    def edge(self):
        return self._edge

    @property
    def size(self):
        return len(self._edge)

    def at(self, index):
        return self._edge[index]

    def insert_from_list(self, list):
        print("List size : {}".format(len(list)))
        print("Edge size1: {}".format(self.size))
        size = min(self.size, len(list))
        for i in range(0, size):
            self._edge[i] = list[i]
        print("Edge size2: {}".format(self.size))

    def iter(self, callback):
        print("Edge size3: {}".format(self.size))
        for i in range(0, self.size):
            callback(i)
        return
