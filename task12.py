import re

def parse_emails(path: str) -> set:
    emails: set = {}
    raw_text: str = ""
    pattern: str = r"[^@]+@[^@.]+\.[^@.]+\n"
    
    with open(path, "r+", encoding="utf-8") as datafile:
        raw_text = datafile.read()
        
    emails = set(re.findall(pattern, raw_text))
    
    return emails

if __name__ == "__main__":
    path: str = "data/emails.txt"
    print(parse_emails(path))