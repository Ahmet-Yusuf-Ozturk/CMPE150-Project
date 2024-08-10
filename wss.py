text_input = input()

text_input = text_input.split(",N,")

height_list = []
width_list = []

for _ in text_input:
    curr_width = -1
    curr_height = 0
    row = _.split(",")
    for shapes in row:
        if shapes.startswith("T"):
            curr_width += 2 * int(shapes[1:])
            curr_height = max(curr_height, int(shapes[1:]))
        elif shapes.startswith("S"):
            curr_width += int(shapes[1:]) + 1
            curr_height = max(curr_height, int(shapes[1:]))
        elif shapes.startswith("R"):
            r_height, r_width = shapes[1:].split("x")
            r_height, r_width = int(r_height), int(r_width)
            curr_width += r_width + 1
            curr_height = max(curr_height, r_height)
        elif shapes.startswith("E"):
            r_height, r_width = shapes[1:].split("x")
            r_height, r_width = int(r_height), int(r_width)
            curr_width += r_width + 1
            curr_height = max(curr_height, r_height)
        elif shapes.startswith("V"):
            curr_width += int(shapes[1:]) + 1
            curr_height = max(curr_height, (int(shapes[1:]) + 1) // 2)
        elif shapes.startswith("B"):
            curr_height += 1
        elif shapes.startswith("O"):
            curr_width += int(shapes[1:])

    if "DL" in row:
        curr_height += 1

    height_list.append(curr_height)
    width_list.append(curr_width)

max_width = max(width_list)

for index, _ in enumerate(text_input):
    row = _.split(",")
    curr_width = width_list[index]
    curr_height = height_list[index]
    curr_matrix = [[" " for _ in range(max_width)] for _ in range(curr_height)]

    start_place = (max_width - curr_width) // 2

    if "DL" in row:
        curr_matrix[0] = ["-" for _ in range(max_width)]

    current_row = curr_height

    for shapes in row:
        if shapes.startswith("T"):
            shape_height = int(shapes[1:])
            shape_width = 2 * shape_height - 1
            for i in range(shape_height):
                for j in range(shape_width):
                    if shape_height - 1 + i >= j >= shape_height - 1 - i:
                        curr_matrix[current_row - shape_height + i][start_place + j] = "*"
            start_place += shape_width + 1
        elif shapes.startswith("S"):
            shape_size = int(shapes[1:])
            for i in range(shape_size):
                for j in range(shape_size):
                    curr_matrix[current_row - shape_size + i][start_place + j] = "*"
            start_place += shape_size + 1
        elif shapes.startswith("R"):
            shape_height, shape_width = shapes[1:].split("x")
            shape_height, shape_width = int(shape_height), int(shape_width)
            for i in range(shape_height):
                for j in range(shape_width):
                    curr_matrix[current_row - shape_height + i][start_place + j] = "*"
            start_place += shape_width + 1
        elif shapes.startswith("E"):
            shape_height, shape_width = shapes[1:].split("x")
            shape_height, shape_width = int(shape_height), int(shape_width)
            start_place += shape_width + 1
        elif shapes.startswith("V"):
            shape_width = int(shapes[1:])
            shape_height = shape_width // 2
            if "DL" in row:
                inverted_start_row = 1
            else:
                inverted_start_row = 0
            for i in range(shape_height + 1):
                for j in range(shape_width - 2 * i):
                    curr_matrix[inverted_start_row + i][start_place + i + j] = "*"
            start_place += shape_width + 1
        elif shapes.startswith("O"):
            start_place += int(shapes[1:])
    for row in curr_matrix:
        print("".join(row))

print("-" * max_width)
