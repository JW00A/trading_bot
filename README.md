# trading_bot

# Running the Trading Mock Bot

To execute the bot from the command line, run one of the following commands:

## Market Order Example
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

## Limit Order Example
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 30000

# Important
Make sure your terminal is opened in the same directory where cli.py is located.
If not, navigate to the correct folder using:
cd path/to/your/project

You can copy the folder path by right‑clicking the directory in your file explorer and selecting Copy as path
If running through cmd and not bash, first change the directory if it's different from C: by typing the name of the driver, e.g. E:
