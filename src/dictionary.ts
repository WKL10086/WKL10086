import { Octokit } from "@octokit/rest";

export const getDictionary = async (octokit: Octokit) => {
  const { data: dictionary } = await octokit.rest.repos.getContent({
    owner: "WKL10086",
    repo: "WKL10086",
    path: "dictionary/word_list.txt",
    mediaType: {
      format: "raw",
    },
  });

  if (Array.isArray(dictionary)) {
    throw new Error("FILE_IS_DIR");
  }

  if ("content" in dictionary) {
    const content = Buffer.from(dictionary.content, "base64").toString();

    return content.split("\n");
  }

  return [];
};
