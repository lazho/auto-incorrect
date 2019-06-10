import auto_incorrect

string =  'auto-incorrect.py -s 95'.split(' ')
string.insert(2, '"this is a test message. The point of this is to scramble it"')

result = auto_incorrect.auto_incorrect(string)
print(result)
