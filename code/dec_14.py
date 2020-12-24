from typing import List 

# Load file
in_file = open("data/day_14_input.txt", "r")
content = in_file.read()
file = content.split("\n")
in_file.close()


def complete_memory_1(file: List) -> dict:
    """Get the complete memory of the program."""
    mem = {}
    for line in file:
        if "mask" in line:
            mask = line.split(" = ")[1]
            continue
        else:
            mem_helper, value = line.split(" = ")
            mem_helper = mem_helper.replace("[",",").replace("]","")
        value = f'{int(value):036b}'

        # Verify if mask modifies value
        for i in range(len(value)):
            if mask[i] == 'X' or mask[i] == value[i]:
                continue
            else:
                value = value[:i] + mask[i] + value[i+1:]
        mem[mem_helper.split(",")[1]] = int(str(value),2)
    return mem

def complete_memory_2(file: List) -> dict:
    """Get the complete memory of the program."""
    mem = {}
    for line in file:
        if "mask" in line:
            mask = line.split(" = ")[1]
            continue
        else:
            mem_helper, value = line.split(" = ")
            mem_helper = mem_helper.replace("[",",")
            mem_helper = mem_helper.replace("]","")
            value = int(value)
        address = f'{int(mem_helper.split(",")[1]):036b}'

        address_helper = []
        for a, m in zip(address,mask):
            if m == 'X' or m == a:
                address_helper.append(m)
            else: 
                address_helper.append("1")

        first_x = address_helper.index('X') -1
        replaces = ["1","0"]
        clean_address = address_helper.copy()
        for num in range(0, 2**address_helper.count('X')):
            bin_num = bin(num)[2:].zfill(address_helper.count('X'))

            for char in bin_num:
                address_helper[address_helper.index('X')] = char

            mem[(''.join(address_helper))] = value
            address_helper = clean_address.copy()
    return mem