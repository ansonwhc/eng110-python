# input scrabble class, record inputted words and scores
from scrabble_calc import Scrabble


class ScrabbleRecord:
    def __init__(self, scrabble, file_name=None):
        self.scrabble = scrabble()
        self.file_name = file_name

        self.reset()

    def reset(self):
        # TODO: More flexible, not resetting every time we init the class
        self.check_file_name()
        open(self.file_name, 'w')

    def append(self):
        # TODO: make file to append to file if selected
        return NotImplemented

    def calculate(self, word):
        word_score = self.scrabble.score_calculator(word)
        return word_score

    def check_file_name(self):
        if self.file_name is None:
            self.file_name = "scrabble_game_record.txt"
        elif '.' not in self.file_name:
            self.file_name = f"{self.file_name}.txt"
        else:
            raise ValueError("Only .txt format is accepted")
            # Double-check the Error for wrong extension

    def record(self, word):
        word_score = self.calculate(word)

        with open(self.file_name, 'a') as file:
            file.write(f"Word inputted: {word}\nScore: {word_score}\n\n")

    def total_score(self):
        # TODO: After all calls of record, generate a total score
        #  (without recording as we can be appending without reset)
        with open(self.file_name, 'a+') as file:
            total_score = 0
            for line in file.readlines():
                if line.startswith("Score"):
                    total_score += int(line.split(': ')[1])
            file.write(f"Total Score: {total_score}\n")


if __name__ == "__main__":
    scrabble_record = ScrabbleRecord(Scrabble)
    scrabble_record.record('Sparta')
    scrabble_record.record('Global')
    scrabble_record.record('DevOps')

