from my_lib.wall import Wall


class WallView(object):
    def __init__(self):
        return

    def show(self, wall):
        def visit(i):
            print("[{:>3}]".format(wall.at(i)), end="")
            return

        wall.iter(visit)
        return
