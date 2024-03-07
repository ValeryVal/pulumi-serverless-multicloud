### Install Serverless module via NPM:

```
npm install -g serverless
```
If you don’t already have Node.js on your machine, install it first. 
If you don't want to install Node or NPM, 
you can install serverless as a standalone binary:
```
curl -o- -L https://slss.io/install | bash
```
####  This GCP project was created with Serverless template:
```
serverless create -t google-python
```
#### More templates you can find here:
```
serverless create --help
```
### Download GCP plugin
```
serverless plugin install -n serverless-google-cloudfunctions
```
### Install Google Cloud CLI following this [link](https://cloud.google.com/sdk/docs/install-sdk)

### Adjust your GCP account
Follow this [link](https://www.serverless.com/framework/docs/providers/google/guide/credentials) and make these steps:
- Create a Google Cloud Billing Account
- Create a new Google Cloud Project
- Enable the necessary APIs

### Authenticate to Google Cloud
```
gcloud auth application-default login
```
In logs after this command you can see:

>Credentials saved to file: [~\AppData\Roaming\gcloud\application_default_credentials.json]

- Copy this path to serverless.yml to field *credentials:* 

- Also in serverless.yml change field *project:* to the name of the project you've created.


### Deploy changes
```
serverless deploy
```