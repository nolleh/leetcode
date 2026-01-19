class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []

        curr_num = 0
        curr_str = ""

        for ch in s:
            if ch.isnumeric():
                curr_num = 10 * curr_num + int(ch)
            elif ch == "[":
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif ch == "]":
                repeat = num_stack.pop()
                curr_str = str_stack.pop() + curr_str * repeat
            else:
                curr_str += ch
        return curr_str
