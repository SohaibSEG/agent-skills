# Worked review examples

These synthetic examples teach causal review moves, not a checklist of defects to find. Read the relevant example, then inspect the actual contract and source. Similar syntax is a lead, not proof. The correction sketches are not production patches or authorization to implement or run QA. Existing specialist guides own the full procedures.

| What needs examination | Example |
|---|---|
| Meaning and rule ownership | [Presentation as policy](#presentation-as-policy), [Units erased](#units-erased) |
| Trust and integrity | [Identity without authority](#identity-without-authority), [Check then act](#check-then-act) |
| Module responsibilities | [Wrong abstraction](#wrong-abstraction), [Query with hidden effects](#query-with-hidden-effects) |
| UI state and recovery | [Stale async completion](#stale-async-completion), [Failure disguised as empty](#failure-disguised-as-empty) |
| Test evidence | [Circular oracle](#circular-oracle) |

## Presentation as policy

```ts
if (subscription.displayName.startsWith("Business")) allowBulkExport();
```

**Inspect:** Trace who edits `displayName` and where export permission is enforced. Suppose marketing can rename the tier while its purchased entitlements stay unchanged. A permitted rename then changes access: a display property is standing in for the entitlement contract.

**Reframe:** The operation is deciding whether this subscription permits bulk export, not recognizing a marketing name. Resolve the capability from authoritative subscription policy and enforce it at the server operation; a client-supplied `canExport` boolean is no replacement for authorization. Trace provisioning, updates and every export entry point.

**Contrast:** An immutable, documented protocol discriminator can legitimately select behavior. A display label can also select presentation. Naming it a string or finding a conditional is not a defect. [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) supports the enforcement boundary; the example is this guide's synthesis.

## Identity without authority

```python
require_signed_in(user)
attachment = attachments.get(request.attachment_id)
attachments.delete(attachment)
```

**Inspect:** Can another tenant's attachment ID reach this operation? Trace lookup scope, signed capabilities and downstream policy before claiming a leak. Authentication establishes the actor; it does not establish authority over this attachment.

**Correction boundary:** Resolve the resource under trusted tenant/principal context and enforce the action permission before deletion. Include alternate download, bulk and worker paths that rely on the same authorization contract. Hidden buttons and difficult-to-guess IDs do not enforce ownership.

**Contrast:** A repository that already scopes every lookup, or a correctly verified resource/action capability, may defend this code. Verify that boundary instead of demanding redundant predicates everywhere. [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).

## Check then act

```python
if stock.available(item) >= quantity:
    stock.decrement(item, quantity)
    reservations.create(item, quantity)
```

**Inspect:** With one unit left, two requests can both pass the read. Trace whether decrement is conditional, locks are held, transactions are serializable, or another constraint prevents overselling. Sequential happy-path tests cannot answer this.

**Correction boundary:** Let one atomic reservation operation validate a positive quantity, enforce available stock, check success, and create the reservation in the same transaction. A conditional update or lock-and-recheck may fit; select from the actual database contract. Moving the same stale check into a helper does not fix the race.

**Contrast:** A supported single-writer model or an already conditional decrement may make the visible check advisory. Trace every writer and failure result before flagging it. PostgreSQL's [isolation documentation](https://www.postgresql.org/docs/current/transaction-iso.html) explains why a transaction alone is insufficient; other engines need their own evidence.

## Units erased

```python
total = sum(payment.amount for payment in payments)
```

**Inspect:** Does the supported input contain different currencies? If `10 USD` and `10 EUR` become the number `20`, the projection has discarded information required to interpret the total. The error is in the aggregation contract, not a missing currency symbol in the UI.

**Correction boundary:** Preserve amount and currency together. Group totals by currency or convert under an explicitly owned rate/time/rounding policy. Follow serialization and reports so the dimension is not lost again. Do not invent exchange policy.

**Contrast:** If the account contract enforces one currency at every producer, a scalar aggregate can be sound. A wrapper class alone adds no protection unless construction and combination preserve the invariant. Related technique: [Introduce Parameter Object](https://refactoring.com/catalog/introduceParameterObject.html).

## Wrong abstraction

```python
send_email(recipient, message, marketing=True, bypass_opt_out=False)
```

**Inspect:** Suppose the same helper owns newsletter consent and password-reset delivery. A new global unsubscribe guard can suppress requested resets, while an escape flag lets marketing callers bypass consent. Enumerate actual callers and permitted combinations; establish which policy is required for each operation.

**Correction boundary:** Separate the commands and their policies, sharing template rendering and transport where those contracts genuinely match. The shared reason to change is delivery mechanics, not necessarily consent or eligibility. Explain which caller responsibility becomes explicit.

**Contrast:** A small named option controlling one coherent mechanism is legitimate. Flags, duplication and branching are not automatically bad; neither is a class hierarchy automatically better. [Sandi Metz: The Wrong Abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction).

## Query with hidden effects

```python
def preview_shipping(order):
    quote = carrier.quote(order)
    carrier.purchase_label(quote)
    return quote
```

**Inspect:** If the preview contract promises no purchase, a page refresh or preview retry can create another paid label. Trace real callers, idempotency and provider effects; the function name alone does not establish the promise.

**Correction boundary:** Keep observation separate from an explicit purchase command with its own authority and duplicate protection. Revalidate price/availability when committing; an old preview is not a reservation. Preserve intentionally atomic commands.

**Contrast:** `dequeue`, `reserve` and compare-and-swap can legitimately return data while changing state. Do not split an atomic business operation merely to satisfy a naming rule. Related technique: [Separate Query from Modifier](https://refactoring.com/catalog/separateQueryFromModifier.html).

## Stale async completion

```ts
async function search(query: string) {
  setResults(await api.search(query));
}
```

**Inspect:** Type `ca`, then `cat`. If the newer result returns first, the older response can overwrite it while the input still shows `cat`. Trace the actual query library, cache key and response ownership; do not assume the minimal snippet represents the surrounding code.

**Correction boundary:** Bind result/error/loading updates to the active request identity, or use the established query mechanism that supplies that guarantee. Cancellation can reduce work, but verify that late completion cannot commit after cancellation. Check selection identity as well as visible results.

**Contrast:** If query changes are prevented for the request lifetime, or the existing library already binds displayed state to the active query, another guard may be redundant. This is source-established state behavior; rendered usability still needs separate evidence. [React's data-fetching guidance](https://react.dev/reference/react/useEffect#fetching-data-with-effects) illustrates response-order cleanup.

## Failure disguised as empty

```ts
const rows = await api.listProjects().catch(() => []);
return rows.length ? <Projects rows={rows} /> : <CreateFirstProject />;
```

**Inspect:** A network failure now tells an existing user to create their first project. Trace whether failure is communicated elsewhere and whether creation risks duplicates. The user needs recovery from an unavailable list, not onboarding for a confirmed empty account.

**Correction boundary:** Preserve loading, successful-empty, successful-populated and failed states. Reuse the application's error/retry pattern and retain useful prior data where its freshness is clear. Error copy alone cannot repair a state model that discarded the error.

**Contrast:** An explicitly optional recommendation panel may deliberately disappear on failure. Check whether absence is an honest supported outcome and whether another part of the interface owns recovery. [NN/g empty-state guidance](https://www.nngroup.com/articles/empty-state-interface-design/) informs task guidance; the failure trace is this guide's synthesis.

## Circular oracle

```python
expected = calculate_shipping(cart)
assert checkout(cart).shipping == expected
```

**Inspect:** If the test claims to prove free shipping above a threshold, this expected value can repeat the same faulty policy used by checkout. Trace the oracle's independence and whether the production decision is exercised. Replacing `calculate_shipping` with a mock returning zero also cannot prove eligibility.

**Correction boundary:** Derive expected outcomes from the rule, with explicit below/at/above cases and consequential totals. Keep the real policy for a policy test; replace external I/O only where that preserves the claim. Recommend the evidence without running or rewriting tests during review.

**Contrast:** This comparison or a mocked fee may legitimately test checkout's delegation/propagation contract. It becomes misleading only when used as proof of the shipping policy itself. [Google: Don't Put Logic in Tests](https://testing.googleblog.com/2014/07/testing-on-toilet-dont-put-logic-in.html).
