Feature: GoogleSearchF
  As a Google user
  I want to do a search for test automation
  So I can verify that I can search successfully on google

  Scenario: User can google searching
	Given I am on the "Google" homepage
	And I entered "test automation" into the search field
	When I press enter
	Then I go to the search results page
	And The first three results contain the word "automation"

Scenario: User can navigate to first result page
	Given I search by "test automation"
	When I click on the first link
	Then I go to the page
	And The title contains the word "automation"
