---
name: trellis-multimodel-goal
description: "Run an evidence-driven Trellis lifecycle with project profiles and explicit verifier, model, forge, and CI adapters."
---

# Trellis Multimodel Goal

This skill is the routing index for the reusable lifecycle. Initialize a task
with a profile, snapshot the resolved policy, and advance one phase at a time.
Adapters produce sealed artifacts; the core accepts them only when the producer
exit code is successful and the `head_sha` and tree fingerprint are still live.

Read `references/profiles.md` when configuring a consumer and
`references/adapters.md` when implementing an adapter. The offline fake
adapters and `mm-smoke` provide a network-free contract check.

The source repository is canonical. Consumers use a versioned export generated
by `scripts/export_skill.py`; they do not maintain a hand-edited implementation.
