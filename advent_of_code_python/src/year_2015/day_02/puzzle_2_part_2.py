from utils.utils import get_strings_from_file
from math import prod


def process_dimensions(input_list: list) -> int:
    length_collector: int = 0

    for dimension in input_list:
        l_w_h: list[int] = [int(size) for size in dimension.split("x")]
        l_w_h.sort()

        ribbon_wrap: int = 2 * l_w_h[0] + 2 * l_w_h[1]
        ribbon_bow: int = prod(l_w_h)
        length_collector += ribbon_wrap + ribbon_bow

    return length_collector


input_file: str = r"puzzle_input.txt"
dimensions_list: list[str] = get_strings_from_file(input_file)
feet_of_ribbon: int = process_dimensions(dimensions_list)

print("Feet of ribbon: " + str(feet_of_ribbon))


"""
[Answer]
Feet of ribbon: 3783758
"""
