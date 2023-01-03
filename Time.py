import random
import numpy as np
import time
import math
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


def distance(p1, p2):
    # Calculate the distance
    return math.sqrt(pow(p1[0] - p2[0], 2)
                     + pow(p1[1] - p2[1], 2))


def closest_pair_range(P, Q, d):
    midPoint = P[len(P) // 2][0]
    p1_x = p1_y = p2_x = p2_y = 0

    # Get the points in range (-d, d) according tho the mid point
    rangeDist = [Q[i] for i in range(len(Q)) if midPoint - d <= Q[i][0] <= midPoint + d]
    minDist = math.inf

    # i + 1, min(i + 15, len(rangeDist))
    # or
    # i + 1, min(i + int(d) // 2, len(rangeDist))
    # or
    # i + 1, min(i + int(d ** (1.0/5.0)), len(rangeDist))
    for i in range(len(rangeDist)):
        # Check at most 15 next values
        for j in range(i + 1, min(i + 15, len(rangeDist))):
            dNew = distance(rangeDist[i], rangeDist[j])

            if dNew < minDist:
                p1_x, p1_y, p2_x, p2_y = rangeDist[i][0], rangeDist[i][1], rangeDist[j][0], rangeDist[j][1]
                minDist = dNew  # Update the min distance
    return minDist, ([p1_x, p1_y], [p2_x, p2_y])


def closest_pair(P):
    # Brut if tree points are left:
    lenP = len(P)
    if lenP <= 3:
        return find_closest_brute_force(P)

    # Sort arrays by x and y coordinates
    Pn = sorted(P, key=lambda x: x[0])
    Qn = sorted(P, key=lambda x: x[1])

    midPoint = lenP // 2
    Qx = Pn[:midPoint]  # Get left part of array with x sorted
    Rx = Pn[midPoint:]  # Get right part of array with x sorted

    # Recursively call
    dLeft, ([p1Left_x, p1Left_y], [p2Left_x, p2Left_y]) = closest_pair(Qx)  # Left side min
    dRight, ([p1Right_x, p1Right_y], [p2Right_x, p2Right_y]) = closest_pair(Rx)  # Right side min

    # Take the min value and assign the points
    if dLeft > dRight:
        minDistAll = dRight
        p1Min_x, p1Min_y, p2Min_x, p2Min_y = \
            p1Right_x, p1Right_y, p2Right_x, p2Right_y
    else:
        minDistAll = dLeft
        p1Min_x, p1Min_y, p2Min_x, p2Min_y = \
            p1Left_x, p1Left_y, p2Left_x, p2Left_y

    # Check the middle for closest pair of points
    d, ([p1_x, p1_y], [p2_x, p2_y]) = closest_pair_range(Pn, Qn, minDistAll)
    minDistPlane = min(d, minDistAll)

    # Return the min distance on a plane
    if minDistPlane == d:
        return minDistPlane, ([p1_x, p1_y], [p2_x, p2_y])
    else:
        return minDistPlane, ([p1Min_x, p1Min_y], [p2Min_x, p2Min_y])


def find_closest_brute_force(array):
    
    result = {}
    result["p1"] = array[0]
    result["p2"] = array[1]
    result["distance"] = np.sqrt((array[0][0]-array[1][0])**2
                                +(array[0][1]-array[1][1])**2)
    
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            distance = np.sqrt((array[i][0]-array[j][0])**2
                              +(array[i][1]-array[j][1])**2)
            if distance < result["distance"]:
                result["p1"] = array[i]
                result["p2"] = array[j]
                result["distance"] = distance
		
  
    return distance, (array[i], array[j])


def brute_force(array):
    
    result = {}
    result["p1"] = array[0]
    result["p2"] = array[1]
    result["distance"] = np.sqrt((array[0][0]-array[1][0])**2
                                +(array[0][1]-array[1][1])**2)
    
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            distance = np.sqrt((array[i][0]-array[j][0])**2
                              +(array[i][1]-array[j][1])**2)
            if distance < result["distance"]:
                result["p1"] = array[i]
                result["p2"] = array[j]
                result["distance"] = distance	
    return result


Size = 500
x_values_brute = []
y_values_brute = []
x_values_divide = []
y_values_divide =[]



while Size <= 10000:

    coords = [(random.randint(1, 100000), random.randint(1, 100000)) for _ in range(Size)]
    
    brute_start = time.time()
    closest_brute = brute_force(coords)
    brute_end = time.time()
    x_values_brute.append(brute_end - brute_start)
    y_values_brute.append(Size)

    divide_start = time.time()
    closest_divide = closest_pair(coords)
    divide_end = time.time()
    x_values_divide.append(divide_end - divide_start)
    y_values_divide.append(Size)
    
    Size = Size + 1000


print(x_values_brute, y_values_brute)
print(x_values_divide, y_values_divide)

#x, y = zip(*coords)
#plt.scatter(x,y)
#x_values = [closest_brute["p1"][0], closest_brute["p2"][0]]
#y_values = [closest_brute["p1"][1], closest_brute["p2"][1]]
plt.plot(x_values_brute,y_values_brute , color = 'r')
plt.plot(x_values_divide,y_values_divide , color = 'b')
plt.show()












