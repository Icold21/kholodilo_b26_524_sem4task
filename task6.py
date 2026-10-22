import pathlib

if __name__ == '__main__':
    path = ""
    cat: pathlib.Path = pathlib.Path(path)
    files_count: int = 0
    py_files_count: int = 0
    subcat_count: int = 0
    
    for item in cat.iterdir():
        if item.is_file():
            files_count += 1
            if '.py' == item.name[-3:]:
                py_files_count += 1
        elif item.is_dir():
            subcat_count += 1
            
    report: str = f"""
Files amount: {files_count};
Python files amount: {py_files_count};
Sub catalogs amount: {subcat_count}.
    """.strip()
    
    print(report)