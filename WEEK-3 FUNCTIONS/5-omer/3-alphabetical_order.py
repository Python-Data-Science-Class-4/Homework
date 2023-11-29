'''
@description
Write a function that takes an input of different words with hyphen (-) in between them and then:
sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words.

Example:
Input >>> green-red-yellow-black-white
Output >>> black-green-red-white-yellow
'''
#take a string vlaue 
def getStringValueByUser():
    stop = ''
    resultValue=''
    #take a first input
    resultValue=input('please write a string value : ')

    #take new inputs as much as writing h/H
    while stop.lower()!='h':
        #create result value with new inputs, insert '-' between string value
        resultValue = f"{resultValue}-{input('please write a string value : ')}"
        stop = input('type a h/H to exit : ')
    return resultValue

def orderAlphabeticalStringValue(value):
    #create a list with parameter value
    list=value.split("-")
    #alphabetical order
    list.sort()
    #create result ordered value with list elements, insert '-' between string value
    resultOrder=list[0]
    for i in list[1:]:
        resultOrder = f"{resultOrder}-{i}"
    return resultOrder

print(orderAlphabeticalStringValue(getStringValueByUser()))