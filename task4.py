from csv import reader, writer

if __name__ == "__main__":
    file_name: str = "data/prices.csv"
    target_file_name: str = "data/expensive.csv"
    data: list = list()
    price_index: int = -1
    is_header_read: bool = False

    with open(file_name, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = reader(csv_file)
        
        for row in reader:
            if not is_header_read:
                price_index = row.index("price")
                is_header_read = True
            else:
                if float(row[price_index]) > 100:
                    data.append(row)
            
    with open(target_file_name, mode="w+", newline="") as csv_file:
        try:
            writer = writer(csv_file)
            writer.writerows(data)
            print("Processed successfully")
        except Exception as e:
            print(f"Error: {e}")