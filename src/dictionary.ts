// import { Octokit } from "@octokit/rest";

// export const getDictionary = async (octokit: Octokit): Promise<string[]> => {
//   const { data: dictionary } = await octokit.repos.getContent({
//     owner: "WKL10086",
//     repo: "WKL10086",
//     path: "dictionary/word_list.txt",
//     ref: "wkldle",
//     mediaType: {
//       format: "raw",
//     },
//   });

//   if (Array.isArray(dictionary)) {
//     throw new Error("FILE_IS_DIR");
//   }

//   if (!("content" in dictionary)) {
//     return [];
//   }

//   const content = Buffer.from(dictionary.content, "base64").toString();

//   return content.split("\n");
// };

// // TODO: use a better random number generator
// export const pickRandomWord = (dictionary: string[]): string => {
//   const randomIndex = Math.floor(Math.random() * dictionary.length);
//   return dictionary[randomIndex];
// };
