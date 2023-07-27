
clean_file_lines = []



with open(r"C:/Users/becht/Desktop/Python & Coding/hr_system.txt") as file:
    for line in file:
        file = line.strip()
        clean_line_split = file.split(" ")
        clean_file_lines.append(clean_line_split)

for i in clean_file_lines:
    name = i[0]
    id_number = i[1]
    title = i[2]
    annual_salary = float(i[3])

    bi_monthly_salary = annual_salary / 12 / 2

    # Add 1000 bonus to Engineers
    if title == "Engineer":
        bi_monthly_salary += 1000

    # Print everything!
    print(f"{name} (ID: {id_number}), {title} - ${bi_monthly_salary:.2f}")