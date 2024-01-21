class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return self.check_palindrome_with_skip(s, left) or self.check_palindrome_with_skip(s, right)
            else:
                left += 1
                right -= 1
                
        return True
            
    def check_palindrome_with_skip(self, s: str, int_to_skip: int) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if int_to_skip == left:
                left += 1
                continue
                
            if int_to_skip == right:
                right -= 1
                continue
            
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
            
        return True
    