# Kenesis Vision: global direct-competitor evidence

Research date: 15 September 2026. Scope: software using installed industrial CCTV, with particular attention to factory safety and operations. This is a public-source review, not a hands-on benchmark or customer interview study. Product statements and results below are vendor claims unless explicitly labeled otherwise. Public pages can change. No future-dated material was intentionally used.

## Main conclusion

**Reusing factory CCTV is already the standard pitch of several established competitors.** Safety detection alone is crowded. Moving into operations does not create an empty category either: Protex, Intenseye, Voxel, viAct and Avathon all advertise operational visibility. The more promising opening is a specific factory problem solved with demonstrably better economics, deployment effort and accepted accuracy. That remains a hypothesis until tested with Kenesis customers.

“Software company” and “no additional computing hardware” are different promises. Cameras can be reused while video processing still needs an on-site computer, cloud capacity or both. Existing footage also cannot reveal objects or process states outside the camera's view. These constraints matter more than headline detection counts.

## Comparison at a glance

The cells summarize the linked evidence in the profiles below. “Offered” means publicly advertised, not independently tested.

| Competitor | Factory overlap | Existing-camera reality | Beyond basic safety | Commercial evidence | Main competitive strength: assessment |
|---|---|---|---|---|---|
| Protex AI | Very high | RTSP cameras + supplied edge computer; event clips in cloud | Material flow, downtime context, jams, enterprise-system data, action follow-up | Public AWS list pricing; named M&S case | Safety workflow maturity plus enterprise operational context |
| Intenseye | Very high | Existing IP cameras plus Sentinel Hub; optional specialized cameras | Cycle-time/flow, hygiene/quality checks, custom engineering | Annual per-camera model; numeric quote unavailable | Broad detections and physical interventions within one offering |
| Voxel | Very high | Existing cameras + shipped edge device; hybrid cloud | Workflow, space and resource use, margin-loss visibility | Named industrial cases; no numeric price verified | Named deployments, intervention workflows and safety expertise |
| viAct | High | RTSP software overlay offered; broader portfolio includes edge devices, wearables and sensors | Anomaly, workforce, inventory and space monitoring | Named construction case; factory cases often anonymous; quote-based | Wide industrial scenarios and software/hardware options |
| CompScience | High for safety; less direct for production performance | Existing video uploads documented; real-time SafetyPulse now advertised | Insurance claims and loss-cost analytics | Named food-manufacturing case; insurance-led distribution | Connection to brokers, insurance and financial risk management |
| Avathon / former SparkCognition | Very high for broad industrial vision | Existing feeds; standard GPU computers; local/cloud options | Inspection, productivity, logistics KPIs | Technical product sheet; anonymous India logistics case; no price verified | Broad industrial platform and customizable visual use cases |

## 1. Protex AI

### Product and deployment

Its current positioning spans safety and operations. Publicly listed detections include protective equipment, ergonomics, vehicle interactions, spills, blocked exits and conveyor jams. Operational examples include line starvation, machine downtime, material flow and dock use. It advertises joining camera evidence with manufacturing, warehouse, transport and maintenance systems, then generating recommendations and tracking actions. Video processing is local; anonymized event clips reach cloud dashboards. **This is direct overlap with an “AI on existing factory CCTV” company.** [Current product page](https://www.protex.ai/)

### Pricing and implementation friction

The vendor's AWS table lists **US$45,000 per site plus US$2,500 per camera for 12 months**. The site charge includes edge computing, setup and onboarding. Twenty cameras therefore imply **US$95,000** at list price. Renewal treatment of the site charge needs confirmation; do not assume it is permanently one-time. Embedded G2 reviews describe camera-selection burden, ergonomic false alerts and local IT work. These are individual reports, not representative failure rates. [AWS listing and reviews](https://aws.amazon.com/marketplace/pp/prodview-673or3sh2ujpe)

### Customer evidence

At M&S's Castle Donington distribution centre, Protex reports an 80% reduction in incidents and over 10% more near-miss reporting. The title says ten weeks; the narrative describes three months. The account links improvements to staff training triggered by observed patterns. “Incidents” and unsafe events are used loosely: **do not convert this into an 80% reduction in injuries.** No control group or complete exposure-adjusted dataset is provided. [M&S case](https://www.protex.ai/case-studies/marks-and-spencer)

### Implications for Kenesis — assessment

Its defensible advantage is likely the installed customer relationships, adoption process and accumulated operational context, rather than simply detecting helmets. A smaller, lower-effort package could compete where enterprise economics or onboarding are excessive. That requires measuring Kenesis's real support and compute costs. Do not claim that enterprise integrations or corrective-action follow-up are unserved opportunities.

## 2. Intenseye

### Product and commercial model

The current pricing page offers an annual subscription per connected camera. All standard safety detections, insights, action tracking and its AI assistant are included; enterprise connectivity and its broader safety-management suite are separate flat-fee modules. Numeric rates are not public on that page. It describes adding a **Sentinel Hub** to process camera feeds locally and optional cameras where coverage is insufficient. It also offers custom engineering for safety, operations and quality. **Do not describe the current offer as cloud-only or hardware-free.** [Pricing and deployment](https://www.intenseye.com/pricing)

The product menu covers PPE, vehicle–pedestrian interactions, restricted zones, ergonomics, housekeeping and behavior. Advertised extensions include cycle-time analysis, asset/area utilization, handwashing, quality-station checks and cleanroom integrity. These menu claims establish competitive intent; they do not prove equivalent maturity across every workflow. [Use-case overview](https://www.intenseye.com/customers/case-studies)

### Compatibility and limits

The FAQ lists cloud and on-premises options and H.264/RTSP camera compatibility. It explicitly acknowledges that the AI cannot model a small item that a person cannot see in the image, giving earplugs as an example. Camera positioning and visibility therefore remain deployment work. The FAQ and new pricing page describe different levels of the offer; confirm the available deployment configuration in a quote rather than assuming every historical option remains equivalent. [FAQ](https://www.intenseye.com/resources/faq)

### Customer evidence

The Swire Coca-Cola case reports a 27% decrease in lost day rate within a year and over 60% fewer hazard detections in 2022. A 50% total injury-rate reduction by 2030 is a **target**, not an achieved result. The described deployment is in Hong Kong; do not generalize the result across all Coca-Cola facilities. The page even contains inconsistent facility-count descriptions, so those counts are excluded here. Results followed inspections and safety briefings as well as AI deployment. [Swire case](https://www.intenseye.com/case-studies/swire-coca-cola)

### Implications for Kenesis — assessment

“More safety use cases at no extra charge” is already part of a competitor's packaging. Intenseye's combination of standard detection, custom engineering and optional physical devices challenges both generic software and bespoke vision projects. A narrower promise with clear performance boundaries is more credible than competing on the longest feature list.

## 3. Voxel

### Product and deployment

Voxel sells industrial safety, operations and risk-management visibility using installed camera systems. It advertises task ownership, deadlines, coaching and executive reporting. Its compatibility and accuracy percentages are vendor claims without a public benchmark sufficient for comparison here. No public numeric subscription price was verified. [Product overview](https://www.voxelai.com/)

The August 2026 Autokiniton story describes an edge device shipped to the plant, installed in its network room, approved through change control and connected after firewall rules were applied. The first installation took about **one week from device arrival to live video**, followed by expansion to four additional plants. That is a better planning example than treating the homepage's 48-hour deployment claim as a universal guarantee. [Autokiniton deployment](https://www.voxelai.com/customer-stories/how-autokiniton-deployed-safety-technology-without-overloading-it)

### Covered factory problems

Beyond ergonomics, PPE and vehicle risk, the operations offering addresses workflow and space utilization to expose lost capacity and throughput. The Piston Automotive example distinguishes an 86% drop in vehicle safety incidents from a measured 60% utilization rate for material handlers. **The latter is a diagnostic finding, not a 60% productivity improvement.** [Operations offering](https://www.voxelai.com/solutions-operations)

### Customer evidence and inconsistency

The current Americold case claims 70% fewer injuries, 100% fewer lost-time days and US$1.1 million in savings. It describes changes in training, lifting behavior, speeding and refrigerated-door practices. [Current Americold case](https://www.voxelai.com/customer-stories/americold-saved-1-1m-annually-and-reduced-injures-by-70)

A **2022** vendor PDF instead gives 77% fewer overall injuries and US$1.1 million direct annual savings for a central California distribution centre. It also claims 100% lower recordable incident rate and 2,000% return on investment. The differences may reflect definition or presentation changes, but the source does not reconcile them. Do not combine the most favorable metrics into a supposedly verified result. [Historical Americold PDF](https://uploads-ssl.webflow.com/62cf4f5eff50c678585c2a90/6345405a43792138e7a4434d_Americold%20Case%20Study.pdf)

### Implications for Kenesis — assessment

Named factory and warehouse deployments strengthen Voxel's sales credibility. Its strength includes helping customers act on data. The opening is not simply adding dashboards; it is making one intervention measurably easier or more economic for a defined factory segment.

## 4. viAct

### Product scope

The manufacturing offering advertises RTSP camera reuse and a library of 200+ AI modules. Relevant categories include PPE, work at height, confined spaces, vehicle proximity, suspended loads, housekeeping, ergonomics and workforce heatmaps. The broader catalogue includes inventory, space and workforce monitoring. It also promotes sensors and wearables. Thus, **not every claimed outcome is attributable to CCTV software alone.** A larger catalogue is not proof of greater tested coverage. [Manufacturing offering](https://www.viact.ai/industry/manufacturing-ai-safety-solution)

Anomaly detection is explicitly marketed for production workflows and machine idling. An anonymous Saudi manufacturer case claims 76% less unplanned downtime in six months. With no customer identity, baseline data or method sufficient to reproduce the measure, treat this as a weak lead for validation rather than an established performance benchmark. [Anomaly detection](https://www.viact.ai/video-analytics-solution/anomaly-detection)

### Hardware and pricing

viMAC is a distinct in-cabin edge system with cameras, alarms and a display for vehicle collision risks. It is not equivalent to installing only software on a factory's existing fixed cameras. [viMAC](https://www.viact.ai/vimac)

The fleet-management page says pricing depends on vehicle count, camera coverage, selected modules and cloud/local/hybrid deployment. No fixed price is published there. Factory CCTV-only pricing still requires a separate quote. [Commercial terms description](https://www.viact.ai/fleet-management?lang=zh)

### Customer evidence

A dated 28 August 2026 announcement names Alliad's healthcare construction project in Côte d'Ivoire. It reports 41.7% fewer PPE violations and 46.3% fewer danger-zone violations over three months using existing cameras. That is useful named evidence for camera reuse, but **it is construction evidence, not a manufacturing productivity result**. It remains vendor-reported and does not provide a controlled comparison. [Alliad announcement](https://www.viact.ai/news/viact-ai-delivers-measurable-safety-gains-for-alliad)

### Implications for Kenesis — assessment

viAct overlaps with both standard safety detection and custom industrial scenarios. Software-only focus may simplify Kenesis's operations, but “no new cameras” is already in viAct's offer. A reliable, independently scored factory-specific result would be more persuasive than matching anonymous percentage claims.

## 5. CompScience

### Business model and current scope

CompScience combines workplace-risk technology with workers' compensation insurance and broker distribution. Its current risk-management page advertises live SafetyPulse alerts for missing PPE, slip hazards and machine-guard problems. Alerts are prioritized for safety and risk teams; dashboards connect observations to claims and financial exposure. **It is stale to classify CompScience solely as retrospective video analysis.** [Active Risk Management](https://www.compscience.com/active-risk-management/)

It says it does not sell cameras and can use most typical security-camera systems, with installation partners where needed. Phone capture is another option. These statements establish flexibility, but they do not specify all compute requirements for its real-time product. No numeric software price or factory-specific Indian offer was verified. [Broker portal FAQ](https://www.compscience.com/portal/)

### Customer evidence

The Keystone Natural Holdings case describes uploading 270 hours of existing security footage for analysis. It reports 43% lower ergonomic hazards at Parsippany and 77% lower slip/trip/fall hazards at Philadelphia following recommendations and training. These are different facilities and different hazard measures; they should not be merged into a company-wide injury reduction. The public text does not establish a controlled baseline or measurement period. [Keystone case](https://www.compscience.com/keystone-case-study/)

The SafetyPulse link resolves to a login screen. No authenticated inspection was performed; current detailed performance and deployment specifications remain unknown. [SafetyPulse access page](https://safety.compscience.com/)

### Implications for Kenesis — assessment

Insurance distribution and connecting detected hazards to financial losses can be a stronger commercial advantage than another detector. A broker-led route is worth investigating for Kenesis, but copying a US workers' compensation model into another country cannot be assumed to work. For pure production performance, CompScience is less directly overlapping than the other five.

## 6. Avathon / SparkCognition

### Identity and product

SparkCognition became Avathon in October 2024; do not count them as separate competitors. [Company announcement](https://avathon.com/resources/avathon-launches-the-first-system-level-industrial-ai-platform/)

Its Visual AI product sheet lists more than 125 use cases spanning safety, security, inspection and productivity. It describes existing CCTV/PTZ/mobile/drone feeds, GPU computers, local or cloud deployment, configurable dashboards and role-based alerts. This supports software-led camera reuse, not zero compute costs. Numeric pricing was not verified. [Visual AI product sheet](https://avathon.com/wp-content/uploads/2024/11/Visual-AI-Product-Sheet-A-VAA-PS-1162024-v1.0-1.pdf)

The current safety offering advertises temporal video analysis using NVIDIA VSS, including vehicle near misses, PPE, unauthorized access, machine guarding, working at height, fire/smoke, person-down and suspended-load zones. Claims of fewer false alarms lack a comparable public benchmark in the reviewed page. [Visual AI for safety](https://avathon.com/solutions/avathon-autonomy-for-hse/)

### Customer evidence

An anonymous global distributor used existing CCTV for third-party logistics oversight in India. The public case covers vehicle use, turnaround time, labor utilization, throughput by unit type and space use. It says productivity improved but gives no numeric result in its ungated summary. This is particularly relevant evidence that **India logistics operations on existing CCTV is already an offered use case**, not an uncontested opening. [India logistics case](https://avathon.com/resources/case-study-improve-logistics-and-productivity-visual-ai/)

### Implications for Kenesis — assessment

Avathon overlaps with an open-ended industrial vision platform. Its breadth makes “we customize factory AI” insufficient differentiation. Kenesis can instead test whether a packaged solution delivers a specific business result with much less project work. The public evidence reviewed here is stronger on product breadth than named factory outcomes.

## Targeted follow-up: Kenesis's actual pilot requests

**Updated commercial context:** India is the practical first market. Existing engagements are unpaid pilots, not paid traction. Workstation absence, chitchatting, SOP validation, unauthorized restricted-area arrival, a CCTV intelligence chatbot and falls are requested features. Demand for a free trial does not establish a software budget or willingness to renew.

| Requested feature | Verified competitive overlap | What is still unproven |
|---|---|---|
| Workstation absence | Spot AI explicitly markets person-absent alerts at critical production stations. ACTi lists configurable absence-duration and station-occupancy rules. | That Kenesis can earn a premium for the same basic alert. Neither feature page supplies comparable India pricing or independently checked factory savings. |
| Chitchatting | viAct advertises idle/waiting time, break overstay and late-start monitoring. This is related, not evidence of recognizing conversation meaning. | That silent CCTV distinguishes casual talk from instructions, a quality discussion or waiting for material. |
| SOP validation | viAct advertises procedure deviations and assembly-sequence errors using vision plus context. NAVA lists configured work-sequence monitoring as a professional service. | Reusable setup across materially different processes with little engineering. A generic claim of “SOP compliance” does not establish this. |
| Restricted-area arrivals | Several profiles already document zone/intrusion overlap. | Whether a person entering is unauthorized requires an authorization rule or external access/permit context. Crossing a line alone does not establish identity or permission. |
| CCTV chatbot | Protex and Intenseye offer assistants over platform data; Avathon explicitly advertises natural-language video search. | Exhaustive answers over all stored footage, with known missed-event rates and affordable processing. |
| Fall detection | viAct specifically advertises sudden collapse/fall and prolonged immobility; Avathon's safety offer includes person-down. | Performance for actual factory camera angles, occlusion and normal crouching/lying tasks. Detecting someone down is not proof of diagnosing unconsciousness. |

Sources and precise distinctions:

- **Station coverage is already a named feature.** Spot AI's August 2026 article describes configurable person-absent alerts for critical workstations. ACTi describes production-station occupancy and absence duration thresholds. These are vendor feature descriptions, not evidence of paid Indian installations. [Spot AI](https://www.spot.ai/blog/person-absent-alerts-monitoring-workstation-downtime), [ACTi](https://www.acti.com/fr/applications/absence-detection)
- **Idle time is broader than worker absence.** viAct's workforce page includes waiting for tools, permits, approvals and handovers, plus excess walking and break overstays. It does not establish reliable identification of non-work conversation. This matters commercially: blaming workers for upstream shortages would misidentify the factory's actual loss. [viAct workforce monitoring](https://www.viact.ai/solutions/industrial-workforce-productivity-monitoring-solution)
- **SOP capability may still be a project.** viAct's quality article advertises SOP deviations and assembly-sequence errors. NAVA's AWS offer explicitly calls itself a computer-vision professional service; it includes camera assessment, activity-state definition and optional machine/production data. These claims show competition but not self-service SOP generalization. [viAct quality](https://www.viact.ai/post/ai-powered-quality-management-systems-5-ways-generative-ai-adds-value), [NAVA service listing](https://aws.amazon.com/marketplace/pp/prodview-ntumluomj67bu)
- **Three chatbot products are easy to confuse.** Protex's whitepaper shows questions about top risks with detected-event counts. Intenseye's Chief is an assistant grounded in platform information; its Visual Analytics product is primarily spatial heatmaps and pathways. Avathon separately advertises searching live and archived video with natural language plus indexing and summaries. None of these public descriptions proves lossless recall of every activity across unlimited footage. [Protex event-query example](https://24888392.fs1.hubspotusercontent-eu1.net/hubfs/24888392/Content/Mastering%20Unstructured%20Data%20in%20Health%20and%20Safety%20Management%20Whitepaper.pdf), [Intenseye Chief](https://www.intenseye.com/products/software-chief), [Intenseye Visual Analytics](https://www.intenseye.com/products/software-visual-analytics), [Avathon video search](https://avathon.com/resources/transforming-industrial-safety-and-efficiency-avathon-integrates-nvidia-metropolis-to-supercharge-ai-powered-video-intelligence/)
- **Fall alerts are not a new category.** viAct describes detecting sudden collapse, prolonged immobility and abnormal posture. The page does not provide a controlled factory benchmark sufficient to establish precision or missed-fall frequency. Test staged safe scenarios and ordinary similar movements; do not treat emergency marketing language as measured reliability. [viAct worker-down detection](https://www.viact.ai/video-analytics-solution/unconscious-worker-detection)

**Recommendation — assessment:** test a narrowly defined critical-station coverage product first if absence creates measurable stoppage at these pilots. Include approved breaks, machine state and reviewable clips. Treat this as a candidate to win on deployment and economics, not feature novelty. Offer the chatbot initially as an evidence-linked interface to measured events, with its coverage stated. Keep arbitrary SOP understanding and judgments about chitchatting out of the initial guaranteed promise until their commercial value and reliability are demonstrated.

## What this evidence does and does not validate

**Validated:** multiple companies sell this category; camera reuse is common; named industrial deployments exist; some customers describe financial gains; software deployments still involve configuration, compute and organizational follow-through.

**Not validated:** Kenesis's willingness-to-pay, expected conversion, achievable margins, independent comparative accuracy, market share or a feature competitors cannot provide. Vendor case studies cannot establish these.

**The strongest testable opening:** investigate one recurring loss at Kenesis's unpaid pilot sites. If it is verified, package detection, a specific corrective action and a measured financial result. Require the same camera set, operating shifts, human-reviewed events and exposure denominator before/after. Compare against the factory's current method and at least one credible competing quote. The minimum distinctiveness is a repeatable customer outcome, not a novel-sounding use-case name.

## Questions to put in competitive quotes

1. Which exact camera views are usable? Which fail, and why? What happens at night, during occlusion and after a camera moves?
2. What local computer, graphics capacity, network access and cloud transfer are needed? Who pays and maintains them?
3. What is the full annual cost at the same camera/site scope, including deployment, support, custom rules, integrations and renewals?
4. What human-reviewed precision, missed-event rate and false alerts per camera-hour will the vendor accept in a live trial?
5. Which named customer will confirm an outcome with its denominator, time window and non-AI interventions disclosed?

Source inventory: distinct primary/vendor URLs are cited inline, including vendor-authored marketplace listings and embedded third-party user reviews. No claim here should be represented as an independently replicated trial result.
