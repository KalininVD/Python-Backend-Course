from models.product import Product


def extract_prices(products: list[Product]) -> list[float]:
    """Extracts prices from list of products
    
    Args:
        products (list[Product]): list of products as a list of Product objects
    
    Returns:
        list[float]: list of prices as a list of real numbers"""

    return [product.get_price() for product in products]