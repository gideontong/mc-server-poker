"""
Main function of mc-server-poker.
"""

from lib import *

def main():
    """
    Main function of mc-server-poker.
    """

    Server.init()
    status = Server.query()
    print(status)

main()