import "dotenv/config";

export interface ENV {
  mode: "DAILY" | "MAIN";
  accessToken: string;
  issueTitle: string;
  userName: string;
}

export const getEnv = (): ENV => {
  const mode = (process.env.MODE as "DAILY" | "MAIN") ?? "MAIN";
  const accessToken = process.env.ACCESS_TOKEN ?? "";
  const issueTitle = process.env.ISSUE_TITLE ?? "";
  const userName = process.env.USER_NAME ?? "";

  const env: ENV = {
    mode,
    accessToken,
    issueTitle,
    userName,
  };

  return env;
};
