# Maintenance Management API

## Base URL
`domain-name/api/`
# Quick Navigation


- [Overview](#overview)
- [Common App Endpoints](#common-app-endpoints)
- [Clients App Endpoints](#clients-app-endpoints)
- [Accounts App Endpoints](#accounts-app-endpoints)
- [Estate App Endpoints](#estate-app-endpoints)
- [Supervisor App Endpoints](#supervisor-app-endpoints)
- [Contractors App Endpoints](#contractors-app-endpoints)
- [Engineering App Endpoints](#engineering-app-endpoints)


## Overview
The Maintenance Management API is currently in a test phase and is a work in progress. Its primary focus is to provide data from the database to support the creation of a frontend and visualization of information. It is important to note that the API is not implemented with full security measures or comprehensive validation at this stage.

**Note:** This API is intended for testing purposes and is not suitable for production use in its current state.

The API provides access to resources for managing common, accounts, clients, and estate information. Please be aware of its limitations and evolving nature as development continues.

## Common App
Access the common app by navigating to `domain-name/api/`.

### Common App Endpoints
- `GET /domain-name/api/companies/`
  - Description: Show all companies.
  - Endpoint: `companies/`
  - Method: `GET`
- `POST /domain-name/api/companies/`
  - Description: Create a new company.
  - Endpoint: `companies/`
  - Method: `POST`
- `GET /domain-name/api/companies/<int:pk>/`
  - Description: Get company by ID.
  - Endpoint: `companies/<int:pk>/`
  - Method: `GET`
- `PATCH /domain-name/api/companies/<int:pk>/`
  - Description: Update company by ID.
  - Endpoint: `companies/<int:pk>/`
  - Method: `PATCH`
- `GET /domain-name/api/companies/<int:pk>/address/`
  - Description: Get company address by ID.
  - Endpoint: `companies/<int:pk>/address/`
  - Method: `GET`
- `GET /domain-name/api/companies/<int:pk>/employees/`
  - Description: Get company employees by ID.
  - Endpoint: `companies/<int:pk>/employees/`
  - Method: `GET`


## Accounts App
Access the accounts app by navigating to `accounts/`.

### Accounts App Endpoints
- `GET /domain-name/api/accounts/profiles/`
  - Description: Get all profiles.
  - Endpoint: `profiles/`
  - Method: `GET`
- `POST /domain-name/api/accounts/profiles/`
  - Description: Create a new profile.
  - Endpoint: `profiles/`
  - Method: `POST`
- `GET /domain-name/api/accounts/profiles/<int:pk>/`
  - Description: Get profile by ID.
  - Endpoint: `profiles/<int:pk>/`
  - Method: `GET`
- `PATCH /domain-name/api/accounts/profiles/<int:pk>/`
  - Description: Update profile by ID.
  - Endpoint: `profiles/<int:pk>/`
  - Method: `PATCH`
- `GET /domain-name/api/accounts/app-user/<int:pk>/`
  - Description: Get app user by ID.
  - Endpoint: `app-user/<int:pk>/`
  - Method: `GET`
- `GET /domain-name/api/accounts/app-user/current/`
  - Description: Get current logged in app user.
  - Endpoint: `app-user/current/`
  - Method: `GET`
- `POST /domain-name/api/token/`
  - Description: Obtain an access token.
  - Endpoint: `token/`
  - Method: `POST`
- `POST /domain-name/api/token/refresh/`
  - Description: Refresh an access token.
  - Endpoint: `token/refresh/`
  - Method: `POST`
- `POST /domain-name/api/token/verify/`
  - Description: Verify an access token.
  - Endpoint: `token/verify/`
  - Method: `POST`

## Clients App
Access the clients app by navigating to `clients/`.

### Clients App Endpoints
- `GET /domain-name/api/clients/reviews/`
  - Description: Show all reviews.
  - Endpoint: `reviews/`
  - Method: `GET`
- `POST /domain-name/api/clients/reviews/`
  - Description: Create a new review.
  - Endpoint: `reviews/`
  - Method: `POST`
- `GET /domain-name/api/clients/reviews/<int:pk>/`
  - Description: Get review by ID.
  - Endpoint: `reviews/<int:pk>/`
  - Method: `GET`
- `PATCH /domain-name/api/clients/reviews/<int:pk>/`
  - Description: Update review by ID.
  - Endpoint: `reviews/<int:pk>/`
  - Method: `PATCH`
- `DELETE /domain-name/api/clients/reviews/<int:pk>/`
  - Description: Delete review by ID.
  - Endpoint: `reviews/<int:pk>/`
  - Method: `DELETE`
- `GET /domain-name/api/clients/service-reports/`
  - Description: Show all service reports.
  - Endpoint: `service-reports/`
  - Method: `GET`
- `POST /domain-name/api/clients/service-reports/`
  - Description: Create a new service report.
  - Endpoint: `service-reports/`
  - Method: `POST`
- `GET /domain-name/api/clients/service-reports/<int:pk>/`
  - Description: Get service report by ID.
  - Endpoint: `service-reports/<int:pk>/`
  - Method: `GET`
- `PATCH /domain-name/api/clients/service-reports/<int:pk>/`
  - Description: Update service report by ID.
  - Endpoint: `service-reports/<int:pk>/`
  - Method: `PATCH`
- `DELETE /domain-name/api/clients/service-reports/<int:pk>/`
  - Description: Delete service report by ID.
  - Endpoint: `service-reports/<int:pk>/`
  - Method: `DELETE`

## Estate App
Access the estate app by navigating to `estate/`.

### Estate App Endpoints
- `GET /domain-name/api/estate/buildings/`
  - Description: Show all buildings.
  - Endpoint: `buildings/`
  - Method: `GET`
- `GET /domain-name/api/estate/buildings/<int:pk>/`
  - Description: Get building by ID.
  - Endpoint: `buildings/<int:pk>/`
  - Method: `GET`

## Supervisor App

Access the Supervisor app by navigating to `supervisor/`.

### Supervisor App Endpoints
- `GET /domain-name/api/supervisor/assignments/`
  - Description: Retrieve all assignments.
  - Endpoint: `assignments/`
  - Method: `GET`

- `GET /domain-name/api/supervisor/assignments/<int:pk>/`
  - Description: Retrieve assignment details by ID.
  - Endpoint: `assignments/<int:pk>/`
  - Method: `GET`

- `PATCH /domain-name/api/supervisor/assignments/<int:pk>/`
  - Description: Update assignment details by ID.
  - Endpoint: `assignments/<int:pk>/`
  - Method: `PATCH`

- `DELETE /domain-name/api/supervisor/assignments/<int:pk>/`
  - Description: Delete assignment by ID.
  - Endpoint: `assignments/<int:pk>/`
  - Method: `DELETE`

- `GET /domain-name/api/supervisor/auto-assign/`
  - Description: Automatically assign service reports to engineers if suitable matches are found.
  - Endpoint: `auto-assign/`
  - Method: `POST`

- `POST /domain-name/api/supervisor/assign-report/<int:pk>/`
  - Description: Assign a service report to an engineer or contractor.
  - Endpoint: `assign-report/<int:pk>/`
  - Method: `POST`

- `POST /domain-name/api/supervisor/reject-report/<int:pk>/`
  - Description: Reject a service report.
  - Endpoint: `reject-report/<int:pk>/`
  - Method: `POST`
## Contractors App

Access the Contractors app by navigating to `contractors/`.

### Contractors App Endpoints
- `GET /domain-name/api/contractors/meetings/`
  - Description: Retrieve all meetings.
  - Endpoint: `meetings/`
  - Method: `GET`

- `POST /domain-name/api/contractors/meetings/`
  - Description: Create a new meeting.
  - Endpoint: `meetings/`
  - Method: `POST`

- `GET /domain-name/api/contractors/meetings/<int:pk>/`
  - Description: Retrieve meeting details by ID.
  - Endpoint: `meetings/<int:pk>/`
  - Method: `GET`

- `PATCH /domain-name/api/contractors/meetings/<int:pk>/`
  - Description: Update meeting details by ID.
  - Endpoint: `meetings/<int:pk>/`
  - Method: `PATCH`

- `DELETE /domain-name/api/contractors/meetings/<int:pk>/`
  - Description: Delete meeting by ID.
  - Endpoint: `meetings/<int:pk>/`
  - Method: `DELETE`

- `GET /domain-name/api/contractors/expenses-estimates/`
  - Description: Retrieve all expenses estimates.
  - Endpoint: `expenses-estimates/`
  - Method: `GET`

- `POST /domain-name/api/contractors/expenses-estimates/`
  - Description: Create a new expenses estimate.
  - Endpoint: `expenses-estimates/`
  - Method: `POST`

- `GET /domain-name/api/contractors/expenses-estimates/<int:pk>/`
  - Description: Retrieve expenses estimate details by ID.
  - Endpoint: `expenses-estimates/<int:pk>/`
  - Method: `GET`

- `PATCH /domain-name/api/contractors/expenses-estimates/<int:pk>/`
  - Description: Update expenses estimate details by ID.
  - Endpoint: `expenses-estimates/<int:pk>/`
  - Method: `PATCH`

- `DELETE /domain-name/api/contractors/expenses-estimates/<int:pk>/`
  - Description: Delete expenses estimate by ID.
  - Endpoint: `expenses-estimates/<int:pk>/`
  - Method: `DELETE`

## Engineering App

Access the Engineering app by navigating to `engineering/`.

### Engineering App Endpoints
- `POST /domain-name/api/engineering/self-assign/<int:pk>/`
  - Description: Assign a service report to yourself.
  - Endpoint: `self-assign/<int:pk>/`
  - Method: `POST`

- `POST /domain-name/api/engineering/accept/<int:pk>/`
  - Description: Accept an assignment.
  - Endpoint: `accept/<int:pk>/`
  - Method: `POST`

- `POST /domain-name/api/engineering/reject/<int:pk>/`
  - Description: Reject an assignment.
  - Endpoint: `reject/<int:pk>/`
  - Method: `POST`