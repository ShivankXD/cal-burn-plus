import json

# Load JSON
with open('D:/AIML Projects/cal-burn-plus/batch-write.json') as f:
    data = json.load(f)

# Fix invalid entries
fixed_items = []
for item in data['mergedb']:
    if isinstance(item['PutRequest'], str):
        continue  # Skip invalid entries
    fixed_items.append(item)

# Save fixed JSON
data['mergedb'] = fixed_items
with open('D:/AIML Projects/cal-burn-plus/batch-write-fixed.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Fixed JSON saved as batch-write-fixed.json")
