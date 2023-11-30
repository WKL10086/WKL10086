import { Octokit } from "@octokit/rest";
import { ENV, getEnv } from "./utils";

export const initOctokit = (env: ENV) => {
  const octokit = new Octokit({
    auth: env.accessToken,
  });
  return octokit;
};

export default async function main() {
  const env = getEnv();
  const octokit = initOctokit(env);

  const {
    data: { login },
  } = await octokit.users.getAuthenticated();
  console.log(`Hello, ${login}!`);
}
