<!-- WARNING: This README is generated automatically
-->

<!-- markdownlint-disable no-inline-html -->

# Security Misconfigurations

## GitHub Actions pull_request_target


Detects the use of the pull_request_target trigger in GitHub Actions workflow files.
This trigger runs in the context of the base repository with access to secrets,
even for pull requests from forks, which can lead to secret exfiltration if
combined with untrusted input execution or code checkout from the PR branch.

_version: v0.1_

**Comments / Notes:**


- Detects pull_request_target trigger in GitHub Actions workflow YAML files

- This trigger grants access to secrets and is dangerous when combined with untrusted code execution

- See: https://jessehouwing.net/github-actions-learnings-from-the-recent-nx-hack/
  

<details>
<summary>Pattern Format</summary>

```regex
pull_request_target
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:(?:\n|\r\n|\A)[ \t]*(?:-[ \t]+)?|[\[,][ \t]*)
```

</details><details>
<summary>End Pattern</summary>

```regex
[ \t]*(?:[:\],\n\r]|\z)
```

</details>
