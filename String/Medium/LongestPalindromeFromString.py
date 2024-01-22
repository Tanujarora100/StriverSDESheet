from collections import Counter


from collections import Counter

def longest_palindrome(n: int, s: str) -> int:
    # Create a hash map to count the occurrences of each character in the string
    hash_map = Counter(s)
    # Initialize counts for even and odd character occurrences
    even_count = 0
    odd_count = 0
    # Iterate through the values in the hash map
    for i in hash_map.values():
        # If the count of the character is even, add it to the even count
        if i % 2 == 0:
            even_count += i
        else:
            # If the count is odd, add it to the odd count and subtract 1 from the count before adding it to the even count
            odd_count += 1
            even_count += i - 1
        # We are making sure that okay even if it odd then we will use the even part of it to make the string as longer as possible.
    
    # If there are any odd counts, add 1 to the even count to account for the center character of the palindrome
    # At the end it would not harm us that we add another odd character to the string to make sure.
    
    # Hum Odd Count ko last mei add kar rahe hain kyuki hum ek character aur add karke string ki length aur badhwa sakte hain.
    if odd_count > 0:
        even_count += 1
    
    # Return the total count of characters that can be used to form a palindrome
    return even_count