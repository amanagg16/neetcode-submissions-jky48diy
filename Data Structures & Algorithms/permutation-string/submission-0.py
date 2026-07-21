class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Count characters in s1
        counter = {}
        for c in s1:
            counter[c] = counter.get(c, 0) + 1
        
        unique_chars = len(counter)
        matches = 0
        window_size = len(s1)
        
        # First window
        for i in range(window_size):
            c = s2[i]
            if c in counter:
                counter[c] -= 1
                if counter[c] == 0:
                    matches += 1
            if matches == unique_chars:
                return True
        
        # Slide the window
        for i in range(window_size, len(s2)):
            # Remove left character
            left = s2[i - window_size]
            if left in counter:
                if counter[left] == 0:
                    matches -= 1
                counter[left] += 1
            
            # Add right character
            right = s2[i]
            if right in counter:
                counter[right] -= 1
                if counter[right] == 0:
                    matches += 1
            
            if matches == unique_chars:
                return True
        
        return False
        
