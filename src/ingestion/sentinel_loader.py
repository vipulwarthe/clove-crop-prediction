import pystac_client
import planetary_computer

def fetch_sentinel_data(bbox, date_range):
    catalog = pystac_client.Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1"
    )

    search = catalog.search(
        collections=["sentinel-2-l2a"],
        bbox=bbox,
        datetime=date_range,
        query={"eo:cloud_cover": {"lt": 10}}
    )

    items = list(search.get_items())
    signed_items = [planetary_computer.sign(item) for item in items]

    return signed_items