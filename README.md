# **B-market** web service
+ This is `B-market` webservice repo, created to contribute in, includes `dev` branch and `prod`
## **`B-market`** - Web service *(website)* for selling/buing/investing in small and medium businesses
This repo only includes `B-market` webservice, a single microservice

## **Included:**
1. RESTful api, written in `Flask`
2. Frontend client on `jinja2`
3. Userful commands for dev environment
4. `Docker` files for testing local deployement
5. Autotests (in `python` and `bash`)
6. Docs
## **Architecture:**
+ We are using `MVC`, model based architecture
+ Frontend renders on serversite, non-endless routing
+ Provided `JWT` token auth
+ Using caching *(`Redis`)* for boost perfomance
+ Using custom model class (no `SQLAlchemy`)
+ Launch on prod without `venv`, only `Docker` container with `docker-compose`
+ No load ballancer
+ `Nginx` reverse proxy routing
+ No clusters (at yet)

## **Routings(pages)**
Working at....

## **Tech stack:**
+ `Python3`
+ `Flask`
+ `Jinja2`
+ `js, html, css`
+ `Postgresql`
+ `Redis`
+ `postman`
+ `vscode dev tunnels`
+ `docker`
+ `nginx`
+ `bash`

## **How to setup:**
This is complete guidence for setting up project for developing
### 1st method:
1. Clone repo, `dev` branch
2. Run docker-compose up
- this will create container with DB's and application (if everything installed)
### 2nd method:
1. Clone repo, `dev` branch
2. Install dependencies via same-nammed script
3. Go to source dir
4. Run `server.py`

## **How to autotest:**
+ This will be soon updated, once we hit all tests
## **Error handling:**
+ This will be soon updated
+ More detailes could be found in `docs` dir, via `main` branch
