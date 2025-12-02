from datetime import datetime

with open("locker_input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines if line]

start_time = datetime.now()
print(f"\nStart time: {start_time}\n")

pointer = 50
print(f"Pointer: {pointer}")
stops = 0
passes = 0

for line in lines:
    direction = line[0]
    distance = int(line[1:])
    print(f"{direction} {distance}")
    if pointer:
        passes += distance // 100
    else:
        passes += (distance - 1) // 100
    distance = distance % 100
    if direction == "R":
        new_pointer = (pointer + distance) % 100
        if pointer and new_pointer and new_pointer < pointer:
            passes += 1
    elif direction == "L":
        new_pointer = (pointer - distance) % 100
        if pointer and new_pointer and new_pointer > pointer:
            passes += 1
    else:
        print("Error: direction is not R or L")
        exit(1)
    pointer = new_pointer
    if pointer == 0:
        stops += 1
    print(f"Pointer: {pointer} Stops: {stops} Passes: {passes}")

end_time = datetime.now()
print(f"\nEnd time: {end_time}\n")
print(f"Part 1 Answer : {stops}")
print(f"Passes past 0 (without stopping at 0): {passes}")
print(f"Part 2 Answer : {stops + passes}")
print(f"Time taken: {end_time - start_time}\n")
