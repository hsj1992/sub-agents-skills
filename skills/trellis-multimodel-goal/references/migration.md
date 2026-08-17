# Migration and Rollback

Before switching a consumer, preserve its existing wrappers and representative
artifacts as a consumer-owned compatibility baseline. Compare verifier, model,
forge, and CI adapter outputs against that baseline before enabling the generic
lifecycle for delivery.

If parity is not established, keep the consumer's existing integration and
remove only the generated skill export. Application and database rollback are
outside this tooling migration. Distribution copies are regenerated from the
canonical skill source and checked by digest.
