def get_ordered_products_by_price(products):
    return sorted(products, key=lambda product: product.get_price(), reverse=True)
