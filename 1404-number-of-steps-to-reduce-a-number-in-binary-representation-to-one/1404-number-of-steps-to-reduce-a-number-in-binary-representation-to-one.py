class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0

        carry = 0

        for i in reversed(range(1, len(s))):
            digit = (int(s[i]) + carry) % 2

            if digit == 0:
                steps += 1

            else:
                carry = 1
                steps += 2

        return steps + carry
