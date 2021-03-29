**Project based in API REST - PYTHON/DJANGO**

- A simple API that allows us to register and manage loans and payments.

---

# LOANS API REST 

The main functionalities of this API are:

1. Register a loan. The data inputs of each loan are value, interest_rate, bank, client and created (date).
2. Register a payment. The data inputs of each payment are value, loan (id) and created (date).
3. Return some extra details about the loan, like the manager's IP and the outstanding balance.
4. The manager is only allowed to see the loans and payments registered by him/her.

---

## Peculiarities Explanations

1. This project uses compound interest to calculate the outstanding balance.
2. This project uses a monthly interest rate.
3. The interest rate and the values in the models are decimal numbers with two decimal places.
4. The payment "view" have two different serializers. One for the "retrieve" endpoint, and another one to the "list" endpoint. The "retrieve" endpoint shows more information than the other one.
5. This SQL VIEW used in this project is in "loans_api/loans/db/".

---

## JWT Authentication

This API uses JWT to authentication. It means that you have to use one JSON Web Token to call every endpoint. In order to do that, you'll have to follow this procedure (or use the "Authorize" button in Swagger UI):

1. Get access token from **_"/api/token/"_**:

```
{
  "email": "admin@email.com",
  "password": "loans1234"
}
```

2. Insert this token in the request's HEADER after 'Bearer ', like the example below:

```
Authorization: Bearer aaaaaaaaaaaaa.bbbbbbbbbbb.ccccccccccc
```

3. If your token expires, you'll have to use the refresh token from the first step into the **_"/api/token/refresh/"_** call:

```
{
  "refresh": "ddddddddddddd.eeeeeeeeeeeeeee.fffffffffffff"
}
```
_This call will return another access token, that you'll have to use in the second step._

---

## Swagger

This API uses Swagger as a documentation tool. In order to use JWT Authentication and Swagger UI, you have to follow the steps in previous section and use the Authorize button (in Swagger UI) to increment the requisition's header.

* In this project the root is redirecting to this swagger documentation endpoint. It can be accessed in http://localhost:8000/ 

---

## Endpoints

If you rather use Postman to test the endpoints, they are listed below:

1. **(POST)** **_"/api/token/"_** - *Authenticate sending email and password to get access token and refresh token (JWT).*
2. **(POST)** **_"/api/token/refresh/"_** - *Send refresh token to get another access token (JWT).*
3. **(GET)** **_"/loans/{id}"_** - *Returns a specific loan (with details).*
4. **(GET)** **_"/loans/"_** - *Returns all loans registered.*
5. **(POST)** **_"/loans/"_** - *Register a new loan.*
6. **(GET)** **_"/payments/{id}"_** - *Returns a specific payment.*
7. **(GET)** **_"/payments/"_** - *Returns all payments registered.*
8. **(POST)** **_"/payments/"_** - *Register a new payment*

---

## Endpoints - EXTRA

Some filters were implemented in the: **(GET)** **_"/payments/"_** endpoint. 

Filter by attributes:

* loan (loan ID)

Filter by an specific date, or between dates :

_date format: 2021-01-01_

* created
* created_before
* created_after 

_If you would like, you can also use them in the **Swagger UI**._

---

## Utils

I've created 17 Makefile commands to use in this project. However, you'll just need to use 6 of them to run locally:

* **_make setup_**: To set up the entire environment to run the project. Only need to use this command once.
* **_make start_**: Create the project's container and run the project.
* **_make stop_**: Stop the project's container.
* **_make tests_**: Run all tests in the project.
* **_make coverage_**: Measures code coverage during test execution.
* **_make clean_**: Clean this project's containers, images, volumes and network from your computer. It's recommended to read this Makefile command before you use it, to make sure that you do not have other projects with similar names.

---

## Django Admin

This API model's are also registered on the Django Admin.

_To make it easy to analyse this project... when the project runs for the first time, one super user is automatically created (username:admin, password:loans1234). You'll have to use this user to access the admin area. If you'ld like, you can create your own super user with the "make createsuperuser" command and delete the previous one in the Django admin._

_Django's admin can be accessed in:_ http://localhost:8000/admin/

---

## Run Locally


1. Make sure you have the Docker and Docker-compose installed.
2. You'll also need to generate one Django **SECRET KEY** and insert it in the **_develop.env_** file. I've already inserted a random secret key in the file, however is highly recommended to change it by a new one. (The key can be generated here: https://djecrety.ir/)
3. In the first time running the project (and just in the first one) you will have to use the command _make setup_ to create the project's image.
4. Then, use _make start_ to run it locally. Next time, you will just have to use _make start_ and _make stop_ commands.
5. This project runs in: http://localhost:8000/

---

## Tests

There are 15 tests being tested in this project. The characteristics of this tests can be readden below:

1. Three unit tests running in the users app.
2. Two unit tests running in the loans app.
3. Seven integration tests running in the loans app.
4. Three custom tests running in the loans app.
5. There is a specific command to run the tests (**_make tests_**). However, the tests also runs when it's necessary to build the project's image. 
6. There is a specific command to run the tests coverage (**_make coverage_**).

---

## Logs

There are 3 ways to analyse logs in this application:

1. **_make start_api_**.
2. **_make start_**, then **_make logs_**.
3. **_make start_api_** and **_make logs_** (in separated tabs).

---

## Requirements

* **DOCKER-COMPOSE**: 1.27.4
* **DOCKER**: 19.03.13

