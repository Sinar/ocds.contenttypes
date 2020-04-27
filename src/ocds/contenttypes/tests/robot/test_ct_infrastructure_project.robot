# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ocds.contenttypes -t test_infrastructure_project.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ocds.contenttypes.testing.OCDS_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/ocds/contenttypes/tests/robot/test_infrastructure_project.robot
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

Scenario: As a site administrator I can add a Infrastructure Project
  Given a logged-in site administrator
    and an add Infrastructure Project form
   When I type 'My Infrastructure Project' into the title field
    and I submit the form
   Then a Infrastructure Project with the title 'My Infrastructure Project' has been created

Scenario: As a site administrator I can view a Infrastructure Project
  Given a logged-in site administrator
    and a Infrastructure Project 'My Infrastructure Project'
   When I go to the Infrastructure Project view
   Then I can see the Infrastructure Project title 'My Infrastructure Project'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Infrastructure Project form
  Go To  ${PLONE_URL}/++add++Infrastructure Project

a Infrastructure Project 'My Infrastructure Project'
  Create content  type=Infrastructure Project  id=my-infrastructure_project  title=My Infrastructure Project

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Infrastructure Project view
  Go To  ${PLONE_URL}/my-infrastructure_project
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Infrastructure Project with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Infrastructure Project title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
