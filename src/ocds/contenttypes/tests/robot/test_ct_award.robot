# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ocds.contenttypes -t test_award.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ocds.contenttypes.testing.OCDS_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/ocds/contenttypes/tests/robot/test_award.robot
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

Scenario: As a site administrator I can add a Award
  Given a logged-in site administrator
    and an add OCDS Release form
   When I type 'My Award' into the title field
    and I submit the form
   Then a Award with the title 'My Award' has been created

Scenario: As a site administrator I can view a Award
  Given a logged-in site administrator
    and a Award 'My Award'
   When I go to the Award view
   Then I can see the Award title 'My Award'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add OCDS Release form
  Go To  ${PLONE_URL}/++add++OCDS Release

a Award 'My Award'
  Create content  type=OCDS Release  id=my-award  title=My Award

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Award view
  Go To  ${PLONE_URL}/my-award
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Award with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Award title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
