seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

overstock_risk = (current_stock > high_stock_threshold) or seasonal
discount_eligible = not (selling_well) and not (on_sale)
make_discount = (overstock_risk) or (discount_eligible)
print("should the item be discounted?", make_discount)