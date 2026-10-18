# Research basis and evaluation

This workflow is an engineering synthesis, not a validated claim that adversarial prompting improves review accuracy. Sources inform specific operations; they do not endorse this skill or its blocking policy. Consulted 19 October 2026.

## Primary sources translated into review actions

| Source | Relevant principle | Application in this skill |
|---|---|---|
| [Google Engineering Practices: what to look for in review](https://google.github.io/eng-practices/review/reviewer/looking-for.html) | Review overall design and whether the intended functionality serves users; reject speculative generality and inspect tests critically. | Judge the intended rule before local correctness. Compare against actual callers and requirements, and reject a larger abstraction with no demonstrated need. |
| [Maria Rosala, NN/g: framing the right problem](https://www.nngroup.com/articles/how-might-we-questions/) | Start from discovered problems, avoid building a solution into the question, and retain a useful scope around the desired outcome. | Rewrite a proposed mechanism as an outcome or invariant, preserving evidence and constraints. This is an adaptation for engineering review, not a requirement to run a design workshop. |
| [NASA Systems Engineering Handbook, Appendix C: requirements checklist](https://www.nasa.gov/reference/system-engineering-handbook-appendix/) | Distinguish what is needed from implementation; inspect assumptions, consistency, traceability and necessity. | Classify observations, outcomes, constraints and mechanism claims separately. Trace a design assumption to its owner and consequences before accepting it. |
| [NASA: design solution definition](https://www.nasa.gov/reference/4-4-design-solution-definition/) | Evaluate design alternatives against requirements and constraints, make assumptions explicit, and validate against stakeholder expectations. | Compare the submitted design and a meaningful correction under the same requirements. No mandatory alternative count, heavyweight trade-study process or automatic redesign. |
| [Kazman, Klein and Clements, SEI: ATAM overview](https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/) | Architecture decisions trade off qualities including security, availability, performance and modifiability. | Explain the relevant trade-off rather than announcing one universally superior architecture. This skill does not implement or claim a full ATAM evaluation. |
| [Huang et al., ICLR 2024: Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html) | In the studied reasoning settings, intrinsic self-correction without external feedback was unreliable and could degrade answers. | Require checkable source evidence and a counterevidence pass instead of treating “be more critical” as verification. The study is not a measurement of this skill, current models, or code-review accuracy. |

The decision-authority trace, evidence requirements for reframing, inherited-contract relevance test and separation from implementation authority are this package's own synthesis. They must be evaluated empirically. Prior successes do not make their conclusions true in a new review.

## Framing-specific evaluation

Use the shared [evaluation protocol](../../../references/evaluation.md) for frozen inputs, fresh contexts, comparison, adjudication and limitations. Evaluate whether the reviewer establishes the underlying operational rule, invalid selection/ownership assumption, reachable consequence and complete correction. A smell name or another manifestation is not root-design detection.

Include defended sound designs, legitimate specialization and corrected revisions. Distinguish a justified reframe from mandatory abstraction or contrarian disagreement. This role does not replace structural coverage or prove full review readiness.
