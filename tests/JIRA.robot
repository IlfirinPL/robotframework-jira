*** Settings ***
Force Tags        JIRA
Test Timeout      1 minute
Library           JIRALibrary
Library           Collections

*** Test Cases ***
Connect To JIRA
    ${session}    Connect To Jira    %{URL}    %{USER}    %{PASS}
    ${dict}    Projects    ${session}
    ${size}    Get Length    ${dict}
    Log Dictionary    Project found ${size}

*** Keywords ***
