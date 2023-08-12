def first_non_repeating_char(string):
    """
    Time Complexity - O(N) since we are iterating through the elements. Though we iterate twice, it's not O(N^2)  but
    Space Complexity - O(1) since the dictionary is going to have at most 26 characters, num of english alphabets
    O(N) + O(N) = O(N)
    :param string:
    :return:
    """
    char_index = dict()
    for i, ch in enumerate(string):
        # if the character is already present in the dictionary assign it -1 indicating that its repeated
        # else assign the index as the value
        char_index[ch] = -1 if char_index.get(ch) else str(i)
    for ch, index in char_index.items():
        if index != -1:
            return int(index)
    return -1


def first_non_repeating_char_sol2(string):
    """
    Time Complexity - O(N) since we are iterating through the elements. Though we iterate twice, it's not O(N^2)  but
    Space Complexity - O(1) since the dictionary is going to have at most 26 characters, num of english alphabets
    O(N) + O(N) = O(N)
    :param string:
    :return:
    """
    char_freq = dict()
    # Find frequency of characters
    for ch in string:
        char_freq[ch] = char_freq.get(ch, 0) + 1
    # Now iterate through the string and find the freq of the char. If it's 1, then return the index
    for index, ch in enumerate(string):
        if char_freq[ch] == 1:
            return index
    return -1


def first_non_repeating_char_brute_force(string):
    """
    Time complexity - O(N^2) since we have nested iteration
    Space complexity - O(1) since we are using duplicate variable only which is independent of the input length
    :param string:
    :return:
    """
    for i in range(len(string)):
        duplicate = False
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
                duplicate = True
                break
        if not duplicate:
            return i
    return -1


string = "faadabcbbebdf"
print(first_non_repeating_char(string))
print(first_non_repeating_char_sol2(string))
print(first_non_repeating_char_brute_force(string))
