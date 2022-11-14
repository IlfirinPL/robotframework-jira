*** Settings ***
Documentation       Example Suite For Using JIRALibrary

Library             Collections
Library             JIRALibrary

Test Timeout        1 minute


*** Variables ***
${JIRA URL}         %{URL}
${JIRA USER}        %{USER}
${JIRA PASSWORD}    %{PASS}


*** Test Cases ***
Connect To JIRA
    [Documentation]    Print List of Projects
    [Tags]    jira
    ${session}    Connect To Jira    ${JIRA URL}    ${JIRA USER}    ${JIRA PASSWORD}
    ${dict}    Projects    ${session}
    ${size}    Get Length    ${dict}
    Log Dictionary    Project found ${size}
