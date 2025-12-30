#This use case reads a log file and counts how many times the word ERROR appears.
#It is commonly used in automation to decide pass/fail status, trigger alerts, or stop pipelines.
Error_count=0

with open ("Automation_file.log", "r") as file:
    #file.readline()
    for x in file:
        if "ERROR" in x:
            Error_count +=1
print("Number Of ERROR count in log file:",Error_count)

"""
Real Automation Scenario
Automation script runs health checks
Output is written to a log file
Script scans the log
If errors > 0 → raise alert / fail job
"""

"""Dry Explanation (Simple)
File opens safely using with open()
Script reads file line by line
Checks if "ERROR" exists in a line
Increments counter
File closes automatically
Final error count is printed
"""