from utils.utils import get_strings_from_file


def process_dimensions(input_list: list) -> int:
    area_collector: int = 0

    for dimension in input_list:
        l_w_h: list[int] = [int(size) for size in dimension.split("x")]
        l_w_h.sort()

        gift_area: int = 2 * l_w_h[0] * l_w_h[1] + 2 * l_w_h[1] * l_w_h[2] + 2 * l_w_h[2] * l_w_h[0]
        smallest_side_area: int = l_w_h[0] * l_w_h[1]
        area_collector += gift_area + smallest_side_area

    return area_collector


input_file: str = r"puzzle_input.txt"
dimensions_list: list[str] = get_strings_from_file(input_file)
wrapping_paper_square_feet: int = process_dimensions(dimensions_list)

print("Square feet of wrapping paper: " + str(wrapping_paper_square_feet))


"""
[Answer]
Square feet of wrapping paper: 1588178
"""
