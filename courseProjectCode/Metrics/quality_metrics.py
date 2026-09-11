import os
import sys
import re
from collections import defaultdict

def count_file_metrics(filepath):
    """Calculates comment lines, cyclomatic complexity, and unit test count for a file."""
    metrics = {
        'loc': 0,
        'comment_lines': 0,
        'complexity': 0,
        'unit_tests': 0
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')
            
            metrics['loc'] = len(lines)
            
            # Basic cyclomatic complexity approximation (control flow graph branches)
            complexity_keywords = [
                r'\bif\b', r'\belif\b', r'\belse\b', r'\bfor\b', r'\bwhile\b', 
                r'\band\b', r'\bor\b', r'\bcatch\b', r'\bexcept\b', 
                r'\bmatch\b', r'\bcase\b', r'\?'
            ]
            
            in_multiline_comment = False
            
            for line in lines:
                stripped = line.strip()
                
                # Comment Density logic
                if filepath.endswith('.py'):
                    if stripped.startswith('#'):
                        metrics['comment_lines'] += 1
                else: # .rs, .c, .cpp, etc.
                    if stripped.startswith('//'):
                        metrics['comment_lines'] += 1
                    elif stripped.startswith('/*'):
                        in_multiline_comment = True
                    
                    if in_multiline_comment:
                        metrics['comment_lines'] += 1
                        if '*/' in stripped:
                            in_multiline_comment = False

                # Complexity logic
                for keyword in complexity_keywords:
                    metrics['complexity'] += len(re.findall(keyword, line))
                    
                # Unit tests logic
                if re.search(r'\bdef test_', line) or re.search(r'#\[test\]', line) or re.search(r'\bTEST\(', line):
                    metrics['unit_tests'] += 1
                    
            # Base complexity is at least 1 if there's any code
            if metrics['loc'] > 0 and metrics['complexity'] == 0:
                metrics['complexity'] = 1
                
    except Exception:
        pass
        
    return metrics

def get_coverage(repo_path):
    """
    Attempts to read test coverage from a standard coverage.xml file.
    Note: Unit test coverage requires dynamic analysis (running the tests).
    """
    coverage_file = os.path.join(repo_path, 'coverage.xml')
    if os.path.exists(coverage_file):
        try:
            with open(coverage_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Simple regex to extract line-rate from standard Cobertura coverage.xml
                match = re.search(r'line-rate="([0-9.]+)"', content)
                if match:
                    return float(match.group(1)) * 100
        except Exception:
            pass
    return None

def analyze_repo(repo_path):
    """Traverses the repository and calculates quality metrics for each directory."""
    metrics_data = defaultdict(lambda: {'loc': 0, 'comment_lines': 0, 'complexity': 0, 'unit_tests': 0})
    
    ignore_dirs = {
        '.git', '.github', '__pycache__', 'venv', '.venv', '.tox', '.nox', 
        'target', 'build', 'dist', '.pytest_cache', '.mypy_cache', 'node_modules'
    }
    
    target_extensions = ('.py', '.rs', '.c', '.h', '.cpp')
    
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        for file in files:
            if file.endswith(target_extensions):
                filepath = os.path.join(root, file)
                file_metrics = count_file_metrics(filepath)
                
                rel_dir = os.path.relpath(root, repo_path)
                if rel_dir == '.':
                    rel_dir = '(root)'
                
                metrics_data[rel_dir]['loc'] += file_metrics['loc']
                metrics_data[rel_dir]['comment_lines'] += file_metrics['comment_lines']
                metrics_data[rel_dir]['complexity'] += file_metrics['complexity']
                metrics_data[rel_dir]['unit_tests'] += file_metrics['unit_tests']
                
    return metrics_data

def main():
    if len(sys.argv) > 1:
        repo_path = sys.argv[1]
    else:
        repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        
    print(f"Analyzing Quality Metrics for repository at: {repo_path}\n")
    
    metrics_data = analyze_repo(repo_path)
    sorted_metrics = sorted(metrics_data.items(), key=lambda x: x[0].lower())
    
    print(f"{'Directory':<40} {'LOC':>10} {'Comment %':>12} {'Complexity':>12} {'Unit Tests':>12}")
    print("-" * 90)
    
    total_loc = 0
    total_comments = 0
    total_complexity = 0
    total_unit_tests = 0
    
    for dirpath, data in sorted_metrics:
        loc = data['loc']
        comments = data['comment_lines']
        complexity = data['complexity']
        unit_tests = data['unit_tests']
        
        total_loc += loc
        total_comments += comments
        total_complexity += complexity
        total_unit_tests += unit_tests
        
        comment_density = (comments / loc * 100) if loc > 0 else 0
        
        print(f"{dirpath:<40} {loc:>10} {comment_density:>11.2f}% {complexity:>12} {unit_tests:>12}")
        
    print("-" * 90)
    
    total_comment_density = (total_comments / total_loc * 100) if total_loc > 0 else 0
    print(f"{'TOTAL':<40} {total_loc:>10} {total_comment_density:>11.2f}% {total_complexity:>12} {total_unit_tests:>12}")
    
    print("\n--- Unit Test Coverage ---")
    coverage = get_coverage(repo_path)
    if coverage is not None:
        print(f"Repository Unit Test Coverage: {coverage:.2f}%")
    else:
        print("Coverage data not found. To calculate unit test coverage, run your test suite with a coverage tool (e.g., `pytest --cov=src --cov-report=xml`) and ensure `coverage.xml` is in the repository root.")

if __name__ == '__main__':
    main()

