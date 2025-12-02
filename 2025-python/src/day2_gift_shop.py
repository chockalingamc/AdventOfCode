from datetime import datetime

with open("../input/day2_product_id_ranges.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines if line]
id_ranges = [id_range for line in lines for id_range in line.split(",")]

start_time = datetime.now()
print(f"Start time: {start_time}\n")

first_total = 0
second_total = 0
for id_range in id_ranges:
    [start, end] = id_range.split("-")
    for id in range(int(start), int(end) + 1):
        id_str = str(id)
        length = len(id_str)
        mid = length // 2
        for chunk_size in range(mid, 0, -1):
            if length % chunk_size: # string does not split into equal part of chunk_size length
                continue
            first_chunk = id_str[:chunk_size]
            is_invalid = True
            for i in range(1, length // chunk_size):
                next_chunk = id_str[chunk_size*i:chunk_size*(i+1)]
                if first_chunk != next_chunk:
                    is_invalid = False
                    break
            if is_invalid:
                if (chunk_size << 1) == length:
                    first_total += id
                second_total += id
                break

        # first_half = id_str[:mid]
        # second_half = id_str[mid:]
        # if first_half == second_half:
        #    first_total += id

end_time = datetime.now()
print(f"Part 1 Answer: {first_total}")
print(f"Part 2 Answer: {second_total}")
print(f"\nEnd time: {end_time}")
print(f"Time taken: {end_time - start_time}\n")
