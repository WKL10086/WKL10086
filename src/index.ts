import { Octokit } from "@octokit/rest";
import { ENV } from "./utils";

const _initOctokit = (env: ENV) => {
  const octokit = new Octokit({
    auth: env.accessToken,
  });
  return octokit;
};
