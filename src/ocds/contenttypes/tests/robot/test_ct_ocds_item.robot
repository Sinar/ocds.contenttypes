# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ocds.contenttypes -t test_ocds_item.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ocds.contenttypes.testing.OCDS_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/ocds/contenttypes/tests/robot/test_ocds_item.robot
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

Scenario: As a site administrator I can add a ocds item
  Given a logged-in site administrator
    and an add Award form
   When I type 'My ocds item' into the title field
    and I submit the form
   Then a ocds item with the title 'My ocds item' has been created

Scenario: As a site administrator I can view a ocds item
  Given a logged-in site administrator
    and a ocds item 'My ocds item'
   When I go to the ocds item view
   Then I can see the ocds item title 'My ocds item'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Award form
  Go To  ${PLONE_URL}/++add++Award

a ocds item 'My ocds item'
  Create content  type=Award  id=my-ocds_item  title=My ocds item

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the ocds item view
  Go To  ${PLONE_URL}/my-ocds_item
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a ocds item with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the ocds item title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
