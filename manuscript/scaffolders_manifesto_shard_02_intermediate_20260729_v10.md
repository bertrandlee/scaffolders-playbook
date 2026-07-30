# INTERMEDIATE

*Twenty-one patterns for work that has to outlive the conversation that created it.*

Assumes the Beginner section. If you skipped ahead, skim it first — it is ten patterns and it will not take long. Grouped below by category: **Foundation** is workflow and lifecycle hygiene, **Practices** is established discipline applied with unusual rigour, and **Architecture** begins where a single conversation stops being enough.

## Foundation

### Debugging a Spreadsheet Like Production Code
*Find every cause before you fix anything.*
*(cross-reference: `[SCF-09]` · **Intermediate**)*

A formula breaks, you patch the one cell you noticed, and three other broken cells sail on untouched — because you fixed a symptom, not the cause. Spreadsheets are where non-developers actually live, and they deserve the same discipline a programmer gives code.

- **Analogy:** The plumber who paints over the damp patch and leaves the burst pipe. You'll be calling again next month.
- **Benefit:** Converts a silent, spreading spreadsheet error into a loud, located one — before it corrupts a decision you make off the numbers.
- **Apply:** Find *all* the root causes first, before fixing anything. Then fix each one behind a check that proves it's fixed. The standout technique is an **assertion cell** — a formula that shouts ("COLUMN MOVED") the moment a column silently shifts out from under your other formulas. *"Don't fix anything yet. List every distinct root cause you can find in this sheet, and for each one tell me what check would prove it's fixed."*
- **Guardrail:** A check you've never seen fail is a hope, not a control. Deliberately break it once to confirm it actually fires.
- **Related:** → Self-Installing Guards

### Prune the Ceremony Your AI Can't See
*Name the ritual it can't see itself performing.*
*(cross-reference: `[SCF-12]` · **Intermediate**)*

An AI given a standing instruction ("check the files at the start of each session") can misfire it on *every* turn — because from the inside, it can't tell a fresh start from a continuation. Worse, the repetition reads to the AI as diligence. It cannot perceive its own ritual.

- **Analogy:** A colleague who introduces himself fully every morning. Not thorough — genuinely unable to tell you've already met.
- **Benefit:** Removes empty ceremony that would otherwise accumulate unchecked, because the only party who can see it is you.
- **Apply:** Part of your job as the human is to watch for and name repetition the AI is structurally blind to. When a step fires that doesn't need to, say so, and scope the instruction to its real trigger. *"You've run that check on every turn this session. Scope it: run it only when [trigger], not on continuations."*
- **Guardrail:** This isn't the AI being careless. It's a genuine blind spot: ritual and diligence look identical from inside the loop. The pruning has to come from outside it.

### Treat "I Can't" as a Claim to Test
*Treat "I can't" as a claim to test.*
*(cross-reference: `[SCF-13]` · **Intermediate**)*

You reconnect a tool, open a fresh thread, or upgrade an app, and ask the AI to do something it did easily last week — it tells you it can't. Often, it's wrong: a stale self-image, not a real limit. An AI's model of its own abilities is perishable and frequently out of date, especially right after anything changed.

- **Analogy:** The shop assistant who says "we don't stock that" without looking. Sometimes true; it costs nothing to make them check the back.
- **Benefit:** Recovers capabilities you'd otherwise leave on the table because the AI misdescribed itself — a real cost, paid silently.
- **Apply:** Treat "I can't" as a claim to test, not a fact to accept. Probe the capability directly with a small disposable attempt. If it fails, read *why* — a permission problem is different from a genuine absence. *"Don't tell me whether you can — try it on something disposable and show me what actually happened, including the error if it fails."*
- **Guardrail:** The flip side of Time-Grounding's lesson: the model is an unreliable narrator of *itself*, in both directions. Don't trust the "no" any more than you'd trust an unverified "yes."
- **Related:** → Time-Grounding ([SAFE-04])

### Test the Whole Channel, Not Just the Step
*Test the assembled workflow on something disposable before you trust it on something real.*
*(cross-reference: `[SCF-14]` · **Intermediate**)*

You attach a document to your AI session and the model replies with a confident, detailed summary — and three exchanges later you notice the reply makes no reference to anything in the document, because the upload failed silently. Or you write a file to cloud storage, get a confirmation ID back, verify the metadata — and discover nine days later that what landed on the server is not what you composed. Every individual step confirmed itself. The property *does the assembled chain produce what I intended* was never tested as a whole.

- **Analogy:** A building whose wiring, plumbing and fire doors each passed their own inspections — but nobody ran the fire drill that would have shown the door doesn't seal the hallway in a real fire.
- **Benefit:** Catches the failure class where every step individually succeeds but the assembled chain fails — which produces no error message and is therefore invisible until you check the end-to-end output.
- **Apply:** Before using a workflow on real work, run it once end-to-end on a small, disposable test and check the final result, not just the intermediate confirmations. "Upload succeeded" is a step result. "The model read what I uploaded" is a chain result. They are not the same claim. *"Before we use this on the real task: run it on this dummy input and tell me what came out at the end — not just whether each step reported success."*
- **Guardrail:** A successful end-to-end test confirms the channel worked once, under those conditions. A different model, a different connection, or a larger payload can produce a different result. Re-run the channel test whenever something in the chain changes.
- **Related:** → Treat "I Can't" as a Claim to Test ([SCF-13]), → Both of You Can Be Wrong ([PRAC-01])
- **Lineage:** End-to-end testing versus unit testing — the integration testing discipline in software engineering. The specific failure mode here (step-level confidence with chain-level failure) is the integration gap.

---

### One Thread Per Topic, Like a Standing Specialist
*Keep one thread per topic, like a standing specialist.*
*(cross-reference: `[SCF-01]` · **Intermediate**)*

Mix legal questions into your finance thread and the context bleeds both ways — the thread starts sounding like neither advisor, competently. Keep one durable thread per domain, each treated like a standing specialist.

- **Analogy:** Nobody asks their accountant about a rash.
- **Benefit:** Keeps each thread's context pure and its persona stable, instead of slowly blending into a generalist that's mediocre at everything.
- **Apply:** One durable thread per domain, treated like a standing advisor; don't conflate.
- **Guardrail:** Segmentation minimizes token bloat and drift; it doesn't substitute for the memory registry that lets a fresh thread inherit context.
- **Related:** → Intentional Model Routing

### Match the Model to the Job, Not Habit
*Match the model to the job, not habit.*
*(cross-reference: `[SCF-02]` · **Intermediate**)*

Default to one model out of habit and you'll either overpay for a simple task or underpower a hard one — and a model asked "are you the right choice for this?" will rarely say no.

- **Analogy:** You don't take the motorway car to the corner shop. And the salesman is the last person to ask which car you need.
- **Benefit:** Matches spend to task difficulty instead of habitually overpaying or underpowering, and catches a model recommending itself out of built-in bias.
- **Apply:** Route the judgment to a *different* AI lineage: describe your workflows and real cost constraints, **require it to search the current model lineup and pricing live**, and ask for the best fit-for-purpose balance with reasoning shown. *"Here's my workflow and my cost constraints. Search the current model lineup and pricing, then tell me which model fits which task and why — including where a cheaper one would do."*
- **Guardrail:** A competitor model has mild structural bias; treat its recommendation as a second opinion to reconcile against the provider's own current pricing page.
- **Perishability (as of 1 Jul 2026, SST — illustrative, expected to change):** Opus 4.8 leads on the hardest long-horizon reasoning/coding; Sonnet 5 is at rough parity on most knowledge work at lower cost. *Memorize the method, not the models.*
- **Related:** → Cross-Model Create-and-Review

### Don't Trust What It Says About Itself
*Don't trust it when it tells you how much it remembers.*
*(cross-reference: `[SCF-03]` · **Intermediate**)*

Ask a model "how full is your context window?" and you'll get a confident-sounding number that has nothing to do with reality — it's a guess, not a readout. Trust what you can observe instead.

- **Analogy:** Asking someone late in the evening how sober they are. The answer is confident, and the answer is not evidence.
- **Benefit:** Catches quality decay before it produces a bad answer you act on, rather than after.
- **Apply:** Trust behavioral signs of decay (dropped constraints, forgetfulness) over the model's self-report; do a clean handover the moment continuity slips.
- **Guardrail:** Self-reported context health is unreliable — the same self-attestation trap that runs through this whole book.
- **Related:** → The Swap Disk Protocol

### Communication Style Adjustment
*Ask for the tone you need, not the default one.*
*(cross-reference: `[SCF-04]` · **Intermediate**)*

You need a blunt, skeptical read on a decision, and the model hands you warm, hedged, helpful-generalist prose instead — because that's its default register, not because it can't do better. Ask for the register you need instead of accepting whatever arrives.

- **Analogy:** A waiter's default is cheerful. If you want the honest verdict on tonight's fish, you have to ask for it plainly.
- **Benefit:** Gets the right kind of answer on the first try, instead of a generically helpful one you then have to re-ask in the tone you actually needed.
- **Apply:** Command the register directly rather than accepting the default. *"Answer as a skeptical analyst, not an assistant. No hedging, no encouragement — tell me what's weak."*
- **Guardrail:** Changing the register changes the delivery, not the reliability. A model told to be blunt produces blunt-sounding prose whether or not the claim underneath deserves it — skepticism in the tone is not skepticism in the sourcing. Ask for the tone you need, then check the content exactly as you would have anyway.

### Asymmetric Resource Substitution
*Paste text instead of a picture whenever you can.*
*(cross-reference: `[SCF-05]` · **Intermediate**)*

You screenshot a page of plain text and upload it as an image, burning one of a handful of daily image slots — when pasting the same words as text would have cost nothing. Spend the scarce channel on content that genuinely needs it, not on content that had a cheaper option available.

- **Analogy:** Using the last stamp in the drawer for a message you could have phoned in.
- **Benefit:** Stretches a thread's useful life further before hitting a hard cap, by not spending a scarce quota on content that had a cheaper channel.
- **Apply:** If content can be read as text, paste the text rather than uploading an image of it; ration scarce image slots for genuinely un-extractable visuals.
- **Guardrail:** Extends a thread's useful life *further*, not indefinitely — text still accumulates tokens toward the same limit.
- **Perishability (as of 2026, illustrative):** the specific caps and their asymmetry are interface-specific and change; state the principle, not the numbers.

### Flat-File Text Injection
*Attach big text as a file, don't paste it.*
*(cross-reference: `[SCF-06]` · **Intermediate**)*

You paste a genuinely large document straight into the chat box, and the formatting mangles or the interface silently truncates it. The same content attached as a plain file sails through untouched.

- **Analogy:** Nobody reads a fifty-page contract down the phone. You send it over.
- **Benefit:** Avoids the silent formatting corruption or hard rejection a giant inline paste risks, for the cost of one extra click.
- **Apply:** For bulky text payloads, attach as a file rather than pasting inline.
- **Guardrail:** Perishable — interface-specific behavior; state as an as-of-2026 technique.
- **Related:** → Reader vs. Machine: Choosing the Output Format

### Workflow-Anchored Connector Discovery
*Describe your actual task and ask what can do it for you.*
*(cross-reference: `[SCF-07]` · **Intermediate**)*

You spend twenty minutes manually copying data between two tools before it occurs to you to ask whether a connector already does this — it did, and nobody had ever surfaced it to you. Describing the actual friction surfaces it; asking generically "what can you do" doesn't.

- **Analogy:** Ask a hardware shop "what do you sell?" and you get a shrug. Describe the dripping tap and you get the part.
- **Benefit:** Replaces manual busywork with a native integration you didn't know existed, often in the same conversation where you first hit the friction.
- **Apply:** *"I'm working on [workflow]. What connectors, integrations, or tools do you have that could do this more efficiently?"*
- **Guardrail:** Discovering a live data connector doesn't retire source-grounding — a live feed is still a source to reconcile, not a trusted endpoint to automate without oversight.
- **Perishability (as of 2026):** the specific capabilities are date-sensitive; the durable move is the probe.
- **Related:** → Intentional Model Routing

### Park a Task So You Don't Lose Your Train of Thought
*Park a task in a list instead of losing your train of thought.*
*(cross-reference: `[SCF-08]` · **Intermediate** — not a novel idea; the mid-flow capture ritual is the teaching point)*

A task surfaces mid-conversation and you have two bad options: derail to handle it now, or hold it in your head and probably lose it. The work queue is the third option — capture it into the persistent artifact and keep going.

- **Analogy:** A note on the fridge, not a promise to yourself that you'll remember. The fridge is still there tomorrow.
- **Benefit:** Keeps your current thread of thought intact while nothing gets silently dropped — the task waits in a durable ledger instead of your memory.
- **Apply:** Mid-flow, *"put this in our work queue at [low / mid / high / top] priority."* Notice the phrase is fixed. That is deliberate: *"remember this if it's important"* hands the model a judgement about how much you meant it, and that judgement is least reliable exactly when the stakes are highest. A phrase you chose in advance removes the inference step. The queue lives as a section in the working file, not in the chat.
- **Guardrail 1 — it must live in the persistent artifact, not chat memory.** A queue kept only in the conversation dies with the thread — "add to queue" quietly becomes "mention and forget."
- **Guardrail 2 — priorities are the human's call, and they drift.** The model records what you assign; it shouldn't silently re-rank. Review periodically — a mid-priority item from months ago may now be dead or urgent.
- **Related:** → The Swap Disk Protocol, The Self-Correcting Feedback Loop

---

## Practices

### Both of You Can Be Wrong
*Trust each other's work — but both of you check it.*
*(cross-reference: `[PRAC-01]` · **Intermediate**)*

An AI-drafted expense reconciliation looks clean — tidy formatting, plausible totals — until a human catches a transposed account number the model never flagged. The following week, having learned to trust the tool, the same human misses an error the AI would have caught instantly. Two failure modes bookend this relationship: trusting everything the model produces, or trusting so little you barely use it. Both come from the same mistake — assuming only one party can be wrong. Build the working relationship on the premise that both of you err.

- **Analogy:** Two people counting the till at closing. Not because either is dishonest, but because two counts catch what one misses.
- **Benefit:** Errors get caught in both directions — it catches your slips, you catch its guesses — instead of either blind faith or so much second-guessing the tool isn't worth using.
- **Apply:** The AI owns mechanical work; you do final review and supply what it can't access.
- **Guardrail:** This is peer review, not command-and-obey or blind faith.
- **Related:** → Cross-Model Create-and-Review (the same idea applied *between* two AIs)

### Active Interrogation & Steering
*Push back the moment something feels off.*
*(cross-reference: `[PRAC-02]` · **Intermediate**)*

A model states a growth rate off by an order of magnitude in the same even, confident tone as everything else in the answer — nothing about the delivery signals the error, only the number itself does, if you're checking. The first output is a draft, not a verdict — but it's easy to forget that once the tone reads confidently. The moment a number looks off or the answer drifts toward pleasant filler, that's the signal to intervene, not to move on.

- **Analogy:** The mechanic quotes a figure that sounds wrong. Ask in the garage, not after you've paid.
- **Benefit:** Catches a problem while it's cheap to fix — one follow-up question — instead of discovering it after you've already acted on the answer.
- **Apply:** Question the calculation, demand the source, redirect to the lane — as soon as something feels off, mid-conversation. *"Stop there. Show me how you got that number, and what source it came from."*
- **Guardrail:** The steering is yours to do; the model won't reliably self-correct without it.
- **Related:** *(lineage)* ← The Adversarial Framing Shift, The Blind-Spot Inquiry

### Canonical-File Discipline
*Keep exactly one file that's the real one.*
*(cross-reference: `[PRAC-03]` · **Intermediate**)*

This book's own production hit "which copy is real?" more than once — two versions of the same file, both plausible, both confidently believed to be current, disagreeing on a detail nobody caught until later. The fix is boring and absolute: exactly one current version, ever.

- **Analogy:** One signed will, in one drawer. Photocopies round the house are how families end up in court.
- **Benefit:** Eliminates an entire category of confusion — arguing about which copy is right — because there's only ever one possible answer to check against.
- **Apply:** Version-stamped filenames; retire superseded copies immediately; keep the live version singular. If the model's memory and the file disagree, **the file wins.**
- **Guardrail:** This is what stops "which one is real?" drift across long projects.
- **Related:** → The Swap Disk Protocol

### Structured Elicitation Before Action
*Make it ask questions before it starts the real work.*
*(cross-reference: `[PRAC-04]` · **Intermediate**)*

The Interview Primitive works on a casual first question. This is its fuller form for a real decision: hand the model the actual constraints and source material, then still make it interview you before it commits any of that to a draft.

- **Analogy:** A builder who starts laying bricks before asking where the door goes.
- **Benefit:** Catches a misalignment before the model spends real effort generating something built on a wrong assumption — cheaper to correct a question than to redo a draft.
- **Apply:** *"Don't write the report yet. Review these constraints and give me the top three clarifying questions you need for full alignment."*
- **Guardrail:** The discipline is answering the questions crisply, not skipping them.
- **Related:** *(lineage)* ← The Interview Primitive

### Explicit Source-Grounding
*Feed it real documents, not memory.*
*(cross-reference: `[PRAC-05]` · **Intermediate**)*

Asked for last quarter's revenue, a model returns a specific, confident figure — sourced from nowhere, indistinguishable in tone from a number it actually looked up. A model asked to recall a figure will hand you back something plausible whether or not it's real. Reconcile to actuals, never to a book estimate — and when a number genuinely can't be grounded, say so, rather than let it pass for a fact.

- **Analogy:** Quoting a price from memory versus reading it off the invoice. Both sound equally certain out loud.
- **Benefit:** Keeps assumptions honestly labeled instead of laundered into facts, so nobody downstream mistakes a guess for something verified.
- **Apply:** Feed real documents. When a number can't be grounded, label it an estimate. *"Answer only from the attached documents. If a figure isn't in them, say 'not grounded' rather than estimating."*
- **Guardrail (approximate-data rail):** Where data genuinely can't be grounded to exact actuals — inferred from a screenshot, read off a plotted curve — state it as an estimate *with a confidence band.* The rule isn't "only use exact data"; it's "never let slick formatting invite more trust than the data justifies."
- **Related:** *(lineage)* ← Direct Grounding · → Reconcile-to-Primary-Source (the maintenance-time, whole-system form of this practice)
- **Lineage:** retrieval-augmented generation and evidence provenance. Lewis et al. (arXiv 2005.11401, 2020) named the move: pair the model with a non-parametric memory it can cite, rather than trusting what it recalls.

### Pin Down Its Role So It Stops Drifting
*Pin down its role so it stops drifting.*
*(cross-reference: `[PRAC-07]` · **Intermediate**)*

You open a new thread for the same recurring task — say, reviewing your monthly budget — and the model that was a cautious, skeptical analyst last week greets you today as an eager cheerleader, praising a spending pattern it would have flagged before. Nothing in your prompt changed; the tone drifted on its own, and nothing tells you why. Pin the role explicitly, including what it is *not*, and hold it constant.

- **Analogy:** You hire a bookkeeper, not "a helpful person."
- **Benefit:** Predictable behavior across sessions — you stop re-explaining the boundaries every time you open a new thread.
- **Apply:** Hard-code a role prompt that defines the boundaries (e.g. "informative calculator and trend-spotter, not a decision-maker").
- **Guardrail:** The discipline is keeping it stable and precise, not rewriting it each session.

### The Negative Must Be Earned
*"Nothing found" requires exhausted search — a first-page scan is not a result.*
*(cross-reference: `[PRAC-10]` · **Intermediate**)*

You search for recent feedback, get nothing back, and conclude none has arrived — but the search returned the first page only and the feedback was on page two. Or you poll an inbox and find it quiet. The silence was real; the conclusion was manufactured from incomplete evidence.

The failure has a specific structure: a continuation token in a search result tells you nothing about whether more results exist behind it. A token with more behind it looks identical to a token with nothing behind it — only exhausted pagination tells you which one you have. "I received a token" means nothing; "I polled until there was no more token" means the search ran to completion.

- **Analogy:** A conductor counts passengers after checking only the first three carriages and reports the train is full.
- **Benefit:** Distinguishes a genuinely quiet channel from an unsearched one — two states that are otherwise identical in output.
- **Apply:** When any search or scan result matters, exhaust all pagination before asserting the result is complete. State the scope explicitly when reporting a negative: "I searched [X] through page [N] and found nothing" is different from "I searched [X] and found nothing." *"Before concluding nothing is there: paginate the full result set. Report what scope you searched and how many pages you consumed."*
- **Guardrail:** Pagination does not guarantee freshness. A complete result set from a minute ago may have new entries now. "Exhausted" means the channel was fully read at that moment, not that it is permanently quiet.
- **Related:** → Canonical-File Discipline ([PRAC-03]), → Resolve Standing Instructions by Rule, Not by Name ([ARC-09])

### Reader vs. Machine: Choosing the Output Format
*Match the format to whoever reads it next.*
*(cross-reference: `[PRAC-11]` · **Intermediate**)*

Handed a clean, well-written paragraph in a thread handoff, the next AI has to re-parse prose to extract the one number it actually needed — and gets it slightly wrong. A clean paragraph and a clean JSON blob can carry the same information, but only one of them survives being handed to a script, a second model, or a spreadsheet without being re-parsed first. Match the format to who — or what — reads it next.

- **Analogy:** A recipe told to a friend versus written on a card for the kitchen. Same information; only one survives being handed on.
- **Benefit:** Portable, diffable, lossless output that survives being passed along, instead of a human-readable paragraph the next tool has to re-interpret.
- **Apply:** For hand-offs between AI threads, or output feeding a tool, request the machine-readable format explicitly — Markdown, CSV, JSON. *"Output this as [Markdown / CSV / JSON] — it's going to another thread, not to me."*
- **Guardrail:** Don't confuse "looks structured" with "is verified" — a clean JSON blob can still be wrong; format is transport, not truth.
- **Related:** → The Swap Disk Protocol

---

## Architecture

### Structured Handoff Briefs
*Write a short brief so the next thread doesn't start from zero.*
*(cross-reference: `[ARC-06]` · **Intermediate** — a reminder that skill tier and category are independent axes)*

A fresh thread — or a human reviewer — opens a raw transcript dump and spends its first several exchanges re-deriving what actually matters from the noise. A purpose-built brief, scoped to exactly what *they* need, gets them working immediately instead.

- **Analogy:** The nurse handing over at shift change doesn't replay the whole day — just what the next shift must act on.
- **Benefit:** A fresh thread or human reviewer is productive from message one, instead of spending the first several exchanges reconstructing context that already existed.
- **Apply:** Ask the maintaining thread to produce a brief for the specific recipient — a kickoff brief for a fresh thread, or a scoped package for a human reviewer — containing what that recipient needs to act on, not everything that happened. *"Write a handoff brief for a fresh thread continuing this work: what's decided, what's open, what to read first. Not a transcript."*
- **Guardrail:** A brief is a summary, and summaries drop things. Treat it as orientation and re-read the canonical artifact for ground truth — the brief orients, the artifact is the source of truth.
- **Related:** → The Swap Disk Protocol (re-hydration), The Single-Writer Reconciliation Pattern (its write-path complement)
- **Lineage:** structured clinical handoff — I-PASS (Illness severity, Patient summary, Action list, Situation awareness, Synthesis by receiver), which carries moderate-certainty evidence of reduced medical error. Note its final step, which this pattern does not have: the receiver states their understanding back before the handoff counts as complete.
