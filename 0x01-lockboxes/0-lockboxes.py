def canUnlockAll(boxes):
    if not boxes:
        return False
    
    n = len(boxes)
    keys = set(boxes[0])  # Initialize keys with keys in the first box
    opened = {0}          # Initialize opened set with the first box
    
    while keys:
        key = keys.pop()
        if key < n and key not in opened:  # Ensure the key is within range and not opened already
            opened.add(key)
            keys.update(boxes[key])
    
    return len(opened) == n

# Test cases
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False

