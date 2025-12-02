from datetime import datetime

with open("../input/day2_product_id_ranges.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines if line]
id_ranges = [id_range for line in lines for id_range in line.split(",")]

start_time = datetime.now()
print(f"Start time: {start_time}\n")

total = 0
for id_range in id_ranges:
    [start, end] = id_range.split("-")
    for id in range(int(start), int(end) + 1):
        id_str = str(id)
        mid = len(id_str) // 2
        first_half = id_str[:mid]
        second_half = id_str[mid:]
        if first_half == second_half:
            total += id

end_time = datetime.now()
print(f"Part 1 Answer: {total}")
print(f"\nEnd time: {end_time}")
print(f"Time taken: {end_time - start_time}\n")
