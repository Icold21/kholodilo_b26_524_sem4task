import re

def parse_number(value):
    if not value:
        raise ValueError("Passed null string")
    if re.findall(r"(-?)\d+(\.d+)?"):
        return float(value)
    else:
        raise ValueError("Incorrect number format")

if __name__ == '__main__':
    try:
        print(parse_number(input("String into num: ")))
    except ValueError:
        print("Error passed")