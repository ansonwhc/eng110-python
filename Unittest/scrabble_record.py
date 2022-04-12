# input scrabble class, record inputted words and scores
from scrabble_calc import Scrabble
# TODO: write the unittest scripts for all the methods tested within this scripts


class ScrabbleRecord:
    def __init__(self, scrabble=Scrabble, file_name=None, mode='w'):
        assert mode in ['w', 'a'], AssertionError(f"Only the write mode ('w') or append mode ('a') are supported\n\
        Inputted {mode}")

        self.scrabble = scrabble()
        self.file_name = file_name
        self.mode = mode

        self.start()

    def start(self):
        self.check_file_name()
        if self.mode == 'w':
            open(self.file_name, self.mode)

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
            # TODO: Double-check the Error for wrong extension

    def record(self, *words):
        # does not
        for words_with_spaces in words:
            for word in words_with_spaces.strip().split(' '):
                word_score = self.calculate(word)
                with open(self.file_name, 'a') as file:
                    file.write(f"Word inputted: {word}\nScore: {word_score}\n\n")
                self.total_score()

    def total_score(self):
        #  Without recording, as we can be appending when initialising the class
        with open(self.file_name, 'r') as read_file:
            read_lines = read_file.readlines()
        with open(self.file_name, 'w') as write_file:
            # since we are looping through all the lines, so it doesn't matter if we recalculate the entire total_score
            # ideally, maybe we don't loop the lines and use regex to look for the "Total ..." str, and delete it
            # but... does that mean we're loading the entire txt file onto the memory??? which can lead to other issues?
            total_score = 0
            for line in read_lines:
                if not line.startswith("Total"):
                    write_file.write(line)
                    if line.startswith("Score"):
                        total_score += int(line.split(': ')[1])
            write_file.write(f"Total Score: {total_score}\n")

    def read_record(self):
        with open(self.file_name, 'r') as file:
            for line in file.readlines():
                print(line.strip('\r?\n+'))


if __name__ == "__main__":
    scrabble_record = ScrabbleRecord(Scrabble)
    scrabble_record.record('Sparta')
    scrabble_record.record('Global')
    scrabble_record = ScrabbleRecord(Scrabble, mode='a')
    scrabble_record.record('DevOps', 'Consultant')
    scrabble_record.record(' Trainee Anson ', 'Anson again')
    scrabble_record.read_record()

