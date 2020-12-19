"""
File:         norgard.py
Author:       Vu Nguyen
Date:         11/22/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  Replicate the sequence given by the Per Norgard
              , a Danish composer, into a recursive function.
              It takes in a position of nth term and calculate
              the value of the sequence.
"""


def norgard(n):
    # BASE CASE
    if n == 0:
        return 0
    else:
        # Checks for even number
        if n % 2 == 0:
            return norgard((n // 2)) * (-1)
        # Checks for odd number
        else:
            return norgard((n - 1) // 2) + 1


if __name__ == "__main__":
    print(norgard(int(input("What value do you want to calculate? "))))
