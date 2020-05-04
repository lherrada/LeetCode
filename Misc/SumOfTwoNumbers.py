# https://www.youtube.com/watch?v=XKu_SEDAykw&t=297s
# Find the pair of numbers which sum is 45
a = [3, 5, 7, 9, 10, 13, 14, 20, 25]
mysum = 45


# Quadratic solution (O(n^2))
def bruteForce(array, mysum):
    L = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == mysum:
                L.append((a[i], a[j]))
    return L


# Solution O(n) . Sorted input
def assumeSortedArray(array, mysum):
    i = 0
    j = len(array) - 1
    L = []
    while i < j:
        if a[i] + a[j] < mysum:
            i += 1
        elif a[i] + a[j] > mysum:
            j -= 1
        else:
            L.append((a[i], a[j]))
            i += 1
    return L


# Different approach: using complements
# Solution O(n) . Unsorted input
def complementSolution(array, mysum):
    H = {}
    L = []
    for index in range(len(array)):
        number = array[index]
        if number in H:
            L.append((number, mysum - number))
        else:
            H.setdefault(mysum - number, index)
    return L

print(bruteForce(a,mysum))
print(assumeSortedArray(sorted(a),mysum))
print(complementSolution(a, mysum))
