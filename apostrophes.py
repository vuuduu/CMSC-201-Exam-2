"""
File:         apostrophes.py
Author:       Vu Nguyen
Date:         11/22/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This program loops through each character of the string using recursion
              and added in the apostrophe before the last s of each word. 
"""

APOSTROPHE = "'"
LETTER_S = 's'


def apos(apos_string, user_string, index):
    """
    :param apos_string: the updated string with the added apostrophe.
    :param user_string: the string that needed to be modify with apostrophe.
    :param index: The position of the character in a string.
    :return: return the updated string with apostrophe s.
    """
    # BASE CASE
    if index > len(user_string) - 1:
        return apos_string
    else:

        # This condition checks to see if the letter is S or not.
        if user_string[index] == LETTER_S:

            # This condition checks to see if the letter s is the last letter in the string
            if index == len(user_string) - 1:
                return apos(apos_string + APOSTROPHE + user_string[index], user_string, index+1)
            else:

                # Check to see if the next character is not a letter.
                if not user_string[index + 1].isalnum():
                    return apos(apos_string + APOSTROPHE + user_string[index], user_string, index+1)
                else:
                    return apos(apos_string + user_string[index], user_string, index+1)

        else:
            return apos(apos_string + user_string[index], user_string, index+1)


if __name__ == "__main__":
    print(apos('', input("Enter a string: "), 0))




