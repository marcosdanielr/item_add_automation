import re

def validate_text_format(text):
    for line in text.splitlines():
        match = re.match(r'.*\[(\d+)\]\s+x(\d+)', line)
        if not match:
            return False
    return True
