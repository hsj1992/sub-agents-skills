# Adapter Contracts

Implement `VerifierAdapter`, `ModelAdapter`, `ForgeAdapter`, and `CiAdapter`
from `trellis_mm.adapters.protocols`. Each operation returns an `Artifact` with
an exit code and provenance. Local and CI evidence must carry the exact commit
and tree observed by the producer. Forge and CI evidence additionally carries
repository/event identity where relevant. A non-zero exit code or mismatched
identity closes the gate regardless of model prose.
