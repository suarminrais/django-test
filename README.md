## Issues
1. Solve the circular dependency and migration issues
2. Create API for owner sign-up
    - ![Screenshot](./images/register.png)
3. Create API for user login
    - ![Screenshot](./images/login.png)
    - ![Screenshot](./images/login-refresh.png)
4. Create API for company creation (This API can be accessed after user login)
    - ![Screenshot](./images/company.png)
5. Create API for registered new employee (Only Owner of company has access to it)
    - ![Screenshot](./images/employee.png)
6. Create django admin for User and Company models
    - ![Screenshot](./images/admin.png)
7. Create django command to filled the Authentication and Authorization Group in the django admin that all staff can only add and view all models 
    - ![Screenshot](./images/command.png)
8. If employee created from django admin, add validation for the company must not be null
    - ![Screenshot](./images/validation.png)
    - ![Screenshot](./images/validation-02.png)
    - ![Screenshot](./images/validation-03.png)
9.  Use OpenAPI schema based to showed all of the API endpoint
    - ![Screenshot](./images/open-api.png)
10. Use SQLlite3 as DB that already migrated with the models (put it in the project as POC)
