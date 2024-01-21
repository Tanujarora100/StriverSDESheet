class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        if k < n:
            k = k + 1
        else:
            k = n
        mp = {}
        i = 0
        j = 0
        while j < n:
            mp[nums[j]] = mp.get(nums[j], 0) + 1
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                if len(mp) < k:
                    return True
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1
                j += 1
        return False