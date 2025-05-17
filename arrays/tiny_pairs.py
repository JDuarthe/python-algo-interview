
def tiny_pairs(a: list[int], b: list[int], k: int):
    count = 0
    n = len(a)
    for i in range(n):
        combined = int(str(a[i]) + str(b[n-1-i]))
        if combined < k:
            count += 1
    return count
         

def main():
    a = [1, 2, 3]
    b = [1, 2, 3]
    k = 31
    print(tiny_pairs(a, b, k))


if __name__ == "__main__":
    main()