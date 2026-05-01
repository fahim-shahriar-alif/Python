# Write a python program to print the content of a directory using the os module.
import os

def list_directory_contents(path='.'):
    try:
        content_list = os.listdir(path)
        
        print(f"Contents of '{os.path.abspath(path)}':")
        print("-" * 30)
        
        for item in content_list:
            print(item)
            
    except FileNotFoundError:
        print("Error: The specified directory does not exist.")
    except PermissionError:
        print("Error: You do not have permission to access this directory.")

if __name__ == "__main__":
    list_directory_contents('.')