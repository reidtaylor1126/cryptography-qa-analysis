import os
import sys
from collections import defaultdict

def count_lines(filepath):
    """Counts the number of lines in a file."""
    try:
        # Using errors='ignore' to skip non-utf-8 files gracefully
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

def get_loc_per_dir(repo_path):
    """Traverses the repository and calculates LOC for each directory."""
    loc_data = defaultdict(int)
    
    # Directories to ignore
    ignore_dirs = {
        '.git', '.github', '__pycache__', 'venv', '.venv', '.tox', '.nox', 
        'target', 'build', 'dist', '.pytest_cache', '.mypy_cache', 'node_modules'
    }
    
    # Consider specific extensions that are part of the source code.
    target_extensions = (
        '.py', '.rs', '.c', '.h', '.cpp', '.rst', 
        '.toml', '.json', '.yaml', '.yml'
    )
    
    for root, dirs, files in os.walk(repo_path):
        # Mutate dirs in-place to ignore certain directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        for file in files:
            if file.endswith(target_extensions):
                filepath = os.path.join(root, file)
                loc = count_lines(filepath)
                
                # Get the relative path of the directory
                rel_dir = os.path.relpath(root, repo_path)
                if rel_dir == '.':
                    rel_dir = '(root)'
                
                loc_data[rel_dir] += loc
                
    return loc_data

def main():
    # If a path is provided as an argument, use it. Otherwise, default to the repository root.
    if len(sys.argv) > 1:
        repo_path = sys.argv[1]
    else:
        repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        
    print(f"Analyzing LOC for repository at: {repo_path}\n")
    
    loc_data = get_loc_per_dir(repo_path)
    
    # Sort directories alphabetically to group neighbors together
    sorted_loc_data = sorted(loc_data.items(), key=lambda x: x[0].lower())
    
    print(f"{'Directory':<100} {'LOC':>10}")
    
    total_loc = 0
    for dirpath, loc in sorted_loc_data:
        print(f"{dirpath:<100} {loc:>10}")
        total_loc += loc
        
    print("\nTotal LOC:")
    print(f"{total_loc}")

if __name__ == '__main__':
    main()
