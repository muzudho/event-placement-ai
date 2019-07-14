class Wall(object):
    """
    壁。1列。
    """

    def __init__(self, name, edge_size):
        self._name = name
        self._edge = [0] * edge_size
        return

    def __len__(self):
        return len(self._edge)

    @property
    def name(self):
        return self._name

    @property
    def edge(self):
        return self._edge

    def at(self, index):
        return self._edge[index]

    def inject_from_list(self, list, start, end):
        sub_list = list.slice(start, end)

        # print("List size : {}".format(len(list)))
        # print("Edge size1: {}".format(self.size))
        size = min(len(self), len(sub_list))
        for i in range(0, size):
            self._edge[i] = sub_list[i]
        # print("Edge size2: {}".format(self.size))
        return start + size

    def iter(self, callback):
        # print("Edge size3: {}".format(self.size))
        for i in range(0, len(self)):
            callback(i)
        return
