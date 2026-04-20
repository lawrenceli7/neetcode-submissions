class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # key=string, val=[[value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        left, right = 0, len(values) - 1
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] == timestamp:
                return values[middle][0]
            elif values[middle][1] > timestamp:
                right = middle - 1
            else:
                res = values[middle][0]
                left = middle + 1
        return res