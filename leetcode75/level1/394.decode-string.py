class Solution:
    def decodeString(self, s: str) -> str:
        # k[encoded_string] -> repeated k times
        # "3[a2[c]]" -> 3[acc] -> accaccacc
        # 2[abc]3[cd]ef -> abcabccdcdcdef

        # 3[ decodeString(a2[c]) ]

        ans = ""

        num_stack = []
        str_stack = []

        curr_num = 0
        curr_str = ""

        for ch in s:
            if ch.isnumeric():
                # accumulate number
                curr_num = 10 * curr_num + int(ch)
            else:
                if ch == "[":
                    # meaning end of number. push that to num_stack
                    num_stack.append(curr_num)
                    str_stack.append(curr_str)
                    curr_str = ""

                elif ch == "]":
                    # end of repeated charactor. do repeat
                    curr_str = curr_str * num_stack.pop(-1)
                    curr_str = str_stack.pop(-1) + curr_str

                    if not num_stack:
                        ans += curr_str
                        curr_str = ""

                else:
                    curr_str += ch

                curr_num = 0

        if curr_str:
            ans += curr_str

        return ans
