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

## Receipt strip

`REGISTERED` [`0x220bbd1a…`](https://explorer-studio.genlayer.com/transactions/0x220bbd1a9e9e21daa985461aee79d3b59c1014ffb8c7fcb5fdeffa82acdabff3)
→ `DRIFT` [`0xab234bd6…`](https://explorer-studio.genlayer.com/transactions/0xab234bd69178fb7676a5e3cba061520d9b2c2007690d32bad3da32bff3ff8ad3)
→ `RESTORED` [`0xc9c93a80…`](https://explorer-studio.genlayer.com/transactions/0xc9c93a80ab9d6dcf0742cbd011b32218748af87afd107478ad361047ea68a19e)

- Contract: [`0x097Ec90fE613E37f2D5E878c4E09dCE464e782F4`](https://explorer-studio.genlayer.com/address/0x097Ec90fE613E37f2D5E878c4E09dCE464e782F4)
- Deployment: [`0x2ddba0e593d658a1414bd49d1cb0bb59040dea76452e811a4ae80cd213fdd663`](https://explorer-studio.genlayer.com/transactions/0x2ddba0e593d658a1414bd49d1cb0bb59040dea76452e811a4ae80cd213fdd663)
- Live record: `CHARTER-1791123041`; repaired side `RIGHT`; final codes are three `EQUIVALENT` entries.
- Exact deployed source SHA-256: `0ccbb13c6c66ae59ebb69a8ba2e41c6ac405e6d083444b4fc54312819d464527`.
