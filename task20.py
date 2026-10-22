import re

string = (
    "Встречи состоятся 15.09.2026, 21.09.2026 и 03.10.2026."
    "Следующая встреча запланирована на 1.11.2026."
)

def parse_dates(texts: list) -> list:
    # `DD.MM.YYYY`
    pattern = re.compile(
        r"(?<!\d)\d{2}\.\d{2}\.\d{4}(?!\d)"
    )
    
    return [re.findall(pattern, text) for text in texts]

if __name__ == "__main__":
    packed = [string, ]
    print(parse_dates(packed)[0])