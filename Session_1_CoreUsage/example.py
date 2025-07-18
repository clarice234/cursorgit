def get_discounted_price(price, discount_percent):
    if price <= 0 or discount_percent < 0:
        return 0
    return price - (price * discount_percent / 100)
