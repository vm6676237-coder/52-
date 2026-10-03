# Дан массив положительных целых чисел nums и положительное целое число target. Верните минимальную длину массива.
# подмассивСумма элементов которого больше или равна нулю target. Если такого подмассива нет, верните 0 вместо этого.

def minSubArrayLen(target, nums):
    left = 0
    window_sum = 0
    answer = 100001

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            answer = min(answer, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return answer if answer != 100001 else 0

print(minSubArrayLen(11, [1, 3, 4, 5]))
