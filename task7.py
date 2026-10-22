import pathlib

def recursive_parsing(path: str, target_ext:str, found:set):
    cat: pathlib.Path = pathlib.Path(path)
        
    for item in cat.iterdir():
        if item.is_file():
            if item.name[-3:] == '.py':
                found.add(item.name)
        elif item.is_dir():
            recursive_parsing(item.name, ".py", found)
    return found

if __name__ == '__main__':
    path: str = ""
    py_files_found: set = recursive_parsing(path, ".py", {})
            
    report: str = f"""
Py files: {py_files_found};
    """.strip()
    
    print(report)