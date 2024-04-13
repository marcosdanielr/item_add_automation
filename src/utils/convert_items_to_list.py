import re

def convert_items_to_list(text):
    items = []

    for line in text.splitlines():
        match = re.match(r'.*\[(\d+)\]\s+x(\d+)', line)
        if match:
            id = int(match.group(1))
            name_match = re.match(r'(.+)\[\d+\]\s+x\d+', line)
            if name_match:
                name = name_match.group(1).strip()
            else:
                name = "Name not found"
            quantity = int(match.group(2))
            items.append({'id': id, 'name': name, 'quantity': quantity})

    return items
