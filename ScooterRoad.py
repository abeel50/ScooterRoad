# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def calcDist (A,S,T):
    return (A* 5) + (S*40) if T == 1 else (A*20) + (S*30)


def solution(R):
    # write your code in Python 3.6
    
    asphlat, sand, road = 0, 0, len(R)
    if R[0] == 'A':
        asphlat = R.count('A')
        sand = road - asphlat
    else:
        sand  = R.count('S')
        asphlat = road - sand
    if asphlat == road:
        return 5 * asphlat
    if sand == road:
        return 30 * sand
    dis = []
    dis.append(calcDist(asphlat,sand,2))
    scooterDis = 0
    for i in R:
        if i == 'A':
            scooterDis += 5
            asphlat -= 1
            dis.append(scooterDis + calcDist(asphlat,sand,2))
        else:
            scooterDis += 40
            sand -= 1
            dis.append(scooterDis + calcDist(asphlat,sand,2))
    return min(dis)