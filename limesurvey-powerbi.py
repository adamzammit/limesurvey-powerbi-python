import pandas as pd #For data frames in a format PowerBI understands
from limesurveyrc2api.limesurvey import LimeSurvey #To talk to LimeSurvey API
from limesurveyrc2api.exceptions import LimeSurveyError
import base64 #To convert base64 encoded data
import io #To convert a string to a buffer for pandas to read

#Limesurvey details - change these to match your Survey
remotecontrolurl = "http://localhost/index.php/admin/remotecontrol"
limeuser = "admin"
limepasswd = "password"
surveyid = "1"

#Output details - change this to match your locale (i.e change the "." to a "," if your locale requires a "," as a decimal separator)
decimalseparator = "."

#Code to call the LimeSurvey API to extract data
 
#Connect to LimeSurvey
lime = LimeSurvey(url=remotecontrolurl,username=limeuser)
lime.open(password=limepasswd)
#Read using the survey export responses API call
result = lime.survey.export_responses(survey_id=surveyid,document_type='csv',heading_type='full',response_type='long')
#Convert data to a pandas data frame
surveydata = pd.read_csv(io.StringIO(base64.b64decode(result).decode("utf-8")),sep=';')
print(surveydata.to_string(decimal=decimalseparator))
#Read using the token list participants API call
attlist = []
for x in range(1,255):
    attlist.append("attribute_" + str(x))
result = lime.token.list_participants(survey_id=surveyid,start=0,limit=100000,attributes=attlist)
if('status' not in result):
    #We have token data so include and merge
    #Flatten out participant_info and add attributes
    nl = []
    for x in result:
        print(x)
        items = {'tid': x['tid'], 'token': x['token'], 'firstname': x['participant_info']['firstname'], 'lastname': x['participant_info']['lastname'], 'email': x['participant_info']['email']}
        for att in attlist:
            if att in x:
                items[att] = x[att]
        nl.append(items)
    #Convert data to a pandas data frame
    tokendata = pd.DataFrame(nl)
    print(tokendata)
    mergeddata = tokendata.merge(right=surveydata,how='outer',left_on='token',right_on='Token')
    print(mergeddata.to_string(decimal=decimalseparator))
#Disconnect
lime.close()
