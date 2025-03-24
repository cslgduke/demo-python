def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后的元素已经在位，所以每次减少一个元素
        for j in range(0, n-i-1):
            # 遍历数组从0到n-i-1
            # 交换如果找到元素大于下一个元素
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # 测试代码
if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(array)
    print("Sorted array is:", array)