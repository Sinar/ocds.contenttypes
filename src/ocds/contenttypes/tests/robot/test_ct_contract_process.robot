# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ocds.contenttypes -t test_contract_process.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ocds.contenttypes.testing.OCDS_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/ocds/contenttypes/tests/robot/test_contract_process.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Contract Process
  Given a logged-in site administrator
    and an add Infrastructure Project form
   When I type 'My Contract Process' into the title field
    and I submit the form
   Then a Contract Process with the title 'My Contract Process' has been created

Scenario: As a site administrator I can view a Contract Process
  Given a logged-in site administrator
    and a Contract Process 'My Contract Process'
   When I go to the Contract Process view
   Then I can see the Contract Process title 'My Contract Process'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Infrastructure Project form
  Go To  ${PLONE_URL}/++add++Infrastructure Project

a Contract Process 'My Contract Process'
  Create content  type=Infrastructure Project  id=my-contract_process  title=My Contract Process

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Contract Process view
  Go To  ${PLONE_URL}/my-contract_process
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Contract Process with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Contract Process title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
