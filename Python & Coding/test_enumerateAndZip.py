shopping_cart = ["apples", "bananas", "carrots"]
running_total = [1.25, 2, 64.009]

if shopping_cart:
    for i, s in enumerate(zip(shopping_cart, running_total), 1):
        print(f"\n{i}. {s[0]} - ${s[1]:.2f}")
else:
    exit