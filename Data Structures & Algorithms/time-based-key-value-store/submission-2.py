class TimeMap:

    def __init__(self):
        self.moods = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.moods:
            self.moods[key].append((value,timestamp))
        else:
            self.moods[key] = [(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.moods:
            return ""
        else:
            lo =0
            hi =len(self.moods[key])-1
            best = None
            while lo <= hi:
                mid = (lo+hi)//2
                middle = self.moods[key][mid][1]
                if middle == timestamp:
                    return self.moods[key][mid][0]
                elif middle >timestamp: #searching into the future
                    hi = mid-1      #move left due to out of range
                        
                else:               #still within the left of the list
                    best = mid
                    lo = mid +1 #allows for search to the right?
            if best == None:
                return ""
            else:            
                return self.moods[key][best][0]
            
        
