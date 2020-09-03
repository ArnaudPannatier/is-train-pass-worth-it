import argparse
from datetime import date

import numpy as np
from dateutil.relativedelta import relativedelta
from dateutil.rrule import SU, WEEKLY, rrule

parser = argparse.ArgumentParser(
    description="Compute if train pass is worth it"
)
parser.add_argument(
    "--price_travel",
    type=float,
    default=8.2,
    nargs="?",
    help="price of a single travel")

parser.add_argument(
    "--price_pass",
    type=float,
    default=252,
    nargs="?",
    help="price of the monthly pass")

parser.add_argument(
    "--days_of_work",
    type=int,
    default=[3, 4],
    nargs="*",
    help="Day of work during the week : Monday:0, Tu:1, ... Sat:5, Sun:6"
    )


def main():
    args = parser.parse_args()

    number_of_travel_max = int(np.floor(args.price_pass/args.price_travel))
    print("If you travel more than {} times, you should take the pass".format(number_of_travel_max))
    print("")
    today = date.today()
    today_in_one_month = today + relativedelta(months=+1)
    days_of_travel = list(rrule(
        WEEKLY,
        dtstart=today,
        until=today_in_one_month,
        byweekday=args.days_of_work)
    )
    print(
        "Next months you are supposed to take the train {} times :".format(
            2*len(days_of_travel)
        ).ljust(100)
    )
    print("_"*100)
    for d in days_of_travel:
        print(d.strftime("%a %d.%m.%Y") + " x2")

    total_price_travel = 2*len(days_of_travel)*args.price_travel
    print("")
    if total_price_travel > args.price_pass:
        print(
            "You should take the pass for {:.2f} CHF as the total for single travels is {:.2f} CHF".format(
                args.price_pass,
                total_price_travel
            ))
    else:
        print(
            "You should NOT take the pass for {:.2f} CHF as the total for single travels is {:.2f} CHF".format(
                args.price_pass,
                total_price_travel
            ))

if __name__ == "__main__":
    print("")
    main()
    print("")
