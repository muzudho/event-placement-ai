class Search(object):

    def __init__(self):
        self._max_value = -1
        self._prod_num = 0
        self._var_num = 0
        self._progress_num = 0
        self._retry = True
        print("Info    : Search __init__ self._retry={}".format(self._retry))
        return

    @property
    def max_value(self):
        return self._max_value

    @max_value.setter
    def max_value(self, value):
        self._max_value = value

    @property
    def prod_num(self):
        return self._prod_num

    @prod_num.setter
    def prod_num(self, value):
        self._prod_num = value

    @property
    def var_num(self):
        return self._var_num

    @var_num.setter
    def var_num(self, value):
        self._var_num = value

    @property
    def progress_num(self):
        return self._progress_num

    @progress_num.setter
    def progress_num(self, value):
        self._progress_num = value

    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
