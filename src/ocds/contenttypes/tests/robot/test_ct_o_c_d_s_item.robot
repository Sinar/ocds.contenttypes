# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ocds.contenttypes -t test_o_c_d_s_item.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ocds.contenttypes.testing.OCDS_CONTENTTYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/ocds/contenttypes/tests/robot/test_o_c_d_s_item.robot
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

Scenario: As a site administrator I can add a OCDS Item
  Given a logged-in site administrator
    and an add Award form
   When I type 'My OCDS Item' into the title field
    and I submit the form
   Then a OCDS Item with the title 'My OCDS Item' has been created

Scenario: As a site administrator I can view a OCDS Item
  Given a logged-in site administrator
    and a OCDS Item 'My OCDS Item'
   When I go to the OCDS Item view
   Then I can see the OCDS Item title 'My OCDS Item'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Award form
  Go To  ${PLONE_URL}/++add++Award

a OCDS Item 'My OCDS Item'
  Create content  type=Award  id=my-o_c_d_s_item  title=My OCDS Item

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the OCDS Item view
  Go To  ${PLONE_URL}/my-o_c_d_s_item
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a OCDS Item with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the OCDS Item title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
