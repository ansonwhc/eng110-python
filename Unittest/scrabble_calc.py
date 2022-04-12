def scrabble_calculator(word, show=False):
    assert word.isalpha(), "Only alphabets are accepted"

    letter_value = {letter: value
                    for letters, value in [(list('AEIOULNRST'), 1),
                                           (list('DG'), 2),
                                           (list('BCMP'), 3),
                                           (list('FHVWY'), 4),
                                           (list('K'), 5),
                                           (list('JX'), 8),
                                           (list('QZ'), 10)]
                    for letter in letters}
    word_score = 0
    for char in word.upper():
        word_score += letter_value[char]
    if show:
        print(f"The score for {word} is: {word_score}")

    return word_score


class Scrabble:
    def __init__(self):
        self.letter_value = {letter: value
                             for letters, value in [(list('AEIOULNRST'), 1),
                                                    (list('DG'), 2),
                                                    (list('BCMP'), 3),
                                                    (list('FHVWY'), 4),
                                                    (list('K'), 5),
                                                    (list('JX'), 8),
                                                    (list('QZ'), 10)]
                             for letter in letters}

    def score_calculator(self, word, show=False):
        word = word.strip()
        if not word.isalpha():
            raise AssertionError("Only alphabets are accepted")

        word_score = 0
        for char in word.upper():
            word_score += self.letter_value[char]
        if show:
            print(f"The score for {word} is: {word_score}")

        return word_score


if __name__ == "__main__":
    s = Scrabble()
    class_score = s.score_calculator("sparta", True)
    class_score = s.score_calculator("123", True)
    # func_score = scrabble_calculator("sparta", True)
