#4 跳出循环
nums = [23, 45, 8, 13, 50, 43, 21]

# 把 nums 里的值从前向后累加
# 当总和超过 100 时则不再继续累加

sum = 0
for n in nums:
# 累加
    sum += n
    if sum > 100:
# 满足条件时跳出循环
        break

print(sum)
