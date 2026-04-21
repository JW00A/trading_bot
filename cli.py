from bot.client import MockBinanceClient
from bot.validators import validate_order
from bot.logging_config import setup_logging
from argparse import ArgumentParser
import logging

def main():
    setup_logging()

    parser = ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)
    args = parser.parse_args()

    try:
        validate_order(args)
        client = MockBinanceClient()
        response = client.place_order(
            args.symbol, args.side, args.type, args.quantity, args.price
        )
        logging.info(f"Order placed: {response}")
        print("Order successful:", response)

    except Exception as e:
        logging.error(f"Error: {e}")
        print("Error:", e)

if __name__ == "__main__":
    main()
