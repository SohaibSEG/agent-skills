# Discover code relationships

Use this guide when a change crosses modules, shares a contract, or leaves a source-to-sink edge unresolved. The objective is to find the relevant code and establish its relationships, not to read the most files. [Inspection](investigation.md) owns causal review; this guide supplies its retrieval strategy.

## Choose the query before the tool

Start with `rg --files`, the diff and project configuration to locate languages, packages and likely entry points. Then choose the operation that answers the missing relationship. Repeating broader keyword searches is not a substitute for changing the query.

| Question | Useful operation | Limit to account for |
|---|---|---|
| Where is this symbol defined, used or implemented? | Language-server/compiler references, implementations and call hierarchy; a revision-matched SCIP index when available. | A name match is not a resolved reference. Dynamic dispatch and unindexed packages may be missing. |
| What code performs this operation in a different shape or wrapper? | AST/structural search for calls, assignments, JSX attributes, decorators or registrations; inspect captured expressions and enclosing owners. | Syntax is not type resolution, reachability or data flow. Include computed expressions and spreads, not only literal arguments. |
| Where is this behavior implemented when names are unknown? | Available semantic search and repository symbol/signature maps; then inspect returned source and references. | Ranked results are starting points, not exhaustive lists. Low-ranked or unrelated-looking consumers can matter. |
| Where does this value originate or end up? | Local def-use inspection, then targeted interprocedural data-flow/path queries where tooling supports the language/framework. | A call edge does not prove a particular value flows along it. Library models, aliasing and dynamic code affect results. |
| What crosses an HTTP, queue, storage or configuration boundary? | Join producer and consumer through actual route registration, payload/schema, event key, table/column, serializer and dispatch code. | Ordinary symbol graphs often stop at these boundaries. Similar names do not prove identity. |

Use installed read-only capabilities first; inspect supported operations rather than assuming an editor or MCP provides them. A language's parser/compiler API can supply structural queries without a new service. Check the tool version and parse/index diagnostics. If a richer tool is unavailable, use targeted text/source tracing and state the unresolved relationship. Missing optional tooling alone is not a blocker; missing essential evidence is. These are source-navigation operations, not permission to run scanner suites or analysis extraction that builds/executes the project. Use an existing revision-matched analysis database for targeted flow queries when available; otherwise trace source or hand off the missing analysis. Do not install infrastructure, upload source, run application code or invoke QA merely to obtain an index without the necessary authority.

## Expand from both code and contracts

1. **Extract seeds from the change.** Record changed symbols and affected contracts: types, field/configuration keys, stored records, events, routes and user outcomes. Include removed or renamed owners. Use outlines/signatures to orient; open bodies only where the decision or edge needs inspection.
2. **Resolve the symbol neighborhood.** Inspect definitions, actual implementations, callers and consumers. Include aliases, wrappers and re-exports through semantic resolution where supported. Follow both changed owners and consequential sinks; group callers only after checking equivalent behavior.
3. **Search for alternative implementations.** References to a shared helper cannot reveal consumers that do not use it. Search the underlying operation or structural shape independently: native controls as well as components, direct writes as well as repositories, scheduled handlers as well as request routes. Include computed selectors, dispatch tables, generated clients and configuration-driven behavior where the source supports them.
4. **Bridge lost edges explicitly.** At serialization, persistence or deferred work, identify the exact contract/version and enumerate its relevant writers/readers or publishers/subscribers. Inspect how values are renamed, defaulted, copied or discarded. Record framework/model gaps rather than drawing an invented edge between matching strings.
5. **Expand the unresolved frontier.** Follow new edges when they can change policy, identity, timing, authority, state or effects. Stop at an inspected stable boundary with a stated reason, or report the precise missing evidence. Neither a fixed hop count nor a first page/top-k search result closes coverage. Exhausting a graph query does not prove the graph is complete.

For example, a review of notification delivery should inspect references to the shared sender, structurally find direct transport calls and event registrations, then connect queued payloads to their handlers and recipients. A UI-control review should inspect wrapper callers and alternative native/configuration-driven controls. These are different retrieval questions; finding one family does not account for the other.

## Keep the map small and evidenced

Extend the existing review record, not a second mandatory report. Retain only relevant edges and outstanding work:

```text
revision · from symbol/contract → to symbol/contract · relationship
source locations · how resolved · inspected / inferred / unresolved
why relevant · next missing edge or reason to stop
```

Distinguish `calls`, `references`, `reads/writes`, `serializes/deserializes`, `publishes/handles` and `renders/edits`. An import graph is not a data-flow graph; an AST match is not a reachable path; a semantic-search result is not a reference. Inspect both ends before relying on an edge for a finding. Batch independent lookups and retrieve focused source spans; keep surrounding guards and transaction/lifecycle context when they affect meaning.

Bind indexes and cached source facts to the candidate revision (and base separately), tool configuration and relevant file hashes. Record excluded/unparsed files, dependency gaps, truncation and failed queries. Reuse unchanged source facts across specialists, but do not give discovery conclusions or the initial map to a blind omission auditor. Invalidate affected edges after a source/configuration change. Keep generated indexes and evidence outside product code.

## Check retrieval separately from reasoning

During evaluation, freeze the same case, skill, agent roles and available tools except the intended discovery change. Record whether a decisive path was retrieved, opened, traced, correctly interpreted, retained and verified. A path found only after revealing the expected defect is a diagnostic recovery, not blind detection. Measure supported findings and false alarms alongside retrieval coverage and effort; do not reward more retrieved files or a larger graph.

## Sources and adaptation

These sources establish capabilities and limitations, not proof that this workflow improves review accuracy:

- [Sourcegraph precise code navigation](https://sourcegraph.com/docs/code-navigation/precise-code-navigation): symbol-aware indexes and SCIP. [Serena](https://github.com/oraios/serena) exposes symbol navigation to agents, with language/backend-dependent capabilities.
- [Tree-sitter queries](https://tree-sitter.github.io/tree-sitter/using-parsers/queries/1-syntax.html), [ast-grep](https://ast-grep.github.io/guide/quick-start.html), and [TypeScript compiler API](https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API): structural parsing/search; use APIs matching the installed version.
- [CodeQL data-flow concepts](https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/) and [JavaScript/TypeScript flow](https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-javascript-and-typescript/): local versus global flow, source/sink scoping, cost and possible spurious paths. [Library models](https://codeql.github.com/docs/codeql-language-guides/customizing-library-models-for-javascript/) explain framework coverage gaps.
- [Aider repository maps](https://aider.chat/docs/repomap.html): signatures and relevance-ranked dependency maps. [Cursor semantic-search evaluation](https://cursor.com/blog/semsearch): vendor-reported benefits from combining semantic search and grep, not a guarantee for review defect recall.
- [CodeRabbit context engine](https://www.coderabbit.ai/blog/explainable-reviews-coderabbit-review-context-engine): change-related graphs and contextual retrieval before review/verification. The explicit cross-boundary frontier and evidence rules above are this package's synthesis.
