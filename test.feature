Feature: RHEL CABS
  	
  Scenario: The Continuous Automated Build System (CABS) shall leverage the Linux server as the primary Operating System (OS) Platform	
		
    Given the Continuous Automated Build System exists
    When I query the Ansible API for the CABS Operating System
    Then the API returns RHEL7
