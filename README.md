# Flatfox API: Swiss rental apartments and houses in Python and Node

Get **Swiss apartments and houses for rent or sale from Flatfox** as clean JSON with real prices, rooms, living area and coordinates. The [Swiss Rentals Scraper](https://apify.com/swissalpinedata/swiss-rentals-scraper) on Apify uses the public Flatfox API with filters for city, ZIP, canton, price and rooms.

Pay per result, no subscription, no login and no proxy setup. New Apify accounts get free monthly credit, which covers a few thousand results.

## Quick start

1. Create a free account on [Apify](https://apify.com) and copy your API token from Settings, Integrations.
2. `export APIFY_TOKEN=your_token`
3. Run one of the examples below.

### Python

```bash
pip install apify-client
python example.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("swissalpinedata/swiss-rentals-scraper").call(run_input={
    "offerType": "RENT",
    "city": "Zürich",
    "objectCategory": "ANY",
    "maxItems": 20
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item)
```

### Node.js

```bash
npm install apify-client
node example.mjs
```

```js
import { ApifyClient } from "apify-client";

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor("swissalpinedata/swiss-rentals-scraper").call({
  "offerType": "RENT",
  "city": "Zürich",
  "objectCategory": "ANY",
  "maxItems": 20
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### curl

```bash
curl -X POST "https://api.apify.com/v2/acts/swissalpinedata~swiss-rentals-scraper/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"offerType": "RENT", "city": "Zürich", "objectCategory": "ANY", "maxItems": 20}'
```

## Example output

One record looks like this:

```json
{
  "source": "flatfox",
  "listing_id": "86384926",
  "url": "https://flatfox.ch/en/flat/hauptstrasse-4-3706-leissigen/86384926/",
  "title": "Hauptstrasse 4, 3706 Leissigen - CHF 1’850",
  "offer_type": "RENT",
  "object_category": "APARTMENT",
  "object_type": "APARTMENT",
  "price_chf": 1850.0,
  "price_period": "month",
  "rent_net_chf": 1650.0,
  "rent_charges_chf": 200.0,
  "rooms": 4.0,
  "surface_m2": 85.0,
  "floor": 1,
  "year_built": 1988,
  "is_furnished": false,
  "is_temporary": false,
  "address": "Hauptstrasse 4, 3706 Leissigen",
  "street": "Hauptstrasse 4",
  "zip": "3706",
  "city": "Leissigen",
  "canton": "BE",
  "latitude": 46.6573878,
  "longitude": 7.7840874,
  "available_from": "2026-12-01",
  "published_at": "2026-09-22T13:48:30.538356+02:00",
  "images": [
    "https://cdn.flatfox.ch/t_listing_card_716x390/listings/v2/isx50985/4003492750/image/5473c310c0220c02506b8158b7b5ace6.png"
  ],
  "description": "Per 1. Dezember 2026 oder nach Vereinbarung vermieten wir eine charmante 4-Zimmer-Wohnung in der idyllischen Gemeinde Leissigen am Thunersee. \n\nDas erwartet Sie ...",
  "agency": "Ruchti Partner AG",
  "scraped_at": "2026-09-22T20:52:32.248740+00:00"
}
```

## What you can build

* Rent monitoring by city or ZIP
* Swiss housing market analysis
* New listing alerts
* Property research and price maps

## Schedules and integrations

On Apify you can save this input as a task, run it on a schedule (for example every morning) and send new results to Google Sheets, Slack, a webhook, Make, n8n or Zapier without writing code. All input fields are documented on the [actor page](https://apify.com/swissalpinedata/swiss-rentals-scraper).

## More Swiss and DACH data APIs

* [swiss-jobs-api](https://github.com/swissalpinedata/swiss-jobs-api): Swiss Jobs API
* [arbeitsagentur-jobs-api](https://github.com/swissalpinedata/arbeitsagentur-jobs-api): Arbeitsagentur Jobsuche API
* [zefix-api-python](https://github.com/swissalpinedata/zefix-api-python): Zefix API in Python
* [austria-jobs-api](https://github.com/swissalpinedata/austria-jobs-api): Austria Jobs API
* [personio-jobs-api](https://github.com/swissalpinedata/personio-jobs-api): Personio, Workable, Recruitee, SmartRecruiters and Teamtailor jobs API in Python and Node

## No code: n8n and Make

Ready to import n8n workflows and Make guides for these actors: [n8n-swiss-data-templates](https://github.com/swissalpinedata/n8n-swiss-data-templates).

## License

The example code in this repo is MIT licensed. The data comes from public sources; you are responsible for using it in line with the GDPR and the terms of the source sites.
