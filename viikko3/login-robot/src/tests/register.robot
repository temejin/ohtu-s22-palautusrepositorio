*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User  kalle  kalle123
    Created Users Should Be  1

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Create User  kalle  kalle321
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Create User  ka  kalle123
    Output Should Contain  Username must be at least 3 characters long
