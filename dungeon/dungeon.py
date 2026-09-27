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


def get_map_from_file(file):
    with open(file) as f:
        return f.read().splitlines()


def get_map(from_file=None):
    if not from_file:
        list_of_strings = get_starter_map()
    else:
        list_of_strings = get_map_from_file(from_file)
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


def start_new_run(remove_doors=False, from_file=None):
    start = None
    map = get_map(from_file)
    for j, r in enumerate(map):
        for i, l in enumerate(r):
            if l == "S":
                start = Point(i, j)
            if l == "D" and remove_doors:
                map[j][i] = "."
    if not start:
        raise Exception("Didn't find the start omg")
    return PlayerState(start, 0, 0, False), map


def do_a_run(moves, remove_doors=False, from_file=None):
    state, map = start_new_run(remove_doors, from_file)
    return execute_moves(moves, state, map)


def execute_moves(moves, state, map):
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


def find_route_to_target(pos, map, target, blocking_symbols):
    visited = [[False for _ in row] for row in map]
    visited[pos.j][pos.i] = True
    if map[pos.j][pos.i] == target:
        return ""
    queue = []
    queue.append((pos, ""))

    def process_a_move(new_pos, new_path):
        if (
            not visited[new_pos.j][new_pos.i]
            and map[new_pos.j][new_pos.i] not in blocking_symbols
        ):
            queue.append((Point(new_pos.i, new_pos.j), new_path))
            visited[new_pos.j][new_pos.i] = True
            if map[new_pos.j][new_pos.i] == target:
                return new_path
        return None

    while len(queue) > 0:
        p, path = queue.pop(0)
        for new_point, new_path in [
            (Point(p.i, p.j + 1), path + "d"),
            (Point(p.i, p.j - 1), path + "u"),
            (Point(p.i + 1, p.j), path + "r"),
            (Point(p.i - 1, p.j), path + "l"),
        ]:
            winning_path = process_a_move(new_point, new_path)
            if winning_path:
                return winning_path
    return None


def solve_map_no_doors_and_run():
    state, map = start_new_run(True, "dungeon1.txt")
    route = find_route_to_target(state.pos.copy(), map, "E", set("#"))
    print("number of moves is", len(route), "route is", route)
    state = do_a_run(route, True, "dungeon1.txt")
    print("final sate is", state)


def solve_by_treasure_key_door_exit():
    state, map = start_new_run(False, "dungeon_big.txt")
    # print_map_nice(map)

    route = find_route_to_target(state.pos.copy(), map, "k", set({"#", "D"}))
    state = execute_moves(route, state, map)
    route = find_route_to_target(state.pos.copy(), map, "T", set("#"))
    state = execute_moves(route, state, map)
    route = find_route_to_target(state.pos.copy(), map, "E", set("#"))
    state = execute_moves(route, state, map)
    print(state)


def test_do_a_run():
    # hit a door
    result = do_a_run("dddrrurrddrr")
    print(result)

    # get a key
    result = do_a_run("dddrrurruurrddrruu")
    print(result)
    # wins
    result = do_a_run("dddrrurruurrddrruuddlluulldddddddddrrrrr")
    print(result)


test_do_a_run()
print("\nSolving no doors\n")
solve_map_no_doors_and_run()
print("\nSolving \n")
solve_by_treasure_key_door_exit()
