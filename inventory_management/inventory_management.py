
def return_sorted_products(products, sort_key, ascending):
    return sorted(
        products, key=lambda x: x[sort_key],
        reverse=(not ascending)
    )
