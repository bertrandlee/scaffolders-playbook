# APPENDIX: Patterns at a Glance

*A distilled, one-line-per-pattern index of all fifty patterns in this book, grouped by family. For the full write-up of any pattern — the motivating scenario, Apply, Benefit, Guardrail, Related — read the full entry in its tier section; this is the index, not the text.*

> **Selection is a judgment call.** This is a recognition aid, not an auto-apply library — match the pattern to the actual problem in front of you; don't reach for one just because it's here. Read it the way you'd consult a table of contents, not the way a script executes a lookup. When unsure, read the full pattern in its section before applying it.

## ONR — On-Ramps (Beginner)
- **[ONR-01] The Interview Primitive** — reach for this when you're about to ask for something important and haven't given the model enough of your actual situation to work with.
- **[ONR-02] The Adversarial Framing Shift** — reach for this when you want your draft critiqued, not approved, and suspect a direct "does this look okay?" will just get flattery back.
- **[ONR-03] The Blind-Spot Inquiry** — reach for this before a high-stakes meeting or process, to surface the question you didn't know to ask.
- **[ONR-04] Direct Grounding: Don't Explain — Show** — reach for this whenever you're about to describe a document from memory instead of just showing it the original.
- **[ONR-05] Multi-Modal Equity: Talk to the Tool** — reach for this when typing itself, not the technology, is the real barrier for someone.

## PRAC — Practices (Intermediate–Advanced)
- **[PRAC-01] Both of You Can Be Wrong** — reach for this to set the working relationship up right from day one: both you and the model can be wrong, so both of you check.
- **[PRAC-02] Active Interrogation & Steering** — reach for this the moment an answer feels off mid-conversation, instead of waiting to catch it later.
- **[PRAC-03] Canonical-File Discipline** — reach for this whenever more than one copy of a working file could plausibly exist.
- **[PRAC-04] Structured Elicitation Before Action** — reach for this before a real, consequential piece of work begins, not just a casual first question.
- **[PRAC-05] Explicit Source-Grounding** — reach for this whenever a number or fact matters and shouldn't be recalled from memory alone.
- **[PRAC-06] The Decoupled Reference Audit** — reach for this after any structural change, to check the result against a copy nobody touched.
- **[PRAC-07] Pin Down Its Role So It Stops Drifting** — reach for this when you need a role to stay stable across sessions instead of quietly drifting.
- **[PRAC-08] The Disconfirmation Gate** — reach for this before committing to a real decision, to make the model argue it's wrong first.
- **[PRAC-09] The Unrun Check** — reach for this when citing a figure whose verification route was closed — to distinguish a computed result from an inherited number that was never checked.
- **[PRAC-10] The Negative Must Be Earned** — reach for this when a model reports that nothing is there, before treating absence as a clean result.
- **[PRAC-11] Reader vs. Machine: Choosing the Output Format** — reach for this whenever output is headed to another tool or thread, not just a human reader.

## ARC — Architecture (Intermediate–Advanced)
- **[ARC-01] The Swap Disk Protocol: Give the AI a Permanent Notebook** ★ — reach for this the moment a project needs to survive past one conversation.
- **[ARC-02] Self-Installing Guards** — reach for this to stop the same class of mistake from recurring, instead of just fixing today's instance.
- **[ARC-03] Have a Different AI Attack the First One's Work** — reach for this when a draft needs a genuinely different set of blind spots looking at it.
- **[ARC-04] The Single-Writer Reconciliation Pattern** — reach for this when more than one thread (or person) might edit the same working file.
- **[ARC-05] Archived Versions + Embedded Changelog** — reach for this so a bad edit is always recoverable, not just the current state.
- **[ARC-06] Structured Handoff Briefs** — reach for this when a fresh thread or a human reviewer needs to get productive fast, without re-deriving context from a raw transcript.
- **[ARC-07] Recheck the Record Against the Original** — reach for this periodically, to catch a wrong-but-plausible value that internal checks alone would never see.
- **[ARC-08] A Copy You Edit Isn't a Backup** — reach for this when deciding whether a duplicate file is a backup or a liability.
- **[ARC-09] Resolve Standing Instructions by Rule, Not by Name** — reach for this instead of hard-coding a specific filename into a standing instruction.

## SCF — Foundation & Lifecycle (mostly Intermediate)
- **[SCF-01] One Thread Per Topic, Like a Standing Specialist** — reach for this to keep one thread per domain, rather than letting contexts bleed together.
- **[SCF-02] Match the Model to the Job, Not Habit** — reach for this instead of defaulting to the same model out of habit for every task.
- **[SCF-03] Don't Trust What It Says About Itself** — reach for this instead of trusting a model's own claim about how full its context window is.
- **[SCF-04] Communication Style Adjustment** — reach for this to get the register you actually need, instead of the model's default helpful-generalist tone.
- **[SCF-05] Asymmetric Resource Substitution** — reach for this before spending a scarce image-upload slot on content that could just be pasted as text.
- **[SCF-06] Flat-File Text Injection** — reach for this instead of pasting a large document straight into the chat box.
- **[SCF-07] Workflow-Anchored Connector Discovery** — reach for this before manually doing something a native integration might already do for you.
- **[SCF-08] Park a Task So You Don't Lose Your Train of Thought** — reach for this to park a mid-conversation task without losing your current train of thought.
- **[SCF-09] Debugging a Spreadsheet Like Production Code** — reach for this when a spreadsheet error needs root-cause treatment, not a one-cell patch.
- **[SCF-10] Encryption Is Not the Answer** — reach for this when the instinct to "encrypt everything" is aimed at the wrong actual threat.
- **[SCF-11] Email Is the Master Key** — reach for this before connecting an AI assistant to email, the one account whose compromise cascades into everything else.
- **[SCF-12] Prune the Ceremony Your AI Can't See** — reach for this when a standing instruction is firing more often than it needs to, and only you can see it.
- **[SCF-13] Treat "I Can't" as a Claim to Test** — reach for this whenever a model claims it can't do something it did easily before.
- **[SCF-14] Test the Whole Channel, Not Just the Step** — reach for this when every step reported success but the end result is wrong — to check whether the pipeline itself delivered.

## GOV — Governance (Elite, Gated)
- **[GOV-01] The Self-Correcting Feedback Loop** — reach for this to turn a caught mistake into a standing rule, not just a one-time fix.
- **[GOV-02] The Structural Unit Test** — reach for this to check structural integrity against a reference nobody involved in the change could have touched.
- **[GOV-03] See What Else Moves When You Move One Thing** — reach for this when changing one variable could ripple into domains you weren't thinking about.
- **[GOV-04] Screen Instructions by Where They Came From** — reach for this whenever an instruction arrives inside content rather than being typed by you directly.
- **[GOV-06] Name the Ceiling, Not the Comfort** — reach for this when describing what a safeguard does — say what it can't guarantee in the same breath.
- **[GOV-07] Only One Channel Publishes — Make Forgery Loud** — reach for this when multiple threads share a space and you need a way to tell a real standing rule from a fake one.
- **[GOV-08] Graceful Session Close** — reach for this to make the state record the final action of a session, not merely something written before the session ends.

## SAFE — Safety (cross-tier, non-negotiable)
- **[SAFE-01] The Data Ingestion Boundary** — reach for this before typing or uploading anything — decide what never goes in, in the first place.
- **[SAFE-02] The Decoupling Charter (The Bright Line)** — reach for this in medicine, law, or money: the AI preps the questions, a credentialed professional makes the call.
- **[SAFE-03] Temporal Drift Verification** — reach for this for anything current — give the model today's date rather than trusting its memory.
- **[SAFE-04] Time-Grounding: The Clock It Doesn't Have** — reach for this whenever a time-sensitive answer arrives without a dated source behind it.

---

# APPENDIX: Platform Compatibility

*The cells below are hypotheses from published capability docs (`[doc]`) or hands-on tests (`[verify: DD/MM/YY, tier]`). Platform capability is the book's most perishable content — re-check with [SCF-07] before relying on any cell. AS OF: 29 Jul 2026 SST.*

**How to read this:** Most patterns are **platform-agnostic** — pure prompting/process disciplines that work on any capable chat model. They carry no compatibility flag. Only the **feature-dependent** patterns below need one. Baseline = **free** tier; **paid** shows what the paid consumer tier unlocks.

**A note on DeepSeek:** included here as a reader reference, not a tested scope platform. This book's verified three-platform set remains ChatGPT, Gemini, and Claude (see Preface). DeepSeek cells are documented claims only; none are hands-on verified.

| Pattern | Needs | ChatGPT (free / Plus) | Gemini (free / AI Plus+) | Claude (free / paid) | DeepSeek (free) |
|---|---|---|---|---|---|
| [ONR-04] Direct Grounding | file/image upload | `[doc]` Free: 3 files/24h · Plus: 80/3h rolling, 20/message | `[doc]` Free: 10 files/session (no code files) · AI Plus+: Drive attach, code files | `[doc]` consistent across tiers (message limits vary, not file count) / Projects: persistent | `[doc]` app: yes — session-based text extraction; not retained between chats |
| [ONR-05] Multi-Modal Equity | voice + image input | `[doc]` Free: limited voice · Plus: full voice + vision | `[doc]` Free: Gemini Live (mobile only) + image · AI Plus+: full | `[doc]` app: voice (iOS/Android) / yes | `[doc]` No voice in official app; image input not supported in consumer chat |
| [ARC-01] Swap Disk | file re-hydration; persistent project | `[doc]` Free: Projects (5 files/project, since Sep 2025) · Plus: Projects (25 files/project) | `[doc]` Free: Gemini Notebook (50 sources/notebook, syncs in-app) + Gems for persona · AI Plus: 100 sources/notebook | `[doc]` manual upload / Projects (paid): persistent workspace | `[doc]` No Projects or notebook equivalent; each session starts fresh |
| [ARC-03] Cross-Model Review | access to 2nd model lineage | `[doc]` use any 2 platforms (even 2 free tiers) | — | — | — |
| [ARC-04] Single-Writer Reconciliation | store write/copy | `[doc]` read-only connector (paid); no write | `[doc]` Gemini Notebook + Drive: read/write with human-review step (AI Plus+, Workspace) | `[verify: 02/07/26, this env]` create/write(text)+copy verified; no move/delete; binary human-placed | `[doc]` no file store connector; no write capability |
| [ARC-05] Archived Versions | file store + archive | `[doc]` manual versioning; no AI copy | `[doc]` manual + AI can create in Gemini Notebook | `[doc]` manual + AI `copy` | `[doc]` manual only; no AI copy; session-based |
| [ARC-07] Reconcile-to-Source | read linked sources | `[doc]` manual re-upload (free) / read connector (paid) | `[doc]` upload / Gemini Notebook maintains source links | `[doc]` manual / read connector | `[doc]` manual re-upload only; session-based |
| [SCF-01] Advisor Model | persistent threads/persona | `[doc]` Free: Projects (basic, 5 files) · Plus: full Projects | `[doc]` Free: Gems (persona, all tiers) + Gemini Notebook (source workspace) · AI Plus: more notebook sources | `[doc]` manual threads / Projects (paid) | `[doc]` no persistent threads; no Projects/Gems equivalent |
| [SCF-02] Model Routing | tier/model choice | `[doc]` Free: GPT-5 (~10 msg/5h then mini) · Plus: GPT-5.5 + model picker | `[doc]` Free: Gemini 3.6 Flash + 30 Pro prompts/day · AI Plus: 128K ctx · AI Pro: 1M ctx | `[doc]` — / model choice (Sonnet, Opus etc.) | `[doc]` DeepSeek V4 + V4-Flash available; no consumer model picker |
| [SCF-05] Resource Substitution | (manages upload quotas) | `[doc]` Free: tight (3 files/24h) · Plus: 80/3h rolling | `[doc]` Free: generous (10/session); no code files free | `[doc]` paid-leaning (message limits vary, file count consistent) | `[doc]` session-based; quota not displayed |
| [SCF-06] Flat-File Injection | file attach | `[doc]` Free: 3/24h · Plus: 80/3h, 20/message | `[doc]` Free: 10/session · AI Plus+: Drive attach | `[doc]` paid (limited free) | `[doc]` app: yes (session-only, text extraction) |
| [SCF-07] Connector Discovery | connectors | `[doc]` paid only — Agent mode: GitHub, Google services | `[doc]` Free: Google Search · AI Plus+: Gmail sidebar · AI Pro+: full Workspace | `[doc]` paid only | `[doc]` no connectors in consumer app |

**The cross-platform finding worth stating in prose (mid-2026):** none of the four platforms grants an AI unrestricted autonomous write/move/delete on your file store as a standard consumer feature — Claude reads/copies and (in this project's configuration) writes raw text at a path; ChatGPT's connector is read-only; Gemini creates/edits and *proposes* moves behind a human-review dashboard; DeepSeek has no file store connector at all. This is *why* [ARC-04]'s split-responsibility model (AI writes content, human controls placement) is the correct pattern everywhere, not a workaround for one platform.

**Gemini nomenclature note (updated 29 Jul 2026):** two distinct tools that are often confused. **Gems** = reusable custom AI personas with full Gemini capabilities (analogous to ChatGPT's custom GPTs); available on all tiers including free. **Gemini Notebook** (renamed from NotebookLM on 16 Jul 2026) = source-grounded research workspace where the AI answers only from uploaded sources; now integrated in the Gemini app sidebar; available free (50 sources/notebook) with higher limits on paid tiers. The two can be combined. Gemini tier names as of mid-2026: Free · AI Plus ($4.99/mo) · AI Pro ($19.99/mo) · AI Ultra ($99.99+/mo); compute-based usage limits since I/O 2026.

**Two caveats that outlast any version number.** Many readers work in Microsoft environments (OneDrive/SharePoint) rather than Google Drive — the Swap Disk Protocol's mechanics are cloud-agnostic, but connector tooling differs by provider and should be re-verified per platform. And the exact click-sequence to grant or re-grant a write scope is interface-specific, and has been observed to change between releases: treat the *need* to re-verify write access per thread as durable, the *steps* as perishable.

**Verification note:** every `[doc]` cell is a documented hypothesis, not a hands-on test. The single `[verify]` cell is from this project's own production environment — Claude, Jul 2026. Two AI models agreeing on a cell is not verification. This appendix is itself an instance of [PRAC-05]: a documented estimate, flagged as such, awaiting reconciliation to actuals.

---

# APPENDIX: Standing Rules of Engagement

*Working rules for producing this book across multiple AI threads — and directly reusable by any reader running their own multi-model workflow. Every rule here was earned by a specific failure during this book's own production.*

1. **No self-attestation.** Never claim your own output is "verified," "audited," "locked," or "consensus." State what you changed; leave confirmation to an independent pass. An audit entry is written *after* the reviewer returns, never pre-filled.
2. **Reference by stable ID, never display number.** IDs are frozen; display order is cosmetic; never renumber a reference.
3. **After any structural change, list the affected pointers as unverified** for the reviewer — don't assert they're fine.
4. **The verifier must be external to the verified.** Any check must sit outside the thing checked; no model grading its own work.
5. **Perishable content is principle-first and timestamped (SST).** Lead with the durable principle; mark specifics (models, prices, limits) as "as of [date], illustrative."
6. **One canonical file; the frozen version wins ties.** When a pattern exists in two places and they differ, flag it — don't silently reconcile. Never compress or drop cleared content when porting; if compressing for display, say so.
7. **Flat engineering register.** No hype adjectives, in the manuscript or the surrounding notes.
8. **Standard submission format:** what changed · affected pointers (unverified) · the draft · `[PENDING]` audit line.
9. **Bright line on high-stakes content** stated in-section: AI prepares questions and surfaces what to check; human and professional decide.
10. **Beginner bar on Beginner-tier content:** followable by a non-technical reader; no jargon.

*(Note: the disciplines in these rules also appear as reader-facing patterns — [PRAC-06] Decoupled Reference Audit, [PRAC-03] Canonical-File Discipline, [SCF-03] Self-Reporting Trap, [SAFE-03] Temporal Drift Verification and [SAFE-04] Time-Grounding. The rules are the operational version; the patterns are the taught version.)*

---

*The project's internal work queue, backlog, status notes, and full production changelog are maintained in the separate private editorial file — not in this public manuscript.*

---

# APPENDIX: Further Reading

*This book covers one layer. These cover the ones around it. Listed because a reader who wants the whole picture should have it — not as prerequisites. You can start here and read outward.*

**The layer below: prompting.**
DAIR.AI, *Prompt Engineering Guide* — promptingguide.ai. Free, open-source, community-maintained, kept current. The definitive practical treatment of the turn: zero-shot and few-shot, chain-of-thought, self-consistency, and the rest. If a pattern in this book assumes you can get a decent answer out of a single question, this is where that skill is taught.

White, J. et al., *A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT* — arXiv:2302.11382 (Vanderbilt, 2023). Sixteen prompt patterns documented in the software-pattern form this book also borrows. Written for software development tasks, so the examples are developer-facing, but the pattern discipline transfers.

**The layer sideways: building things on top of models.**
Lakshmanan, V. and Hapke, H., *Generative AI Design Patterns* (O'Reilly). Thirty-two patterns for people shipping applications and agents — hallucination, non-determinism, guardrails, retrieval. Assumes you write code.

Gullí, A., *Agentic Design Patterns* (Springer). Patterns for building autonomous agents, worked through agent frameworks. Also assumes you write code.

**Why these are not competitors to this book.** Every one of them is written for someone building *with* a model — engineers, application developers, agent authors. This book is written for someone working *alongside* one in a chat window. The prompting resources sit underneath it: they make each turn better. This book is about everything that has to survive after the turn ends. Read them together and you have both floors of the same building.

**A caution, in this book's own spirit.** Links rot and editions change. Titles and authors are durable; the URL above was checked on 29 July 2026 and may not be by the time you read this.
