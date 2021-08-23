class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        alpha = []

        # divide logs into two groups
        for log in logs:
            if log.split()[1].isnum():
                digits.append(log)
            else:
                alpha.append((log))

        # sort alpha array by order if order is same, then sort by log order
        alpha.sort(key = lambda x: x.split()[1],x.split()[0])

        # merge two lists
        return alpha + digits