

def main():
    userInput = input("Enter the topics you're interested in (just separate topics by space): ").lower()
    spacesep = split_input(userInput)
    return spacesep 
    

def split_input(userInput):
    spacesepvalues = None

    if (userInput.find(',') == -1):
        spacesepvalues = userInput.split(' ')
        spacesepvalues = [x.strip() for x in spacesepvalues]
        return spacesepvalues
    else:
        spacesepvalues = userInput.split(',')
        spacesepvalues = [x.strip() for x in spacesepvalues]
        return spacesepvalues


if __name__ == '__main__':
    main()