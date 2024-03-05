# Azure Functions

Refer to [Serverless docs](https://serverless.com/framework/docs/providers/azure/guide/intro/) for more information.

### Installation

#### Install serverless module via NPM:

```
npm install -g serverless
```
If you don’t already have Node.js on your machine, install it first. 
If you don't want to install Node or NPM, 
you can install serverless as a standalone binary:
```
curl -o- -L https://slss.io/install | bash
```
### Creating A Service
Create a new serverless project, then follow the prompts.
```
serverless
```
Move into the newly created directory
```
cd your-service-name
```
### Installing Azure Functions Provider Plugin
You should have azure plugin installed:
```
npm i --save serverless-azure-functions
```
or without npm:
```
serverless plugin install -n serverless-azure-functions
```
### Create project from template

Create basic Python template
```
serverless create -t azure-python
```
Or see the full list of templates:
```
serverless create --help
```
### Deploy

Having Azure plugin and all files ready you can deploy changes.
During this authorization to Azure will happen.
```
sls deploy
```

### To authorize to Azure manually:

Login to Azure
```
az login
```
This will give you a code and prompt you to visit [azure login portal.](aka.ms/devicelogin)

#### If you have multiple accounts, you can specify the "current" subscription for the session by running

```
$ az account set -s <subscriptionId>
```
#### To get your subscription and tenant id:
```
az account list
```