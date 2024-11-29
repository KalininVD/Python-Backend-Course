def extract_prices(products):
    return [product.get_price() for product in products]
