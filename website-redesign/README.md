# US website improvement research

## Start here

Open [the searchable report](Website-Redesign-Prospects.html) after downloading the repository. [Structured research](Website-Redesign-Prospects.json) contains the same company evidence and market notes.

## Result

- **30 businesses screened:** ten each in Pennsylvania, North Carolina and Ohio.
- **Five priority conversations, 12 conditional leads, 13 reserves.** These are research judgments, not sales forecasts.
- **30 published email routes:** nine owner-associated, 18 general and three uncertain or restricted-purpose contacts.
- All 13 primary email domains had mail-routing records. Inbox delivery was not tested.

The sample focuses on visitor farms, orchards and direct farm sales. It also includes a wholesale nursery and garden-service business. These states are a practical test sample, not a proven ranking of the best US markets.

## What each company record contains

Website and reviewed-page links; state and county; owner evidence; email and phone; commercial offers; activity evidence; the observed issue; a suggested improvement; qualification gaps; source URLs.

The report also includes market evidence, two competing providers' advertised prices, a bounded sales-test approach and an explicitly hypothetical time/revenue calculation.

## Main recommendation

Start with a narrow improvement to booking, ordering or current-season information. A small content error does not establish a need for an expensive redesign or rebrand. Full-site mockups have not been created and no outreach has been sent.

## Important unfinished work

**Homepage screenshots and visual assessments are not included.** Browser access was unavailable when requested. Current rankings use public page text and links only. No visual, mobile, speed, accessibility, form-delivery or checkout test was performed. A research-tool fetch failure was not treated as proof a website is down.

Before pitching a visual redesign, capture the live homepage, inspect desktop and mobile layouts, and revise the assessment. Confirm current operations, website control, existing supplier, budget and the actual business impact of the issue.

## Included working material

| File group | Purpose |
|---|---|
| `redesign_pa.json`, `redesign_nc.json`, `redesign_oh.json` | Source-backed state research |
| `redesign_market.json` | Market reasoning, competition, assumptions and limitations |
| `redesign_mail_domains.json` | Dated DNS checks |
| `build_redesign_report.py` | Generates HTML and the combined data export |
| `check_redesign_mail_domains.ps1` | Repeats mail-domain checks on Windows |
| `redesign_script_check.js` | Extracted report JavaScript for syntax checking |

To rebuild locally from this folder:

```sh
python build_redesign_report.py
```

Rebuilding does not revisit websites or refresh findings.
