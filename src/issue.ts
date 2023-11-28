import { Octokit } from "@octokit/rest";

export const addLabel = async (octokit: Octokit, issueNumber: number) => {
  await octokit.issues.addLabels({
    owner: "WKL10086",
    repo: "WKL10086",
    issue_number: issueNumber,
    labels: ["wkldle"],
  });
};

export const closeIssueWithComment = async (
  octokit: Octokit,
  issueNumber: number,
  comment: string
) => {
  await octokit.issues.createComment({
    owner: "WKL10086",
    repo: "WKL10086",
    issue_number: issueNumber,
    body: comment,
  });
  await octokit.issues.update({
    owner: "WKL10086",
    repo: "WKL10086",
    issue_number: issueNumber,
    state: "closed",
    state_reason: "completed",
  });
};
