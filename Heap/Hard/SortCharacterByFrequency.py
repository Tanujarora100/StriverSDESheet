from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count up the occurrences.
        counts = Counter(s)

        # Sort characters by frequency.
        characters = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)

        # Convert the counts into a string using a StringBuilder.
        result = []
        for char in characters:
            result.extend([char] * counts[char])

        return ''.join(result)
