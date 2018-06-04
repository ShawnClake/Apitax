from apitax import Apitax

import sys

def main():

    apitax = Apitax()
    args = sys.argv[1:]
    apitax.apitax(args)
    # apitax.apitax(["--grammar-test", "-s", "apitax/grammar/scripts/test.ah"])

if __name__ == '__main__':
    main()
