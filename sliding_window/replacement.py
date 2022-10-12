##https://leetcode.com/problems/longest-repeating-character-replacement/

def valid_dict(d, k):
    """
    recives a dictionary, 
    returns True if the dictionary has only one item,
    or if the values of all items except one add to less or equal to k
    returns False otherwise
    """
    if d == {}:
        return True
    values = list(d.values())
    values.sort()
    if len(values) < 2:
        return True
    return sum(values[:len(values)-1]) <= k


def characterReplacement(s: str, k: int) -> int:
        ##is the same problem as looking for the longest substrings where all the elements are the same except for k elements
        substring = ""
        dict_substring = {}
        max_length = 0
        for elem in s:
            substring += elem
            print(substring)
            if elem in dict_substring:
                dict_substring[elem] += 1
            else:
                dict_substring[elem] = 1
            if not valid_dict(dict_substring, k):
                print("+")
                max_length = max(max_length, len(substring) -1)
                while not valid_dict(dict_substring, k):
                    removed = substring[0]
                    substring = substring[1:]
                    dict_substring[removed] -= 1
        max_length = max(max_length, len(substring))
        return max_length
            