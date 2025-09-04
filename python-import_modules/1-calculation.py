#!/usr/bin/python3
if __name__ == "__main__":
    # add_module is an internal alias for human-friendly use
    import calculator_1 as calc

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calc.add(a, b)))
    print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    print("{} / {} = {}".format(a, b, calc.div(a, b)))
