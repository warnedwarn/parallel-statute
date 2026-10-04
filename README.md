# Parallel Statute

> Two official texts. One legal effect. Every section must survive the crossing.

Parallel Statute is a clause-complete parity register for instruments published in two official languages. It is not a translator and it does not reward similar wording. It records whether the paired texts preserve the same rights, duties, quantities, exceptions, and deadlines.

## The ledger card

The publisher freezes:

1. two language labels;
2. a short ordered section map;
3. two separately hosted official texts;
4. an independent auditor wallet; and
5. a bounded repair window.

The auditor starts the comparison. Validators retrieve both texts and must return one code and one note for **every** frozen section. Contract code rejects shortened arrays, unknown labels, or a leader result whose source digests differ.

| Code | Meaning |
|---|---|
| `EQUIVALENT` | same operative effect |
| `MATERIAL_DRIFT` | a right, duty, number, exception, or deadline changes |
| `MISSING_LEFT` | the left text omits the section |
| `MISSING_RIGHT` | the right text omits the section |

All-equivalent records become `PARITY`. Any other partition becomes `DRIFT`. The publisher may replace exactly one side, from that side's original authority, while the untouched digest stays frozen. That produces `RESTORED` or terminal `UNRESOLVED`. Anyone may close an abandoned repair after expiry.

## Local proof

```text
genvm-lint contracts/contract.py
python -m pytest -q
```

The included bilingual excerpts are synthetic operator-controlled fixtures. They test the primitive; they are not authoritative translations.
