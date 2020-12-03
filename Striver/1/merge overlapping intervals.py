def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    print(intervals)
    print()
    merged = []
    for interval in intervals:
        if len(merged)==0 or  merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

a=merge([[1,3],[2,6],[8,10],[8,9],[9,11],[9,10],[15,18],[2,4],[16,17]])
print(a)