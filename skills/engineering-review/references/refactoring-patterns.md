# Refactoring patterns to recommend during review

Use this catalog after establishing a concrete responsibility or representation problem. Recommendations are review output, not permission to edit. First inventory existing controls, domain objects and services. For each proposal name the callers affected, the behavior preserved, the intentional behavior correction and the proof needed. Refactoring preserves observable behavior; describe any bug fix or contract change separately.

These are original review applications of the linked techniques. Do not demand every pattern, count smells as defects, or infer that a named technique alone removes the root cause.

## Responsibility and control flow

### 1. Extract Function: a block performs a distinct operation

1. Identify a coherent operation mixed into another responsibility; name its inputs, result and side effects.
2. Recommend extraction only if its interface communicates more than the implementation details callers currently need to know.
3. Require equivalent return values, exception behavior and effect ordering. Check captured mutable state and resource lifetimes.
4. Avoid helpers created only to satisfy a line-count target; a pass-through name can add navigation without hiding complexity.

Technique: [Extract Function](https://refactoring.com/catalog/extractFunction.html).

### 2. Move Function: policy lives with the wrong owner

1. Inspect which data and decisions the function repeatedly reaches across boundaries to use.
2. Recommend moving policy to its actual owner while leaving transport parsing and provider I/O at their appropriate boundaries.
3. Identify all callers, authorization context and transaction assumptions that must remain intact.
4. Reject moves that merely turn one dependency cycle into another or create a generic utility dumping ground.

Technique: [Move Function](https://refactoring.com/catalog/moveFunction.html).

### 3. Inline Function: indirection hides rather than explains

1. Follow wrappers that only forward arguments or rename an equally clear expression.
2. Recommend inlining when there is no meaningful contract, policy, reuse or replaceable boundary to preserve.
3. Verify that the wrapper does not own instrumentation, access checks, caching, cleanup or an external API.
4. Do not inline a useful seam just because its present implementation is small.

Technique: [Inline Function](https://refactoring.com/catalog/inlineFunction.html).

### 4. Split Phase: interpretation, calculation and effects are interleaved

1. Mark the transitions between input interpretation, deterministic calculation and applying effects.
2. Recommend a clear intermediate representation when it prevents later stages from reinterpreting raw input differently.
3. Check validation timing, error priority, partial writes and memory cost; the proposed split must preserve those contracts or name intentional changes.
4. Do not split atomic business transitions into independent commits merely to create stages.

Technique: [Split Phase](https://refactoring.com/catalog/splitPhase.html).

### 5. Guard clauses: exceptional cases bury the main path

1. Identify nested branches that reject invalid or exceptional states before useful work begins.
2. Recommend early returns only where branch precedence and effects can be preserved.
3. Check cleanup, locks, audit events and finalization that a new exit could skip.
4. Preserve state-machine ordering; flattening syntax is not a reason to reorder domain decisions.

Technique: [Replace Nested Conditional with Guard Clauses](https://refactoring.com/catalog/replaceNestedConditionalWithGuardClauses.html).

### 6. Replace Conditional with Polymorphism: variants repeat across operations

1. Identify the same stable variant distinction repeated in several operations, with diverging rules or incomplete new-variant handling.
2. Compare a small strategy, a dispatch table and ordinary explicit branching. Recommend the least complex representation that keeps each variant's behavior coherent.
3. Require coverage of supported variants, unknown values and existing serialization boundaries.
4. Keep a simple local conditional when no repeated variation or extension problem exists; a class hierarchy is not automatically cleaner.

Technique: [Replace Conditional with Polymorphism](https://refactoring.com/catalog/replaceConditionalWithPolymorphism.html).

## Representation and interfaces

### 7. Introduce Parameter Object: related values travel together

1. Locate repeated groups such as amount/currency or start/end, and verify they represent one concept rather than coincidental arguments.
2. Recommend a small value object or typed record that can own shared validation and make invalid combinations explicit.
3. Check units, optional/default values, serialization and callers that only need part of the concept.
4. Avoid an ever-growing context bag that conceals dependencies or adds privileges callers do not need.

Technique: [Introduce Parameter Object](https://refactoring.com/catalog/introduceParameterObject.html).

### 8. Replace Primitive with Object: strings or numbers carry hidden rules

1. Locate repeated parsing, comparison, validation or conversion around one concept.
2. Recommend an explicit value representation that owns those rules and has clear construction boundaries.
3. Require proof for equality, normalization, invalid values, persistence and round trips.
4. Do not wrap every primitive. A wrapper that permits the same invalid states without reducing caller knowledge does not solve the problem.

Technique: [Replace Primitive with Object](https://refactoring.com/catalog/replacePrimitiveWithObject.html).

### 9. Encapsulate Variable or Collection: callers can bypass an invariant

1. Find direct writes and exposed mutable references, including mutations through objects returned by getters.
2. Recommend operations that own permitted transitions; for collections, consider read-only views or copies and explicit membership commands.
3. Check aliases, nested mutable values, ordering, uniqueness and concurrent writers. A shallow copy does not isolate nested objects.
4. Do not mistake accessor syntax for protection if it still exposes the same mutable state.

Techniques: [Encapsulate Variable](https://refactoring.com/catalog/encapsulateVariable.html), [Encapsulate Collection](https://refactoring.com/catalog/encapsulateCollection.html).

### 10. Replace Derived Variable with Query: copies of a fact drift

1. Identify values fully derivable from authoritative inputs and enumerate every invalidation path.
2. Recommend computing the value when affordable, or an explicitly maintained projection with a clear freshness contract when measurement justifies storage.
3. Require update, retry and concurrent-read evidence for consistency; inspect query cost before removing a cache.
4. Preserve intentional historical snapshots. Recomputing a past invoice from today's rate changes meaning rather than merely refactoring.

Technique: [Replace Derived Variable with Query](https://refactoring.com/catalog/replaceDerivedVariableWithQuery.html).

### 11. Replace Magic Literal: a value obscures its meaning

1. Ask what the literal represents, including units and whether identical literals actually share one meaning.
2. Recommend a named constant for stable meaning, or a domain value/policy when the value has validation or behavior.
3. Verify boundaries and conversions, not just that the constant was substituted everywhere.
4. A name alone does not repair competing authorities or behavior inferred from presentation text. Recommend an explicit capability when the real rule should survive renaming or translation.

Technique: [Replace Magic Literal](https://refactoring.com/catalog/replaceMagicLiteral.html). The presentation-policy check is this cookbook's application, not a prescription to replace every condition with a flag.

### 12. Remove Flag Argument: one operation conceals different commands

1. Inspect mode arguments that select unrelated actions, especially positional booleans whose call sites hide intent.
2. Recommend named operations with shared internals when callers are really asking for different commands.
3. Verify that each command retains authorization, errors and effects; avoid duplicating the policy while improving naming.
4. Distinguish command-selection flags from legitimate state or constraints. A named configuration property such as a future-date restriction is not automatically a design flaw.

Technique: [Remove Flag Argument](https://refactoring.com/catalog/removeFlagArgument.html).

## Effects and reuse

### 13. Separate Query from Modifier: inspecting state changes it

1. Look for getters, previews or validation calls that also persist, notify or acknowledge work.
2. Recommend an explicit separation between observation and the command that changes state.
3. Check the interval between query and command: authorization and invariants must be revalidated at the mutation boundary.
4. Preserve operations whose contract is intentionally atomic, such as compare-and-swap or dequeue. Splitting them can introduce the race the review should prevent.

Technique: [Separate Query from Modifier](https://refactoring.com/catalog/separateQueryFromModifier.html).

### 14. Undo the wrong abstraction: reuse requires caller-specific exceptions

1. Inspect shared functions accumulating switches and parameters for callers with different rules.
2. Identify whether the callers share a reason to change, not merely similar syntax.
3. Recommend separating distinct policies, then sharing only the stable common mechanism if one remains.
4. Require preserved caller-specific behavior. Temporary duplication can be clearer than a configurable abstraction with undocumented interactions; it is not a blanket instruction to duplicate established policy.

Source: [Sandi Metz, The Wrong Abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction).

Use the shared [finding record](review-records.md), adding the proposed responsibility/representation, affected callers and technique-specific preservation constraints.
