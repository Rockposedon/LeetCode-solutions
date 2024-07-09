class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time = 0
        curr_time = 0
        for arrival,prepare in customers:
            if curr_time < arrival:
                curr_time = arrival
            curr_time += prepare
            wait_time += curr_time-arrival
        avg_wait = wait_time/len(customers)
        return avg_wait
            