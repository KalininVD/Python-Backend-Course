from models.product import Product


def get_ordered_products_by_price(products: list[Product]) -> list[Product]:
    """Sorts products by price
    
    Args:
        products (list[Product]): list of products as a list of Product objects
    
    Returns:
        list[Product]: list of products as a list of Product objects"""

    return sorted(products, key=lambda product: product.get_price(), reverse=True)