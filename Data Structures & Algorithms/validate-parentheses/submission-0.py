class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            '}':'{',
            ')':'(',
            ']':'[',
        }
        stack = []
        for p in s:
            if p in hashmap:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[p]:
                        return False
            else:
                stack.append(p)

        return not stack