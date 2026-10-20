---
name: ui-ux-review
description: Review rendered interface states, visual consistency, responsive layout, forms and accessibility using source and supplied screenshots or interaction evidence.
---

# UI, UX and Accessibility Review

Read the [shared review contract](../../references/review-contract.md). Inherit the
parent's frozen target, assigned gate and evidence scope. Record loaded guides,
inspected paths and open proof requirements in the shared coverage record.

Use the procedure below at the experience gate and
[QA evidence handoff](../../references/qa-evidence.md) before assessing evidence.
Compare applicable established patterns under matching viewport, data, theme and
state. Include validation, loading, failure and denied states where relevant.
Return reproducible observations with reference pattern, artifact identity and
source location when known. Separate observed defects from predictions. Screenshots
cannot prove keyboard completion, persistence or real-user understanding; request
those observations from authorized QA. Do not execute browser flows in this role.

Use source and supplied rendered/interaction evidence at the experience gate.
[User journeys](../user-journey-review/SKILL.md) owns the task path; [Frontend engineering](../frontend-engineering-review/SKILL.md)
owns state/transport implementation. Reuse its state map rather than repeating
source inspection. Read the [QA evidence handoff](../../references/qa-evidence.md) for missing
screenshots, recordings, keyboard or persistence evidence. Reviewers do not execute
browser flows. Do not progress past a blocked prerequisite gate.

## Establish the comparison


1. **Inventory applicable patterns before judging the change.** Find existing screens for the same interaction and their components, tokens, layouts, and form conventions. Map changed controls to established counterparts. Verify each counterpart serves the same purpose; superficial resemblance does not establish authority. Consistency should preserve familiar meanings and behavior. [NNGroup: usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)

2. **Compare rendered interfaces, not just component names.** Use matching data, viewport, theme, and interaction state to compare the changed screen with the applicable pattern. Examine spacing, typography, density, alignment, action placement, labels, icons, and state styling. A demonstrated inconsistency against an established applicable pattern is a blocker under this cookbook even when the feature functions. Cite the reference screen and exact discrepancy; check for an approved intentional exception. Personal taste or an unsupported redesign preference is not a finding.

For the end-to-end path, action hierarchy, disclosure and recovery decisions, use [User journeys](../user-journey-review/SKILL.md). The checks below inspect their concrete UI/state implementation.

## Inspect information and state

3. **Identify unnecessary memory demands.** Check whether labels, selected values, units, current filters, and relevant record identity remain visible at the moment of decision. Inspect how two records with similar names are distinguished; request missing rendered evidence. Prefer meaningful identifying context over requiring a person to remember an internal identifier from another screen. Verify that icons and abbreviated labels are understandable in context; do not assume a tooltip solves discovery on touch devices. [NNGroup: recognition and recall](https://www.nngroup.com/articles/recognition-and-recall/)

4. **Build a state-evidence matrix.** Cover view, edit, dirty, submitting, saved, empty, loading, validation failure, request failure, and permission denial when applicable. Ensure view mode is distinguishable from editable fields; cancellation restores the intended values; server refresh does not silently erase edits. Verify repeated submissions and stale responses cannot show the wrong result. Separate an empty dataset from a failed request. Check that page, section, and field feedback have an intelligible priority rather than competing banners and spinners.

5. **Inspect error mechanics.** For missing, malformed and conflicting input, trace field association, textual error identification, preserved valid values and focus/retry state. Assess supplied evidence against the project's accessible form pattern; the journey guide owns the recovery action and explanation. Do not claim that WCAG mandates one particular inline or summary layout. [W3C: Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html)

## Inspect implementation and realistic constraints

6. **Trace CSS conflicts to the winning rule.** Inspect supplied computed-style evidence and the source cascade for problematic elements in default, hover, focus, disabled, and error states. Check global selectors, inherited styles, utility ordering, component variants, specificity, and media queries. Demonstrate the actual affected state before flagging a conflict. Recommend removing the conflicting rule or using an existing variant where appropriate; do not propose another override without identifying why it wins and which other consumers it affects.

7. **Use realistic data shapes and volume.** Inspect source and supplied states for long labels, multiline content, absent optional values, duplicate display names, many results and the last page. Check bounded fetching, search, pagination, and stable selection across updates. Confirm truncation retains a usable way to identify the item. Compare supplied supported desktop/mobile and zoomed states; inspect overlays, sticky controls, tables, and overflow. For WCAG reflow evidence, assess the applicable 320 CSS pixel width and respect exceptions for content that needs two dimensions. [W3C: Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

## Verify access and evidence

8. **Assess keyboard completion evidence.** Inspect accessible names and roles, tab order, activation, dialog dismissal, and focus after closing or saving. Ensure keyboard focus remains visible; inspect CSS resets that remove indicators. Record the exact element and state that fails. Automated checks supplement this interaction review. [W3C: Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)

9. **Check feedback without relying on sight or color alone.** Verify that status messages such as save completion and result counts are exposed to assistive technology without unnecessarily moving focus. Distinguish these messages from general content updates. Check that errors, selection, and status are distinguishable through text, shape, or another visual cue as appropriate. [W3C: Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html), [W3C: Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)

10. **Report a reproducible correction.** Include the state, steps, expected pattern or requirement, actual result, and supporting visual evidence. For a refactor, name the existing component or boundary to reuse, what responsibility moves, and what behavior must remain unchanged. Inspect affected consumers and cite the available visual evidence; request missing states from separate QA. A screenshot demonstrates appearance; it does not prove persistence, keyboard behavior, or the complete task succeeded.
