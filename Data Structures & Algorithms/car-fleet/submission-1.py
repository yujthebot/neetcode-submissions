class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        fleets = 0
        position, speed = zip(*sorted(zip(position,speed)))
        position = list(position)
        speed = list(speed)
        print(position,speed)
        while position:
            pos = position.pop()
            spd = speed.pop()
            t  = (target-pos)/spd
            if not time or t > time[-1]:
                fleets += 1
                time.append(t)
            
        return fleets