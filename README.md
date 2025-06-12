# LimeSurvey PowerBI Python Integration


A Python 3 script for reading data from [LimeSurvey](https://limesurvey.org) in a format that Power BI will understand using the "Python Script" connector for data import.

1. Install [Python 3 for Windows](https://www.python.org/downloads/windows/)
2. Open a Command Prompt and run the following (copy each line and press enter after each):

```
    pip install pandas requests matplotlib
    pip install https://github.com/ESchae/limesurveyrc2api/archive/refs/heads/master.zip
```

3. Update the script to include your LimeSurvey JSON-RPC URL, username, password and survey id (Hint: make a new copy of this script for each survey)
4. If your computer running Power BI expects the decimal separator to be a "," instead of a ".", please change the decimalseparator line in the script to reflect this
5. Run the script from the Power BI desktop using Data Import then "Python Script"
