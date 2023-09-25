class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def create_char_count_dict(input_string):
            char_count = {}

            for char in input_string:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

            return char_count

        def subtract_dict_counts(large_dict, small_dict):
            result_dict = large_dict.copy()  

            for char, count in small_dict.items():
                if char in result_dict:
                    result_dict[char] -= count

            return result_dict

        def dict_to_string(input_dict):
            return ''.join([key * value for key, value in input_dict.items()])

        str_long = ""
        str_short = ""
        length_str1 = len(s)
        length_str2 = len(t)

        if length_str1 >= length_str2:
            str_short = t
            str_long = s
        else:
            str_long = t
            str_short = s

        long_dict = create_char_count_dict(str_long)
        short_dict = create_char_count_dict(str_short)

        diff_dict = subtract_dict_counts(long_dict, short_dict)
        diff_str = ""
        diff_str = dict_to_string(diff_dict)

        return diff_str

            
