def left_maximums(
    arr: list[int],
    left: int,
    right: int,
    current_max: int,
    result: list[str],
) -> int:
    if left == right:
        current_max = max(current_max, arr[left])
        result.append(str(current_max))
        return current_max

    middle = (left + right) // 2
    current_max = left_maximums(arr, left, middle, current_max, result)
    return left_maximums(arr, middle + 1, right, current_max, result)


n = int(input())
arr = list(map(int, input().split()))
result: list[str] = []
left_maximums(arr, 0, n - 1, arr[0], result)
print(" ".join(result))
