class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}":"{","]":"[",")":"("}
        visited = []
        for c in s:
            if c in pairs:
                if visited and visited[-1] == pairs[c]:
                    visited.pop()
                else:
                    return False
            else:
                visited.append(c)
        return True if not visited else False