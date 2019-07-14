class ParticipantList(object):
    def __init__(self):
        self._entry = []

    def __len__(self):
        return len(self._entry)

    def append_id(self, id):
        self._entry.append(id)

    def slice(self, start, end):
        # print("self._entry : {}".format(self._entry))
        # print("Start: {}".format(start))
        # print("End  : {}".format(end))
        arr = [entry for entry in self._entry[start:end]]
        # print("Arr  : {}".format(arr))

        return arr
