def mutation(arr: list[int]) -> list[int]:
    n = len(arr)
    result = []
    for i in range(n):
        left = arr[i-1] if i > 0 else 0
        center = arr[i]
        right = arr[i+1] if i < n-1 else 0
        result.append(left+center+right)
    return result

def main():
    arr = [4, 0, 1, -2, 3]
    print(mutation(arr))

if __name__ == "__main__":
    main()