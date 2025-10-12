def get_integers_from_file(file: str) -> list[int]:
    with open(file=file, mode="r", encoding="utf-8") as input_file:
        return [int(line.strip()) for line in input_file.readlines()]


def get_strings_from_file(file: str) -> list[str]:
    with open(file=file, mode="r", encoding="utf-8") as input_file:
        return [line.strip() for line in input_file.readlines()]


def get_strings_as_matrix_from_file(file: str) -> list[list[str]]:
    with open(file=file, mode="r", encoding="utf-8") as input_file:
        return [list(line.strip()) for line in input_file.readlines()]
