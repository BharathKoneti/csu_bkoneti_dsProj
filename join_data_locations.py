#Join Location and and data dataframes
data_join = data.join(locations[['geographiclevel','stateabbr','cityname']]).copy()
# Keeping only census level data
census_data = data_join[data_join['geographiclevel'] == 'Census Tract']
# Drop unnecessary and NOT needed columns
census_data_req = census_data.drop(['datavaluetypeid','geographiclevel','stateabbr','cityname'],axis=1).reset_index().set_index('uniqueid')