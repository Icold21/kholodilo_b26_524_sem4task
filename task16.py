import re

if __name__ == "__main__":
    logs_raw = None
    levels = ["INFO", "WARNING", "ERROR"]
    log_stats = {}

    try:
        with open("data/test_logs.txt", "r", encoding="utf-8") as log_file:
            logs_raw = log_file.read()
    except Exception as exc:
        print(exc)

    if logs_raw is not None:
        lines = logs_raw.splitlines()

        for level in levels:
            pattern = re.compile(rf"\b{level}\b")
            matching = [ln for ln in lines if pattern.search(ln)]
            log_stats[level] = len(matching)

            if level == "ERROR":
                users = []
                for ln in matching:
                    m = re.search(r"User (\d+)", ln)
                    if m:
                        users.append(int(m.group(1)))
                log_stats["Users_with_error"] = users

        print(log_stats)