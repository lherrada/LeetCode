class Ksum():
    def sumk(self, array: list, target: int, k: int) -> list:
        H = {}
        solution = set()
        if k is 2:
            return self.sum2(array, target)

        for i in range(len(array)):
            num = array[i]
            if num not in H:
                H[num] = self.sumk(array[i + 1:], target - num, k - 1)

        for k, v in H.items():
            for i in v:
                solution.add(tuple(sorted((k,) + i)))
        return list(solution)

    def sum2(self, array: list, target: int) -> list:
        H = {}
        solution = []
        for num in array:
            if num in H:
                solution.append((num, target - num))
            else:
                H[target - num] = num
        return solution


a = [1, 0, -1, 0, -2, 2]
print(Ksum().sumk(a, 0, 4))
