# Function converting a search query term into a boolean containment statement
def termToBool(inStr, tweet):
    splitStr = inStr.split(" ")
    if len(splitStr) == 2:
        return splitStr[0] in tweet and splitStr[1] in tweet
    elif len(splitStr) == 1:
        return splitStr[0] in tweet
    else:
        return "Error in converting query term into boolean check"

# Grouping function to convert a group of terms into a check
def termsToChecks(checkList, groupName, tweet, initDict):
    allCheck = reduce(lambda acc, t: acc or termToBool(t, tweet), checkList, False)
    if allCheck:
        if groupName in initDict.keys():
            initDict[groupName] += 1
        else:
            initDict[groupName] = 1
    return initDict

# query = ['asset bubble', 'market bubble', 'financial bubble', 'bubble economy', 'speculative bubble', 'bubble property', 'economic deflation', 'market deflation', 'world deflation', 'money deflation', 'wage deflation', 'global deflation', 'energy price', 'gasoline price', 'petrol price', 'oil collapse', 'oil price', 'plummeting oil', 'market collapse', 'stock crash', 'market recession', 'bank collapse', 'bank failure', 'bank closing', 'infrasture failure', 'road failure', 'critical infrastrure', 'bridge collapse', 'broken infrastructure', 'power outage', 'market failure', 'financial crisis', 'fiscal crisis', 'financial panic', 'economic collapse', 'fiscal collapse', 'extreme weather', 'weather disaster', 'weather  chaos', 'dangerous weather', 'terrible weather', 'severe weather', 'climate change', 'global warming', 'climate science', 'climate breaking', 'climate analysis', 'climate failure', 'oil spill', 'radioactive contamination', 'contamination water', 'water poison', 'radioactive waste', 'radioactive leak', 'organized crime', 'political corruption', 'political impunity', 'political deadlock', 'government failure', 'illegal government', 'region conflict', 'syrian war', 'global war', 'state conflict', 'iraq invasion', 'troop invasion', 'terrorist attack', 'boko haram', 'terror attack', 'civil war', 'fail state', 'state collapse', 'nation collapse', 'military takeover', 'civil failure', 'mass destruction', 'nuclear bomb', 'dirty bomb', 'biological warfare', 'chemical warfare', 'nuclear warfare', 'fail urban', 'urban collapse', 'urban failure', 'slum urban', 'urban sprawl', 'city sprawl', 'food crisis', 'food shortage', 'grain crisis', 'food shortage', 'food emergency', 'mass hunger', 'refugee crisis', 'refugee problem', 'immigration crisis', 'mass refugee', 'migrant crisis', 'syria refugee', 'social instability', 'social breakdown', 'civil unrest', 'civil instability', 'social unrest', 'civil breakdown', 'water crisis', 'water shortage', 'water poison', 'water fail', 'water emergency', 'water emergency', 'internet breakdown', 'cyber attack', 'cyber war', 'cyber terror', 'cyber crime', 'data attack', 'cyber operations', 'data fraud', 'data breach', 'data theft', 'data leak', 'data crime', 'data attack', 'danger technology', 'misuse technology', 'abuse technology', 'dangerous technology', 'danger genome', 'danger biology', 'recession', 'unemployment', 'underemployment', 'layoffs', 'inflation', 'flood', 'tornado', 'hurricane', 'biodiversity', 'earthquake', 'volcano', 'tsunami', 'terrorism', 'terrorist', 'al quaeda', 'coup', 'WMD', 'nuke', 'ebola', 'zika', 'polio', 'pandemic', 'dengue', 'drought', 'cyberattack', 'ddos', 'refugee']


# def main():
#     print termsToChecks(query[:5], "hi hi", "financial bubble", {})

# main()