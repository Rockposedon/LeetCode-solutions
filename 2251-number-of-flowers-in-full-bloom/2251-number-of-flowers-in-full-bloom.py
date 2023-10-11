class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        events = []
        for i, flower in enumerate(flowers):
            events.append((flower[0] - 0.01, i, "open"))
            events.append((flower[1] + 0.01, i, "close"))
        for i, person in enumerate(people):
            events.append((person, i, "arrival"))
        
        bloom = set()
        events = sorted(events, key=lambda x: x[0])
        print(events)
        res = [0] * len(people)
        for event in events:
            if event[2] == "open":
                bloom.add(event[1])
            if event[2] == "close":
                bloom.remove(event[1])
            if event[2] == "arrival":
                res[event[1]] = len(bloom)
        
        return res