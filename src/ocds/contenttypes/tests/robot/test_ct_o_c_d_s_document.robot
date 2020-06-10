# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ocds.contenttypes -t test_o_c_d_s_document.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ocds.contenttypes.testing.OCDS_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/ocds/contenttypes/tests/robot/test_o_c_d_s_document.robot
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

Scenario: As a site administrator I can add a OCDS Document
  Given a logged-in site administrator
    and an add Infrastructure Project form
   When I type 'My OCDS Document' into the title field
    and I submit the form
   Then a OCDS Document with the title 'My OCDS Document' has been created

Scenario: As a site administrator I can view a OCDS Document
  Given a logged-in site administrator
    and a OCDS Document 'My OCDS Document'
   When I go to the OCDS Document view
   Then I can see the OCDS Document title 'My OCDS Document'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Infrastructure Project form
  Go To  ${PLONE_URL}/++add++Infrastructure Project

a OCDS Document 'My OCDS Document'
  Create content  type=Infrastructure Project  id=my-o_c_d_s_document  title=My OCDS Document

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the OCDS Document view
  Go To  ${PLONE_URL}/my-o_c_d_s_document
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a OCDS Document with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the OCDS Document title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
