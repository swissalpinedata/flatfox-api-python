import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("swissalpinedata/swiss-rentals-scraper").call(run_input={
    "offerType": "RENT",
    "city": "Zürich",
    "objectCategory": "ANY",
    "maxItems": 20
})

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(json.dumps(items, ensure_ascii=False, indent=2))
print(f"{len(items)} records", flush=True)
