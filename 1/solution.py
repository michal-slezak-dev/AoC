# def solution_1_1(input_file):
#     # print((5-10) % 100)
#     # print(-10%100)

#     with open(input_file) as file:
#         rotations = [line.strip() for line in file]
#     # print(rotations)

#     state = 50
#     # dial_after_rotation = []
#     password = 0

#     for rotation in rotations:
#         direction = rotation[0]
#         distance = int(rotation[1:])

#         state = (state + distance) % 100 if direction == 'R' else (state - distance) % 100
#         if state == 0:
#             password += 1
#         print(f"rotation --> {state}")

#     return password

# print(solution_1_1('input.txt'))

def solution_1_1(input_file):
    state = 50
    password = 0
    with open(input_file) as file:
        for line in file:
            rotation = line.strip()
            direction = rotation[0]
            distance = int(rotation[1:])

            state = (state + distance) % 100 if direction == 'R' else (state - distance) % 100
            if state == 0:
                password += 1
            print(f"rotation --> {state}")

    return password

def solution_1_2(input_file):
    state = 50
    password = 0
    with open(input_file) as file:
        for line in file:
            rotation = line.strip()
            direction = rotation[0]
            distance = int(rotation[1:])
            direction_sign = 1 if direction == 'R' else -1

            for _ in range(1, distance + 1):
                state = (state + direction_sign) % 100

                if state == 0:
                    password += 1

                # if state > 99 or state < 0:
                #     state %= 100

                print(f"{state}")

    return password

print(solution_1_1('input1_1.txt'))
print()
print(solution_1_2('input1_2.txt'))
