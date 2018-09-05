


'''the user is asked to input certain types of words, then they are applied within a sentence and the snetence is returned to the user in the terminal'''



def getUserInput():
    storyList=[{"noun":'crab', "adverb":'moved', "adjective":'red'},
                       {"noun":'robin', "adverb":'flipped', "adjective":'blue'}]
    randOrNo=str(input("Pre-written story?: (y/n)")).lower()
    while randOrNo!='n' and randOrNo!='y':
        randOrNo=str(input("Pre-written story?: (y/n)")).lower()     
    if str(randOrNo).lower()=='n':
        noun=input("input a noun: ")
        adverb=input("input an adverb: ")
        adjective=input("input an adjective: ")
        wordDict={"noun":noun, "adverb":adverb, "adjective":adjective}
        return wordDict
    elif str(randOrNo).lower()=='y':
        listInd=input("which story?:(0-1) ")
        while listInd!='0' and listInd!='1':
            listInd=input("which story?:(0-1) ")
        return storyList[int(listInd)]
    
    
     
def checkInput(dictList):
    
    while len(dictList["noun"])==0:
        dictList["noun"]=input("input a noun: ")
        
    while len(str(dictList["adverb"]))==0:
        dictList["adverb"]=input("input an adverb: ")
        
    while len(str(dictList["adjective"]))==0:
        dictList["adjective"]=input("input an adjective: ")
        
    return dictList

def mad_libs():
    newDict = getUserInput()
    madlibs=checkInput(newDict)
    noun=madlibs["noun"]
    adverb=madlibs["adverb"]
    adjective=madlibs["adjective"]
    print ("{} {} {}".format(adjective,noun,adverb))
    

