from io import StringIO

def count_lines(file_obj):
    count = 0
    with file_obj as stream:
        for row in stream:
            count += 1
            
    return count

if __name__ == "__main__":
    file_object_1 = open("data/operation.log", "r")
    file_object_2 = StringIO("first\nsecond\nthird")
    
    print("First obj (operation.log) lines count =", count_lines(file_object_1))
    print("Second obj (StringIO) lines count =", count_lines(file_object_2))