import sys
import re

def fix_indentation(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    fixed_lines = []
    indent_level = 0
    indent_str = "  " # 2 spaces

    # Tags that don't increase indent
    void_tags = ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr']
    
    for line in lines:
        # Clean up the line
        stripped = line.strip().replace('\xa0', ' ')
        if not stripped:
            continue
        
        # Check for closing tag
        is_closing = stripped.startswith('</')
        
        if is_closing:
            indent_level = max(0, indent_level - 1)
            
        # Add indentation
        fixed_lines.append((indent_str * indent_level) + stripped + '\n')
        
        # Check for opening tag (simplified logic)
        # This is a very basic parser, might not be perfect but better than broken indentation
        # It assumes one tag per line mostly, or at least structure based
        
        # Count opening and closing tags in the line to adjust next indent
        # This is tricky with multiple tags on one line.
        # Let's try a simpler approach: use BeautifulSoup if available, else this custom logic.
        pass

# Let's rely on BeautifulSoup if possible, it's much more robust.
try:
    from bs4 import BeautifulSoup
    
    file_path = r"c:\git\my_portfolio\index.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace non-breaking spaces
    content = content.replace('\xa0', ' ')
    
    soup = BeautifulSoup(content, 'html.parser')
    pretty_html = soup.prettify()
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(pretty_html)
        
    print("Successfully reformatted using BeautifulSoup")

except ImportError:
    print("BeautifulSoup not found. Please install it or use a different method.")
    # Fallback or exit?
    # I'll just exit and let the agent know.
    sys.exit(1)
