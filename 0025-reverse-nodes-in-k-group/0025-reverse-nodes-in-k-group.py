# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        for i in range(0, len(nums), k):
            if i + k <= len(nums):
                nums[i:i+k] = nums[i:i+k][::-1]

        dummy = ListNode(0)
        curr = dummy

        for x in nums:
            curr.next = ListNode(x)
            curr = curr.next

        return dummy.next