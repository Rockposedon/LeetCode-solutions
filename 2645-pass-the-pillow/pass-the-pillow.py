class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        current = 1
        forward = True
        while time > 0:
            if current == n:
                forward = False
            if current == 1:
                forward = True

            if forward:
                current += 1
            else:
                current -= 1
            time -= 1
        return current