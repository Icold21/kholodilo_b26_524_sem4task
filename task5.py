import json

if __name__ == "__main__":
    file_name: str = "data/students.json"
    target_file_name: str = "data/new_students.json"
    
    with open(file_name, "r", encoding="utf") as f:
        data: list = json.load(f)
    
    best_student: str = ""
    max_score: float = -float("inf")
    
    ind = 0
    for row in data:
        buffer: list = row.copy()
        buffer["passed"] = None
        data[ind] = buffer.copy()
        ind += 1
        
        if buffer["score"] >= max_score:
            best_student = buffer["name"]
            max_score = buffer["score"]
            
    print(data)
    with open(target_file_name, "w+", encoding="utf") as f:
        json.dump(data, f)