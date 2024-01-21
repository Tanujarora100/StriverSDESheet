from typing import List, Optional

from Heap.Hard.MergeKSortedList import ListNode


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[0] * n for _ in range(m)]
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        ans = []
        filling_value = -1
        dummy = head
        while len(ans) < m * n:
            for j in range(left, right + 1):
                if len(ans) < m * n:
                    if dummy:
                        matrix[top][j] = dummy.val
                        ans.append(dummy.val)
                        dummy = dummy.next
                    else:
                        matrix[top][j] = filling_value
                        ans.append(filling_value)
            for i in range(top + 1, bottom):
                if len(ans) < m * n:
                    if dummy:
                        matrix[i][right] = dummy.val
                        ans.append(dummy.val)
                        dummy = dummy.next
                    else:
                        matrix[i][right] = filling_value
                        ans.append(filling_value)
            for j in range(right, left - 1, -1):
                if len(ans) < m * n:
                    if dummy:
                        matrix[bottom][j] = dummy.val
                        ans.append(dummy.val)
                        dummy = dummy.next
                    else:
                        matrix[bottom][j] = filling_value
                        ans.append(filling_value)
            for i in range(bottom - 1, top, -1):
                if len(ans) < m * n:
                    if dummy:
                        matrix[i][left] = dummy.val
                        ans.append(dummy.val)
                        dummy = dummy.next
                    else:
                        matrix[i][left] = filling_value
                        ans.append(filling_value)
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return matrix