import re

string = (
    "Полезные сайты: https://python.org, http://example.com/page, "
    "https://example.com/docs/index.html и ftp://files.example.com/data."
)

validation = (
    "https://python.org "
    "http://example.com/page "
    "https://example.com/docs/index.html"
).split()

def parse_url(texts: list) -> list:
    pattern = re.compile(
        r"(?<!\S)https?://[\w.-]+(?:/[\w./-]*)?"
    )
    return [re.findall(pattern, text) for text in texts]

if __name__ == "__main__":
    packed = [string, ]
    urls = parse_url(packed)[0]
    
    print(f"Result:\n{urls}\n")
    is_passed = urls == validation
    
    if is_passed:
        print("Validation is passed")
    else:
        print("Validation isn't passed")