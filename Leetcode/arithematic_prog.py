class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        s = set()
        for i in range(1, len(arr)):
            if i == 1:
                s.add(arr[i] - arr[i-1])
            else:
                if arr[i] - arr[i-1] not in s:
                    return False
        return True

class Solution2:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    arr.sort()
    in_diff=abs(arr[0]-arr[1])
    for i in range(0,len(arr)-1):
        if abs(arr[i]-arr[i+1])!=in_diff:
        return (False)