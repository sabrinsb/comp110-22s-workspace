"""EX02 - One - Shot - Wordle."""
__author__ = "730221505"

secret_word: str = "python"
sw_len: int = len(secret_word)
sw_index: int = 0 
gw_index: int = 0 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji_results: str = ""
guessed_char: bool = False

guess_word: str = input(f"What is your {sw_len}-letter guess? ")
gw_len: int = len(guess_word)
while gw_len != sw_len:
    guess_word = input(f"That was not {sw_len} letters! Try again: ")
    gw_len = len(guess_word)
while gw_index < sw_len:
    if guess_word[gw_index] == secret_word[gw_index]:
        emoji_results = emoji_results + GREEN_BOX
    else:
        guessed_char = False 
        sw_index = 0 
        while not guessed_char and sw_index < sw_len: 
            if guess_word[gw_index] == secret_word[sw_index]:
                guessed_char = True 
            else:
                sw_index += 1
        if guessed_char:         
            emoji_results = emoji_results + YELLOW_BOX
        else:
            emoji_results = emoji_results + WHITE_BOX
    gw_index += 1

print(emoji_results)

if guess_word == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")