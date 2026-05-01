#Level the program written in previous problem with comments .


import os

def list_directory_contents(path='.'):
    try:
        # Get the list of all files and directories
        # '.' refers to the current directory by default
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
    # You can change '.' to any specific path on your MacBook
    list_directory_contents('.')