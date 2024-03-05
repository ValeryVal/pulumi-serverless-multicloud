#### Container resource Service example was taken from here https://github.com/pulumi/pulumi-cloud/blob/master/examples/containers/index.ts
### Prerequisites
Install [Pulumi](https://www.pulumi.com/docs/install/) 

Configure [AWS](https://www.pulumi.com/registry/packages/aws/installation-configuration/) and/or [Azure](https://www.pulumi.com/registry/packages/azure/installation-configuration/) credentials

Make sure Docker is installed and running.

### Installing the project:
```
mkdir container-quickstart && cd container-quickstart && pulumi new javascript
```
Make sure you have these dependencies in package.json:
```
"dependencies": {
        "@pulumi/cloud": "dev",
        "@pulumi/cloud-aws": "dev",
        "@pulumi/cloud-azure": "dev"
    }
```
install dependencies:
```
npm install
```

### Before deploying to AWS:
```
pulumi config set cloud:provider aws
pulumi config set aws:region us-west-2
pulumi config set cloud-aws:useFargate true
or 
pulumi config set cloud:ecsClusterARN true
```

### Before deploying to Azure:
```
az login
az account set -s f1414fb0-566b-41f5-a09b-41d9981ce0dd
pulumi config set cloud:provider azure
pulumi config set cloud-azure:location eastus
```
### Pulumi commands

Deploy to AWS or Pulumi
```
pulumi up
```

To create new stack e.g. Azure:
```
pulumi stack init azure
```

To get list of stacks and see current stack:
```
pulumi stack ls
```

To switch to another stack:
```
pulumi stack select your-stack-name
```
### Azure commands
Login to Azure:
``` 
az login
```
Show current subscription info:
```
az account show
```
Show list of all subscriptions in account:
```
az account list
```