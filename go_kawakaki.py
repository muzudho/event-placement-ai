from placement.island import Island
from placement.island_view import IslandView
from placement.wall import Wall
from placement.wall_view import WallView

"""
Example
-------

第29回世界コンピュータ将棋選手権
http://sizer.main.jp/wcsc29/

川崎市産業振興会館 ４F
https://kawasaki-sanshinkaikan.jp/gyoumu/kaikan/hall-guide/4f.html


G              E                C              A island
+--+--+--+--+  +--+--+--+--+    +--+--+--+--+  +--+--+--+--+
|  |  |  |  |  |  |  |  |  |    |  |  |  |  |  |  |  |  |  |
+--+--+--+--+  +--+--+--+--+    +--+--+--+--+  +--+--+--+--+
|  |  |  |  |  |  |  |  |  |    |  |  |  |  |  |  |  |  |  |
+--+--+--+--+  +--+--+--+--+    +--+--+--+--+  +--+--+--+--+

H              F                D              B
+--+--+--+--+  +--+--+--+--+    +--+--+--+--+  +--+--+--+--+
|  |  |  |  |  |  |  |  |  |    |  |  |  |  |  |  |  |  |  |
+--+--+--+--+  +--+--+--+--+    +--+--+--+--+  +--+--+--+--+
|  |  |  |  |  |  |  |  |  |    |  |  |  |  |  |  |  |  |  |
+--+--+--+--+  +--+--+--+--+    +--+--+--+--+  +--+--+--+--+

"""

# Settings.
id_list = []
team_num = 40
for id in range(0, team_num):
    id_list.append(id+1)

islands = [
    Island("A", 4, 4),
    Island("B", 4, 4),
    Island("C", 4, 4),
    Island("D", 4, 4),
    Island("E", 4, 4),
    Island("F", 4, 4),
    Island("G", 4, 4),
    Island("H", 4, 4),
]

# Entry.
start = 0
for i_is in range(0, len(islands)):
    end = start + len(islands[i_is])
    start = islands[i_is].inject_from_id_list(id_list, start, end)

# Show.
island_view = IslandView()
for i_is in range(0, len(islands)):
    print("{} island.".format(islands[i_is].name))
    island_view.show(islands[i_is])

print("Info    : Finished.")
