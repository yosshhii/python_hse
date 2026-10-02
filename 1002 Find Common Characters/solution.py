class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        chars = list(dict.fromkeys(words[0]))
        chars_counter = [words[0].count(char) for char in chars]
        for word in words[1:]:
            for i in range(len(chars) - 1, -1, -1):
                if chars[i] not in word:
                    chars.pop(i)
                    chars_counter.pop(i)
                else:
                    chars_counter[i] = min(chars_counter[i], word.count(chars[i]))

        answer_chars = []
        for i in range(len(chars)):
            answer_chars.extend([chars[i]] * chars_counter[i])

        return answer_chars