def calculate_discount(mrp, selling_price):
    """
    Calculate the discount percentage.

    Args:
        mrp (float): The Maximum Retail Price.
        selling_price (float): The Selling Price.

    Returns:
        float: The discount percentage.

    Example usage:
        discount = calculate_discount(3495, 1398)
        print(f"The discount percentage is: {discount}%")
    """
    # Calculate the difference between MRP and Selling Price
    discount_amount = mrp - selling_price
    
    # Calculate the discount percentage
    discount_percentage = (discount_amount / mrp) * 100
    
    return discount_percentage