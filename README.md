# DCF-Stock-Price-Valuation
Simple DCF Tools helps Valuate Stock Price!

DCF is a method which use future cash flow to valuate stock price.
DCF isn't suitable for all kinds of company, while you can use it as a reference.

python DCF.py -h
usage: DCF.py [-h] [-rev REVENUE] [-stock STOCK_AMOUNT] [-r DISCOUNT_RATE] [-y YEARS] [-growth GROWTH_RATE] [-scale SCALE]

Must need options:
  -h, --help            show this help message and exit
  -rev REVENUE, --revenue REVENUE
                        Set Base Revenue
  -stock STOCK_AMOUNT, --stock_amount STOCK_AMOUNT
                        Set Stock amounts
  -r DISCOUNT_RATE, --discount_rate DISCOUNT_RATE
                        Set Discount Rate, Default = 1.05 (5%)
  -y YEARS, --years YEARS
                        Set Years, Default=5

Single Rate DCF:
  -growth GROWTH_RATE, --growth_rate GROWTH_RATE
                        Set Inc Growth Rate

Inc Scale DCF:
  -scale SCALE, --scale SCALE
                        Set Final Inc Scale Multiple (you predict that the market size will be x times bigger! )
                        EX: 2 = market value BECOMES 2 times bigger.

------------------------------------------------------------------------------------------------------------------------------------------

Usage Example:

        $python .\DCF.py -scale 2 -y 10 -rev 248888888888 -stock 437000000

          +-----------------+-------------------+
          |       Year      |     Cash Flow     |
          +-----------------+-------------------+
          |      Year1      |  $260740740739.81 |
          |      Year2      |  $273156966489.32 |
          |      Year3      |  $286164441084.05 |
          |      Year4      |  $299791319230.91 |
          |      Year5      |  $314067096337.15 |
          | Total Cash Flow | $1433920563881.25 |
          |   Stock Amount  |    437000000 股   |
          | Predicted Price |      $3281.28     |
          +-----------------+-------------------+


        $python .\DCF.py -scale 2 -y 5 -rev 248888888888 -stock 437000000
        
          +-----------------+-------------------+
          |       Year      |     Cash Flow     |
          +-----------------+-------------------+
          |      Year1      |  $284444444443.43 |
          |      Year2      |  $316049382714.92 |
          |      Year3      |  $343999328125.08 |
          |      Year4      |  $368570708705.45 |
          |      Year5      |  $390021913974.02 |
          | Total Cash Flow | $1703085777962.90 |
          |   Stock Amount  |    437000000 股   |
          |     DCF估值     |      $3897.22     |
          +-----------------+-------------------+







        
