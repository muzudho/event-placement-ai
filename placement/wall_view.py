from placement.wall import Wall


class WallView(object):
    def __init__(self):
        return

    def show(self, wall):
        def visit(id):
            print("[{:>3}]".format(wall.at(id)), end="")
            return

        wall.iter(visit)
        print("")
        return
