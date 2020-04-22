#file_name = 'c:/users/sicou/Learning/pcc/python_work/pcc_review.txt'
file_name = 'text_files/pi_digits.txt'


with open(file_name) as file_object:
    lines = file_object.read()
print(lines)

with open(file_name) as file_object:
    for line in file_object.readline(-1):
        print(line.strip())