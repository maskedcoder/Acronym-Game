import random
import re

# This sets the width of the decorative lines
LINE_WIDTH = 48

def getLinesFromFile(filename):
    """
    Returns a list of lines from a file

    filename {string} - The name of a file

    returns {list} - The lines from the file
    """
    
    lines = []
    f = open(filename, 'r')

    for line in f:
        lines.append(line)
        
    f.close()
    return lines


def getData():
    """
    Grabs a list of acronyms from external files

    These files must be in the current working
    directory, and be named 801-words.txt and
    802-words.txt

    returns {list} The lines from the files
    """
    
    words1 = getLinesFromFile('./801-words.txt')
    words2 = getLinesFromFile('./802-words.txt')

    return [w for w in set(words1).union(words2)]


def test(data):
    """
    Test the user on an individual acronym

    data {string} - An acronym to test. There must
                    be just a space between the acronym
                    and its definition.

    returns {int} - The result of the test
                    1 means success
                    -1 means failure
                    0 means the user wishes to exit
    """
    
    parts = data.split(' ', 1)
    acronym = parts[0]
    answer = parts[1].strip()

    print()
    print('-' * LINE_WIDTH)
    print()
    guess = input(acronym+'\n')

    if guess == 'exit':
        return 0

    check = input('Are these the same?\n"'+guess+'"\n"'+answer+'"\n\n[y/n]:')

    if check and check[0].lower() == 'y':
        print('Congratulations! '+acronym+' means "'+answer+'"')
        return 1
    else:
        print('Wrong. '+acronym+' means "'+answer+'"')
        return -1


def main():
    """
    We have lift off, captain.

    This will gather the available acronyms from
    a file and then test the user on them until
    the user types 'exit'.

    Afterwards, it will display the user's score
    along with a list of missed acronyms.
    """
    
    data = getData()
    count = len(data)

    misses = []
    
    print('There are '+str(count)+' acronyms')
    
    score = 0
    questionCount = 0

    while True:
        t = random.choice(data)
        index = data.index(t)

        result = test(t)
        
        if result == 0:
            break
        else:
            score += result
            questionCount += 1
            
            # I'm tired of getting the duplicate questions
            del data[index]

            if result < 0:
                misses.append(t)

            if len(data) == 0:
                print('All done! ...You\'ve been doing this too long...')
                break
            
    print('-' * LINE_WIDTH)
    print('All done!')
    print('Your score was '+str(score)+' over '+str(questionCount)+' questions')
    print()
    print('Missed acronyms')
    print('-'*LINE_WIDTH)
    print()
    [print(x) for x in misses]


if __name__ == '__main__':
    main()
