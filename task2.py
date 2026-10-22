if __name__ == "__main__":
    file_name: str = "data/numbers.txt"
    result_file_name: str = "data/result.txt"
    
    min_num: float = float("inf")
    max_num: float = -float("inf")
    accumulated_sum: float = 0
    length: int = 0
    
    with open(file_name, "r", encoding="utf") as f:
        for line in f:
            try:
                num: float = float(line.strip())
            except:
                continue
            
            min_num = min(min_num, num)
            max_num = max(max_num, num)
            accumulated_sum += num
            length += 1
    mean = accumulated_sum / length
    
    report: str = f"""
min, max, mean 
{min_num}, {max_num}, {mean}
    """.strip()
    print(report)
    
    with open(result_file_name, "w+", encoding="utf") as f:
        f.write(report)