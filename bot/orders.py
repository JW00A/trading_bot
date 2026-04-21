import logging

def place_order(client, symbol, side, order_type, quantity, price=None):

    logging.info(
        f"Placing order: symbol={symbol}, side={side}, type={order_type}, "
        f"quantity={quantity}, price={price}"
    )

    try:
        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        logging.info(f"Order response: {response}")
        return response

    except Exception as e:
        logging.error(f"Order failed: {e}")
        raise
