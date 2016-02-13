# Written by John Cannon for finding Tweets concerning "risks" as determined
# by "The Global Risks Report 2015" (from World Economic Forum).

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import config
import json
import csv

risk_values = {"Asset_bubble_in_a_major_economy":0,"Deflation_in_a_major_economy":0,"Energy_price_shock_to_the_global_economy":0,"Failure_of_a_major_financial_mechanism_or_institution":0,"Failure_shortfall_of_critical_infrastructure":0,"Fiscal_crises_in_key_economies":0,"High_structural_unemployment_or_underemployment":0,"Unmanageable_inflation":0,"Extreme_weather_events_eg_floods_storms_etc":0,"Failure_of_climatechange_adaptation":0,"Major_biodiversity_loss_and_ecosystem_collapse_land_or_ocean":0,"Major_natural_catastrophes_eg_earthquake_tsunami_volcanic_eruption_geomagnetic_storms":0,"Manmade_environmental_catastrophes_eg_oil_spill_radioactive_contamination_etc":0,"Failure_of_national_governance_eg_corruption_illicit_trade_organized_crime_impunity_political_deadlock_etc":0,"Interstate_conflict_with_regional_consequences":0,"Largescale_terrorist_attacks":0,"State_collapse_or_crisis_eg_civil_conflict_military_coup_failed_states_etc":0,"Weapons_of_mass_destruction":0,"Failure_of_urban_planning":0,"Food_crises":0,"Largescale_involuntary_migration":0,"Profound_social_instability":0,"Rapid_and_massive_spread_of_infectious_diseases":0,"Water_crises":0,"Breakdown_of_critical_information_infrastructure_and_networks":0,"Largescale_cyber_attacks":0,"Massive_incident_of_data_fraud_theft":0,"Massive_and_widespread_misuse_of_technologies":0}

query = ['asset bubble','market bubble','financial bubble','bubble economy','speculative bubble','bubble property','economic deflation','market deflation','world deflation','money deflation','wage deflation','global deflation','energy price','gasoline price','petrol price','oil collapse','oil price','plummeting oil','market collapse','stock crash','market recession','bank collapse','bank failure','bank closing','infrasture failure','road failure','critical infrastrure','bridge collapse','broken infrastructure','power outage','market failure','financial crisis','fiscal crisis','financial panic','economic collapse','fiscal collapse','unemployment','underemployment','layoffs','mass firing','inflation','extreme weather','weather disaster','weather  chaos','weather danger','weather terrible','severe weather','flood','tornado','hurricane','climate change','global warming','climate science','climate breaking','climate analysis','climate failure','biodiversity','earthquake','volcano','tsunami','oil spill','radioactive contamination','radioactive waste','radioactive leak','organized crime','political corruption','political impunity','political deadlock','government failure','illegal government','airstrike','region conflict','syrian war','global war','state conflict','iraq invasion','troop invasion','terrorism','terrorist','qaeda','terrorist attack','boko haram','terror attack','coup','civil war','fail state','state collapse','nation collapse','military takeover','civil failure','mass destruction','nuclear bomb','dirty bomb','biological warfare','chemical warfare','nuclear warfare','fail urban','urban collapse','urban failure','slum urban','urban sprawl','city sprawl','food crisis','food shortage','grain crisis','food shortage','food emergency','mass hunger','refugee crisis','refugee problem','immigration crisis','mass refugee','migrant crisis','syria refugee','social instability','social breakdown','civil unrest','civil instability','social unrest','civil breakdown','dengue','zika','ebola','influenza','polio','cholera','malaria','hiv','measles','water crisis','water shortage','water poison','water fail','water emergency','internet breakdown','cyber attack','cyber war','cyber terror','cyber crime','data attack','cyber operations','ddos','cyberattack','data fraud','data breach','data theft','data leak','data crime','data attack','danger technology','misuse technology','abuse technology','dangerous technology','danger genome','danger biology']

data_file = 'data.txt'

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
            print (tweet, 'dictionary', groupName)
            print ('')
            initDict[groupName] += 1
        else:
            initDict[groupName] = 1
    return initDict

def query_check(tweet,risk_dict):

    risk_dict = termsToChecks(query[0:6], "Asset_bubble_in_a_major_economy", tweet, risk_dict)
    risk_dict = termsToChecks(query[6:12], "Deflation_in_a_major_economy", tweet, risk_dict)
    risk_dict = termsToChecks(query[12:18], "Energy_price_shock_to_the_global_economy", tweet, risk_dict)
    risk_dict = termsToChecks(query[18:24], "Failure_of_a_major_financial_mechanism_or_institution", tweet, risk_dict)
    risk_dict = termsToChecks(query[24:30], "Failure_shortfall_of_critical_infrastructure", tweet, risk_dict)
    risk_dict = termsToChecks(query[30:36], "Fiscal_crises_in_key_economies", tweet, risk_dict)
    risk_dict = termsToChecks(query[36:40], "High_structural_unemployment_or_underemployment", tweet, risk_dict)
    risk_dict = termsToChecks(query[40:41], "Unmanageable_inflation", tweet, risk_dict)
    #risk_dict = termsToChecks(query[41:50], "Extreme_weather_events_eg_floods_storms_etc", tweet, risk_dict)
    risk_dict = termsToChecks(query[50:56], "Failure_of_climatechange_adaptation", tweet, risk_dict)
    risk_dict = termsToChecks(query[56:57], "Major_biodiversity_loss_and_ecosystem_collapse_land_or_ocean", tweet, risk_dict)
    risk_dict = termsToChecks(query[57:60], "Major_natural_catastrophes_eg_earthquake_tsunami_volcanic_eruption_geomagnetic_storms", tweet, risk_dict)
    risk_dict = termsToChecks(query[60:64], "Manmade_environmental_catastrophes_eg_oil_spill_radioactive_contamination_etc", tweet, risk_dict)
    risk_dict = termsToChecks(query[64:70], "Failure_of_national_governance_eg_corruption_illicit_trade_organized_crime_impunity_political_deadlock_etc", tweet, risk_dict)
    risk_dict = termsToChecks(query[70:77], "Interstate_conflict_with_regional_consequences", tweet, risk_dict)
    risk_dict = termsToChecks(query[77:83], "Largescale_terrorist_attacks", tweet, risk_dict)
    risk_dict = termsToChecks(query[83:90], "State_collapse_or_crisis_eg_civil_conflict_military_coup_failed_states_etc", tweet, risk_dict)
    risk_dict = termsToChecks(query[90:96], "Weapons_of_mass_destruction", tweet, risk_dict)
    risk_dict = termsToChecks(query[96:102], "Failure_of_urban_planning", tweet, risk_dict)
    risk_dict = termsToChecks(query[102:108], "Food_crises", tweet, risk_dict)
    risk_dict = termsToChecks(query[108:114], "Largescale_involuntary_migration", tweet, risk_dict)
    risk_dict = termsToChecks(query[114:120], "Profound_social_instability", tweet, risk_dict)
    risk_dict = termsToChecks(query[120:129], "Rapid_and_massive_spread_of_infectious_diseases", tweet, risk_dict)
    risk_dict = termsToChecks(query[129:134], "Water_crises", tweet, risk_dict)
    risk_dict = termsToChecks(query[134:135], "Breakdown_of_critical_information_infrastructure_and_networks", tweet, risk_dict)
    risk_dict = termsToChecks(query[135:143], "Largescale_cyber_attacks", tweet, risk_dict)
    risk_dict = termsToChecks(query[143:149], "Massive_incident_of_data_fraud_theft", tweet, risk_dict)
    risk_dict = termsToChecks(query[149:], "Massive_and_widespread_misuse_of_technologies", tweet, risk_dict)

    return risk_dict


class MyListener(StreamListener):
    
    """Custom StreamListener for streaming data."""

    def __init__(self, data_file, query):
        self.outfile = data_file

    def on_data(self, data):
        try:
            with open('data.csv', 'a') as csvfile:
                parsed_json = json.loads(str(data))
                
                rowwriter = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_NONE, quotechar='')
                
                if parsed_json['lang'] == 'en':
                    text_to_write = str(parsed_json['text'].encode('utf-8').lower().replace('#','').replace(':','').replace('\n','').replace('|',''))

                    print text_to_write
                    #rowwriter.writerow([text_to_write,str(parsed_json['place'])])

                    a = query_check(parsed_json['text'].encode('utf-8').lower(),risk_values)

                    #print parsed_json['place']
                    for item in risk_values:
                        print item, risk_values[item]
                    print ''

                    return True
                
                else:
                    return True
                
            """
            with open(self.outfile, 'a') as f:
                parsed_json = json.loads(str(data))
                f.write(parsed_json['text'].encode('utf-8').lower())
                query_check(parsed_json['text'].encode('utf-8').lower(),risk_values)
                #print parsed_json['place']
                for item in risk_values:
                    print item, risk_values[item]
                print ''
                return True
            """
            
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
            
        return True
    
if __name__ == '__main__':
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)

    twitter_stream = Stream(auth, MyListener(data_file, query))
    twitter_stream.filter(track=query)