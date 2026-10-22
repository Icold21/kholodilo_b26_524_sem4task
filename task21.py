import re

validation = (
    ("user_123",           True),
    ("admin",              True),
    ("123user",            False),
    ("ab",                 False),
    ("user-name",          False),
    ("very_long_username", False),
)

def is_valid_login(login):
    # * содержит от 4 до 16 символов;
    # * начинается с латинской буквы;
    # * содержит только латинские буквы, цифры и символ `_`.
    
    pattern = re.compile(
        r"[A-Za-z][0-9A-Za-z_]{3,15}"
    )
    return re.fullmatch(pattern, login) is not None
    
    
if __name__ == "__main__":
    test_logins = [v[0] for v in validation]
    result_batch = [is_valid_login(t_l) for t_l in test_logins]
    
    is_passed = [v[1] for v in validation] == result_batch
    
    print("Result:\n", list(zip(test_logins, result_batch)), "\n")
    if is_passed:
        print("Validation is passed")
    else:
        print("Validation isn't passed")