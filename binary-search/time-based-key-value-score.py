# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key] = self.times.get(key, [])
        self.times[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        
        storedTimes = self.times[key]

        left, right = 0, len(storedTimes) - 1

        highestAcceptedTimeVal = ""
        while left <= right:
            mid = (left + right) // 2

            if storedTimes[mid][0] > timestamp:
                right = mid - 1
            elif storedTimes[mid][0] < timestamp:
                highestAcceptedTimeVal = storedTimes[mid][1]
                left = mid + 1
            else:
                return storedTimes[mid][1]

        return highestAcceptedTimeVal

