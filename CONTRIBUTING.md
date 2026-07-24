# Contributing

Contributions should be reproducible, clearly named, and safe to share.

## File Naming

- Use lowercase `kebab-case` for new files and directories.
- Use descriptive names that identify the subject and purpose, such as `flux-character-consistency-test.md`.
- Use `.json` for ComfyUI workflow exports and `.md` for notes, prompts, tests, and guides.
- Add a date in `YYYY-MM-DD` format only when chronology is important.
- Keep related assets under a directory with the same descriptive base name.
- Do not commit model weights, credentials, private data, copyrighted source assets without permission, or generated files that are too large for normal Git use.

## Documentation

- State the tool, model, and version used whenever known.
- Record important settings, dependencies, inputs, expected results, and known limitations.
- Use relative links for files inside this repository.
- Remove secrets and personal filesystem paths from examples and logs.

## Commit Guidelines

- Create a dedicated branch for each focused change.
- Keep commits small and limited to one logical purpose.
- Write commit messages in the imperative mood, for example `Add FLUX prompt adherence test`.
- Avoid mixing unrelated workflow, prompt, documentation, and maintenance changes.
- Update `CHANGELOG.md` when a change materially affects the repository's content or organization.

## Pull Requests

- Explain what changed and why.
- List any models, tools, custom nodes, or assets required to reproduce the contribution.
- Describe how the content was checked.
- Link related issues or references when available.
- Request review before merging into `main`.
