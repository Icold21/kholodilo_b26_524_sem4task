import re

not_formatted = "Это   строка    с     большим    количеством   пробелов.  "
validation = "Это строка с большим количеством пробелов."

def format_string(string: str) -> str:
    pattern = re.compile(r" {2,}")
    return re.sub(pattern, " ", string).strip()

if __name__ == "__main__":
    formatted_str = format_string(not_formatted)
    print("Result:", formatted_str, "\n")
    
    is_passed = formatted_str == validation
    if is_passed:
        print("Validation is passed")
    else:
        print("Validation isn't passed")