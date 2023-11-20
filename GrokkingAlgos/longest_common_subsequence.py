def longest_common_subsequence(word_a, word_b):
    Cell = [[0 for x in range(len(word_a) + 1)] for x in range(len(word_b) + 1)]

    # print(Cell)
    for i in range(len(word_b) + 1):
        for j in range(len(word_a) + 1):
            if i == 0 or j == 0:
                Cell[i][j] = 0
            elif word_b[i-1] == word_a[j-1]:
                Cell[i][j] = Cell[i-1][j-1] + 1
            else:
                Cell[i][j] = max(Cell[i-1][j], Cell[i][j-1])
    # print(Cell)
    return Cell[len(word_b)][len(word_a)]


if __name__ == '__main__':
    print(longest_common_subsequence('vista', 'hish'))
    print(longest_common_subsequence('fosh', 'fish'))
    print(longest_common_subsequence('fosh', 'fabc'))
    print(longest_common_subsequence('blue', 'clues'))