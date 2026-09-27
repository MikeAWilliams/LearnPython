import copy
import dataclasses
from operator import truediv


# hit a door "dddrrurrddrr"
def get_starter_map():
    return [
        "###########",
        "#S..#...#k#",
        "#.#.#.#.#.#",
        "#.#...#...#",
        "#T..#.#####",
        "#.###..D.E#",
        "###########",
    ]


def get_map_from_file():
    with open("dungeon1.txt") as f:
        return f.readlines()


def get_map():
    # list_of_strings = get_starter_map()
    list_of_strings = get_map_from_file()
    dungeon = [list(r) for r in list_of_strings]
    return dungeon


def print_map_nice(map):
    print("the map")
    for r in map:
        print(r)


@dataclasses.dataclass
class Point:
    i: int
    j: int

    def copy(self):
        return copy.deepcopy(self)


@dataclasses.dataclass
class PlayerState:
    pos: Point
    treasure: int
    keys: int
    victory: bool

    def copy(self):
        return copy.deepcopy(self)


def start_new_run(remove_doors=False):
    start = None
    map = get_map()
    for j, r in enumerate(map):
        for i, l in enumerate(r):
            if l == "S":
                start = Point(i, j)
            if l == "D" and remove_doors:
                map[j][i] = "."
    if not start:
        raise Exception("Didn't find the start omg")
    return PlayerState(start, 0, 0, False), map


def do_a_run(moves, remove_doors=False):
    state, map = start_new_run(remove_doors=remove_doors)
    for m in moves:
        new_pos = state.pos.copy()
        if m == "u":
            new_pos.j -= 1
        elif m == "d":
            new_pos.j += 1
        elif m == "l":
            new_pos.i -= 1
        elif m == "r":
            new_pos.i += 1

        execute_move = False
        if map[new_pos.j][new_pos.i] == ".":
            execute_move = True
        elif map[new_pos.j][new_pos.i] == "T":
            execute_move = True
            state.treasure += 1
            map[new_pos.j][new_pos.i] = "."
        elif map[new_pos.j][new_pos.i] == "k":
            execute_move = True
            state.keys += 1
            map[new_pos.j][new_pos.i] = "."
        elif map[new_pos.j][new_pos.i] == "D" and state.keys > 0:
            execute_move = True
            state.keys -= 1
            map[new_pos.j][new_pos.i] = "."
        elif map[new_pos.j][new_pos.i] == "E":
            state.victory = True
            return state

        if execute_move:
            state.pos = new_pos
    return state


def solve_map_no_doors(pos, map):
    visited = [[False for _ in row] for row in map]
    visited[pos.j][pos.i] = True
    if map[pos.j][pos.i] == "E":
        return ""
    queue = []
    queue.append((pos, ""))
    while len(queue) > 0:
        p, path = queue.pop(0)
        if map[p.j + 1][p.i] != "#" and not visited[p.j + 1][p.i]:
            queue.append((Point(p.i, p.j + 1), path + "d"))
            visited[p.j + 1][p.i] = True
            if map[p.j + 1][p.i] == "E":
                return path + "u"
        if map[p.j - 1][p.i] != "#" and not visited[p.j - 1][p.i]:
            queue.append((Point(p.i, p.j - 1), path + "u"))
            visited[p.j - 1][p.i] = True
            if map[p.j - 1][p.i] == "E":
                return path + "d"
        if map[p.j][p.i + 1] != "#" and not visited[p.j][p.i + 1]:
            queue.append((Point(p.i + 1, p.j), path + "r"))
            visited[p.j][p.i + 1] = True
            if map[p.j][p.i + 1] == "E":
                return path + "r"
        if map[p.j][p.i - 1] != "#" and not visited[p.j][p.i - 1]:
            queue.append((Point(p.i - 1, p.j), path + "l"))
            visited[p.j][p.i - 1] = True
            if map[p.j][p.i - 1] == "E":
                return path + "l"
    raise Exception("couldn't find the exit")


def solve_map_no_doors_and_run():
    state, map = start_new_run(True)
    route = solve_map_no_doors(state.pos.copy(), map)
    print("number of moves is", len(route), "route is", route)
    state = do_a_run(route, True)
    print("final sate is", state)


state, map = start_new_run(True)
print_map_nice(map)

# hit a door
result = do_a_run("dddrrurrddrr")
print(result)

# get a key
result = do_a_run("dddrrurruurrddrruu")
print(result)
# wins
result = do_a_run("dddrrurruurrddrruuddlluulldddddddddrrrrr")
print(result)

print("\nsolving without doors\n")
solve_map_no_doors_and_run()
