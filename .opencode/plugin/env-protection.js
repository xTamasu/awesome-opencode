export const EnvProtection = async ({ project, client, $, directory, worktree }) => {
  return {
    "tool.execute.before": async (input, output) => {
      const fileName = output.args.filePath.split('/').pop();
      if (input.tool === "read" && fileName.match(/^\.env(\.|$)/i)) {
        throw new Error("Reading .env files is prohibited for security reasons. Use environment variables or configuration management instead.")
      }
    },
  }
}