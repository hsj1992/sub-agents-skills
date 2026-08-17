# Migration and Rollback

`baseline/cnsdigital` is a frozen import of the original implementation. Compare
its artifacts with the new core and compatibility profile before switching a
consumer. If parity is not established, keep the consumer's existing wrappers
and remove only the generated export; no application or database rollback is
needed. Distribution copies are regenerated from this repository and checked by
digest.
