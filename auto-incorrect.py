# Author: lazho
# This program will take a string or a file's contents as input and make spelling errors. It is by no way polished and is prone to errors due to lack of exception handling. I made this for fun, don't do a whole code review on it.

import sys, random

# usage:
# argument  1: -s flag means input is string, -f means filename
#           2: string, could be filename if specified -f
#           3: (optional) non-negative int to specify how many times
#              in 100 that a word should have a spelling mistake added
usage = "\
        Usage: \
        python auto-incorrect.py [-s|-f] [string|filename] [percentchance]"
chance = 20

# If ID-10-T user, tell them check usage
if len(sys.argv) < 3:
    print(usage)
    sys.exit(-1)
# If specified, set chance of mistakes
if len(sys.argv) == 4:
    chance = int(sys.argv[3])

# Do we open a file?
openFile = False
if sys.argv[1] == "-f":
    openFile = True
elif sys.argv[1] != "-s":
    print(usage)
    sys.exit(-1)

inputStr = sys.argv[2]

if openFile:
    inputStr = open(inputStr, "r").read()

inputStr = inputStr.split()

# Probably shouldn't hardcode this in and instead read from a file,
# but oh well.
specialCases = {
    "your": "you're",
    "you're": "your",
    "its": "it's",
    "it's": "its",
    "their": "they're",
    "they're": "there",
    "there": "their",
    "lose": "loose",
    "loose": "lose",
    "effect": "affect",
    "affect": "effect",
    "definitely": "definately",
    "weather": "whether",
    "whether": "weather",
    "then": "than",
    "an": "a",
    "the": "teh",
    "like": "liek"
}

outputStr = ""

# Given string s and index i, it swaps s[i] and s[i+1] and returns
def swap(s, i):
    si = s[i]
    sj = s[i+1]
    s = s[:i] + sj + si + s[i+2:]
    return s

# Given string s and index i, it omits the i-th character.
def omit(s, i):
    return s[:i]+s[i+1:]

for w in inputStr:
    # Idiots don't use shift or capslock
    w = w.lower()
    # If jackpot
    if random.randrange(100) < chance:
        # Special cases get priority
        if w in specialCases:
            outputStr = outputStr + specialCases[w]
        # Words less than 3 letters can't stand omit or swap
        elif len(w) >= 3:
            # Decide a random index
            i = random.randrange(len(w)-1)
            # 50/50 chance between omission and swap
            if random.randrange(2) == 1:
                outputStr = outputStr + swap(w, i)
            else:
                outputStr = outputStr + omit(w, i)
        # Leave short words be
        else:
            outputStr = outputStr + w
    else:
        outputStr = outputStr + w
    outputStr = outputStr + " "

print(outputStr)
