if __name__ == "__main__":
    file_name: str = "Задания на семинар 4.md"
    
    rows_amount: int = 0
    words_amount: int = 0
    chars_amount: int = 0
    longest_string_len: int = -1
    
    with open(file_name, "r", encoding="utf") as f:
        for line in f:
            string: str = str(line)
            string_length: int = len(list(string))
            
            rows_amount += 1
            words_amount += len(string.split())
            chars_amount += string_length
            longest_string_len = max(longest_string_len, string_length)
    
    report: str = f"""
Rows amount: {rows_amount}
Words amount: {words_amount}
Chars amount: {chars_amount}
Longest string length: {longest_string_len}
    """.strip()
    print(report)
            