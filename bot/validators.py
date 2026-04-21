def validate_order(args):
    if args.type == "LIMIT" and args.price is None:
        raise ValueError("Price is required for LIMIT orders")

    if args.quantity <= 0:
        raise ValueError("Quantity must be positive")
