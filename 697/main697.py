# Пусть задан непустой массив неотрицательных целых чисел nums. Степень этого массива определяется как максимальная
# частота любого из его элементов.
#
# Ваша задача — найти наименьшую возможную длину (непрерывного) подмассива nums, имеющего ту же степень, что и nums.

def findShortestSubArray(nums: list[int]) -> int:

    quantity = {}
    for element in nums:
        if element in quantity.keys():
            quantity[element] += 1
        else:
            quantity[element] = 1

    quantity = dict(sorted(quantity.items(), key=lambda x: x[1], reverse=True))
    degree = list(quantity.values())[0]

    result = 50000
    for key, value in quantity.items():
        if value == degree:
            left = 0
            right = 50000
            for i in range(len(nums)):
                if nums[i] == key:
                    left = i
                    break
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == key:
                    right = i
                    break
            result = min(result, right - left + 1)
        else:
            break
    return result


nums = list(map(int, input().split()))
print(findShortestSubArray(nums))