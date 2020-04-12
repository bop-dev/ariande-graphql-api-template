# Offline Dev

Set up your .aws credentials, make a DynamoDB table named hangtime-dev

Install node (to run serverless-offline). I use nvm to manage my node versions.

Go to your hangtime-api folder:

`npm install`

`virtualenv -p python3 venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`sls wsgi serve -p 8000`

Run queries in Graphi at http://localhost:8000/graphql

## Run Tests

`TABLE_NAME=hangtime-test python -m pytest`

## Deploy

```console
sls deploy
```
