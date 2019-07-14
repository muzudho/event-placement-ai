from my_lib.wall import Wall


class Island(object):
    """
    島。壁を使い回して2列にする。
    """

    def __init__(self, name, len0, len1):
        self._name = name
        self._edges = [Wall(name, len0), Wall(name, len1)]
        return

    def __len__(self):
        total = 0
        for entry in self._edges:
            total += len(entry)

        return total

    @property
    def name(self):
        return self._name

    def inject_from_id_list(self, id_list, start, end):
        end = 0
        for i_ed in range(0, 2):
            end = start + len(self._edges[i_ed])
            start = self._edges[i_ed].inject_from_id_list(id_list, start, end)

        return end

    def iter(self, cell_callback, line_callback):
        # print("Edge size3: {}".format(self.size))
        for i_ed in range(0, 2):
            for i_ce in range(0, len(self._edges[i_ed])):
                cell_callback(self._edges[i_ed].at(i_ce))
            line_callback(i_ed)
        return

    def at(self, index):
        """
        通し番号でアクセス。
        """

        if index < len(self._edges[0]):
            return self._edges[0].at(index)
        else:
            return self._edges[1].at(index - len(self._edges[0]))
