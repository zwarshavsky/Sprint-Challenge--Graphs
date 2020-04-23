from room import Room
from player import Player
from world import World
from utils import Graph, Queue, Stack
import sys

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
origin_room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(origin_room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

room_graph = {}
for i in range(len(origin_room_graph)):
    room_graph[i] = origin_room_graph[i]



#Created Graph Object for DFS Method
gg = Graph()
for i in room_graph:
        gg.add_vertex(i)
for i in room_graph:
    for key in room_graph[i][1]:
        gg.add_edge(i,room_graph[i][1][key])

# copy_of_origin_room_graph = origin_room_graph
# for key in copy_of_origin_room_graph:
#     copy_of_origin_room_graph[key][1])


# print(origin_room_graph[1][1])


def get_neighbors(room):
    neighbors = []
    if room.n_to is not None:
        neighbors.append(room.n_to.id)
    if room.s_to is not None:
        neighbors.append(room.s_to.id)
    if room.w_to is not None:
        neighbors.append(room.w_to.id)
    if room.e_to is not None:
        neighbors.append(room.e_to.id)
    return neighbors

# print(world.rooms[0].n_to.id)

dft_path = gg.dft(0)
test_path = dft_path
new_list = []


# print(dft_path)
for index,current_room in enumerate(test_path):
    room_lookup = world.rooms[current_room]
    if index + 1 < len(test_path):
        if test_path[index + 1] in get_neighbors(room_lookup):
            new_list.append(current_room)
        else:
            missing_rooms = gg.bfs(current_room,test_path[index + 1])[:-1]
            # print(gg.bfs(current_room,test_path[index + 1])[1:-1])
            print(index,missing_rooms)
            # temp_index = index
            for missing_room in missing_rooms:
                new_list.append(missing_room)
            #     # print(index,temp_index,missing_rooms[index2])
            #     # test_path.insert(temp_index,missing_rooms[index2])
            # # #     # print(test_path)
            #     temp_index += 1 

new_list.append(test_path[-1])

# print(new_list)


for index,room in enumerate(new_list):
    try:
        room1 = room
        room2 =  new_list[index+1]
        # print(room1,room2)
        for _ in room_graph[room1][1].items():
            if (room2) in _:
                direction = _[0] 
                traversal_path.append(direction)
            else:
                continue
                # print("something is wrong!")
    except:
        continue
        # print("list index out of range")

# print(room_graph[new_list[0]][1].items())
print(len(traversal_path))
print(len(new_list))







# print(len(test_path))



# print(dft_path)


# OLD ATTEMPT AT INSERT LIST

# for index,current_room in enumerate(test_path):
#     room_lookup = world.rooms[current_room]
#     if index + 1 < len(test_path):
#         if test_path[index + 1] in get_neighbors(room_lookup):
#             new_list.append(current_room)
#         else:
#             missing_rooms = gg.bfs(current_room,test_path[index + 1])[:-1]
#             # print(gg.bfs(current_room,test_path[index + 1])[1:-1])
#             print(index,missing_rooms)
#             temp_index = index
#             for index2,missing_room in enumerate(missing_rooms):
#             #     # print(index,temp_index,missing_rooms[index2])
#             #     # test_path.insert(temp_index,missing_rooms[index2])
#             # # #     # print(test_path)
#             #     temp_index += 1 
 

# print(new_list)
# # print(len(test_path))






# CODE FOR GREEDY PATH BETWEEN NODES N, N + 1, etc

# t_path = []
# count = 0 
# for i in gg.vertices:
#     t_path.append(gg.bfs(i,i+1))

# print(gg.vertices)
# print(t_path[:3])
# print(len(t_path))
# v_s = set()
# for path in t_path:
#     if path:
#         # print(path)
#         v_s.add(path[0])
#         # while len(v_s) < len(gg.vertices):
#         for index,room in enumerate(path):
#                 try:
#                     room1 = room
#                     room2 =  path[index+1]
#                     # print(room1,room2)
#                     for _ in room_graph[room1][1].items():
#                         if (room2) in _:
#                             direction = _[0] 
#                             # print(direction)
#                             traversal_path.append(direction)
#                             v_s.add(room2)
#                         # print("line1:",room,_[0])
#                         # print("line2:",room_graph[room][1].items()[0])
#                 except:
#                     continue



# print(traversal_path)
# print(len(v_s))
# print(gg.vertices)


###################################################


# v_s = set()
# for path in t_path:
#     if path:
#         # print(path)
#         v_s.add(path[0])
#         for index,room in enumerate(path):
#                 try:
#                     room1 = room
#                     room2 =  path[index+1]
#                     if (room2) not in v_s:
#                         for exit_options in room_graph[room1][1].items():
#                             direction = exit_options[0] 
#                             traversal_path.append(direction)
#                             v_s.add(room2)
#                             print("new room!!",room2,v_s)
#                     elif (room2) in v_s:
#                         for neighbor in gg.get_neighbors(room1):
#                             print("neighbor of current room:",neighbor)
#                             if neighbor not in v_s:
#                                 print("possible item for jump:",neighbor)
#                                 for exit_options in room_graph[neighbor][1].items():
#                                     print("exit_options:",exit_options,"for:",item)
                                #     if item not in v_s:
                                #         print(_[0],_[1])
                                # print(f"been to {room2} already!")
                                # print("new path awaits!")
                                # print(item,room_graph[item][1])
                                # print(room_graph[item][1]) 
                            # else:
                            #     pass
                                # print("no other choice")


                            # elif item in gg.get_neighbors(room2) not in v_s:
                            #     print("eureka!!",room2,v_s,direction) 
                # except:
                #     continue

# print(len(traversal_path))
# print(len(traversal_path))
# print(traversal_path)
# print(len(t_path))
# print(t_path)
# print(v_s)

# print(3 in gg.get_neighbors(0))
    

# next steps: 1) Look up the current room's available rooms (get_neighbors), if the other available room are not in the visited_set, then go there


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
# # print(player.current_room.id)

step = 0
# print(traversal_path)
for move in traversal_path:
    step += 1 
    player.travel(move)
    visited_rooms.add(player.current_room)
    # print(step,move,player.current_room.id)

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

# ll = set()
# counter = 0 
# with open("maps/test_cross.txt", "r") as f:
#     content = [x.strip() for x in f.readlines()]
#     content.remove("}")
#     content.remove("{")

# # print(content[0])
# print(content[0])
# gg = Graph()
# for i in range len(content):
#     gg.add_vertex(content[i][0])
# for i in range len(content):
#     gg.add_edge(content[i][0])



# if __name__ == '__main__':
#     ll = bfs(graph,4,7)
#     print(ll)