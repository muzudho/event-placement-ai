from my_lib.participant_list import ParticipantList
from my_lib.wall import Wall
from my_lib.wall_view import WallView

# Settings.
participant_list = ParticipantList()
for id in range(0, 11):
    participant_list.append_id(id+1)
start = 0
f_wall = Wall(10)

# Entry.
end = start + f_wall.size + 1
sub_list = participant_list.slice(start, end)
f_wall.insert_from_list(sub_list)
start = end

# Show.
wall_view = WallView()
wall_view.show(f_wall)
