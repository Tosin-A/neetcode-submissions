class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Clean the string (keeps only letters/numbers and makes lowercase)
        # This fixes the punctuation and uppercase bugs
        cleaned_list = [char.lower() for char in s if char.isalnum()]
        
        # 2. Make a copy of the cleaned list to act as our stack
        stack = list(cleaned_list)
        
        # 3. Create an empty list to hold the reversed characters
        backwards_list = []
        
        # 4. Use a while loop to safely pop every item off the stack
        while stack:
            last = stack.pop()
            backwards_list.append(last)
            
        # 5. Compare the two lists directly (no need to join into strings!)
        if backwards_list == cleaned_list:
            return True
        else:
            return False