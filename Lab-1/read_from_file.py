from hotel import Hotel


def read_from_file(filename):
    with open(filename) as file:
        list_of_numbers = []
        for line in file:
            line = line.strip("\n").split(",")
            list_of_numbers.append(Hotel(line[0], line[1], line[2]))
    return list_of_numbers
