
def queue_time(customers, n):
    tills = [0]*n
    for c in customers:
        tills[0] += c
        tills.sort()
    return max(tills)


a = queue_time([1, 10, 12], 5)
print(a)
