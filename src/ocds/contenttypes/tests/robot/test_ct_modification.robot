# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ocds.contenttypes -t test_modification.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ocds.contenttypes.testing.OCDS_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/ocds/contenttypes/tests/robot/test_modification.robot
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

Scenario: As a site administrator I can add a Modification
  Given a logged-in site administrator
    and an add ContractingProcess form
   When I type 'My Modification' into the title field
    and I submit the form
   Then a Modification with the title 'My Modification' has been created

Scenario: As a site administrator I can view a Modification
  Given a logged-in site administrator
    and a Modification 'My Modification'
   When I go to the Modification view
   Then I can see the Modification title 'My Modification'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add ContractingProcess form
  Go To  ${PLONE_URL}/++add++ContractingProcess

a Modification 'My Modification'
  Create content  type=ContractingProcess  id=my-modification  title=My Modification

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Modification view
  Go To  ${PLONE_URL}/my-modification
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Modification with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Modification title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
