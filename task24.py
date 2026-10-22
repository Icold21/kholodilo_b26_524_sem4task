import re

products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321"
]

validation = [
    "PRD-12345",
    "PRD-00123",
    "PRD-54321"
]

def validate_id(id_str: str) -> bool:
    # PRD-XXXXX
    pattern = re.compile(r"PRD-\d{5}")
    
    return re.fullmatch(pattern, id_str) is not None

if __name__ == "__main__":
    mask = [validate_id(string) for string in products]
    validated = [v for v, m in zip(products, mask) if m == True]
    print("Result:", validated, "\n")
    
    is_passed = validated == validation
    if is_passed:
        print("Validation is passed")
    else:
        print("Validation isn't passed")