import re 
def checkpattern(string):
    pattern1 = r'This is (\d) round of 12'
    pattern2 = r'This is (\d\d) round of 12'
    search_re1 = re.compile(pattern1)
    search_re2 = re.compile(pattern2)
    result1 = search_re1.search(string)
    if result1:
        print(result1.groups())
        round = result1.groups()[0]
        print("Round is ",round)
        return round
    result2 = search_re2.search(string)
    if result2:
        print(result2.groups())
        round = result2.groups()[0]
        print("Round is ",round)
        return round
    
    

def main():
    string = "Hello This is 01 round of 12"
    round = checkpattern(string)
    if round:
        round = int(round)
    

main()