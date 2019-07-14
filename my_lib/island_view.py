from my_lib.island import Island


class IslandView(object):
    def __init__(self):
        return

    def show(self, island):
        def visit_cell(id):
            print("[{:>3}]".format(id), end="")

        def visit_line(edge_num):
            print("")

        island.iter(visit_cell, visit_line)
        return
