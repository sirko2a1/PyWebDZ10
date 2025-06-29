import os
import django
import json

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

# Now import your models
from quotes.models import Quote, Tag

# Load and insert data
with open("quotes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    q = Quote.objects.create(text=item['quote'], author=item['author'])
    for tag_name in item['tags']:
        tag, _ = Tag.objects.get_or_create(name=tag_name)
        q.tags.add(tag)

print("Quotes successfully loaded.")
