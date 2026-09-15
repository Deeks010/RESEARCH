# Kenesis Vision research

## Start here

1. [Readable market research](Kenesis-Vision-Research.html): competitors, pricing, deployment evidence, six use cases and validation strategy.
2. [First factory shortlist](Kenesis-50-Factory-Prospects.html): 50 India-first prospects.
3. [Owner-led, cross-industry shortlist](Kenesis-Owner-Led-50.html): a separate 50, including nine reused companies.
4. [Updated owner contacts and draft examples](Kenesis-Owner-Email-Pack.html): latest contact enrichment and three worked emails for the second shortlist.

Download the repository and open HTML locally for the readable views. **The two prospect lists contain 91 unique companies, not 100.** The owner-email pack covers the latest 50, not all 91.

## Business context

Kenesis Vision is India-first and in unpaid pilots. The rubber-curing pilot detects machine stages and times removal after readiness. Different machines and camera views still require validation. No paid traction or universal plug-and-play compatibility was established.

The initial [research brief](RESEARCH_GOAL.md) is preserved. Later user clarification that pilots are unpaid takes precedence over its reference to initial customers.

## What is included

| Material | Where to find it |
|---|---|
| Overall assessment | [Market report](KENESIS_MARKET_REPORT.md), [market validation](market_validation.md), [validation playbook](validation_and_research_playbook.md) |
| Competitor research | [India](india_competitors.md), [global](global_competitors.md), [production specialists](operations_competitors.md), [Guardex](guardex_profile.md) |
| Commercial evidence | [Comparison](COMMERCIAL_COMPARISON.md), [India scale](india_commercial_scale.md), [global scale](global_commercial_scale.md), [SOP specialists](sop_scale_and_specialist_commercials.md) |
| Product decisions | [Six requested use cases](YOUR_SIX_USE_CASES.md), [SOP workflow](SOP_REDESIGN.md) |
| Exported prospect data | The four `Kenesis-*.json` files beside the HTML reports |
| Research working data | `prospects_*.json`, `owner_candidates_*.json`, selection, sector evidence and enrichment records |
| Email-domain checks | `prospect_mail_domains.json`, `owner_mail_domains.json` and their PowerShell scripts |
| Supporting evidence | Guardex reports, extracts and page images; `anu_contact_email_check.html` is a saved third-party source page, not an authored report |

## Contact and drafting status

- All 91 unique prospects have a published email. Domain routing is only a basic check; individual delivery remains unverified.
- For the latest 50, the enrichment pack records 12 named-leader routes, eight uncertain associations and 30 general routes. Some named addresses may be shared.
- Three worked draft examples are included. **There are not 50 finished personalized emails.**
- Facts about products, production, clients and owners must stay separate from inferred problems. No outreach has been sent.

## Rebuild the reports

Run from this folder. Python is required; the main market report also uses `markdown-it-py`.

```sh
python -m pip install markdown-it-py
python build_readable_report.py
python build_prospect_report.py
python build_owner_report.py
python build_owner_email_pack.py
```

Working research and checks are dated snapshots. Regenerating HTML does not refresh web evidence. Scripts that recreate contact records should be reviewed before rerunning because they may overwrite curated data.
