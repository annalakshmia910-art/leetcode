class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}

        # Count frequency
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        # Sort by frequency
        result = ""

        while count:
            max_char = None
            max_count = 0

            for ch in count:
                if count[ch] > max_count:
                    max_count = count[ch]
                    max_char = ch

            result += max_char * max_count
            del count[max_char]

        return result