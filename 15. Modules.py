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


# 2. Create a module that handles degree and radian as inputs for finding all six trigonometric ratios.
import m
class T:
    def __init__(s, a, u='degrees'):
        s.a = a
        s.u = u.lower()
        if s.u == 'degrees':
            s.ar = m.radians(a)
        elif s.u == 'radians':
            s.ar = a
        else:
            raise ValueError("Invalid unit. Use 'degrees' or 'radians'.")

    def _cr(s):
        sv = m.sin(s.ar)
        cv = m.cos(s.ar)
        tv = m.tan(s.ar)
        cv = 1 / sv if sv != 0 else float('inf')
        sev = 1 / cv if cv != 0 else float('inf')
        ctv = 1 / tv if tv != 0 else float('inf')
        return {
            'sin': sv,
            'cos': cv,
            'tan': tv,
            'csc': cv,
            'sec': sev,
            'cot': ctv
        }
    def gtr(s):
        return s._cr()
ad = 45
calcd = T(ad, u='degrees')
rd = calcd.gtr()
ar = m.radians(ad)
calcr = T(ar, u='radians')
rr = calcr.gtr()
print(f"Trigonometric Ratios for {ad} degrees: {rd}")
print(f"Trigonometric Ratios for {ar} radians: {rr}")

# 4. Write a Python program to change the current working directory to the downloads folder and change the mode of the directory.
import os

downloads_path = "/path/to/your/downloads/folder"

try: os.chdir(downloads_path); os.chmod(downloads_path, 0o755); print(f"Changed directory to: {os.getcwd()} and mode to: {oct(0o755)}")
except (FileNotFoundError, PermissionError) as e: print(f"An error occurred: {e}")

