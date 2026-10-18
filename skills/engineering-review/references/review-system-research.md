# Research informing the workflow

These are original adaptations of publicly documented methods, researched October 2026. Vendor descriptions establish what vendors say they do; they do not prove this skill detects design defects, or that copying a component improves it. No proprietary implementation or vendor performance ranking is claimed.

| Primary source | Documented method | Adaptation and limitation |
|---|---|---|
| [CodeRabbit context engine](https://www.coderabbit.ai/blog/explainable-reviews-coderabbit-review-context-engine) | Dependency context, relevant engineering knowledge, static-tool signals, reviewer/verifier roles and evaluation of prompt/context changes | Build an inspectable source-backed map and verify candidates separately. A graph does not determine correct business meaning; repository access does not prove coverage. |
| [CodeRabbit learnings](https://docs.coderabbit.ai/knowledge-base/learnings) | Scoped learnings, distinguishing reusable patterns from exceptions, retaining the rationale | Store rule, reason, scope, provenance and exceptions. Keep past reviews challengeable; do not turn individual mistakes into a growing case-specific checklist. |
| [Cursor: Building a better Bugbot](https://cursor.com/blog/building-bugbot) | Early independent passes with varied diff ordering and filtering; later agentic retrieval; experiments sometimes regressed quality | Test discovery diversity and context retrieval. Do not automatically discard a sound singleton by majority vote. Resolution rate measures something different from missed-defect recall. |
| [Qodo 2.0](https://www.qodo.ai/blog/Introducing-qodo-2.0-agentic-code-review/) | Specialized reviewers with dedicated context and a separate judge | Allocate meaningful responsibilities within a gate. Separate discovery from filtering: a verifier cannot recover a candidate never investigated. |
| [Greptile: How to build a code review agent](https://www.greptile.com/blog/how-to-build-a-code-review-agent) | Context infrastructure, requirements, executable investigation and historical-PR evaluation | Inspect surrounding behavior and independently justified outcomes. Execution stays within project/service rules; this skill does not authorize mocks, provisioning or source edits. |

The separate blind omission audit is this framework's proposal. It checks which obligations received actual inspection and investigates missing paths. Its effectiveness must be evaluated rather than attributed to a vendor.

[Independent CodeRabbit feedback study](https://arxiv.org/abs/2607.03316) reports mixed usefulness and developer rejection reasons including false positives, redundancy and intent mismatches. Feedback acceptance is neither a correctness oracle nor a measure of undiscovered defects. [c-CRAB](https://arxiv.org/abs/2603.23448) studies review through human-review-derived tasks and held-out executable checks; such checks can strengthen assessment but cannot decide unresolved business meaning.

## Durable learning discipline

Add a rule only after understanding the cause and its scope. Record the invariant, supported trigger, consequence, source basis and legitimate contrasting case. Separate confirmed defects, unresolved product choices and preferences. Reject rules that merely name the previous sample or proposed solution. Retire or amend learnings when their contract changes. Do not automatically convert author dismissal or historical convention into correctness.
