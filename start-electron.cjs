"use strict";

const { spawn } = require("node:child_process");
const electronPath = require("electron");

const environment = { ...process.env };
delete environment.ELECTRON_RUN_AS_NODE;

const child = spawn(electronPath, ["."], {
  cwd: require("node:path").resolve(__dirname, ".."),
  env: environment,
  stdio: "inherit"
});

child.on("exit", code => process.exit(code ?? 0));
