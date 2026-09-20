# AGENTS.md

## Scope

These rules apply to the entire repository. Work in Traditional Chinese or English, following the language of the task.

## Git workflow

- Create a fresh worktree and an `agent/*` branch for every task.
- Never push directly to the default branch.
- The agent may push only `agent/*` branches and may open Draft pull requests.
- A human must approve merging, releases and production deployment.
- Do not rewrite shared history or run destructive Git commands.

## Safety and authority

- Never store credentials, OAuth tokens, API keys, private customer data or production exports in the repository.
- Do not spend money, purchase credits, change billing, accept contracts, send external communications, publish to production, or submit legal or grant material.
- Do not broaden GitHub, Slack, Google or model permissions.
- Stop and request human action when a task requires any prohibited action.

## Engineering quality

- Read existing documentation before changing code.
- Keep changes limited to the requested task.
- Run relevant tests and report exact results.
- Record material assumptions and unresolved risks in the Draft pull request.
- Before any deployment, increment the application version and keep UI labels, package and release metadata, diagnostics or telemetry, and backend version validation synchronized. Verify the deployed version live.
