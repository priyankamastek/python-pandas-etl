#from pathlib import Path

# file_path = Path(__file__).parent / "file1.txt"

with open("src/foundation/file1.txt", "r") as file:
    it = iter(file)
    print(next(it, "File is empty"), end="")
    print(next(it, "File is empty"), end="")
    print(next(it, "File is empty"), end="")
            
