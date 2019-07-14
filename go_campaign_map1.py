from my_lib.participant_list import ParticipantList
from my_lib.island import Island
from my_lib.island_view import IslandView
from my_lib.wall import Wall
from my_lib.wall_view import WallView

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
participant_list = ParticipantList()
team_num = 60
for id in range(0, team_num):
    participant_list.append_id(id+1)

islands = [
    Wall("A", 16),
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
    start = islands[i_is].inject_from_list(participant_list, start, end)

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
