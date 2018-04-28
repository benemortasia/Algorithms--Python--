import heapq

# returns the longest consecutive character in a string
def longestConsecChar(string):
    str1 = string[0]
    max_heap = []
    char_dict = {}

    for c in range(1, len(string) - 1):
        if string[c] == str1[0]:
            str1 += string[c]
        else:
            str1 = string[c]
        heapq.heappush(max_heap, -len(str1))
        char_dict[len(str1)] = str1

    return char_dict.get(-heapq.heappop(max_heap))

print longestConsecChar('AABCDDBBBEA')
print longestConsecChar('AABBCCGEHGHHHEEEEEEEEEEHHGgggeefga')
print longestConsecChar('11001010101101010010001010101001010101101010100101010100101010110101101010101001010110101010101010010101')
