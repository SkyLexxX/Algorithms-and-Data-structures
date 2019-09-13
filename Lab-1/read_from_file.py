from hotel import Hotel


def read_from_file(filename):
    with open(filename) as file:
        list = []
        for line in file:
            line = line.split(",")
            list.append(Hotel(line[0], int(line[1]), int(line[2])))
        return list

