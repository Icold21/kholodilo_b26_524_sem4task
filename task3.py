if __name__ == "__main__":
    file_name: str = "data/students.csv"
    data: list = list()
    header: dict = dict()
    header_recorded: bool = False
    length = 0
    
    with open(file_name, "r", encoding="utf") as f:
        for line in f:
            if not header_recorded:
                keys: list = line.strip().split(",")
                header = dict(zip(keys, [None for i in range(len(keys))]))
                header_recorded = True
                
                header_keys: list = list(header.keys())
            else:
                length += 1
                values = line.strip().split(",")
                row = header.copy()
                for key, val in zip(header_keys, values):
                    if key == "score":
                        row[key] = float(val)
                    else:
                        row[key] = val
                data.append(row.copy())
                    
    groups: set = set([data[i]["group"] for i in range(len(data))])
    stats_by_groups: dict = dict(zip(groups, [[0, 0] for i in range(len(groups))]))
    
    max_score: float = -float("inf")
    accumulated_sum: float = 0
    best_student = None
    
    for row in data:
        stat = stats_by_groups[row["group"]]
        stat[0] += row["score"]
        accumulated_sum += row["score"]
        stat[1] += 1
        
        if row["score"] >= max_score:
            best_student = row["name"]
            max_score = row["score"]
       
    mean_score = accumulated_sum / length
    mean_by_groups: dict = dict(zip(groups, [0 for i in range(len(groups))]))
    for group in stats_by_groups:
        mean_by_groups[group] = stats_by_groups[group][0] / stats_by_groups[group][1]

    report = f"""
Mean score: {mean_score}
Best student: {best_student}
Mean by groups: {mean_by_groups}
    """.strip()  
    print(report)