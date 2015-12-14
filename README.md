# auto-incorrect
Introducing auto-incorrect: a python script that makes all characters lowercase and adds spelling mistakes randomly throughout a given text. 0% bug free! (No pesticides used)

##Usage
`python auto-incorrect.py [-s|-f] [string|filename] [percentChance]`

###Arguments
*	Flag: `-s` means input is normal string, `-f` means it's a filename
*	string: either text or a filename
*	percentChance: non negative number that specifies percentage of words you'd like to put a mistake in.

###Example

`python auto-incorrect.py -s "The typo train goes choo choo" 10`

might return:

`the typo train goes coho choo`

`python auto-incorrect.py -s "The typo train goes choo choo" 100`

probably returns something like:

`teh tpo trian gos coo coo`

If you put this sentence into the file `choo.txt` and called:

`python auto-incorrect.py -f choo.txt 10`

it will also probably return something like

`the typo trani gose choo choo`

##FAQ

###Does this work?
Kinda?
