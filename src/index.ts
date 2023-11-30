import { Octokit } from "@octokit/rest";
import { ENV, getEnv } from "./utils";

export const initOctokit = (env: ENV) => {
  const octokit = new Octokit({
    auth: env.accessToken,
  });
  return octokit;
};

const _main = async () => {
  const env = getEnv();
  const octokit = initOctokit(env);

  const {
    data: { login },
  } = await octokit.users.getAuthenticated();
  console.log(`Hello, ${login}!`);
};

export default function testDefault(): void {
  console.log("testWebpack console.log");
}

export function testWebpack(): void {
  console.log("testWebpack console.log");
}
