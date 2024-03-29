class Solution(object):
     def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        deque = collections.deque(tokens)

        while deque:
            # When we have enough power, play token face-up
            if power >= deque[0]:
                power -= deque.popleft()
                score += 1

            # We don't have enough power to play a token face-up
            # When there is at least one token remaining,
            # and we have enough score, play token face-down
            elif len(deque) > 2 and score > 0:
                power += deque.pop()
                score -= 1

            # We don't have enough score, power, or tokens 
            # to play face-up or down and increase our score
            else:
                return score

        return score