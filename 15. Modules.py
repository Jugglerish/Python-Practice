# Create a module that holds the functions for finding the number of different ways the various combinations of words can be given with a single word (Include repetition of letter cases also)

#combinations.py
import itertools

def count_combinations(word):
    all_permutations = set(''.join(p) for p in itertools.permutations(word.lower()))
    num_combinations = len(all_permutations)
    return num_combinations

#main.py
from combinations import count_combinations

def main():
    input_word = "Hello"
    result = count_combinations(input_word)
    print(f"The number of different combinations for the word '{input_word}' is: {result}")

if __name__ == "__main__":
    main()



