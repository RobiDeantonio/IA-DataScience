p = [[0, 11], [-7, 1], [-5, -3]]

print(len(p))


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) *
                     (p1[0] - p2[0]) +
                     (p1[1] - p2[1]) *
                     (p1[1] - p2[1]))


def solution(p):
    n = len(p)
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(p[i], p[j]) < min_val:
                min_val = dist(p[i], p[j])
 
    return min_val