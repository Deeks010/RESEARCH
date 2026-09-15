# Kenesis Vision: what to do with your six pilot requests

**Recommendation: test payment for reducing avoidable delays at workstations that need an operator.**

15 September 2026. This brief uses your clarification: India is the practical first market; all work is at the pilot/request stage; nobody has paid and no traction has been established. The recommended use case is a first experiment, not a proven winning market.

## The decision in one minute

You have evidence that factories will discuss problems and try technology. You do not yet have evidence that they will allocate recurring budget. Adding all six requested features would postpone the most important test: which problem is valuable enough to buy a solution for?

Start with one existing pilot site, one process and a production manager who can verify losses. Ask for a paid extension before further custom work. Expand only after the same offer works at more than one factory.

Workstation absence is the first candidate because it is already requested, can be precisely defined and may produce frequent measurable events. It is not unique: Spot and Assert directly advertise related monitoring. Its commercial value depends on whether an unstaffed station actually delays production. [Spot's absence offering](https://www.spot.ai/blog/person-absent-alerts-monitoring-workstation-downtime), [Assert's production measures](https://www.assertai.com/how-ai-powered-vision-is-redefining-time-management-and-productivity-in-manufacturing/)

## Your requests compared

The verdicts below are our assessment. They are not measured Kenesis performance or customer buying decisions.

| Request | Competitor evidence | Can it repeat across factories? | Decision now |
|---|---|---|---|
| Workstation absence | Spot advertises scheduled-zone absence alerts; Assert includes operator presence | Relatively repeatable if zones, shifts and exceptions are configuration | **First paid experiment**, tied to avoidable delay |
| Chitchatting | Visionify markets grouping/crowding; emerging Maglev markets gossip clusters | People gathering is observable; non-work conversation is not reliably established by proximity | **Do not make this the lead product** |
| SOP validation | Wobot checklists, Retrocausal assembly checks, Assert/Awiros industrial workflows | Simple visible rules can repeat; complex new sequences need more work | **Keep a narrow reusable subset** |
| Unauthorized restricted-area entry | Intenseye, Detect, Visionify and surveillance platforms | Entry into a zone is repeatable; individual authorization needs additional context | **Possible add-on**, or lead only with strong buyer urgency |
| CCTV intelligence chatbot | Protex reporting assistant, Staqu conversational dashboard, Avathon video search | Reusable interface; data coverage, indexing and answer trust remain hard | **Use later to access proven data** |
| Fall detection | Visionify explicitly advertises fall/person-down; Avathon also covers person-down | Repeatable in suitable scenes; crouching, occlusion and uncommon events complicate validation | **Targeted safety add-on** where response need is established |

Direct sources and product limitations follow. The wider [market report](KENESIS_MARKET_REPORT.md) covers 20 vendor offerings and major substitutes.

## 1. Workstation absence: useful only with operational context

**Sell:** “Know when a station that currently needs staffing is uncovered, so the supervisor can restore coverage and avoid delay.”

**Do not equate:** absent = idle = unproductive = avoidable financial loss. The worker could be fetching material, supporting another station, taking a planned break or waiting for a machine. Conversely, a person can be present while the process is stopped.

A repeatable first package could include designated station zones, staffing schedules, a configurable delay before alerting, planned-break exclusions, short evidence clips and an assigned responder. This is a proposed scope. Do not promise automatic cause attribution without supporting process data.

Measure confirmed uncovered minutes separately from lost productive minutes. Ask the supervisor to label the cause and action. Only count recovered output if the plant can use or sell it. If staff are absent because the machine is already broken, absence alerts may add no value.

**Main competitors to benchmark:** Spot, Assert, Visionify's staffing controls and Cogniphi. The target advantage is a better purchase for this specific Indian buyer, not ownership of an original feature. [Visionify area controls](https://visionify.ai/safety-platform), [Cogniphi industrial case](operations_competitors.md#cogniphi)

## 2. Chitchatting: the requested label is unreliable

Two people standing together could be troubleshooting, training or coordinating a task. A camera may detect their location and time together; that does not establish the content or usefulness of their conversation. Do not report non-work intent as a fact inferred from posture or proximity.

Visionify's examples advertise grouping and crowding in factories. That is narrower than verified chitchatting. Maglev's public product page uses a gossip-cluster claim, but no independent factory benchmark was established here. This is an emerging watchlist lead, not validated detection performance. [Visionify examples](https://www.visionify.ai/videos), [Maglev product claim](https://www.maglevsoftwares.com/ai-vision)

Ask the factory what harm it is trying to address: blocked passage, an unattended critical station or a delayed task. Measure that observable problem. Do not quietly replace an uncertain behavior label with an employee productivity score.

## 3. SOP validation: your scalability concern is partly right

**An SOP is not inherently unscalable. An unlimited promise to understand every factory's procedure is.**

| Type of check | Example | Likely delivery model |
|---|---|---|
| Reusable visible rule | A required station must be staffed during a defined period | Configure zone, schedule and timing |
| Reusable rule needing another signal | Nobody enters a zone while a machine is running | Camera plus trustworthy machine-state input |
| Repeated industry procedure | A visible packing step must precede dispatch | Reuse across similar lines; validate changed products/views |
| Bespoke detailed sequence | Verify every tiny assembly action across changing products | New labels, views and integration may make it project work |
| Not visible in CCTV | Confirm torque, internal seal quality or temperature | Requires other instruments or dedicated inspection |

Retrocausal already offers assembly-step verification. Its setup discussion emphasizes suitable camera placement for small components. Wobot offers configurable checklists. This is evidence that portions of SOP monitoring are productized, not proof every SOP can be handled cheaply. [Retrocausal](https://retrocausal.ai/), [Wobot checklists](https://wobot.ai/features/ai-powered-checklist-new)

For Kenesis, accept a new SOP only when it fits a reusable rule or a deliberately selected industry procedure. Record how many engineering hours the second and third deployments require. Repeated custom work is a delivery cost, not automatically a durable advantage.

## 4. Restricted-area entry: define “unauthorized”

There are two different problems: anyone entering a no-entry zone, and a particular person lacking permission to enter. A visible zone crossing can establish the first. The second needs an authorization source, such as an access-control record or permit system. Uniform color alone may not establish permission.

Many competitors advertise zone controls; they do not all expose the same authorization logic. Start with an unambiguous rule and ask what the current access-control or camera system already does. [Visionify zone offering](https://visionify.ai/safety-platform), [Detect and Staqu evidence](india_competitors.md)

Choose it as the lead only if a buyer names a costly recurring exposure, can act on alerts and commits budget. Otherwise it is a crowded add-on. A camera alert does not replace a suitable physical safeguard.

## 5. CCTV intelligence chatbot: useful interface, not complete knowledge

Separate three offers:

1. **Ask about recorded events:** counts, locations, durations and reviewed clips.
2. **Search indexed video:** retrieve relevant footage from supported cameras and retention periods.
3. **Explain factory outcomes:** combine video with schedules, machine states, production and business records.

These have different data needs and costs. A chatbot cannot answer reliably about footage never processed, expired recordings, events the detector missed or causes invisible to the cameras.

Staqu's versioned product page advertises Jarvis GPT conversational dashboards; confirm its current package in a demonstration. Avathon explicitly advertises natural-language search across live and archived footage. Both are advertised capabilities, not independent answer-quality benchmarks. [Staqu page](https://www.staqu.com/v2-front-page/), [Avathon video search](https://avathon.com/resources/transforming-industrial-safety-and-efficiency-avathon-integrates-nvidia-metropolis-to-supercharge-ai-powered-video-intelligence/)

Build the first version around the events Kenesis already measures well. Every answer should show the camera, time range, evidence and missing coverage. Distinguish “no matching event recorded” from “this never happened.” Do not lead the commercial pitch with “contains all the data.”

Measure whether it saves investigation/reporting time and whether that saving attracts budget. It is not established as a standalone buying reason for your pilot factories.

## 6. Fall detection: sell response improvement carefully

Visionify has explicit slip/fall and person-down offerings. The product category is therefore established. Its advertised accuracy, injury prevention and savings should not be transferred to Kenesis forecasts. [Fall product documentation](https://docs.visionify.ai/scenarios/slip-and-fall-detection/)

The first relevant buyer is a safety manager with isolated or slow-to-discover incidents and a response team. Test detection delay, notification delivery, false alarms and whether someone acknowledges the alert. Evaluate ordinary crouching, lying down for maintenance and occlusion as well as falls.

Use safely staged recordings or suitable authorized test footage. A short pilot with no actual falls provides little evidence about missed falls. Do not imply detecting a fall after it occurs prevents that fall.

## The first paid offer to test

**Scope:** one factory, one production process, a few existing useful views, scheduled workstation coverage and an agreed daily report. No requirement to build all six features first.

**Buyer:** production/plant manager who can approve spend and arrange a response. Confirm the actual buyer rather than assuming the person requesting features holds budget.

**Commercial commitment:** a paid extension with a fixed end date and written recurring price if agreed conditions are met. Set the fee from Kenesis delivery costs and the buyer's verified opportunity; this research does not establish an accepted rupee price.

**Pass:** usable camera coverage, independently checked events, confirmed avoidable delays, acted-on alerts and willingness to pay enough to cover delivery. Then test transfer to two other similar factories.

**Fail:** the factory likes demonstrations but will not pay; absence has no actionable cost; or every new site requires substantial custom engineering. Investigate the reason before expanding scope.

If this candidate fails, select the requested problem with the clearest budget commitment. Do not keep adding features to avoid a commercial decision.

## What remains unproven

No unique Kenesis feature, accepted price, renewal behavior, repeatable margin or relative detection advantage has been established. The internet research validates competitive coverage and category adoption. Your next evidence must come from a paid commitment and a measured result.
