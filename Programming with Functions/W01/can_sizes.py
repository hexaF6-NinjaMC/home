import math

def compute_storage_efficiency(volume, surface_area):
    efficiency = volume / surface_area
    return efficiency

def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

def retrieve_data():
    whole_data_table = []

    with open("can_sizes.csv") as data_table:
        for line in data_table:
            line = line.strip()

            # Split all the clean data_lines and add the whole line to a list to be evaluated later.
            data_line = line.split(",")
            whole_data_table.append(data_line)

    return whole_data_table

def main():
    table = retrieve_data()
    efficiency_data = []

    for i in table:
        volume = compute_volume(float(i[1]), float(i[2]))
        area = compute_surface_area(float(i[1]), float(i[2]))
        efficiency = round(compute_storage_efficiency(volume, area), 1)
        efficiency_data.append([i[0], efficiency])
    
    for line in efficiency_data:
        print(f"{line[0]} {line[1]}")

main()