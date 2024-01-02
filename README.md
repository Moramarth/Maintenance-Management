# Maintenance-Management

[Screenshots](#screenshots)

Ongoing API update, goal is to leave only admin panel, registration and password change/recovery on the server-side rendering.

# Quick navigation

- [General info](#general-info)
- [Business logic](#business-logic)
- [Test set-up](#getting-started)
- [Permissions for Engineering](#permissions-for-engineering)
- [Permissions for Supervisor](#permissions-for-supervisor)
- [Setting up roles](#setting-up-roles)
- [Intended user creation](#intended-user-creation)
- [Screenshots](#screenshots)

## General info

- Framework:
    * Django 4.2.1
    [![Django](https://skillicons.dev/icons?i=django)](https://docs.djangoproject.com/en/4.2/)


- Database:
    * PostgreSQL [![Postgres](https://skillicons.dev/icons?i=postgres)](https://www.postgresql.org/)

- Third-party apps:
    * [django-filter](https://django-filter.readthedocs.io/en/stable/) 23.2
    * [django-storages](https://django-storages.readthedocs.io/en/latest/) 1.13.2

- Services:
    * AWS S3 [![S3](https://skillicons.dev/icons?i=aws)](https://aws.amazon.com/s3/)
    * [Google Maps API](https://developers.google.com/maps)

- Styles:
    * Bootstrap 5 [![Bootstrap](https://skillicons.dev/icons?i=bootstrap)](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    * [Fontawesome](https://fontawesome.com/)
    * [MagnificPopup](https://dimsemenov.com/plugins/magnific-popup/)
    * CSS ![CSS](https://skillicons.dev/icons?i=css)

## Business Logic

Service is only available for business partners. Registration is available after invitation from the company
service owner.

Tenants(Clients) can report issues that need attention in the owner`s buildings.

Supervisors and the engineering team take appropriate actions to resolve the issues.

If extra work is required a 3rd party (Contractors) can be assigned to tackle the problem.

Contractors can arrange a meeting for getting additional information or if they believe information is enough an offer
can be created for doing the work.

Contacts info is available at any given step so people can communicate via e-mail or phone when needed.

[back to start](#quick-navigation)

## Getting Started

Four Groups need to be created that also work as roles control.
Clients, Contractors, Engineering and Supervisor
One user can belong to only one Group

Clients and Contractors have no permissions in the admin site

If you need any additional information contact me via links on my profile page.

[back to start](#quick-navigation)

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

[back to start](#quick-navigation)

## Permissions for Supervisor

- accounts | app user | Can change, delete and view app user
- accounts | app user profile | Can view app user profile
- accounts | register invitation | full CRUD
- clients | review | delete and view review
- clients | service report | delete and view service report
- common | company | full CRUD
- contractors | expenses estimate | delete and view expenses estimate
- contractors | meeting | delete and view meeting
- estate | additional address information | full CRUD
- estate | building | full CRUD
- supervisor | assignment | full CRUD

[back to start](#quick-navigation)

## Setting up roles

To manually create users(error free) set SUSPEND_SIGNALS to True in settings.py

- create superuser
- create groups and add permission as shown above
- create at least one building object and one company object
- assign superuser to Supervisor group, so you can navigate main site
- create one user and assign it to the Supervisor group to see admin site as intended
- create at least one user for each of the other groups to test different scenarios

[back to start](#quick-navigation)

## Intended user creation

- User is invited by the Supervisor with Register Invitation object
- After receiving the invitation e-mail and following his generated url user can register to the system.
  Empty profile is created and attached to the user object.
- If user is staff Supervisor needs to set it to True after registration(can be changed to automatic later).
- Clients and Contractors can also invite people to become part of their company

[back to start](#quick-navigation)

## Screenshots

- Home

  ![Home_page](https://github.com/Moramarth/Maintenance-Management/assets/122516587/b9315d68-e0cf-4bd6-9e4b-87ef4168bd7b)

- Forms

   ![Forms](https://github.com/Moramarth/Maintenance-Management/assets/122516587/78c4a984-116b-4444-a55a-bea98db01ade)
  
- List views

  ![List_views](https://github.com/Moramarth/Maintenance-Management/assets/122516587/12dbb038-3b57-42f1-a4a7-3f2997409e0d)

- Details views

  ![details_view](https://github.com/Moramarth/Maintenance-Management/assets/122516587/7da5a379-5093-45ea-b680-0f6c4d5555a7)

- Profile

  ![profile](https://github.com/Moramarth/Maintenance-Management/assets/122516587/a7124272-68fa-476e-b058-89d794dbcfd7)


[back to start](#quick-navigation)
