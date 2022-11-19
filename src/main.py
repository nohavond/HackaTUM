#!/usr/bin/env python3
"""
API backend for the Hauspals app for homeowners.
This API provides all the necessary data for the frontend,
as well as supports basic OAUTH authentication.
"""

__author__ = "Martin Mackovik, Ondrej Nohava, Alphar Abdugeni, Malaz Tamim"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse


def main(args):
    """ Main entry point of the app """
    print("hello world")
    print(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # # Optional argument which requires a parameter (eg. -d test)
    # parser.add_argument("-n", "--name", action="store", dest="name")
    #
    # # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    # parser.add_argument(
    #     "-v",
    #     "--verbose",
    #     action="count",
    #     default=0,
    #     help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
