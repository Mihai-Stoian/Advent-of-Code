from utils.utils import get_strings_from_file


def process_parentheses(input_list: list) -> int:
    floor_counter: int = 0
    position: int = 0

    for parenthesis in input_list[0]:
        position += 1

        if parenthesis == "(":
            floor_counter += 1
        else:
            floor_counter -= 1

        if floor_counter == -1:
            return position

    return position


input_file: str = r"puzzle_input.txt"
instructions_list: list[str] = get_strings_from_file(input_file)
position_of_character: int = process_parentheses(instructions_list)

print("Santa's floor is: " + str(position_of_character))


"""
[Answer]
Santa's floor: 1797
"""
