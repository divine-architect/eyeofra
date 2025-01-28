<p align=center>
  <br>
  <img src="https://raw.githubusercontent.com/divine-architect/eyeofra/refs/heads/main/img/eyeofra.png" style="width:50%;height:20%;"/>
  <br>
  <span>One-stop OSINT tool to link digital identities across multiple sites and domains.
</span>
  <br>
</p>

## EyeOfRa
EyeOfRa aims to be the Swiss Army Knife of people centric OSINT. Some of it's planned features are:
- To build upon the `sherlock project` (check for usernames on sites without as many false positives which is currently an issue with the sherlock tool)
- Use `holehe` and improve on false positives, similar to the previous one
- Use face recognition algorithms paired with browser/web testing software to match profile pictures and other visual cues.
- Explore image metadata for other clues to link multiple digital identities, implementing multiple CV and image processing techniques.
- Use dorking techniques via templating to get the most of the best OSINT tool to ever exist (the web browser).
- Generate a unified report with the help of Gen AI.

## Motivation
- Most OSINT tools that aren't for law-enforcement are either paid or hard to [setup](https://www.reddit.com/r/github/s/BhVD6gIscZ). Hence the need for a truly FOSS tool that's easy to use.
- Vet the contributions made to the repo thoroughly, the `sherlock project` has a bunch of suspicious PRs which I (personally) don't like even though they are [closed](https://github.com/sherlock-project/sherlock/issues/2389).
- To create a unified tool that does most of my work as an Offsec professional

## Todo
- [ ] Implement username checker (port from `sherlock`)
- [ ] Implement email checker (port from `holehe`)
- [ ] Implement browser automation/testing software paired with image processing to fetch profile pictures and compare persons
- [ ] Explore image metadata for clues using exiftool
- [ ] Dorking via templating and Gen AI
- [ ] Automated AI based report generator
- [ ] Link to location from metadata or IP (if any are found)
- [ ] Write proper documentation!!

## Contribution
Feel free to open an issue or a PR (preferably an issue to discuss the topic).
**Note**: Regardless of the content of the PR, the PR will merged only if it's from reputable GitHub account(s) with susbstantial contribution to open source projects, this is to ensure high quality code while also preserving the security of
the project.

## License
This tool/project is licensed under the MIT license.
