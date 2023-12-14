# Maintenance Management API

## Base URL
`domain-name/api/`
# Quick Navigation


- [Overview](#overview)
- [Common App Endpoints](#common-app-endpoints)
- [Clients App Endpoints](#clients-app-endpoints)
- [Accounts App Endpoints](#accounts-app-endpoints)
- [Estate App Endpoints](#estate-app-endpoints)
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
- `GET /domain-name/api/home-page/`
  - Description: Generate homepage.
  - Endpoint: `home-page/`
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
- `POST /domain-name/api/accounts/login/`
  - Description: Log in user.
  - Endpoint: `login/`
  - Method: `POST`
- `POST /domain-name/api/accounts/test-token/`
  - Description: Test authentication token.
  - Endpoint: `test-token/`
  - Method: `POST`
- `POST /domain-name/api/accounts/logout/`
  - Description: Log out user.
  - Endpoint: `logout/`
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

