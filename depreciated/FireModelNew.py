#importing relevant libraries
import pandas as pd
import numpy as np
import sqlalchemy as sa
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
#%matplotlib inline

# #1: CLEAN PLI & PITT DATA
# Reading plidata - permits, licenses and inspection
plidata = pd.read_csv('data/pli.csv',encoding = 'utf-8',dtype={'STREET_NUM':'str','STREET_NAME':'str'})
# Reading city of Pittsburgh dataset - building info
pittdata = pd.read_csv('data/pittdata.csv',dtype={'PROPERTYADDRESS':'str','PROPERTYHOUSENUM':'str','STATEDESC':'str'})
#Reading 311 file - request for violation
calldata = pd.read_csv('data/311request.csv')

# Cleaning function for address column in calldata
def removingZeros(x):
    x = x.replace('  ',' ')
    if x[0] == 0 and x[1]==0:
        x= x.replace('0','',2)
    elif x[0] == 0:
        x= x.replace('0','',1)
    return x

#removing extra whitespaces
plidata['STREET_NAME'] = plidata['STREET_NAME'].str.strip()
plidata['STREET_NUM'] = plidata['STREET_NUM'].str.strip()

#removing residential data
pittdata = pittdata[pittdata.STATEDESC!='RESIDENTIAL']
pittdata = pittdata[pittdata.PROPERTYHOUSENUM!= '0']
pittdata = pittdata[pittdata.PROPERTYADDRESS!= '']

#dropping columns with less than 15% data
pittdata = pittdata.dropna(thresh=4000, axis=1)
pittdata = pittdata.rename(columns={pittdata.columns[0]:'PARID'})
pittdata = pittdata.drop_duplicates()

#merging pli with city of pitt
plipca = pd.merge(pittdata, plidata[['PARCEL','INSPECTION_DATE','INSPECTION_RESULT','VIOLATION']], how = 'left', left_on =['PARID'], right_on = ['PARCEL'] )
plipca = plipca.drop_duplicates()

#dropping nas
newpli = plipca.dropna(subset =['PARCEL','INSPECTION_DATE','INSPECTION_RESULT','VIOLATION'] ) #drop lines with NA
newpli = newpli.reset_index()
newpli = newpli.drop(['index','PARID','index',u'PROPERTYOWNER', #**remove unneeded columns
    u'PROPERTYCITY', u'PROPERTYSTATE', u'PROPERTYUNIT', u'PROPERTYZIP',
    u'MUNICODE', u'MUNIDESC', u'SCHOOLCODE', u'SCHOOLDESC', u'NEIGHCODE',
    u'TAXCODE', u'TAXDESC', u'OWNERCODE', u'OWNERDESC', u'STATECODE',
    u'STATEDESC', u'USECODE', u'USEDESC', u'LOTAREA', u'SALEDATE',
    u'SALEPRICE', u'SALECODE', u'SALEDESC', u'DEEDBOOK', u'DEEDPAGE',
    u'AGENT', u'TAXFULLADDRESS1', u'TAXFULLADDRESS2', u'TAXFULLADDRESS3',
    u'TAXFULLADDRESS4', u'CHANGENOTICEADDRESS1', u'CHANGENOTICEADDRESS2',
    u'CHANGENOTICEADDRESS3', u'CHANGENOTICEADDRESS4', u'COUNTYBUILDING',
    u'COUNTYLAND', u'COUNTYTOTAL', u'COUNTYEXEMPTBLDG', u'LOCALBUILDING',
    u'LOCALLAND', u'LOCALTOTAL', u'FAIRMARKETBUILDING', u'FAIRMARKETLAND',
    u'FAIRMARKETTOTAL', u'PARCEL'], axis=1)

newpli = newpli.drop_duplicates()

#converting to datetime
newpli.INSPECTION_DATE = pd.to_datetime(newpli.INSPECTION_DATE)
newpli['violation_year'] = newpli['INSPECTION_DATE'].map(lambda x: x.year)

plipca.SALEPRICE = plipca.SALEPRICE.replace('NaN',0)

#Groups by address and replaces LOTAREA','SALEPRICE','FAIRMARKETLAND','FAIRMARKETBUILDING' by mean
numerical = plipca.groupby( [ "PROPERTYHOUSENUM", "PROPERTYADDRESS"] , as_index=False)[['LOTAREA','SALEPRICE',
    'FAIRMARKETLAND',
    'FAIRMARKETBUILDING']].mean()

# Following blocks of code group by address and get the category with maximum count for each given categorical columns
temp = pd.DataFrame({'count' : plipca.groupby( [ "PROPERTYHOUSENUM", "PROPERTYADDRESS"] ).STATEDESC.value_counts()}).reset_index()
idx = temp.groupby([ "PROPERTYHOUSENUM", "PROPERTYADDRESS"])['count'].transform(max) == temp['count']
result1 = temp[idx]
result1 = result1.drop_duplicates(subset=[ "PROPERTYHOUSENUM", "PROPERTYADDRESS"], keep = 'last')
del result1['count']

temp = pd.DataFrame({'count' : plipca.groupby( [ "PROPERTYHOUSENUM", "PROPERTYADDRESS"] ).STATEDESC.value_counts()}).reset_index()
temp.groupby([ "PROPERTYHOUSENUM", "PROPERTYADDRESS"])['count'].transform(max)
idx = temp.groupby([ "PROPERTYHOUSENUM", "PROPERTYADDRESS"])['count'].transform(max) == temp['count']
result1 = temp[idx]
result1 = result1.drop_duplicates(subset=[ "PROPERTYHOUSENUM", "PROPERTYADDRESS"], keep = 'last')
del result1['count']

temp = pd.DataFrame({'count' : plipca.groupby( [ "PROPERTYHOUSENUM", "PROPERTYADDRESS"] ).SCHOOLDESC.value_counts()}).reset_index()
idx = temp.groupby([ "PROPERTYHOUSENUM", "PROPERTYADDRESS"])['count'].transform(max) == temp['count']
result2 = temp[idx]
result2 = result2.drop_duplicates(subset=[ "PROPERTYHOUSENUM", "PROPERTYADDRESS"], keep = 'last')
del result2['count']

temp = pd.DataFrame({'count' : plipca.groupby( [ "PROPERTYHOUSENUM", "PROPERTYADDRESS"] ).OWNERDESC.value_counts()}).reset_index()
idx = temp.groupby([ "PROPERTYHOUSENUM", "PROPERTYADDRESS"])['count'].transform(max) == temp['count']
result3 = temp[idx]
result3 = result3.drop_duplicates(subset=[ "PROPERTYHOUSENUM", "PROPERTYADDRESS"], keep = 'last')
del result3['count']

temp = pd.DataFrame({'count' : plipca.groupby( [ "PROPERTYHOUSENUM", "PROPERTYADDRESS"] ).MUNIDESC.value_counts()}).reset_index()
idx = temp.groupby([ "PROPERTYHOUSENUM", "PROPERTYADDRESS"])['count'].transform(max) == temp['count']
result4 = temp[idx]
result4 = result4.drop_duplicates(subset=[ "PROPERTYHOUSENUM", "PROPERTYADDRESS"], keep = 'last')
del result4['count']

temp = pd.DataFrame({'count' : plipca.groupby( [ "PROPERTYHOUSENUM", "PROPERTYADDRESS"] ).INSPECTION_RESULT.value_counts()}).reset_index()
idx = temp.groupby([ "PROPERTYHOUSENUM", "PROPERTYADDRESS"])['count'].transform(max) == temp['count']
result5 = temp[idx]
result5 = result5.drop_duplicates(subset=[ "PROPERTYHOUSENUM", "PROPERTYADDRESS"], keep = 'last')
del result5['count']

temp = pd.DataFrame({'count' : plipca.groupby( [ "PROPERTYHOUSENUM", "PROPERTYADDRESS"] ).NEIGHCODE.value_counts()}).reset_index()
idx = temp.groupby([ "PROPERTYHOUSENUM", "PROPERTYADDRESS"])['count'].transform(max) == temp['count']
result6 = temp[idx]
result6 = result6.drop_duplicates(subset=[ "PROPERTYHOUSENUM", "PROPERTYADDRESS"], keep = 'last')
del result6['count']

temp = pd.DataFrame({'count' : plipca.groupby( [ "PROPERTYHOUSENUM", "PROPERTYADDRESS"] ).TAXDESC.value_counts()}).reset_index()
idx = temp.groupby([ "PROPERTYHOUSENUM", "PROPERTYADDRESS"])['count'].transform(max) == temp['count']
result7 = temp[idx]
result7 = result7.drop_duplicates(subset=[ "PROPERTYHOUSENUM", "PROPERTYADDRESS"], keep = 'last')
del result7['count']

temp = pd.DataFrame({'count' : plipca.groupby( [ "PROPERTYHOUSENUM", "PROPERTYADDRESS"] ).USEDESC.value_counts()}).reset_index()
idx = temp.groupby([ "PROPERTYHOUSENUM", "PROPERTYADDRESS"])['count'].transform(max) == temp['count']
result8 = temp[idx]
result8 = result8.drop_duplicates(subset=[ "PROPERTYHOUSENUM", "PROPERTYADDRESS"], keep = 'last')
del result8['count']

dfs = [result1,result2,result3,result4,result6,result7,result8,numerical]

pcafinal = reduce(lambda left,right: pd.merge(left,right,on= [ "PROPERTYHOUSENUM", "PROPERTYADDRESS"] ), dfs)
plipitt_cleaned = pd.merge(pcafinal, newpli, how = 'left', left_on =[ "PROPERTYHOUSENUM", "PROPERTYADDRESS"], right_on = [ "PROPERTYHOUSENUM", "PROPERTYADDRESS"] )
# #1 DONE, ^this is the cleaned dataframe of pli + pitt

# #2 CLEAN FIRE INCIDENT DATA
# load fire incidents csvs
fire_pre14 = pd.read_csv('data/Fire_Incidents_Pre14.csv',encoding = 'latin-1',dtype={'street':'str','number':'str'})
fire_historical = pd.read_csv('data/Fire_Incidents_Historical.csv',encoding = 'utf-8',
                              dtype={'street':'str','number':'str'})
fire_historical = fire_historical.append(pd.read_csv('data/Fire_Incidents_New.csv',encoding = 'utf-8',
                                                     dtype={'street':'str','number':'str'}), ignore_index=True)

# cleaning columns of fire_pre14
fire_pre14['full.code'] = fire_pre14['full.code'].str.replace('  -',' -')
fire_pre14['st_type'] = fire_pre14['st_type'].str.strip()
fire_pre14['street'] = fire_pre14['street'].str.strip()
fire_pre14['number'] = fire_pre14['number'].str.strip()
fire_pre14['st_type'] = fire_pre14['st_type'].str.replace('AV','AVE')
fire_pre14['street'] = fire_pre14['street'].str.strip() +' ' +fire_pre14['st_type'].str.strip()

# drop irrelevant columns

pre14_drop = ['PRIMARY_UNIT','MAP_PAGE','alm_dttm','arv_dttm','XCOORD','YCOORD',
              'inci_id','inci_type','alarms','st_prefix','st_suffix','st_type','CALL_NO']
for col in pre14_drop:
    del fire_pre14[col]
pre14_drop = [0, 4]
fire_pre14.drop(fire_pre14.columns[pre14_drop], axis=1, inplace=True)
post14_drop = ['inci_id','alm_dttm','arv_dttm','pbf_narcan','meds_glucose','meds_epi',
               'meds_nitro','pbf_albut','cpr','car_arr','aed','none','pbf_lift_ass',
               'Med_Assist','XCOORD','YCOORD','LOCATION','REP_DIST','alarms','inci_type',
               'Lift_Ref','Card_CPR','AGENCY','PRIMARY_UNIT','MAP_PAGE','CURR_DGROUP','CALL_NO']
for col in post14_drop:
    del fire_historical[col]

# combine data from two csvs together
fire_historical = fire_historical.append(fire_pre14, ignore_index=True)

# removing events that are not fire related
fire_historical['descript'] = fire_historical['descript'].str.strip()
remove_descript = ['System malfunction, Other',
                   # 'Smoke detector activation, no fire - unintentional']
                   # 'Alarm system activation, no fire - unintentional']
                   'Detector activation, no fire - unintentional', 'Smoke detector activation due to malfunction',
                   'Dispatched & cancelled en route', 'Dispatched & cancelled on arrival',
                   'EMS call, excluding vehicle accident with injury', 'Medical assist, assist EMS crew',
                   'Emergency medical service, other', 'Good intent call, Other', 'Rescue, EMS incident, other',
                   'Medical Alarm Activation (No Medical Service Req)', 'Motor Vehicle Accident with no injuries',
                   'No Incident found on arrival at dispatch address', 'Unintentional transmission of alarm, Other',
                   'Motor vehicle accident with injuries', 'Vehicle accident, general cleanup', 'Power line down',
                   'Person in distress, Other', 'Cable/Telco Wires Down', 'Service Call, other',
                   'Vehicle Accident canceled en route', 'Lock-out', 'False alarm or false call, Other',
                   'Assist police or other governmental agency', 'Special type of incident, Other',
                   'Alarm system sounded due to malfunction', 'Motor vehicle/pedestrian accident (MV Ped)',
                   'Assist invalid ', 'Malicious, mischievous false call, Other', 'Accident, potential accident, Other',
                   'Assist invalid', 'EMS call, party transported by non-fire agency', 'Rescue or EMS standby',
                   'Public service assistance, Other', 'Police matter', 'Lock-in (if lock out , use 511 )',
                   'Sprinkler activation, no fire - unintentional', 'Wrong location',
                   'Local alarm system, malicious false alarm', 'Authorized controlled burning',
                   'Water problem, Other',
                   # 'Smoke or odor removal']
                   'Passenger vehicle fire', 'CO detector activation due to malfunction',
                   'Authorized controlled burning', 'Steam, vapor, fog or dust thought to be smoke', 'Overheated motor',
                   'Local alarm system, malicious false alarm', 'Central station, malicious false alarm',
                   'Public service',
                   # 'Building or structure weakened or collapsed'
                   'Heat detector activation due to malfunction', 'Citizen complaint',
                   'Municipal alarm system, malicious false alarm', 'Sprinkler activation due to malfunction',
                   'Severe weather or natural disaster, Other', 'Water evacuation', 'Breakdown of light ballast',
                   'Extrication of victim(s) from vehicle', 'Flood assessment', 'Telephone, malicious false alarm',
                   'Cover assignment, standby, moveup', 'Road freight or transport vehicle fire']

for descript in remove_descript:
    fire_historical = fire_historical[fire_historical.descript != descript]
fire_historical = fire_historical[fire_historical['full.code'].str.strip()  != '540 - Animal problem, Other']
fire_historical = fire_historical[fire_historical['full.code'].str.strip()  != '5532 - Public Education (Station Visit)']
fire_historical = fire_historical[fire_historical['full.code'].str.strip()  != '353 - Removal of victim(s) from stalled elevator']

#correcting problems with the street column
fire_historical['street'] = fire_historical['street'].replace(to_replace=', PGH', value='', regex=True)
fire_historical['street'] = fire_historical['street'].replace(to_replace=', P', value='', regex=True)
fire_historical['street'] = fire_historical['street'].replace(to_replace=',', value='', regex=True)
fire_historical['street'] = fire_historical['street'].replace(to_replace='#.*', value='', regex=True)
fire_historical['street'] = fire_historical['street'].str.strip()
fire_historical['number'] = fire_historical['number'].str.strip()

#converting to date time and extracting year
fireDate, fireTime = fire_historical['CALL_CREATED_DATE'].str.split(' ', 1).str
fire_historical['CALL_CREATED_DATE']= fireDate
fire_historical['CALL_CREATED_DATE'] = pd.to_datetime(fire_historical['CALL_CREATED_DATE'])
fire_historical['fire_year'] = fire_historical['CALL_CREATED_DATE'].map(lambda x: x.year)

#removing all codes with less than 20 occurences
for col,val in fire_historical['full.code'].value_counts().iteritems():
    if val <20 and col[0]!= '1':
        fire_historical = fire_historical[fire_historical['full.code'] != col]

fire_historical = fire_historical.drop_duplicates()

# #3 JOIN TWO DATASETS AND FINAL CLEANING
pcafire = pd.merge(plipitt_cleaned, fire_historical, how = 'left', left_on =['PROPERTYADDRESS','PROPERTYHOUSENUM'],
                   right_on = ['street','number'])


