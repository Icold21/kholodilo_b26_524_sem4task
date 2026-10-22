if __name__ == "__main__":
    big_file_path = "data/big_file.txt"
    
    stats = dict()
    stats["summ"] = 0
    stats["minimum"] = float("inf")
    stats["maximum"] = -float("inf")
    stats["count"] = 0
    stats["mean"] = None
    
    with open(big_file_path, "r", encoding="utf-8") as datafile:
        for line in datafile:
            try:
                num = int(line.strip())
            except Exception as exc:
                print(exc)
                break
                
            stats["count"] += 1
            stats["summ"] += num
            stats["minimum"] = min(stats["minimum"], num)
            stats["maximum"] = max(stats["maximum"], num)
            
    if stats["count"] > 0:
        stats["mean"] = stats["summ"] / stats["count"]
        print(stats)
    else:
        print("No numbers in file")