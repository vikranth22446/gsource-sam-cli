const getConfig = require("probot-config");
const compareVersions = require("compare-versions");
const hashUrl = require("./hash-url");
const log = require("./log");
const execSync = require("child_process").execSync;

const versionNumber = version => {
  return version.replace(/^v/, "");
};

module.exports = async ({ app, context, configName }) => {
  const config = (await getConfig(context, configName)) || {};
  let { asset, url, tap, template, branches } = config;
  const [owner, repo, path] = (tap && tap.split("/")) || [];

  if (!branches) {
    branches = ["master"];
  }

  if (!owner || !repo || !path || !template) {
    log({
      app,
      context,
      message: `No valid config found`,
      info: { configName, config }
    });
    return;
  }

  let releases = await context.github.paginate(
    context.github.repos.getReleases(context.repo()),
    res => res.data
  );

  releases = releases
    .filter(r => !r.draft)
    .sort((r1, r2) => compareVersions(r2.tag_name, r1.tag_name));

  if (releases.length === 0) {
    log({ app, context, message: `No releases found` });
    return;
  }

  const latest = releases.filter(r => !r.prerelease)[0];

  code = execSync(
    "docker build -t ffmpeg_gource_sam_cli . && docker run -it ffmpeg_gource_sam_cli -v oputput_videos:output_videos -e SAM_CLI_TAG_NAME=" +
      "'" +
      latest.tag_name +
      "'"
  );

  log({
    app,
    context,
    message: `Uploaded Video to Youtube`
  });
};
