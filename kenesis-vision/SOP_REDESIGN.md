# How SOP monitoring actually scales

**Your problem is real: changing the camera can change what the software is able to know. A reusable checklist alone does not fix that.**

Prepared 15 September 2026. This is a proposed redesign of Kenesis's delivery workflow, supported by public competitor evidence. It is not a claim that competitors share the same internal software or that Kenesis's current implementation was inspected. Updated with the founder's rubber-curing example; the second machine's observable signals remain unspecified.

## Your rubber-curing example: what to keep and what to replace

**Keep the production question: how long after the machine is ready does unloading happen? Replace the method of recognizing machine state when the equipment changes.**

Your current system infers loading/cooking/readiness from machine movement and colour intensity. That recognition method is specific to the machine and camera. It is not evidence that the timing workflow must be rebuilt for every factory.

The reusable sequence is: **load confirmed → cycle started → ready for unloading → unloading started → unloading completed**. Some machines may need different states, batch handling or exceptions; reuse this sequence only where the actual process agrees.

| Event | First machine: current candidate evidence | Different machine: evidence to investigate |
|---|---|---|
| Loaded | Your existing movement/colour checks, verified against footage | Visible sheet or tray placement; loading sensor if available |
| Cycle started | Your calibrated machine-motion cue | Machine controller cycle-start signal, visible display or distinct movement |
| Ready for unloading | Your calibrated colour/motion cue | Prefer a documented controller-ready signal; otherwise a validated indicator or display |
| Unloading started | First visible removal action | Hand/tool engagement or material movement, if distinguishable |
| Unloading completed | Mat visibly removed | Empty tray/chamber, exit movement or a removal sensor |

These are investigation options, not verified signals available at the second factory. A controller is the machine's control system; read-only access may require the manufacturer or factory automation engineer.

**Measure two different delays:** response delay = unloading-start time minus ready time; removal duration = unloading-complete time minus unloading-start time. Total ready-to-cleared time combines both. Your buyer should choose which matters. Waiting may be required for cooling or safe access, so agree the earliest permitted unloading time before labelling a delay avoidable. This measures handling delay; colour alone does not establish material cure quality.

### The redesigned onboarding workflow for this product

1. Agree the machine's actual states with its operator. Record normal cycles, aborted cycles, maintenance, product variants and mandatory waiting periods.
2. Find evidence for each event. Check machine signals first for internal readiness; use video where the action is visible. A signal saying ready still needs the factory's process definition.
3. Select an existing machine setup or commission a new one. Store the evidence source, camera requirements, timing settings and exceptions separately from shared delay calculations and reports.
4. Validate timestamps on unseen cycles across shifts. Measure readiness mistakes, unloading mistakes, timing error and the fraction of cycles that cannot be measured. Agree acceptable errors with the buyer before acceptance.
5. Launch silently first. Save evidence for disputed events. When a worker blocks the view, keep the cycle unverified; do not infer prompt unloading or blame the worker.

If readiness occurred between 10:00:05 and 10:00:12 while hidden, and unloading began at 10:00:20, the supported response delay is **8–15 seconds**, not an invented exact value. If readiness cannot be bounded, report it as unmeasurable. Synchronize video and machine clocks before subtracting timestamps.

### What would actually make this scale

Sell **ready-to-unload delay monitoring for supported curing-machine families** first. Build a tested library of machine setups. Reuse one setup across machines with the same relevant signals and validate each camera view. A new machine family may require paid engineering; a new angle may require camera work or additional examples.

Your scaling test is the next three comparable machines: do setup hours fall while timestamp accuracy and measurable-cycle coverage hold? If every machine still needs fresh experimentation, price it as an engineering project. Shared dashboards alone will not make that work economical.

This recommendation refines the earlier absence-monitoring hypothesis: your existing curing pilot now provides a more concrete starting point. It still needs verified economic loss and a paid commitment.

## What competitors actually do

| Approach | Public evidence | What it means |
|---|---|---|
| Constrain what the camera must see | Intenseye explicitly says it cannot model details that are not visible | Some requirements must be rejected or need a better view |
| Calibrate supported detections at each site | Protex describes camera-angle, lighting and layout calibration, followed by a silent validation period | “Pretrained” does not mean zero deployment work |
| Maintain the underlying vision models | Protex's lead vision engineer describes checking labels, balancing datasets and debugging predictions | Shared detectors improve through continuing engineering |
| Teach specific assembly processes | Retrocausal describes recording, labelling and deploying a process | Reusable platform; process-specific setup still exists |
| Control the imaging setup | Invisible AI's trial includes edge cameras and on-site training | Changing equipment can be how a supplier obtains repeatable results |
| Charge for additions | Intenseye lists custom engineering; Protex's public site fee includes setup | Delivery effort can be part of the commercial model |

Sources: [Intenseye visibility limits](https://www.intenseye.com/resources/faq), [Protex calibration and validation](https://www.protex.ai/), [Protex engineer's account](https://voxel51.com/customers/protex-ai-uses-fiftyone-to-intelligently-balance-computer-vision-datasets-and-improve-model), [Retrocausal setup](https://retrocausal.ai/), [Invisible AI trial](https://www.invisible.ai/one-line-offer/), [Intenseye commercial model](https://www.intenseye.com/pricing), [Protex setup pricing](https://aws.amazon.com/marketplace/pp/prodview-673or3sh2ujpe).

These sources do not establish that arbitrary SOP validation is profitable for every competitor. Deployment growth can include common safety detectors, installation services and hardware. It cannot be used as proof that all custom SOPs scale.

## The redesign: separate the procedure from the evidence

Today, your description suggests each SOP combines three decisions: what should happen, how this camera detects it, and what to do when something goes wrong. If these are rebuilt together, a new angle can force a whole new workflow.

**Proposed change:** keep the factory rule separate from the camera-specific way of observing it. Then reuse the rule only when the observations mean the same thing and pass the same test.

| Layer | Example | When it changes |
|---|---|---|
| Business outcome | Prevent dispatch before the required packing checks | Buyer/process changes |
| Procedure | Load item → confirm required component → seal → dispatch | SOP changes |
| Evidence for each step | Component visibly placed; barcode confirmation; sealing-machine signal | Available proof changes |
| Camera setup | Packing-table zone, useful angle, minimum visible detail, obstruction rules | Camera or layout changes |
| Timing and exceptions | Allowed rework loop, approved pause, maximum step interval | Factory operating rules change |
| Response | Review clip; notify supervisor; record correction | Team responsibilities change |

This is a design proposal, not a promise that changing one setting makes different camera views equivalent.

## Example: the same rule, different camera views

**Illustrative SOP:** confirm a component is placed in a box before the box is sealed. This is not assumed to be either of your actual SOPs.

| Factory situation | What the camera can establish | Correct handling |
|---|---|---|
| Overhead view clearly shows the component entering the box | The required action may be observable | Validate a visual step detector |
| Side view loses the component behind the worker | Placement is not reliably observable | Reposition/add a camera or use independent verification |
| Barcode confirms the part but not whether it entered the box | A scan occurred; physical placement remains uncertain | Revise the evidence requirement with the buyer; do not silently call it equivalent |
| Sealed box appears after an obstruction | The box is sealed, but the earlier step was unseen | Mark the sequence unverified; do not mark it passed |

**Key rule:** “not seen” is different from “did not happen.” An unseen step needs an unknown/unverified state. Otherwise, a new camera angle changes your error rate while the dashboard still looks confident.

## A repeatable onboarding workflow

### 1. Define what must be proved

For every SOP step, write the required action, acceptable evidence, timing, exceptions and consequence of an error. Separate visual checks from requirements such as torque, temperature or internal product quality. Agree with the buyer what a pass means.

### 2. Check visibility before quoting automation

Inspect representative day/night footage, worker positions, product variants and obstructions. For each step, record: observable, partly observable or not observable. A stream that connects successfully is not necessarily useful for the requested check.

Create a camera acceptance sheet specifying the useful view and scene conditions. If the camera moves or the layout changes, suspend affected checks until coverage is verified again.

### 3. Route the job into one of four paths

| Path | Definition | Commercial treatment proposed |
|---|---|---|
| Configure | Existing supported detection with a new zone, schedule or timing rule | Standard onboarding |
| Adapt | Familiar action but different view/product requiring labelled examples and testing | Paid bounded adaptation |
| Develop | New visual action, complex sequence or new machine connection | Separately scoped engineering project |
| Not observable | Evidence cannot be obtained from the available view | Change capture, narrow the promise or decline the check |

The distinction must come from tests and effort, not from calling everything “configuration.”

### 4. Build a procedure from supported events

Use shared events such as person entered zone, station covered, object placed, machine started and barcode accepted. Define required order, time limits, alternatives and rework. Each event must state its confidence, timestamp and evidence source.

A new procedure may only need a different sequence of existing events. A new action such as applying an unfamiliar sealant may need new detection work. If every event is novel, there is little reuse to claim.

### 5. Validate on footage that was not used for setup

Test across camera views, shifts, workers, products, valid exceptions and intentionally missing steps. Measure correct detections, missed events, unverified sequences and false alerts. Include unalerted footage so missed steps are not invisible to the evaluation.

Do not accept one blended accuracy number across all SOPs. Report each step's results and the end-to-end procedure result. Clear component placement does not compensate for an unobservable sealing check.

### 6. Launch silently, then enable agreed alerts

First log events without asking operators to react. Let the customer verify results. Enable notifications only for checks that meet the agreed criteria. Keep uncertain cases available for review instead of inventing pass/fail conclusions.

### 7. Maintain one reusable product and a record of exceptions

Store each site's camera setup, procedure rules, supported model versions and acceptance results together. A shared improvement must be tested against representative previous sites before release. Repeated failures should improve a reusable detector or cause a supported-condition restriction, not create an invisible permanent special case.

## How this becomes a business that can grow

There are two ways to get repeatability: reuse across similar customers, or charge enough for custom work. They can coexist, but they must be measured separately.

For Kenesis, start with one family of procedures, such as one defined packing workflow, rather than promising every factory SOP. The right family depends on the actual pilots. Adding a second factory is useful only if it tests reuse of the same evidence and rules.

Track these five quantities per deployment:

| Measure | Decision it supports |
|---|---|
| Engineering hours for first, second and third similar sites | Is reuse actually improving? |
| Fraction of requested checks accepted without new development | Is the supported product broad enough? |
| Share of operating time with adequate camera visibility | Does the service have meaningful coverage? |
| Monthly support and model-maintenance cost per live site | Can recurring fees cover delivery? |
| Paid conversion and renewal at the quoted scope | Is useful detection translating into a business? |

Do not count cameras, customers or funding alone as proof of profitable scaling.

## Illustrative delivery economics

The following numbers are assumptions to demonstrate the decision, not Kenesis actual costs or competitor prices.

Suppose one deployment requires 80 engineering hours at ₹1,500/hour: ₹1.2 lakh. Setup revenue is ₹30,000. Unrecovered setup cost is ₹90,000. If monthly recurring fees are ₹30,000 and direct monthly service costs are ₹12,000, monthly contribution is ₹18,000. Recovering the setup gap takes **five months**, before sales costs and central overhead.

If the same workflow needs 16 engineering hours at the next site, setup labor falls to ₹24,000. The same ₹30,000 setup fee covers that labor with ₹6,000 remaining. That reduction in repeated work is the scaling evidence to seek.

If every new site still needs 80 hours, either price the setup accordingly, narrow the supported procedure or accept that this is partly a services business. A recurring invoice by itself does not make custom delivery scalable.

## What I still need to tailor this to your product

The two actual SOP step lists; representative camera constraints; what the current system detects versus infers; and where your team spends the redesign time. Without those, this is a concrete operating model but not a verified implementation plan for Kenesis.
