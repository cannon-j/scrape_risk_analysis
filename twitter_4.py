import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import config
import json

query = ['Asset bubble','equity bubble','subprime','investment bubble','deflation','falling inflation','reduced inflation','falling prices','energy price','gasoline price','petrol price','bank failure','bank collapse','market collapse','market failure','bank bailout','critical infrastructure','infrastructure failure','fiscal crisis','financial crisis','underemployment','unemployment','Inflation','Storm','Flood','Extreme weather','Climate change','biodiversity','natural disaster','oil spill','environmental contamination','corruption','organized crime','war','state conflict','terrorism','terrorist','state collapse','civil crisis','coup','failed state','WMD','nuclear weapon','nuke','dirty bomb','failed urban planning','food crisis','starvation','refugee','refugees','riot','infectious','disease','epidemic','pandemic','drought','water shortage','internet collapse','cyber attack','cyber warfare','cyber terrorism','data fraud','identity theft','misuse of technology','manmade','layoffs','ebola','polio','influenza','zika']

data_file = 'data.txt'

risk_values = {"Asset_bubble_in_a_major_economy":0,"Deflation_in_a_major_economy":0,"Energy_price_shock_to_the_global_economy":0,"Failure_of_a_major_financial_mechanism_or_institution":0,"Failure_shortfall_of_critical_infrastructure":0,"Fiscal_crises_in_key_economies":0,"High_structural_unemployment_or_underemployment":0,"Unmanageable_inflation":0,"Extreme_weather_events_eg_floods_storms_etc":0,"Failure_of_climatechange_adaptation":0,"Major_biodiversity_loss_and_ecosystem_collapse_land_or_ocean":0,"Major_natural_catastrophes_eg_earthquake_tsunami_volcanic_eruption_geomagnetic_storms":0,"Manmade_environmental_catastrophes_eg_oil_spill_radioactive_contamination_etc":0,"Failure_of_national_governance_eg_corruption_illicit_trade_organized_crime_impunity_political_deadlock_etc":0,"Interstate_conflict_with_regional_consequences":0,"Largescale_terrorist_attacks":0,"State_collapse_or_crisis_eg_civil_conflict_military_coup_failed_states_etc":0,"Weapons_of_mass_destruction":0,"Failure_of_urban_planning":0,"Food_crises":0,"Largescale_involuntary_migration":0,"Profound_social_instability":0,"Rapid_and_massive_spread_of_infectious_diseases":0,"Water_crises":0,"Breakdown_of_critical_information_infrastructure_and_networks":0,"Largescale_cyber_attacks":0,"Massive_incident_of_data_fraud_theft":0,"Massive_and_widespread_misuse_of_technologies":0}

def query_check(tweet,risk_dict):
    if 'Asset' in tweet and 'bubble' in tweet or 'equity' in tweet and 'bubble' in tweet or 'subprime' in tweet or 'investment' in tweet and 'bubble' in tweet:
        risk_dict["Asset_bubble_in_a_major_economy"] += 1
        
    if 'deflation' in tweet or 'falling  inflation' in tweet or 'reduced  inflation' in tweet or 'falling prices' in tweet:
        risk_dict["Deflation_in_a_major_economy"] += 1
        
    if 'energy' in tweet and 'price' in tweet or 'gasoline' in tweet and 'price' in tweet or 'petrol' in tweet and 'price' in tweet:
        risk_dict["Energy_price_shock_to_the_global_economy"] += 1
        
    if 'bank' in tweet and 'failure' in tweet or 'bank' in tweet and 'collapse' in tweet or 'market' in tweet and  'collapse' in tweet or 'market' in tweet and 'failure' in tweet or 'bank' in tweet and 'bailout' in tweet:
        risk_dict["Failure_of_a_major_financial_mechanism_or_institution"] += 1
        
    if 'critical' in tweet and 'infrastructure' in tweet or 'infrastructure' in tweet and 'failure' in tweet:
        risk_dict["Failure_shortfall_of_critical_infrastructure"] += 1
        
    if 'fiscal' in tweet and  'crisis' in tweet or 'financial' in tweet and  'crisis' in tweet or 'market' in tweet and 'crash' in tweet:
        risk_dict["Fiscal_crises_in_key_economies"] += 1
        
    if 'underemployment' in tweet or 'unemployment' in tweet or 'layoffs' in tweet:
        risk_dict["High_structural_unemployment_or_underemployment"] += 1
        
    if 'inflation' in tweet:
        risk_dict["Unmanageable_inflation"] += 1
        
    if 'Storm' in tweet or 'Flood' in tweet or 'Extreme weather' in tweet:
        risk_dict["Extreme_weather_events_eg_floods_storms_etc"] += 1
        
    if 'Climate' in tweet and 'change' in tweet or 'global warming' in tweet:
        risk_dict["Failure_of_climatechange_adaptation"] += 1
        
    if 'biodiversity' in tweet:
        risk_dict["Major_biodiversity_loss_and_ecosystem_collapse_land_or_ocean"] += 1
        
    if 'natural disaster' in tweet or 'earthquake' in tweet or 'tsunami' in tweet or 'volcano' in tweet or 'hurricane' in tweet or 'wildfire' in tweet:
        risk_dict["Major_natural_catastrophes_eg_earthquake_tsunami_volcanic_eruption_geomagnetic_storms"] += 1
        
    if 'oil' in tweet and 'spill' in tweet or 'environmental' in tweet and 'contamination' in tweet or 'manmade' in tweet:
        risk_dict["Manmade_environmental_catastrophes_eg_oil_spill_radioactive_contamination_etc"] += 1
        
    if 'corruption' in tweet or 'organized' in tweet and 'crime' in tweet:
        risk_dict["Failure_of_national_governance_eg_corruption_illicit_trade_organized_crime_impunity_political_deadlock_etc"] += 1
        
    if 'war' in tweet or 'state' in tweet and 'conflict' in tweet:
        risk_dict["Interstate_conflict_with_regional_consequences"] += 1
        
    if 'terrorism' in tweet or 'terrorist' in tweet or 'isis' in tweet or 'isil' in tweet or 'hezbollah' in tweet or 'boko haram' in tweet:
        risk_dict["Largescale_terrorist_attacks"] += 1
        
    if 'state collapse' in tweet or 'civil crisis' in tweet or 'coup' in tweet or 'failed state' in tweet:
        risk_dict["State_collapse_or_crisis_eg_civil_conflict_military_coup_failed_states_etc"] += 1
        
    if 'WMD' in tweet or 'nuclear' in tweet and  'weapon' in tweet or 'nuke' in tweet or 'dirty bomb' in tweet:
        risk_dict["Weapons_of_mass_destruction"] += 1
        
    if 'failed' in tweet and 'urban' in tweet and 'planning' in tweet or 'fail' in tweet and 'urban' in tweet and 'plan' in tweet:
        risk_dict["Failure_of_urban_planning"] += 1
        
    if 'food' in tweet and 'crisis' in tweet or 'starvation' in tweet or 'food' in tweet and 'shortage' in tweet or 'malnutrition' in tweet:
        risk_dict["Food_crises"] += 1
        
    if 'refugee' in tweet or 'refugees' in tweet:
        risk_dict["Largescale_involuntary_migration"] += 1
        
    if 'riot' in tweet:
        risk_dict["Profound_social_instability"] += 1
        
    if 'infectious' in tweet or 'disease' in tweet or 'epidemic' in tweet or 'pandemic' in tweet or 'zika' in tweet or 'ebola' in tweet or 'influenza' in tweet or 'polio' in tweet or 'measles' in tweet :
        risk_dict["Rapid_and_massive_spread_of_infectious_diseases"] += 1
        
    if 'drought' in tweet or 'water' in tweet and 'shortage' in tweet or 'water' in tweet and 'crisis' in tweet:
        risk_dict["Water_crises"] += 1
        
    if 'internet' in tweet and 'collapse' or 'internet' in tweet and 'failure' in tweet or '':
        risk_dict["Breakdown_of_critical_information_infrastructure_and_networks"] += 1
        
    if 'cyberattack' in tweet or 'cyber warfare' in tweet or 'cyber terrorism' in tweet:
        risk_dict["Largescale_cyber_attacks"] += 1
        
    if 'data fraud' in tweet or 'identity theft' in tweet:
        risk_dict["Massive_incident_of_data_fraud_theft"] += 1
        
    if 'misuse of technology' in tweet:
        risk_dict["Massive_and_widespread_misuse_of_technologies"] += 1
        
    else:
        return risk_dict
            
    return risk_dict

class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, data_file, query):
        self.outfile = data_file

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                parsed_json = json.loads(str(data))
                f.write(parsed_json['text'].encode('utf-8').lower())
                query_check(parsed_json['text'].encode('utf-8').lower(),risk_values)
                print ''
                for item in risk_values:
                    print item, risk_values[item]
                print ''
                return True
            
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