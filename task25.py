from pprint import pprint
import re

PATTERN = re.compile(
    r"(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(?P<level>INFO|ERROR|WARNING) "
    r"User (?P<user_id>\d+) "
    r"(?P<message>.+)"
)

logs = [
    "2026-09-24 10:15:32 INFO User 123 logged in",
    "2026-09-24 10:16:04 ERROR User 456 authentication failed",
    "2026-09-24 10:17:21 INFO User 123 opened page",
    "2026-09-24 10:18:45 WARNING User 789 too many requests",
    "2026-09-24 10:19:02 ERROR User 123 database connection failed",
]

validation = "2026-09-24 10:16:04 ERROR User 456 authentication failed"
target = {
    "datetime": "2026-09-24 10:16:04",
    "level": "ERROR",
    "user_id": "456",
    "message": "authentication failed"
}

def parse_log(log: str) -> dict:
    m = PATTERN.fullmatch(log)
    return m.groupdict() if m else {}

if __name__ == "__main__":
    parsed_logs = [parse_log(l) for l in logs]
    print("Result:")
    pprint(parsed_logs)
    
    example = parse_log(validation)
    print("Example:", example, "\n")
    
    is_passed = target == example
    
    if is_passed:
        print("Validation is passed")
    else:
        print("Validation isn't passed")