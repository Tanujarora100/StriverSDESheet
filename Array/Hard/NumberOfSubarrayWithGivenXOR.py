class Solution:
    def solve(self, A, B):
        hash_map = {}
        xor_sum = 0
        count = 0

        for num in A:
            xor_sum ^= num
            # If current XOR sum is equal to B, increment the count
            if xor_sum == B:
                count += 1

            # If there is a prefix subarray with XOR sum equal to (xor_sum - B),
            # add the count of such subarrays to the total count
            if xor_sum ^ B in hash_map:
                count += hash_map[xor_sum ^ B]

            # Update the hash_map with the current XOR sum
            if xor_sum in hash_map:
                hash_map[xor_sum] += 1
            else:
                hash_map[xor_sum] = 1

        return count

