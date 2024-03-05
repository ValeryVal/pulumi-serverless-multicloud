"use strict";
const cloud = require("@pulumi/cloud");

let port = 5000

let service = new cloud.Service("pulumi-flask-app", {
    containers: {
        "flask-app-hello": {
            build: "./python_app",
            memory: 128,
            ports: [{ port: port, external: true }],
        },
    },
});
// export just the hostname property of the container frontend
exports.url = service.defaultEndpoint.apply(e => `http://${e.hostname}:${port}`);


