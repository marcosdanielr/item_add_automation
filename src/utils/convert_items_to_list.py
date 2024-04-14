import re

def convert_items_to_list(text):
    items = []
    all_items = re.findall(r'(.+)\[(\d+)\]\s+x(\d+)', text)

    for name, id, quantity in all_items:
        items.append({'id': int(id), 'name': name.strip(), 'quantity': int(quantity)})

    return items
