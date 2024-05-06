#!/usr/bin/python3

"""
Problem: Given n locked boxes numbered 0 to n-1,
determine if all boxes can be opened by following keys within them.
"""


def canUnlockAll(boxes):

    """
    Checks with bool value if the list type &
    length to invoke two for iterations one to traverse the list
    and the other to compaer if key is idx or not in order to open
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
