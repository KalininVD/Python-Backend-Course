class Product:
    """Class for modeling product entity
    
    Includes product name, category, price and sale fields."""

    def __init__(self, name: str, category: str, price: float) -> None:
        """Constructor for Product class

        Initializes product name, category and price fields with given values.
        By default product sale is 0%.

        Args:
            name (str): product name as a string
            category (str): product category as a string
            price (float): product price as a real number"""
        
        self.name = name
        self.category = category
        self.price = price
        
        self.sale = 0

    def edit_category(self, new_category: str) -> None:
        """Updates product category field
        
        Args:
            new_category (str): new category name as a string"""
        
        self.category = new_category

    def edit_price(self, new_price: float) -> None:
        """Updates product price field (without applying discount)
        
        Args:
            new_price (float): new price as a real number"""
        
        self.price = new_price

    def set_sale(self, sale: int) -> None:
        """Updates product sale field. Note: sale is a percentage
        
        Args:
            sale (int): sale percentage as an integer"""

        if sale < 0 or sale > 100:
            raise ValueError("Sale must be between 0 and 100%")
        
        self.sale = sale

    def cancel_sale(self) -> None:
        """Sets product sale field value to 0"""

        self.sale = 0

    def get_price(self) -> float:
        """Price getter. Returns product price with discount applied
        
        Returns:
            float: product price with discount applied as a real number"""

        return self.price * (1 - self.sale / 100)

    def __repr__(self) -> str:
        """Service method for getting string representation of product with all internal data"""

        return f"Product(name=\"{self.name}\", category=\"{self.category}\", price={self.price}, sale={self.sale}%)"