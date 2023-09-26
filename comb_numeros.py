import itertools
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []

    print(len(digits) > 1)
    if len(digits) > 1:
        comb = []
        for i in range(len(digits)):
            f = []
            if digits[i] == "2":
                f = ["a", "b", "c"]

            if digits[i] == "3":
                f = ["d", "e", "f"]

            if digits[i] == "4":
                f = ["g", "h", "i"]

            if digits[i] == "5":
                f = ["j", "k", "l"]

            if digits[i] == "6":
                f = ["m", "n", "o"]

            if digits[i] == "7":
                f = ["p", "q", "r", "s"]

            if digits[i] == "8":
                f = ["t", "u", "v"]

            if digits[i] == "9":
                f = ["w", "x", "y", "z"]

            comb += f
        res = []
        print(comb)
        res = list(itertools.permutations(comb,len(digits)))

        return res


def main():
    x = input("?")
    print(letterCombinations(x))

main()