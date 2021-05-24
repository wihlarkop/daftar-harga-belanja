def clean_price(price: str) -> int:
    return int(price.replace("Rp", "").replace(".", ""))
