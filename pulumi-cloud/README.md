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
## Errors troubleshooting

#### error: Only public ip address types are supported by Azure currently.
Fixed with adding *external: true*
```ports: [{ port: 80, external: true}],```

#### error: Only a single replicable is supported in Azure currently.
fixed with deleting *replicas:2*

#### error: azure:containerservice/group:Group resource 'examples-nginx' has a problem: Invalid or unknown key. Examine values at 'examples-nginx.containers[0].protocol'.
fixed with deleting *protocol: "http"*. Then default TCP protocol is set. But container works with TCP.
```ports: [{ port: 80, external: true, protocol: "http"}],```

#### Container Group Name: "pulumi-nginxd5be97f0"): performing ContainerGroupsCreateOrUpdate: containerinstance.ContainerInstanceClient#ContainerGroupsCreateOrUpdate: Failure sending request: StatusCode=0 -- Original Error: Code="InvalidContainerPorts" Message="The ports '0' are invalid for container 'pulumi-nginx-nginx' in container group 'pulumi-nginxd5be97f0'. The port must be beteween 1 and 65535." 
Fixed with:
gives error: 
```
let nginx = new cloud.Service("examples-nginx", {
    containers: {
        nginx: {
            image: "nginx",
            memory: 128,
            port: 80
```
fixed:
```
let nginx = new cloud.Service("examples-nginx", {
    containers: {
        nginx: {
            image: "nginx",
            memory: 128,
            ports: [{ port: 80, external: true}],
```