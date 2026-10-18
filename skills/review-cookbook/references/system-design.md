# System-design review: challenge the model, not just the patch

Use this before the implementation checklists when a change affects domain meaning, data relationships, lifecycle, authority, module contracts, execution topology or growth assumptions. Review the affected system, not the whole repository. This is review-only: inspect, reason from evidence, run only authorized safe checks, and recommend. Do not implement a redesign or repair a migration.

The objective is a defensible decision: **does this design express the real rule, enforce it through every affected path, and remain understandable and operable under the required conditions?** Architecture names and attractive diagrams are not evidence.

## 1. Separate the reported symptom from the actual obligation

1. Describe the actor, attempted action, observed failure and required outcome without naming the proposed solution. Compare the issue, discussions, contracts and current implementation; mark disagreements.
2. Identify what the proposed change assumes caused the failure. Inspect a counterexample that would distinguish that explanation from a different cause. A tool, fixture or environment failure is not automatically a product defect.
3. State the invariant and its scope: what must always hold, for whom, and during which states? Separate required behavior from desirable future capability. Do not preserve an accidental implementation rule merely because tests encode it.
4. Convert vague claims into scenarios: trigger, operating conditions, affected operation, expected response and observable measure. Use measured workloads or approved targets; mark unknowns instead of inventing performance requirements.

**Review output:** a short problem statement, the required rule, any established violation and its causal evidence, and unresolved product decisions. The proposed change may already satisfy the rule. Ask product only when meaning is unresolved; do not ask the user to find facts available in code.

Scenario-based evaluation helps expose trade-offs rather than declaring a design universally good. This is a lightweight application, not a claim to perform the full [SEI Architecture Tradeoff Analysis Method](https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/).

## 2. Reconstruct the model from storage to business meaning

1. Inspect schema, constraints, models, serializers, commands and actual readers. Record entity identity, scope, cardinality, optionality, lifecycle and historical references. A diagram inferred from class names is insufficient.
2. Separate dimensions that vary independently. For each overloaded category or status, ask whether it represents presentation, capability, commercial classification, schedule, lifecycle or evidence. Identify which rules consume each dimension.
3. Enumerate supported and forbidden combinations. Ask where invalid combinations are prevented. Several booleans may permit contradictions; a single giant enum may incorrectly couple independent choices. Recommend neither mechanically.
4. Distinguish ownership questions: who configures the value, who is authorized to change it, which module enforces its meaning, and which stored record is authoritative? These need not be the same owner.
5. Inspect consumers for hidden cardinality assumptions: first item only, a scalar field for a collection, display text used as identity, or uniqueness that exists only in a form.

**Working map:**

| Fact or relationship | Business meaning and scope | Authority and allowed writers | Consumers and decisions | Forbidden state / enforcement |
|---|---|---|---|---|
| A changed fact | What it means, not its field name | Actual source and commands | Who relies on it and why | Constraint, policy or identified gap |

Do not impose one universal model on concepts that legitimately differ between business contexts. Record explicit translation and ownership at their interfaces. [Fowler: Bounded Context](https://martinfowler.com/bliki/BoundedContext.html).

## 3. Follow decisions through the complete lifecycle

1. Trace the normal entry point and alternate writers into authoritative state, derived representations and final decisions. Include imports, generation, transfers, administrative actions and background execution when supported.
2. At every transformation, record what information is copied, derived, defaulted, discarded or reinterpreted. Check whether a missing or unknown value silently becomes a plausible but wrong value.
3. Follow the result into operational actions, user-visible status, billing or reporting where applicable. Verify the actual fields read; names such as “type” or “category” do not establish semantics.
4. Repeat the trace for edit, regenerate, renew, cancel, correct and retry. Determine whether the action affects one record, a membership group, future occurrences or historical outcomes. Inspect partial completion and inverse actions.
5. Compare the user's screen with the decision-making state. A screen may show a current configuration while the operation correctly uses a historical snapshot—or may conceal a genuine contradiction. Establish which before reporting a defect.

**Review output:** one compact path showing the actual writer, transformation, authoritative fact, decision and sink, with code locations. Identify any exact point where meanings diverge, or explain why the relevant transformations preserve the rule. Do not replace this with a list of touched files.

## 4. Establish consistency, identity and time boundaries

1. For each invariant, list the records that must agree when the operation completes and the owner that can enforce that agreement. Inspect membership and references before recommending a transaction or lock.
2. Distinguish immediate consistency from permitted delayed propagation. For delayed views, establish acceptable staleness, version/order handling, recovery and whether actions revalidate against authority. A copied read model is not automatically competing truth.
3. Separate stable identity from versions. Distinguish occurrence time, effective time and the time information became known where those differ. Determine whether consumers need current policy, policy at the event time, or policy known when the decision was made. A timestamp alone does not specify this; inspect queued work when policy changes between submission and execution.
4. Inspect the effects of editing a template or configuration on already-created records. Determine which values should remain linked and which should be snapshots. Check corrections, overlapping versions, deletion and retention against supported business rules.

**Challenge:** could two supported commands each succeed locally while leaving the overall obligation false? If yes, identify the interleaving and affected state rather than merely requesting “more transactions.”

Related concepts: [DDD aggregates](https://martinfowler.com/bliki/DDD_Aggregate.html) group objects with an integrity owner; [Temporal Object](https://martinfowler.com/eaaDev/TemporalObject.html) distinguishes continuing identity from versions. Neither requires a particular ORM, class hierarchy, or event-sourced architecture. Fowler labels the temporal material as draft guidance.

## 5. Evaluate responsibility and coupling

1. Inventory existing modules, contracts and capabilities before recommending new infrastructure. Identify where callers already share policy and where apparently similar paths intentionally differ.
2. List everything callers must know to use the interface: arguments, ordering, configuration, scope, errors, retries and transaction obligations. A small method signature can still expose a large conceptual burden.
3. Inspect whether callers repeat internal policy or coordinate several private operations to preserve one invariant. Recommend moving that responsibility to a coherent owner when a demonstrated bypass or coupling problem follows.
4. Apply a conceptual removal check: if the abstraction disappeared, would necessary complexity spread into callers or would only forwarding code disappear? Do not edit anything to perform this review.
5. Distinguish logical separation from deployment separation. A module, separate process and separate service introduce different costs. Require a concrete isolation, ownership or capacity benefit before recommending network boundaries.

**Review output:** the responsibility owner and what callers need to know. If responsibility is misplaced, identify the causal defect and a smaller coherent contract; otherwise retain the sound existing boundary. Avoid line-count rules, pass-through layers and generic “manager” modules.

The [Ousterhout–Martin discussion](https://github.com/johnousterhout/aposd-vs-clean-code) is useful for examining complexity and decomposition trade-offs, not choosing an author whose style rules automatically win.

## 6. Stress growth, failure and operation

1. Name the growth variables: active entities, relationships, retained versions, concurrent operations and fan-out. Estimate how rows, queries, payloads, memory and work grow. For pairwise relationships, distinguish sparse supported links from materializing every possible pair.
2. Find the scarce resource and where waiting accumulates: connection pool, lock, worker, remote quota, memory or browser DOM. Inspect bounds, backpressure and fairness between tenants or heavy and light requests.
3. Draw failure windows around commit, dispatch, remote acceptance and acknowledgement. Check duplicate, late and out-of-order work, cancellation, expired ownership and retry exhaustion. Separate evidence that the calculation works from evidence that the delivery protocol works.
4. Inspect how an operator detects, diagnoses and recovers a stuck or ambiguous operation. Require an attributable state and safe recovery path where the business needs one; logs alone may not establish whether an external action committed.
5. Verify security and configuration follow the same ownership model: scoped reads/writes, trust transitions, cache/job identities and explicit context. Changing transport must not accidentally change the business rule or authorization.

**Review output:** any credible bottleneck or failure mode, its mechanism, evidence and the smallest meaningful validation. If none is established within the supported conditions, say so without inventing one. “Use a queue,” “add caching” and “scale horizontally” are not solutions without identifying the limiting resource and new consistency costs.

Bounded work and overload response should be evaluated as system behavior; see [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/). A thought experiment supports risk identification, not a measured throughput claim.

## 7. Try to falsify the design

Select the counterfactuals relevant to supported behavior; do not invent requirements merely to create findings. Before checking a case, state the observable prediction that distinguishes the competing designs: under one representation this produces X, under the other Y. Capture the result as a short evidence record, not a narration of private deliberation.

| Challenge | Evidence to seek |
|---|---|
| Rename or translate a label without changing meaning | Policy remains attached to explicit identity/capability |
| Create the same fact through another supported writer | The same invariant holds without screen-specific repair |
| Change one independent dimension | Unrelated pricing, eligibility or lifecycle meaning does not change accidentally |
| Edit a template after instances or financial records exist | Current and historical semantics follow the specified contract |
| Repeat, overlap or reverse an operation | Membership, authority and durable outcomes remain valid |
| Delay one consumer or change execution mode | Authority, freshness and failure states remain explicit |
| Add the next documented variation | The rule has an intelligible owner; changes do not require synchronized exception lists everywhere |
| Grow the dominant input or deny a dependency | Work is bounded and recovery is defined rather than silently losing correctness |

Label each conclusion as source-proven, runtime-observed, contradicted or unresolved. Use a compact ledger: hypothesis → discriminating case/prediction → evidence → conclusion. Inspect the strongest existing guard, constraint, snapshot or consumer check that might prevent the alleged failure; explain why it does or does not. Retain a rejected hypothesis in the ledger when its counterevidence materially changes the recommendation; exclude it from actionable findings. A credible future variation can compare maintainability; it is a blocker only when it exposes a current required rule or an explicitly committed requirement.

## 8. Compare alternatives and defend one recommendation

1. Assess the proposed patch on its own merits: which counterexample does it remove, and does any supported path still violate the rule?
2. Describe the smallest complete correction to the responsible representation or owner. Preserve existing identity and sound contracts wherever possible. A new model is not inherently cleaner than completing an existing one. The submitted patch may already be the smallest complete solution; in that case treat them as one option and do not demand further changes.
3. Consider a materially different alternative only when it reveals a real trade-off. Do not manufacture three designs or produce a full redesign for a local correction.
4. Compare alternatives against the same conditions: invariant coverage, caller knowledge, supported extension, operational failure, data transition, user flow and change surface. Record costs as well as benefits.
5. Recommend one option with evidence, its main downside, and what new evidence would change the recommendation. Do not simply endorse the latest suggestion from the author or user.

| Option | Does the rule hold on all affected paths? | Main benefit / cost | Changed contracts and data | Required proof |
|---|---|---|---|---|
| Proposed patch | Evidence or counterexample | Concrete trade-off | Actual scope | Claim to verify |
| Smaller or complete correction, only if different | Why it closes an established gap | Preserved contracts / added cost | Necessary scope | Distinguishing check |

Separate read and write needs when justified, but do not escalate that observation automatically into distributed CQRS. [Fowler's CQRS guidance](https://martinfowler.com/bliki/CQRS.html) explicitly discusses its added complexity. Likewise, repeated syntax does not prove shared policy: see [Sandi Metz on wrong abstractions](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction).

## 9. Bound the recommendation and its transition

1. Trace the proposed correction through storage, public contracts, generated data, background work, UI and downstream consumers. Count changed obligations, not just files. Identify behaviors that could be lost by simplifying the model.
2. Separate necessary changes from optional cleanup and speculative capability. Stop at unchanged contracts whose validity has been demonstrated. A large causal scope is a finding to explain, not authorization to implement it.
3. Assess existing data and overlapping deployments. Identify deterministic conversions, ambiguous records, compatibility windows, resumable backfills and the completion condition for retiring old paths. Do not assume live tenants, empty data or a clean cutover without evidence.
4. Distinguish application rollback from data reversibility; a forward migration may need a forward repair. Recommend explicit recovery and evidence for the supported transition rather than promising rollback universally.

**Review output:** the necessary scope, affected consumers, transition risks and any product or authorization decision needed. The [evolutionary database design guidance](https://martinfowler.com/articles/evodb.html) informs controlled transitions; it does not justify permanent dual authority or an unrequested broad refactor.

## 10. Return a decision brief, not a checklist recital

Use the parent skill's report format: consequential findings first, followed by this design brief as supporting evidence and recommendations. Ground it in three compact artifacts: the fact/authority map, an end-to-end causal trace, and the counterexample ledger. Keep detailed maps available as evidence; show only what the decision needs. Follow supported paths capable of violating the changed invariant, not every lifecycle in the product.

```text
Problem and invariant:
Current model: authoritative fact, owners, relationships, time/lifecycle
Causal path and decisive counterexample:
Proposed patch and smallest complete correction (may be the same):
Recommendation, main cost, and what would change it:
Affected contracts, migration/operational risk, and missing proof:
Source-design conclusion; missing essential runtime proof; overall disposition:
```

Do not call a design sound merely because unit tests pass, use a familiar architecture name, or conceal uncertainty behind a numerical score. Conversely, do not block on an aesthetic architecture preference without a causal defect. If removing a root flaw requires broader work, retain the blocking finding and request a scope decision through the parent review; never start implementing.

A source-consistent design is not by itself a readiness verdict. Apply the parent skill's evidence gate to changed behavior, including deterministic local behavior; the absence of a database or remote service does not make execution proof irrelevant.

The review is complete when the applicable design questions have evidence-backed answers or explicit gaps, recommendations preserve supported behavior, and the report distinguishes defects from uncertainties. This is not a claim that every architectural risk has been eliminated.
