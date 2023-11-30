import "dotenv/config";

export interface ENV {
  issueTitle: string;
  issueCreator: string;
}

export const getEnv = (): ENV => {
  const issueTitle = process.env.ISSUE_TITLE ?? "";
  const issueCreator = process.env.ISSUE_CREATOR ?? "";

  const env: ENV = {
    issueTitle,
    issueCreator,
  };

  return env;
};
