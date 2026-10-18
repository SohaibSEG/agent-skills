# User-story and journey review

Use when a change introduces or alters how a person discovers, understands, completes or recovers a task. Review the journey before judging individual controls. This reference produces findings and design recommendations only; it does not authorize implementation, recruiting participants, analytics instrumentation or changes to real records. Use [Frontend](frontend.md) for component conformance, rendered states, CSS and accessibility mechanics; use [System design](system-design.md) for the underlying state and authority contracts.

The question is: **can the intended person get from their starting situation to a verified outcome, with understandable choices and no unnecessary work?** A working form and a successful request are intermediate events, not necessarily the person's goal. The guidance below translates primary author material into review actions; it does not prescribe a particular organization's visual design system. These are original review procedures, not reproductions of the cited books or a claim to have read them in full.

## 1. Establish the story without prescribing the interface

1. Identify the actor, trigger, starting knowledge, permissions, relevant constraints and desired outcome. Include frequency and interruption risk when supported by research or the product context.
2. Describe success independently of screens: what becomes possible or true for the person? Distinguish their outcome from the organization's conversion or activity metric.
3. Read requirements and available user research, support reports or observed behavior. Mark inferred needs as hypotheses. Code demonstrates system behavior; it does not establish what people understand or want.
4. Identify prerequisites and downstream handoffs. If another role must finish the work, distinguish this person's completion from the overall process completing.

Record a compact story: **When [situation], [actor] needs [outcome], starting with [knowledge/access], and knows they succeeded when [observable evidence].** Do not manufacture personas or demand a formal story template for a small change.

Sources: [Kim Goodwin on Cooper's Goal-Directed Design](https://articles.centercentre.com/goal_directed_design/) and [Maria Rosala: Task Analysis](https://www.nngroup.com/articles/task-analysis/). Build scenarios from supported behaviors and goals, not invented biographies. User goals, business constraints and necessary obligations must be reconciled rather than treating an organizational metric as the entire story.

## 2. Identify what the interface expects the person to know

1. List the knowledge required at each difficult decision: terminology, record relationships, prerequisites, permissions and consequences. Compare it with evidence about what this user already knows.
2. For each gap, first consider removing unnecessary concepts or reusing familiar vocabulary. Where a real decision remains, propose the smallest explanation at the point it is needed.
3. Check a first-time or occasional user and a frequent operator when both are supported. Do not burden repeated work with mandatory tutorials, or assume expert familiarity makes a hidden action discoverable to everyone.
4. State the exact misunderstanding a change would prevent. “Make it intuitive” is not an actionable finding; explain the knowledge currently missing and how the proposed interaction supplies or removes the need for it.

Source: [Jared Spool: What Makes a Design Seem Intuitive?](https://articles.centercentre.com/design_intuitive/). This is a knowledge-gap inspection, not permission to invent research findings or redesign beyond the reviewed flow.

## 3. Map the actual path and its decision points

Start from the entry point users encounter: a queue, search result, notification, record or returning session. Follow the normal route, not a developer-only deep link. Include relevant branches and exits without mapping unrelated product flows.

| Step / state | What the person needs to decide | Information available here | Action and expected result | Actual result / next owner |
|---|---|---|---|---|
| Entry to outcome | A meaningful decision, or none | Identity, evidence, constraints | Visible action and consequence | Persisted state and understandable feedback |

For each transition, check that prerequisites appear before they are needed and consequences are understandable before commitment. Flag unexplained detours between modules, lost selection, hidden dependencies and settings whose effects emerge much later. Separate a task that genuinely requires another role from missing guidance about that handoff.

Source: [Jakob Nielsen: Workflow Expectations](https://www.nngroup.com/articles/workflow-expectations/). The working table is this cookbook's review aid, not a prescribed UX deliverable.

## 4. Check whether the next action is apparent and meaningful

At every consequential state, inspect these questions from the person's visible information:

1. Can they recognize where they are, which record is affected and why attention is needed?
2. Can they locate the appropriate next action and predict its result from its label and context?
3. Do they have the evidence needed to choose safely, including scope, cost or irreversible consequences when relevant?
4. After acting, can they tell whether it worked and what remains?

An issue view must explain the issue and affected outcome before asking for an edit. Check whether visual cues communicate the available action and its scope; do not rely on hidden hover or gesture behavior alone. Separate action importance without making cancel, back or legitimate alternatives hard to find. Distinguish genuine alternatives from accidental competition between commit and destructive reset. Recommend task-specific labels and familiar interaction patterns.

Sources: [Don Norman: Signifiers, Not Affordances](https://jnd.org/signifiers-not-affordances/) and [Luke Wroblewski: Primary and Secondary Actions](https://www.lukew.com/ff/571/primary-secondary-actions-in-web-forms). Wroblewski's study illustrates a trade-off between speed and avoiding accidental cancellation; it does not establish a universal button order. Apply the product's established pattern and test the relevant task. A plausible discoverability concern remains a hypothesis without supporting evidence.

## 5. Remove work before adding guidance

1. Inventory avoidable decisions, repeated input, searches, context switches, waiting and backtracking. Record what each step contributes; remove it from the recommended flow only if no required rule depends on it.
2. Inspect whether the interface already knows the relevant record, scope or previous answer. Recommend carrying valid context forward, with visible and correctable defaults where appropriate. Do not preselect a consequential choice merely to increase completion.
3. Separate essential confirmation from habitual extra confirmation. An additional step may be worthwhile if it prevents a costly mistake; state that trade-off.
4. Compare the existing and proposed paths using completion, errors, recovery and user effort. Do not invent a maximum click count or claim a time saving from counting screens alone.

Sources: [Steve Krug: published sample chapter on choices](https://sensible.com/downloads/DMMT-Revisited-sample-chapter.pdf); [W3C: Redundant Entry](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html). The WCAG criterion concerns repeated information in the same process and includes exceptions for essential re-entry, security and invalidated information; apply its actual scope.

## 6. Choose disclosure and navigation to fit the task

1. Keep information used together available together. Defer rare detail behind a clearly named control; do not hide warnings, prerequisites or evidence needed for the current decision.
2. Use sequential steps when later decisions depend on earlier ones. Avoid forcing repeated backward navigation when users need to compare or adjust choices together.
3. For longer work across sessions, consider a task overview showing remaining work and status. Simplify the process first; do not add a checklist or progress bar merely to decorate complexity. An interrupted user needs to recover their place and pending decisions without reconstructing the whole task.
4. Evaluate a modal by the interruption it causes, the context it obscures and whether the task can finish comfortably there. A sustained or multi-step activity may need its own page. Preserve established navigation and focus behavior.

Sources: [Jakob Nielsen: Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/) and [Therese Fessenden: Modal and Nonmodal Dialogs](https://www.nngroup.com/articles/modal-nonmodal-dialog/). These are conditional choices, not universal mandates for tabs, wizards, cards or dialogs.

## 7. Inspect questions and the commitment boundary

1. Distinguish an accidental action from a misunderstood rule. For the former, inspect constraints, defaults and safe correction; for the latter, inspect the missing explanation or misleading model. Repeated confirmation does not repair a misunderstood concept.
2. Distinguish inspecting saved information from changing it. Make draft, saved and submitted states clear; determine exactly which action creates an external or irreversible effect.
3. When consequences warrant review, show a concise summary of the affected record, important choices and scope before committing. Let users correct one answer and return without replaying unrelated steps.
4. Make the commit action describe the actual effect. Do not use a generic continuation label for an action that publishes, pays or sends something without making that consequence clear.

Source: [Page Laubheimer: Preventing User Errors](https://www.nngroup.com/articles/slips/), including the distinction between slips and mistakes. Preserve valid alternatives; constraints must express actual domain rules, not merely simplify implementation. Do not add confirmation to every action: assess reversibility and the consequence of an error.

## 8. Review recovery as a first-class journey

Walk the relevant failure paths: missing information, conflicting state, denied permission, unavailable dependency, session expiry and interrupted submission. For each, check:

1. Can the person understand what failed and whether any action already completed?
2. Is valid work preserved, and is the next action specific and within their control?
3. Can they fix the affected input without restarting, or reach the appropriate owner when they cannot fix it?
4. Does retry avoid accidental duplicates, and does cancel/back have a clear effect on saved and unsaved work?

Distinguish invalid input from service failure. Do not ask the user to change correct data to recover from an outage. If the result is uncertain, recommend a status/reconciliation path rather than an unconditional invitation to submit again. Trace this claim into the actual backend contract; copy alone cannot make retry safe.

Source: [Ben Shneiderman: Eight Golden Rules](https://www.cs.umd.edu/users/ben/goldenrules.html), specifically recovery, reversal and user control. The retry and uncertain-outcome checks extend these principles to application contracts; they are not claims that Shneiderman prescribes a particular backend mechanism.

## 9. Verify completion and the next useful step

Check that the final state identifies what happened, to which record and whether anything remains pending. For a handoff or background operation, show who acts next and how the person can check progress; do not present acceptance as completed delivery. Give reliable timing only when supported.

Check returning to the result, reloading and reopening a receipt where applicable. A short-lived toast may acknowledge an action but cannot be the only way to recover an important outcome. Recommend relevant next actions rather than a dead end or unrelated promotion. For repeated work, inspect return to the previous queue/filter/selection and whether the resolved item updates without losing the user's place.

Source: [Don Norman: feedback and conceptual models](https://jnd.org/opportunities-and-challenges-for-touch-and-gesture-based-systems/). Apply these principles to the actual operation: distinguish input received, work in progress and completed outcome. A separate confirmation page is one possible treatment, not a requirement after every save.

## 10. Turn the story into a falsifiable task scenario

1. Give the actor a realistic goal and starting context without naming the control to click. A script that says which button to use cannot establish discoverability.
2. Include the normal route and the important recovery or returning-user route. Use realistic data volume, similar record names and supported device/access needs; reuse the frontend reference for detailed checks.
3. State observable success: the correct durable outcome, clear confirmation and no lost work or unintended side effect. Separate frontend appearance from persistence and downstream completion.
4. When authorized, observe where representative users hesitate, misinterpret, backtrack, need help or abandon. Avoid coaching them toward the intended control; distinguish their behavior from the reviewer's predicted behavior. Measure the changed risk; do not manufacture benchmark targets or infer confidence from an agent completing a known script.

Sources: [Marieke McCloskey: Task Scenarios for Usability Testing](https://www.nngroup.com/articles/task-scenarios-usability-testing/) and [Steve Krug: practical usability testing](https://sensible.com/rocket-surgery-made-easy/). If only source inspection is available, label predicted friction accordingly and identify the missing observation. Essential validation still follows the parent skill's readiness gate.

## 11. Return a focused journey finding

Use the parent's findings-first report. Include only the map and evidence needed to explain the decision:

```text
Actor, starting situation and intended outcome:
Actual path and point of friction:
Evidence: observed failure / source-supported behavior / hypothesis:
Consequence: wrong action, lost work, unnecessary effort or incomplete outcome:
Smallest recommended journey change and behavior to preserve:
Task scenario that would distinguish improvement from cosmetic change:
```

Do not demand a redesign because another layout is fashionable. Preserve a working flow when the evidence supports it. Separate established visual-conformance defects from speculative usability concerns, apply the existing blocking policy, and stop after the review recommendations.
