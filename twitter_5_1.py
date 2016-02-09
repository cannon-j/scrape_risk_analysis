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

class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, data_file, query):
        self.outfile = data_file

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                parsed_json = json.loads(str(data))
                f.write(parsed_json['text'].encode('utf-8').lower())
                #query_check(parsed_json['text'].encode('utf-8').lower(),risk_values)
                print ''
            
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