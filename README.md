# Gource Video

Extension upon https://github.com/toolmantim/tap-release to handle running gource and publishing to youtube on release.

Please read up the instructions to use the repo from the tap-release repo.

This requires youtube api credentials. 

Since Github does not support webhooks for accounts you do not own, there is a gitlab mirror at https://gitlab.com/viksrivat122446/aws-sam-cli-mirror which mirrors SAM-CLI's release and run's the CI pipeline on a tagged release to master 
and autopublishes it to youtube.

# Watch the Video
[<img src="https://img.youtube.com/vi/13rF7awO29U/maxresdefault.jpg" width="50%">](https://youtu.be/13rF7awO29U)

# In Progress
- [ ] Confetti Banner with release details such as commit log using github api
- [ ] Push to docker hub
