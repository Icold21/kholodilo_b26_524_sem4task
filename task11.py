import re

def parse_logs(path: str) -> dict:
    parsed_logs: dict = {
        "ids": list(),
        "errors": list(),
        "ids_with_errors": list()
    }
    raw_text: str = ""
    
    with open(path, "r+", encoding="utf-8") as datafile:
        raw_text: str = datafile.read()
    
    parsed_logs["ids"] = list(
        set(map(int, [x[5:] for x in re.findall(r"User \d+", raw_text)]))
    )
    parsed_logs["errors"] = re.findall(r"ERROR.+\n", raw_text)
    parsed_logs["ids_with_errors"] = list(
        set(map(int, [x[11:] for x in re.findall(r"ERROR User \d+", raw_text)]))
    )
    
    return parsed_logs

if __name__ == "__main__":
    path: str = "data/user_logs.txt"
    print(parse_logs(path))