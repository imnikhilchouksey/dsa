# You are given an array with unique elements of stalls[], which denote the positions of stalls. You are also given an integer k which denotes the number of aggressive cows. The task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.

# Examples:
# Input: stalls[] = [1, 2, 4, 8, 9], k = 3
# Output: 3
# Explanation: The first cow can be placed at stalls[0], 
# the second cow can be placed at stalls[2] and 
# the third cow can be placed at stalls[3]. 
# The minimum distance between cows in this case is 3, which is the largest among all possible ways.

# Input: stalls[] = [10, 1, 2, 7, 5], k = 3
# Output: 4
# Explanation: The first cow can be placed at stalls[0],
# the second cow can be placed at stalls[1] and
# the third cow can be placed at stalls[4].
# The minimum distance between cows in this case is 4, which is the largest among all possible ways.

# Input: stalls[] = [2, 12, 11, 3, 26, 7], k = 5
# Output: 1
# Explanation: Each cow can be placed in any of the stalls, as the no. of stalls are exactly equal to the number of cows.
# The minimum distance between cows in this case is 1, which is the largest among all possible ways.

def aggressive_cows(stalls,k): 
  stalls.sort()
  low = 1 , 
  high = stalls[-1] - stalls[0]
  result = 0 
  
  while low <= high : 
    mid = low + (high-low)//2
    
    if isPossible(stalls,k,mid) : 
      result = mid 
      low = mid + 1 
    else : 
      high = mid - 1
      
  return result 

def isPossible(stalls,k,dist): 
  count = 1 
  prevStall = stalls[0]
  for i in range(1,len(stalls)): 
    if stalls[i] - prevStall >= dist : 
      count += 1 
      prevStall = stalls[i]
  
  return count >= k

print(aggressive_cows(stalls=  [2, 12, 11, 3, 26, 7], k = 5))