def isSubsetList(subsetList:list, list:list):
    return set(subsetList).issubset(set(list))

def getSubsetDict(dict:dict, subsetDict:dict):
    return {x:dict[x] for x in subsetDict}