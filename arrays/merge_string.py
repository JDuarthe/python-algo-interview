
def merge_string(string1: str, string2: str) -> str:
    result = []
    i = 0
    while i < len(string1) or i < len(string2):
        if i < len(string1):
            result.append(string1[i])
        if i < len(string2):
            result.append(string2[i])
        i += 1

    return ''.join(result)



def main():
    word1 = "abc"
    word2 = "pqr"
    word3 = "ab"
    word4 = "pqrs"
    print(merge_string(word1, word2))
    print(merge_string(word3, word4))

if __name__ == "__main__":
    main()