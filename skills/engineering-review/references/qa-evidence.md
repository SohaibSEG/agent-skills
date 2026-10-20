# Evidence handoff to authorized QA

Engineering Review and its specialists inspect source and supplied evidence only.
The caller's separate validation workflow may execute tests, browser interactions,
screenshot capture or database experiments when authorized. Selecting a specialist
or requesting missing evidence does not itself authorize execution. In Carli, the
Carli coordinator owns that phase and its isolated environment skill owns setup.

For each material proof gap, record a small evidence request in the existing ledger:

| Field | Needed content |
|---|---|
| Identity | Request ID, reviewer, candidate/base, affected claim and source path |
| Scenario | Actor/permissions, starting state/data, normal entry and relevant failure/return path |
| Observation | Expected visible result plus durable state/downstream effect; what would falsify it |
| Capture | Screenshot/recording, interaction/focus trace, API/database assertion, plan or concurrency result as appropriate |
| Context | Environment/version, viewport/theme/locale where relevant, synthetic dataset and provenance |
| Result | Not executed / blocked / executed with result; artifact, executor, identity and limits |

The validator returns evidence to the requesting specialist for assessment and
finding closure. Keep source inference, supplied evidence and executed observations
separate. A changed candidate/base invalidates affected evidence; record why any
prior evidence remains applicable. A visual capture must identify its actual build
and state. Missing essential evidence keeps the corresponding readiness obligation
pending; it does not require inventing a defect or prohibit reporting completed
source review.

Use screenshots to compare appearance and states, recordings/interaction traces
for transitions and keyboard/focus behavior, and backend/database assertions for
persistence, audit and authorization. Static pictures and route mocks cannot prove
an end-to-end task. Synthetic realistic records must avoid sensitive information.
An agent completing a known script is functional evidence, not representative-user
research or proof of discoverability. Read-only review can assess screenshots
provided by the user without running the application.
