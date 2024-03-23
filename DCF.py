#DCF Model

import argparse
from prettytable import PrettyTable

parser = argparse.ArgumentParser()
parser.add_argument('-rev', '--revenue', help='Set Base Revenue', type=int)
parser.add_argument('-stock', '--stock_amount', help='Set Stock amounts', type=int)
parser.add_argument('-r', '--discount_rate', help = "Set Discount Rate, Default = 1.05 (5%%)", default = 5, type = float)
parser.add_argument('-y', '--years', help = 'Set Years, Default=5', default = 5, type = int)

group_single_rate = parser.add_argument_group('Single Rate DCF')
group_single_rate.add_argument('-growth', '--growth_rate', help = 'Set Inc Growth Rate', type = float, default = 5 )

group_Inc_scale = parser.add_argument_group('Inc Scale DCF')
group_Inc_scale.add_argument('-scale', '--scale', help = 'Set Final Inc Scale Multiple,幾倍市場規模?', type = float)

args = parser.parse_args()


discount_rate = 1 + args.discount_rate / 100
years = args.years
rev = args.revenue
stock = args.stock_amount
growth = args.growth_rate/100
scale = args.scale


table = PrettyTable()

table.field_names = ["Year", "Cash Flow"]


def single_rate_DCF(args):
    final_cash = 0
    for i in range(1, years + 1):
        final_cash += (rev * ((1 + growth) ** i) / (discount_rate ** i))    
        table.add_row(["Year{}".format(i), "${:.2f}".format(rev * ((1 + growth) ** i) / (discount_rate ** i))])
    Predict_price = final_cash / stock
    table.add_row(["Total Cash Flow", "${:.2f}".format(final_cash)])
    table.add_row(["Stock Amount", "{} 股".format(stock)])
    table.add_row(["DCF Valuation", "${:.2f}".format(Predict_price)])
    print(table)
    return Predict_price

def Inc_scale_DCF(args):
    final_cash = 0
    if scale:
        bias = (scale - 1.0) / years
        pow_list = [1 + i * bias for i in range(1, years + 1)]
        yearlist = []
        for i in range(1,years+1):
            yearlist.append(i)
        for i,y in zip(pow_list,yearlist):
            final_cash += (rev * i / ( discount_rate ** y))
            table.add_row(["Year{}".format(y), "${:.2f}".format((rev * i / ( discount_rate ** y)))])
    
    Predict_price = final_cash / stock
    table.add_row(["Total Cash Flow", "${:.2f}".format(final_cash)])
    table.add_row(["Stock Amount", "{} 股".format(stock)])
    table.add_row(["DCF Valuation", "${:.2f}".format(Predict_price)])
    print(table)
    return Predict_price


if __name__ == "__main__":

    if scale:
        Inc_scale_DCF(args)
    else:
        single_rate_DCF(args)





