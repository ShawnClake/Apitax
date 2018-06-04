from .apitax import Apitax

def main():

    apitax = Apitax()

    apitax.apitax(["--grammar-test", "-s", "../apitax/grammar/scripts/test.ah"])

if __name__ == '__main__':
    main()
