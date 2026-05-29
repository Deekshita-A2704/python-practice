class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """

        ans = []
        current = 1

        for num in target:
            while current < num:
                ans.append("Push")
                ans.append("Pop")
                current += 1
            ans.append("Push")
            current += 1

        return ans
        
