
def solution(filename):
    with open(filename) as fp:
        data = fp.readlines()

    # Initial position
    depth = 0
    horizontal = 0

    # cycle over planned course
    for line in data:
        command, units = line.split()
        if command == "forward":
            horizontal += int(units)
        if command == "down":
            depth += int(units)
        if command == "up":
            depth -= int(units)

    return depth * horizontal

if __name__ == "__main__":
    result = solution("./example.txt")
    print(result)   # it should be 150

    result = solution("./input.txt")
    print(result)
