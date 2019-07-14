from placement.participant import Participant
from placement.island import Island
from placement.island_view import IslandView
from placement.wall import Wall
from placement.wall_view import WallView

"""
Example
-------

Campaign map 1.



+--+--+--+--+--+     +--+--+--+--+     +--+--+--+--+--+--+--+
|  |  |  |  |  |C    |  |  |  |  |B    |  |  |  |  |  |  |  |
+--+--+--+--+--+     +--+--+--+--+     +--+--+--+--+--+--+--+
|  |                                                     |  |
+--+  +--+--+--+     +--+--+--+--+     +--+--+--+--+--+  +--+
|  |  |  |  |  |F    |  |  |  |  |E    |  |  |  |  |  |D |  |
+--+  +--+--+--+     +--+--+--+--+     +--+--+--+--+--+  +--+
|  |  |  |  |  |     |  |  |  |  |     |  |  |  |  |  |  |  |
+--+  +--+--+--+     +--+--+--+--+     +--+--+--+--+--+  +--+
|  |                                                     |  |
+--+--+--+--+--+                       +--+--+--+--+--+--+--+
|  |  |  |  |  |                      A|  |  |  |  |  |  |  |
+--+--+--+--+--+                       +--+--+--+--+--+--+--+
                                      
"""

# Settings.
id_list = []
team_num = 60
for id in range(0, team_num):
    id_list.append(id+1)

islands = [
    Wall("A", 18),
    Wall("B", 4),
    Wall("C", 14),
    Island("D", 5, 5),
    Island("E", 4, 4),
    Island("F", 3, 3),
]

# Entry.
start = 0
for i_is in range(0, len(islands)):
    end = start + len(islands[i_is])
    start = islands[i_is].inject_from_id_list(id_list, start, end)

# Show.
wall_view = WallView()
island_view = IslandView()
for i_is in range(0, len(islands)):
    print("{} island.".format(islands[i_is].name))
    if type(islands[i_is]) is Island:
        island_view.show(islands[i_is])
    else:
        wall_view.show(islands[i_is])

print("Info    : Finished.")
