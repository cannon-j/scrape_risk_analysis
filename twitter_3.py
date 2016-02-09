import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import config
import json

query = ['Asset bubble','equity bubble','subprime','investment bubble','deflation','falling inflation','reduced inflation','falling prices','energy price','gasoline price','petrol price','bank failure','bank collapse','market collapse','market failure','bank bailout','critical infrastructure','infrastructure failure','fiscal crisis','financial crisis','underemployment','unemployment','Inflation','Storm','Flood','Extreme weather','Climate change','biodiversity','natural disaster','oil spill','environmental contamination','corruption','organized crime','war','state conflict','terrorism','terrorist','state collapse','civil crisis','coup','failed state','WMD','nuclear weapon','nuke','dirty bomb','failed urban planning','food crisis','starvation','refugee','refugees','riot','infectious','disease','epidemic','pandemic','drought','water shortage','internet collapse','cyber attack','cyber warfare','cyber terrorism','data fraud','identity theft','misuse of technology']
data_file = 'data.txt'

def query_check(tweet):
    Asset_bubble_in_a_major_economy = 0
    Deflation_in_a_major_economy = 0
    Energy_price_shock_to_the_global_economy = 0
    Failure_of_a_major_financial_mechanism_or_institution = 0
    Failure_shortfall_of_critical_infrastructure = 0
    Fiscal_crises_in_key_economies = 0
    High_structural_unemployment_or_underemployment = 0
    Unmanageable_inflation = 0
    Extreme_weather_events_eg_floods_storms_etc = 0
    Failure_of_climatechange_adaptation = 0
    Major_biodiversity_loss_and_ecosystem_collapse_land_or_ocean = 0
    Major_natural_catastrophes_eg_earthquake_tsunami_volcanic_eruption_geomagnetic_storms = 0
    #Manmade_environmental_catastrophes_eg_oil_spill_radioactive_contamination_etc = 0
    Failure_of_national_governance_eg_corruption_illicit_trade_organized_crime_impunity_political_deadlock_etc = 0
    Interstate_conflict_with_regional_consequences = 0
    Largescale_terrorist_attacks = 0
    State_collapse_or_crisis_eg_civil_conflict_military_coup_failed_states_etc = 0
    Weapons_of_mass_destruction = 0
    Failure_of_urban_planning = 0
    Food_crises = 0
    Largescale_involuntary_migration = 0
    Profound_social_instability = 0
    Rapid_and_massive_spread_of_infectious_diseases = 0
    Water_crises = 0
    Breakdown_of_critical_information_infrastructure_and_networks = 0
    Largescale_cyber_attacks = 0
    Massive_incident_of_data_fraud_theft = 0
    Massive_and_widespread_misuse_of_technologies = 0
    
    risks = [Asset_bubble_in_a_major_economy,Deflation_in_a_major_economy,Energy_price_shock_to_the_global_economy,Failure_of_a_major_financial_mechanism_or_institution,Failure_shortfall_of_critical_infrastructure,Fiscal_crises_in_key_economies,High_structural_unemployment_or_underemployment,Unmanageable_inflation,Extreme_weather_events_eg_floods_storms_etc,Failure_of_climatechange_adaptation,Major_biodiversity_loss_and_ecosystem_collapse_land_or_ocean,Major_natural_catastrophes_eg_earthquake_tsunami_volcanic_eruption_geomagnetic_storms,Failure_of_national_governance_eg_corruption_illicit_trade_organized_crime_impunity_political_deadlock_etc,Interstate_conflict_with_regional_consequences,Largescale_terrorist_attacks,State_collapse_or_crisis_eg_civil_conflict_military_coup_failed_states_etc,Weapons_of_mass_destruction,Failure_of_urban_planning,Food_crises,Largescale_involuntary_migration,Profound_social_instability,Rapid_and_massive_spread_of_infectious_diseases,Water_crises,Breakdown_of_critical_information_infrastructure_and_networks,Largescale_cyber_attacks,Massive_incident_of_data_fraud_theft,Massive_and_widespread_misuse_of_technologies]
    
    for risk in risks:
        print risks
    
    
    if 'Asset bubble' in tweet or 'equity bubble' in tweet or 'subprime' in tweet or 'investment bubble' in tweet:
        Asset_bubble_in_a_major_economy += 1
    elif 'deflation' in tweet or 'falling  inflation' in tweet or 'reduced  inflation' in tweet or 'falling prices' in tweet:
        Deflation_in_a_major_economy += 1
    elif 'energy price' in tweet or 'gasoline price' in tweet or 'petrol price' in tweet:
        Energy_price_shock_to_the_global_economy += 1
    elif 'bank failure' in tweet or 'bank collapse' in tweet or 'market collapse' in tweet or 'market failure' in tweet or 'bank bailout' in tweet:
        Failure_of_a_major_financial_mechanism_or_institution += 1
    elif 'critical  infrastructure' in tweet or ' infrastructure failure' in tweet:
        Failure_shortfall_of_critical_infrastructure += 1
    elif 'fiscal crisis' in tweet or 'financial crisis' in tweet:
        Fiscal_crises_in_key_economies += 1
    elif 'underemployment' in tweet or 'unemployment' in tweet:
        High_structural_unemployment_or_underemployment += 1
    elif 'inflation' in tweet:
        Unmanageable_inflation += 1
    elif 'Storm' in tweet or 'Flood' in tweet or 'Extreme weather' in tweet:
        Extreme_weather_events_eg_floods_storms_etc += 1
    elif 'Climate change' in tweet:
        Failure_of_climatechange_adaptation += 1
    elif 'biodiversity' in tweet:
        Major_biodiversity_loss_and_ecosystem_collapse_land_or_ocean += 1
    elif 'natural disaster' in tweet:
        Major_natural_catastrophes_eg_earthquake_tsunami_volcanic_eruption_geomagnetic_storms += 1
    #elif 'oil spill' in tweet or 'environmental contamination':
        #Manmade_environmental_catastrophes_eg_oil_spill_radioactive_contamination_etc += 1
    elif 'corruption' in tweet or 'organized crime' in tweet:
        Failure_of_national_governance_eg_corruption_illicit_trade_organized_crime_impunity_political_deadlock_etc += 1
    elif 'war' in tweet or 'state conflict' in tweet:
        Interstate_conflict_with_regional_consequences += 1
    elif 'terrorism' in tweet or 'terrorist' in tweet:
        Largescale_terrorist_attacks += 1
    elif 'state collapse' in tweet or 'civil crisis' in tweet or 'coup' in tweet or 'failed state' in tweet:
        State_collapse_or_crisis_eg_civil_conflict_military_coup_failed_states_etc += 1
    elif 'WMD' in tweet or 'nuclear weapon' in tweet or 'nuke' in tweet or 'dirty bomb' in tweet:
        Weapons_of_mass_destruction += 1
    elif 'failed urban planning' in tweet:
        Failure_of_urban_planning += 1
    elif 'food crisis' in tweet or 'starvation' in tweet:
        Food_crises += 1
    elif 'refugee' in tweet or 'refugees' in tweet:
        Largescale_involuntary_migration += 1
    elif 'riot' in tweet:
        Profound_social_instability += 1
    elif 'infectious' in tweet or 'disease' in tweet or 'epidemic' in tweet or 'pandemic' in tweet:
        Rapid_and_massive_spread_of_infectious_diseases += 1
    elif 'drought' in tweet or 'water shortage' in tweet:
        Water_crises += 1
    elif 'internet collapse' in tweet:
        Breakdown_of_critical_information_infrastructure_and_networks += 1
    elif 'cyber attack' in tweet or 'cyber warfare' in tweet or 'cyber terrorism' in tweet:
        Largescale_cyber_attacks += 1
    elif 'data fraud' in tweet or 'identity theft' in tweet:
        Massive_incident_of_data_fraud_theft += 1
    elif 'misuse of technology' in tweet:
        Massive_and_widespread_misuse_of_technologies += 1
    else:
        return True

class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, data_file, query):
        self.outfile = data_file

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                parsed_json = json.loads(str(data))
                f.write(parsed_json['text'].encode('utf-8'))
                query_check(parsed_json['text'].encode('utf-8'))

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