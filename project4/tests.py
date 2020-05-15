from project4.helpers import load_map_40
from project4.shortest_path import shortest_path


MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5,  [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24]),
    (8, 3, [8, 14, 16, 37, 12, 17, 15, 3])
]

def _test(shortest_path_function):
    map_40 = load_map_40()
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path_function(map_40, start, goal)
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start,
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")

_test(shortest_path)
