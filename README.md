# Maintenance-Management
This repository contains my final project for the course Python Web Framework - June 2023

# Quick navigation
- [General info](#if-you-want-to-test:)
- [Permissions for Engineering](#permissions-for-engineering)
- [Permissions for Supervisor](#permissions-for-supervisor)
- [Setting up roles](#setting-up-roles)
- [Intended user creation](#intended-user-creation)


# If you want to test:
Keep in mind this is work in progress, not ready for the exam.

If you need any additional information contact me via links on my profile page.
If you are part of the SoftUni team I am also available via phone.

Four Groups need to be created that also work as roles control.
Clients, Contractors, Engineering and Supervisor
One user can belong to only one Group

Clients and Contractors have no permissions in the admin site

## Permissions for Engineering
 - accounts | app user profile | Can view app user profile
 - clients | review | Can view review
 - clients | service report | Can view service report
 - common | company | Can view company
 - contractors | meeting | Can view meeting
 - estate | additional address information | Can view additional address information
 - estate | building | Can view building
 - supervisor | assignment | Can add assignment
 - supervisor | assignment | Can change assignment
 - supervisor | assignment | Can view assignment


## Permissions for Supervisor
- accounts | app user | Can change, delete and view app user
- accounts | app user profile | Can view app user profile
- accounts | register invitation | full CRUD
- clients | review | delete and view review
- clients | service report | delete and view service report
- common | company | full crud
- contractors | expenses estimate | delete and view expenses estimate
- contractors | meeting | delete and view meeting
- estate | additional address information | full CRUD
- estate | building | full CRUD
- supervisor | assignment | full CRUD

## Setting up roles
To manually create users error free in settings.py set SUSPEND_SINGNALS to True
- create super user
- create groups and add permission as shown above
- create at least one building object and one company object
- assign superuser to Supervisor group so you can navigate main site 
- create one user and assign it to the Supervisor group to see admin site as intended
- create at least one user for each of the other groups to test different scenarios

## Intended user creation
- User is invited by the Supervisor with Register Invitation object
- After receiving the invitation e-mail and following his generated url user can register to the system.
  Empty profile is created and attached to the user object.
- If user is staff Supervisor needs to set it to True after registration(can be changed to automatic later).
- Clients and Contractors can also invite people to become part of their company
