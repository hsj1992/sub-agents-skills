# Profiles

Profiles are TOML documents with `name`, `verifier`, `model`, `forge`, `ci`, and
`policy` tables. `verifier.command` is required. Resolve and snapshot a profile
when a task starts; secrets are adapter inputs and are never profile values.

`profiles/example.toml` is portable and offline. Consumer-specific commands,
repository names, branches, and CI events belong in a compatibility profile.
