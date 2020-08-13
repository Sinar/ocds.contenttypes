# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ocds.contenttypes -t test_tender.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ocds.contenttypes.testing.OCDS_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/ocds/contenttypes/tests/robot/test_tender.robot
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

Scenario: As a site administrator I can add a Tender
  Given a logged-in site administrator
    and an add OCDS Release form
   When I type 'My Tender' into the title field
    and I submit the form
   Then a Tender with the title 'My Tender' has been created

Scenario: As a site administrator I can view a Tender
  Given a logged-in site administrator
    and a Tender 'My Tender'
   When I go to the Tender view
   Then I can see the Tender title 'My Tender'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add OCDS Release form
  Go To  ${PLONE_URL}/++add++OCDS Release

a Tender 'My Tender'
  Create content  type=OCDS Release  id=my-tender  title=My Tender

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Tender view
  Go To  ${PLONE_URL}/my-tender
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Tender with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Tender title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
