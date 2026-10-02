class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:

        distances = [0] * len(s)
        last_position = -len(s)

        for i in range(len(s)):
            if s[i] == c:
                last_position = i
            distances[i] = i - last_position

        last_position = 2 * len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                last_position = i
            distances[i] = min(distances[i], last_position - i)

        return distances