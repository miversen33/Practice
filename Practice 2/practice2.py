def sort(stringToSort):
    brokenString = stringToSort.split(" ")
    reversedString = brokenString[::-1]
    #You cannot remove from an array you are currently iterating through. It kinda breaks stuff
    savedStringArray = []
    for s in reversedString:
        if s:
            savedStringArray.append(s)
    returnString = ' '.join(savedStringArray)
    return returnString