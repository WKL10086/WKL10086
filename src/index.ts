import { default as _core } from "@actions/core";
import { Context } from "@actions/github/lib/context";
import { Octokit } from "@octokit/rest";
import { getEnv } from "./utils";

export async function dailyInit(
  octokit: Octokit,
  context: Context,
  core: typeof _core
) {
  console.log("context", context);
  console.log("core", core);

  const {
    data: { login },
  } = await octokit.users.getAuthenticated();
  console.log(`Hello, ${login}!, daily init`);
}

export default async function main(
  octokit: Octokit,
  context: Context,
  core: typeof _core
) {
  const _env = getEnv();

  console.log("context", context);
  console.log("core", core);

  const {
    data: { login },
  } = await octokit.users.getAuthenticated();
  console.log(`Hello, ${login}!, main`);
}
