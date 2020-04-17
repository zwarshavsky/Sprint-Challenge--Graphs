from room import Room
from player import Player
from world import World
from utils import Graph, Queue
import sys

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
# visited_rooms.add(player.current_room)


### Traversal Code ###

# qq = Queue()
# # visited_rooms.add(player.current_room.name)
# qq.enqueue([player.current_room.id])
# room_history = {}
# while len(visited_rooms) < len(world.rooms):
#     path = qq.dequeue()
#     # print("path:",path)
#     if path[-1] not in visited_rooms:
#         visited_rooms.add(path[-1])
#         print(visited_rooms)
#         for direction in player.current_room.get_exits():
#             # print(player.current_room.name)
#             room_history[player.current_room.id] = []
#             room_history[player.current_room.id].append(direction)
#             traversal_path.append(direction)
#             # print(f"You can walk {direction}!")
#             player.travel(direction, False)
#             path_copy = list(path)
#             path_copy.append(player.current_room.id)
#             qq.enqueue(path_copy)
#             # print(qq.size())
            
        
    # else:
    #     qq.dequeue()
            
        # if "n" in player.current_room.get_exits():
        #     print("You can walk north!")
        #     print("Queue size: -------", qq.size())
        #     player.travel("n", False)
        #     print(player.current_room)
        #     path_copy = list(path)
        #     path_copy.append(player.current_room.name)
        #     qq.enqueue(path_copy)
        # elif "s" in player.current_room.get_exits():
        #     print("You can walk south!")
        #     player.travel("s", False)
        #     print(player.current_room.name)
        #     path_copy = list(path)
        #     path_copy.append(player.current_room.name)
        #     qq.enqueue(path_copy)
        # elif "e" in player.current_room.get_exits():
        #     print("You can walk east!")
        #     player.travel("e", False)
        #     print(player.current_room.name)
        #     path_copy = list(path)
        #     path_copy.append(player.current_room.name)
        #     qq.enqueue(path_copy)
        # elif "w" in player.current_room.get_exits():
        #     print("You can walk west!")
        #     player.travel("w", False)
        #     print(player.current_room.name)
        #     path_copy = list(path)
        #     path_copy.append(player.current_room.name)
        #     qq.enqueue(path_copy)
        # else:
        #     print("not my game, man!")
        # for room in player.travel("n",True) or player.travel("s",True) or player.travel("e",True) or player.travel("w",True):
           
# print(len(traversal_path),traversal_path,len(visited_rooms),visited_rooms,qq.size(),room_history)
# print(visited_rooms,room_history)



# New traversal code

qq = Queue()
qq.enqueue([player.current_room])
while qq.size() > 0:
    path = qq.dequeue()
    if path[-1] not in visited_rooms:
        print(path[-1].id)
        visited_rooms.add(path[-1])
        for direction in path[-1].get_exits():
            path_copy = list(path)
            path_copy.append(path[-1].get_room_in_direction(direction))
            traversal_path.append(direction)
            qq.enqueue(path_copy)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")






#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

# ll = []
# counter = [] 
# with open("maps/test_line.txt", "r") as f:
#     for word in f.readlines():
#         counter += 1
#         # print(f'{counter} {word}')
#         for i in word.split(","):
#             print(i)
