import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import config
import json

query = ["asset", "bubble", "market", "bubble", "financial", "bubble", "bubble", "economy", "speculative", "bubble", "bubble", "property", "economic", "deflation", "market", "deflation", "world", "deflation", "money", "deflation", "wage", "deflation", "global", "deflation", "energy", "price", "gasoline", "price", "petrol", "price", "oil", "collapse", "oil", "price", "plummeting", "oil", "market", "collapse", "stock", "crash", "market", "recession", "bank", "collapse", "bank", "failure", "bank", "closing", "infrasture", "failure", "road", "failure", "critical", "infrastrure", "bridge", "collapse", "broken", "infrastructure", "power", "outage", "market", "failure", "financial", "crisis", "fiscal", "crisis", "financial", "panic", "economic", "collapse", "fiscal", "collapse", "recession", "unemployment", "underemployment", "layoffs", "inflation", "extreme", "weather", "weather", "disaster", "weather", "chaos", "dangerous", "weather", "terrible", "weather", "severe", "weather", "flood", "storm", "tornado", "climate", "change", "global", "warming", "climate", "science", "climate", "breaking", "climate", "analysis", "climate", "failure", "biodiversity", "earthquake", "volcano", "tsumani", "oil", "spill", "radioactive", "contamination", "contamination", "water", "water", "poison", "radioactive", "waste", "radioactive", "leak", "organized", "crime", "political", "corruption", "political", "impunity", "political", "deadlock", "government", "failure", "illegal", "government", "region", "conflict", "syrian", "war", "global", "war", "state", "conflict", "iraq", "invasion", "troop", "invasion", "terrorist", "attack", "boko", "haram", "terror", "attack", "al queda", "terrorism", "terrorist", "civil", "war", "fail", "state", "state", "collapse", "nation", "collapse", "military", "takeover", "civil", "failure", "coup", "mass", "destruction", "nuclear", "bomb", "dirty", "bomb", "biological", "warfare", "chemical", "warfare", "nuclear", "warfare", "WMD", "nuke", "fail", "urban", "urban", "collapse", "urban", "failure", "slum", "urban", "urban", "sprawl", "city", "sprawl", "food", "crisis", "food", "shortage", "grain", "crisis", "food", "shortage", "food", "emergency", "mass", "hunger", "foodcrisis", "starvation", "malnutrition", "refugee", "crisis", "refugee", "problem", "immigration", "crisis", "mass", "refugee", "migrant", "crisis", "syria", "refugee", "social", "instability", "social", "breakdown", "civil", "unrest", "civil", "instability", "social", "unrest", "civil", "breakdown", "ebola", "polio", "zika", "pandemic", "water", "crisis", "water", "shortage", "water", "poison", "water", "fail", "water", "emergency", "water", "emergency", "drought", "internet", "breakdown", "cyber", "attack", "cyber", "war", "cyber", "terror", "cyber", "crime", "data", "attack", "cyber", "operations", "cyberattack", "ddos", "data", "fraud", "data", "breach", "data", "theft", "data", "leak", "data", "crime", "data", "attack", "danger", "technology", "misuse", "technology", "abuse", "technology", "dangerous", "technology", "danger", "genome", "danger", "biology"]

data_file = 'data.txt'

risk_values = {"Asset_bubble_in_a_major_economy":0,"Deflation_in_a_major_economy":0,"Energy_price_shock_to_the_global_economy":0,"Failure_of_a_major_financial_mechanism_or_institution":0,"Failure_shortfall_of_critical_infrastructure":0,"Fiscal_crises_in_key_economies":0,"High_structural_unemployment_or_underemployment":0,"Unmanageable_inflation":0,"Extreme_weather_events_eg_floods_storms_etc":0,"Failure_of_climatechange_adaptation":0,"Major_biodiversity_loss_and_ecosystem_collapse_land_or_ocean":0,"Major_natural_catastrophes_eg_earthquake_tsunami_volcanic_eruption_geomagnetic_storms":0,"Manmade_environmental_catastrophes_eg_oil_spill_radioactive_contamination_etc":0,"Failure_of_national_governance_eg_corruption_illicit_trade_organized_crime_impunity_political_deadlock_etc":0,"Interstate_conflict_with_regional_consequences":0,"Largescale_terrorist_attacks":0,"State_collapse_or_crisis_eg_civil_conflict_military_coup_failed_states_etc":0,"Weapons_of_mass_destruction":0,"Failure_of_urban_planning":0,"Food_crises":0,"Largescale_involuntary_migration":0,"Profound_social_instability":0,"Rapid_and_massive_spread_of_infectious_diseases":0,"Water_crises":0,"Breakdown_of_critical_information_infrastructure_and_networks":0,"Largescale_cyber_attacks":0,"Massive_incident_of_data_fraud_theft":0,"Massive_and_widespread_misuse_of_technologies":0}

def query_check(tweet,risk_dict):
    """
    if "asset" in tweet and "bubble" in tweet or "market" in tweet and "bubble" in tweet or "financial" in tweet and "bubble" in tweet or "bubble" in tweet and "economy" in tweet or "speculative" in tweet and "bubble" in tweet or "bubble" in tweet and "property" in tweet:
        risk_dict["Asset_bubble_in_a_major_economy"] += 1

                
    if "economic" in tweet and "deflation" in tweet or "market" in tweet and "deflation" in tweet or "world" in tweet and "deflation" in tweet or "money" in tweet and "deflation" in tweet or "wage" in tweet and "deflation" in tweet or "global" in tweet and "deflation" in tweet:
        risk_dict["Deflation_in_a_major_economy"] += 1
        
    if "energy" in tweet and "price" in tweet or "gasoline" in tweet and "price" in tweet or "petrol" in tweet and "price" in tweet or "oil" in tweet and "collapse" in tweet or "oil" in tweet and "price" in tweet or "plummeting" in tweet and "oil" in tweet:
        risk_dict["Energy_price_shock_to_the_global_economy"] += 1
        
    if "market" in tweet and "collapse" in tweet or "stock" in tweet and "crash" in tweet or "market" in tweet and "recession" in tweet or "bank" in tweet and "collapse" in tweet or "bank" in tweet and "failure" in tweet or "bank" in tweet and "closing" in tweet:
        risk_dict["Failure_of_a_major_financial_mechanism_or_institution"] += 1
        
    if "infrasture" in tweet and "failure" in tweet or "road" in tweet and "failure" in tweet or "critical" in tweet and "infrastrure" in tweet or "bridge" in tweet and "collapse" in tweet or "broken" in tweet and "infrastructure" in tweet or "power" in tweet and "outage" in tweet:
        risk_dict["Failure_shortfall_of_critical_infrastructure"] += 1
        
    if "market" in tweet and "failure" in tweet or "financial" in tweet and "crisis" in tweet or "fiscal" in tweet and "crisis" in tweet or "financial" in tweet and "panic" in tweet or "economic" in tweet and "collapse" in tweet or "fiscal" in tweet and "collapse" in tweet or "recession" in tweet:
        risk_dict["Fiscal_crises_in_key_economies"] += 1
        
    if "unemployment" in tweet or "underemployment" in tweet or "layoffs" in tweet:
        risk_dict["High_structural_unemployment_or_underemployment"] += 1
        
    if "inflation" in tweet:
        risk_dict["Unmanageable_inflation"] += 1
        
    if "extreme" in tweet and "weather" in tweet or "weather" in tweet and "disaster" in tweet or "weather " in tweet and "chaos" in tweet or "dangerous" in tweet and "weather" in tweet or "terrible" in tweet and "weather" in tweet or "severe" in tweet and "weather" in tweet or "flood" in tweet or "storm" in tweet or "tornado" in tweet or "hurricane" in tweet:
        risk_dict["Extreme_weather_events_eg_floods_storms_etc"] += 1
        
    if "climate" in tweet and "change" in tweet or "global" in tweet and "warming" in tweet or "climate" in tweet and "science" in tweet or "climate" in tweet and "breaking" in tweet or "climate" in tweet and "analysis" in tweet or "climate" in tweet and "failure" in tweet:
        risk_dict["Failure_of_climatechange_adaptation"] += 1
        
    if "biodiversity" in tweet:
        risk_dict["Major_biodiversity_loss_and_ecosystem_collapse_land_or_ocean"] += 1
        
    if "earthquake" in tweet or "volcano" in tweet or "tsunami" in tweet:
        risk_dict["Major_natural_catastrophes_eg_earthquake_tsunami_volcanic_eruption_geomagnetic_storms"] += 1
        
    if "oil" in tweet and "spill" in tweet or "radioactive" in tweet and "contamination" in tweet or "contamination" in tweet and "water" in tweet or "water" in tweet and "poison" in tweet or "radioactive" in tweet and "waste" in tweet or "radioactive" in tweet and "leak" in tweet:
        risk_dict["Manmade_environmental_catastrophes_eg_oil_spill_radioactive_contamination_etc"] += 1
        
    if "organized" in tweet and "crime" in tweet or "political" in tweet and "corruption" in tweet or "political" in tweet and "impunity" in tweet or "political" in tweet and "deadlock" in tweet or "government" in tweet and "failure" in tweet or "illegal" in tweet and "government" in tweet:
        risk_dict["Failure_of_national_governance_eg_corruption_illicit_trade_organized_crime_impunity_political_deadlock_etc"] += 1
        
    if "region" in tweet and "conflict" in tweet or "syrian" in tweet and "war" in tweet or "global" in tweet and "war" in tweet or "state" in tweet and "conflict" in tweet or "iraq" in tweet and "invasion" in tweet or "troop" in tweet and "invasion" in tweet:
        risk_dict["Interstate_conflict_with_regional_consequences"] += 1
        
    if "terrorist" in tweet and "attack" in tweet or "boko" in tweet and "haram" in tweet or "terror" in tweet and "attack" in tweet or "al queda" in tweet or "terrorism" in tweet or "terrorist" in tweet:
        risk_dict["Largescale_terrorist_attacks"] += 1
        
    if "civil" in tweet and "war" in tweet or "fail" in tweet and "state" in tweet or "state" in tweet and "collapse" in tweet or "nation" in tweet and "collapse" in tweet or "military" in tweet and "takeover" in tweet or "civil" in tweet and "failure" in tweet or "coup" in tweet:
        risk_dict["State_collapse_or_crisis_eg_civil_conflict_military_coup_failed_states_etc"] += 1
        
    if "mass" in tweet and "destruction" in tweet or "nuclear" in tweet and "bomb" in tweet or "dirty" in tweet and "bomb" in tweet or "biological" in tweet and "warfare" in tweet or "chemical" in tweet and "warfare" in tweet or "nuclear" in tweet and "warfare" in tweet or "WMD" in tweet or "nuke" in tweet:
        risk_dict["Weapons_of_mass_destruction"] += 1
        
    if "fail" in tweet and "urban" in tweet or "urban" in tweet and "collapse" in tweet or "urban" in tweet and "failure" in tweet or "slum" in tweet and "urban" in tweet or "urban" in tweet and "sprawl" in tweet or "city" in tweet and "sprawl" in tweet:
        risk_dict["Failure_of_urban_planning"] += 1
        
    if "food" in tweet and "crisis" in tweet or "food" in tweet and "shortage" in tweet or "grain" in tweet and "crisis" in tweet or "food" in tweet and "shortage" in tweet or "food" in tweet and "emergency" in tweet or "mass" in tweet and "hunger" in tweet or "foodcrisis" in tweet or "starvation" in tweet or "malnutrition" in tweet:
        risk_dict["Food_crises"] += 1
        
    if "refugee" in tweet and "crisis" in tweet or "refugee" in tweet and "problem" in tweet or "immigration" in tweet and "crisis" in tweet or "mass" in tweet and "refugee" in tweet or "migrant" in tweet and "crisis" in tweet or "syria" in tweet and "refugee" in tweet:
        risk_dict["Largescale_involuntary_migration"] += 1
        
    if "social" in tweet and "instability" in tweet or "social" in tweet and "breakdown" in tweet or "civil" in tweet and "unrest" in tweet or "civil" in tweet and "instability" in tweet or "social" in tweet and "unrest" in tweet or "civil" in tweet and "breakdown" in tweet:
        risk_dict["Profound_social_instability"] += 1
        
    if "ebola" in tweet or "zika" in tweet or "polio" in tweet or "smallpox" in tweet or "pandemic" in tweet or "dengue" in tweet:
        risk_dict["Rapid_and_massive_spread_of_infectious_diseases"] += 1
        
    if "water" in tweet and "crisis" in tweet or "water" in tweet and "shortage" in tweet or "water" in tweet and "poison" in tweet or "water" in tweet and "fail" in tweet or "water" in tweet and "emergency" in tweet or "water" in tweet and "emergency" in tweet or "drought" in tweet:
        risk_dict["Water_crises"] += 1
        
    if "internet" in tweet and "breakdown" in tweet:
        risk_dict["Breakdown_of_critical_information_infrastructure_and_networks"] += 1
        
    if "cyber" in tweet and "attack" in tweet or "cyber" in tweet and "war" in tweet or "cyber" in tweet and "terror" in tweet or "cyber" in tweet and "crime" in tweet or "data" in tweet and "attack" in tweet or "cyber" in tweet and "operations" in tweet or "ddos" in tweet or "cyberattack" in tweet:
        risk_dict["Largescale_cyber_attacks"] += 1
        
    if "data" in tweet and "fraud" in tweet or "data" in tweet and "breach" in tweet or "data" in tweet and "theft" in tweet or "data" in tweet and "leak" in tweet or "data" in tweet and "crime" in tweet or "data" in tweet and "attack" in tweet:
        risk_dict["Massive_incident_of_data_fraud_theft"] += 1
        
    if "danger" in tweet and "technology" in tweet or "misuse" in tweet and "technology" in tweet or "abuse" in tweet and "technology" in tweet or "dangerous" in tweet and "technology" in tweet or "danger" in tweet and "genome" in tweet or "danger" in tweet and "biology" in tweet:
        risk_dict["Massive_and_widespread_misuse_of_technologies"] += 1
        
    else:
        return risk_dict
    """    
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