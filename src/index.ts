import "dotenv/config";

import * as core from "@actions/core";
import { createOrUpdateTextFile } from "@octokit/plugin-create-or-update-text-file";
import { Octokit } from "octokit";

const MyOctokit = Octokit.plugin(createOrUpdateTextFile).defaults({
  userAgent: "WKL10086-README-Action",
});

const octokit = new MyOctokit({
  auth: process.env.GITHUB_TOKEN,
});

const main = async () => {
  const getReadme = await octokit
    .request("GET /repos/{owner}/{repo}/contents/{path}", {
      owner: "WKL10086",
      repo: "WKL10086",
      path: "README.md",
    })
    .catch((e: any) => {
      console.error("Failed: ", e);
      core.setFailed(e.message);
    });

  // console.log("getReadme.data: ", getReadme.data);

  const content = Buffer.from(getReadme.data.content, "base64").toString();
  console.log("content: ", content);
};

main();
