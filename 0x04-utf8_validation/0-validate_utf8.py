#!/usr/bin/python3
"""
Function to validate UTF-8 encoding
"""


def validUTF8(data):
    """
    Check if a given list of integers represent a valid UTF-8 encoding.

    Parameters:
    data (list): List of integers representing bytes

    Returns:
    bool: True if data is a valid UTF-8 encoding, False otherwise
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Iterate over each byte in the data
    for byte in data:
        # Get the least significant 8 bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine how many bytes are in the character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # 1 byte character
            if num_bytes == 0:
                continue

            # Invalid scenarios according to UTF-8 rules
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes remaining in the current character
        num_bytes -= 1

    return num_bytes == 0


if __name__ == "__main__":
    # Test cases
    data = [65]
    print(validUTF8(data))  # True

    data = [80, 121, 116, 104, 111, 110, 32, 
    105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False
