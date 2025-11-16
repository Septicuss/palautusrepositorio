*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
  Set Username  kalle123
  Set Password  kalle123
  Set Confirmation  kalle123
  Click Button  Register
  Register Should Succeed

Register With Too Short Username And Valid Password
  Set Username  ka
  Set Password  kalle123
  Set Confirmation  kalle123
  Click Button  Register
  Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
  Set Username  kalle123
  Set Password  ka
  Set Confirmation  ka
  Click Button  Register
  Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
  Set Username  kalle123
  Set Password  kalleeee
  Set Confirmation  kalle123
  Click Button  Register
  Register Should Fail With Message  Password invalid

Register With Nonmatching Password And Password Confirmation
  Set Username  kalle123
  Set Password  kalle123
  Set Confirmation  kalle1234
  Click Button  Register
  Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
  Set Username  kalle
  Set Password  kalle123
  Set Confirmation  kalle123
  Click Button  Register
  Register Should Fail With Message  Username is already in use

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application Create User And Go To Register Page
  Reset Application
  Create User  kalle  kalle123
  Go To Register Page
