

def main(userInput):
    spacesep = split_input(userInput)
    return spacesep 
    

def split_input(userInput):
    spacesepvalues = None
    spacesepvalues = userInput.split(',')
    spacesepvalues = [x.strip().lower() for x in spacesepvalues]
    return spacesepvalues


