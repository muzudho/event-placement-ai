import os
from attribute.participant import Participant
from placement.island import Island
from placement.island_view import IslandView
from placement.wall import Wall
from placement.wall_view import WallView
from attribute.id_sort import id_sort

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

CCCCC..BBBB..AAAAAAA
C..................A
C.FFF..EEEE..DDDDD.A
C.FFF..EEEE..DDDDD.A
C..................A
CCCCC........AAAAAAA

"""

# Participants.
participant_list_src = id_sort(
    "{}/event-placement-ai/data/participant.csv".format(os.getcwd()))
"""
ID,GENRE_CODE
1,Red
2,Red
3,Blue
"""

id_list = []
for i in range(0, len(participant_list_src)):
    id_list.append(participant_list_src[i][0])

print("id_list: {}".format(id_list))

# Settings of placement.
"""
team_num = 60
id_list = []
for id in range(0, team_num):
    id_list.append(id+1)
"""

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
