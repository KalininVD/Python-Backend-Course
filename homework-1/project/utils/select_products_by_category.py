from models.product import Product


def select_products_by_category(products: list[Product], category: str) -> list[Product]:
    """Selects products by category
    
    Args:
        products (list[Product]): list of products as a list of Product objects
        category (str): category name as a string
    
    Returns:
        list[Product]: list of products as a list of Product objects"""

    return [product for product in products if product.category == category]