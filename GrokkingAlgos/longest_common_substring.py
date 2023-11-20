def longest_common_substring(word_a, word_b):
    Cell = [[0 for x in range(len(word_a) + 1)] for x in range(len(word_b) + 1)]
    max = 0
    # print(Cell)
    for i in range(len(word_b) + 1):
        for j in range(len(word_a) + 1):
            if i == 0 or j == 0:
                Cell == [0]
            elif word_b[i-1] == word_a[j-1]:
                Cell[i][j] = Cell[i-1][j-1] + 1
                max = Cell[i][j]
            else:
                Cell[i][j] == 0
    # print(Cell)
    return max

if __name__ == '__main__':
    print(longest_common_substring('vista', 'hish'))
    print(longest_common_substring('fosh', 'fish'))
    print(longest_common_substring('fosh', 'fabc'))
