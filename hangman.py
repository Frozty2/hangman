class Hangman():
    def  __init__(self, word, lives=6, result = 0):
        self.word = word
        self.lives = lives
        self.x = "".join('_ ' for i in range(len(self.word)))
        self.result = result
    def underscore_printer(self):
        print(self.x)
    def life_checker(self, life):
        print("Attempts %s/6" %(life))
    def letter_checker(self):
        while 1:
            letter = input("Guess the letter: ")
            index = [pos for pos, char in enumerate(self.word) if char == letter]
            if letter in self.word:
                if letter == self.word:
                    self.result = 1
                    print("You're right, the word is: %s" %(self.word))
                    return print('You won!')
                else:
                    for i in index:
                        if i == 0:
                            text = letter + self.x[1:]
                        elif i == 1:
                            text = self.x[:i+1] + letter + self.x[2*i+1:]
                        else:
                            text = self.x[:2*i] + letter + self.x[2*i+1:]
                        self.x = text
                        b = self.x.replace(" ", "")
                        if b == self.word:
                            self.result = 1
                            print("You're right, the word is: %s" %(self.word))
                            return print("You won")
                    print(self.x)
            else:
                break
def main():
    input_word = input("Write your word: ")
    hangman = Hangman(input_word)
    hangman.underscore_printer()
    for l in range(7):
        hangman.life_checker(l)
        hangman.letter_checker()
        if hangman.result == 1:
            break
        elif l == 5:
            print("You lost!")
            break
if __name__ == "__main__":
    main()