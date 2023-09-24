
while True:
    sales = float(input("Enter sales: $"))

    if sales < 0:
        print("invalid.")
        break

    # Calculate bonus
    if sales < 1000:
        bonus = sales * 0.10
        print(f" bonus : ${bonus:.4f}")
    else:
        bonus = sales * 0.15

        print(f" bonus: ${bonus:.4f}")