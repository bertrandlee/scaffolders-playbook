# The Scaffolder's Playbook

## Beyond Prompt Engineering to Workflow Architecture

**Bertrand Lee**

*First Edition*

---

*Copyright © 2026 Bertrand Lee, Singapore*

*Published by Bertrand Lee, Singapore*

*First published 2026*

*This is a printed snapshot of a living work, taken 31 July 2026. The current version — with corrections, added patterns and updated platform notes — is at playbook.brightraven.ai*

* * *

*This work is licensed under the Creative Commons Attribution–NonCommercial 4.0 International License (CC BY-NC 4.0). You are free to share and adapt this material for non-commercial purposes, provided you give appropriate credit, link to the license, and indicate if changes were made. Commercial use is not permitted without the author's written consent.*

*Full license: creativecommons.org/licenses/by-nc/4.0*

*This Creative Commons grant is irrevocable and applies to all readers. Separately, the author retains the right to license the work for commercial use; commercial use by others requires the author's written consent.*

*Internal use within organisations is expressly permitted: you may copy, circulate and use this book for training, onboarding and reference inside your organisation — commercial or otherwise — at no charge and without seeking permission. What the NonCommercial term withholds is selling this book, or selling a work derived from it.*

*The Scaffolder's Playbook is intentionally forkable for non-commercial use. If you improve it, add patterns, or adapt it for a specific domain, the author asks — but does not require — that you share your version under the same terms.*

* * *

*Disclaimer*

*This book is an independent publication. It is not affiliated with, endorsed by, sponsored by, or produced in association with Google LLC, Anthropic PBC, OpenAI LP, Microsoft Corporation, or any other technology company or platform provider. Product, platform, and company names are used descriptively and nominatively, to refer to the actual products discussed, in accordance with honest commercial practices. Their use does not imply affiliation, sponsorship, or endorsement.*

*All observations about AI platform behaviour, capabilities, and limitations in this book are based solely on the author's personal experience using publicly available consumer products and services, in the same manner available to any member of the public. Nothing in this book is based on, derived from, or intended to reveal any proprietary, confidential, or non-public information of any company. The author has not been granted any special access to internal systems, source code, training data, or confidential documentation of any AI company.*

*The observations, assessments, and criticisms in this book are the author's own honest opinions, formed in good faith from personal experience on the dates indicated. They are offered for discussion and education and are not assertions of fact about the internal practices of any company.*

*Platform capabilities, model behaviours, pricing, and features described in this book reflect the author's observations as of the dates indicated and may have changed since publication. This book makes no representation that any described behaviour is a complete, accurate, or current characterisation of any platform. Readers should verify current capabilities directly with the relevant platform provider.*

*Nothing in this book constitutes professional medical, legal, financial, investment, or other regulated advice. In matters requiring professional judgment — including but not limited to medical diagnosis, legal proceedings, financial planning, or regulated compliance decisions — readers must consult a qualified professional. AI tools do not replace professional expertise.*

*This book is provided "as is", without warranties of any kind, express or implied.*

*To the maximum extent permitted by applicable law, the author and publisher disclaim all liability for any loss, damage, or claim arising directly or indirectly from reliance on this book or on AI outputs generated using techniques described herein.*

---

## TABLE OF CONTENTS

- The Scaffolder’s Playbook — **1**
    - Beyond Prompt Engineering to Workflow Architecture — **1**
- ABOUT THE AUTHOR — **7**
- PREFACE: Why I Wrote This Book — **9**
- ACKNOWLEDGEMENTS — **17**
    - INTRODUCTION — **18**
- BEGINNER — **24**
- INTERMEDIATE — **36**
    - Foundation — **36**
    - Practices — **51**
    - Architecture — **61**
- ADVANCED — **63**
    - Practices — **63**
    - Architecture — **67**
    - Safety — **81**
- ELITE — GATED — **83**
- PATTERN FINDER — **93**
    - You are already doing the hard part — **93**
    - How to write one up — **94**
    - Four checks before you call it a pattern — **95**
    - Where this goes — **96**
- APPENDIX: Patterns at a Glance — **99**
    - ONR — On-Ramps (Beginner) — **99**
    - PRAC — Practices (Intermediate–Advanced) — **100**
    - ARC — Architecture (Intermediate–Advanced) — **101**
    - SCF — Foundation & Lifecycle (mostly Intermediate) — **102**
    - GOV — Governance (Elite, Gated) — **103**
    - SAFE — Safety (cross-tier, non-negotiable) — **104**
- APPENDIX: Platform Compatibility — **105**
- APPENDIX: Standing Rules of Engagement — **109**
- APPENDIX: Further Reading — **111**

---

# ABOUT THE AUTHOR

Bertrand Lee holds a B.S. in Electrical and Computer Engineering (College and University Honors) from Carnegie Mellon University, USA.

He started at Creative Technology, writing its first open-source Linux audio driver for the Sound Blaster Live! family and working with kernel developers to get it upstreamed. At Microsoft he was principal author of the USB Video Class specification — including the Extension Unit mechanism that let vendors add their own controls without breaking the generic driver — co-founded the USB Video Device Working Group with partners including Logitech, stayed through specification 1.0 in September 2003, and built Windows' UVC driver. Twenty-three years later it is still a reason a webcam works when you plug it in: Windows, macOS and Linux provide built-in class support for compliant UVC devices, and Android supports external UVC cameras on conforming devices. It turns up well beyond webcams — conferencing systems, dashcams, drones, medical endoscopes, the tracking cameras inside VR headsets.

His path into natural-language processing began at VoiceBox, building in-car voice assistants years before phones made them familiar — statistical NLP and grammar-driven parsing on embedded automotive hardware, before deep learning changed the field. He later led video-platform engineering at Panopto, in Seattle and Hong Kong.

In 2018, two decades into his career, he went back to school for the methods that had displaced the ones he knew: four months full-time at a machine learning bootcamp. As a Smart Nation Fellow at GovTech he then led the team that built VICA, the Singapore government's conversational-AI platform, which replaced the earlier Ask Jamie chatbots. He chose its NLP engine by benchmarking eight commercial platforms against a common test set rather than by reputation. Engine-agnosticism was a requirement set for the platform; he built the plugin architecture and migration tooling that made it achievable, letting the engine be swapped without a rebuild. VICA launched in December 2020.

He was not an outsider who learned AI, but a domain expert who went back to being a beginner in the technique. That is why these patterns were discovered rather than theorized — and why none of it is a prerequisite. The argument is not that the author is exceptional, but that the method can be handed to anyone.

He lives in Singapore, runs BrightRaven.ai, an AI consulting firm, and gives pro bono talks on AI in Singapore schools.

*More: linkedin.com/in/bertrandlee · ["A Conversation with Bertrand Lee," GovTech Tech News](https://www.tech.gov.sg/technews/a-conversation-with-bertrand-lee/)*

---

**A note on how this book was written.** The experiences, judgment, and patterns in this book are the author's own — discovered, tested, and vetted across real projects, not theorized. The prose itself was drafted collaboratively with AI, working from his direction and firsthand accounts, then reviewed and revised by him before publication. If that distinction matters to you as a reader — and this book's own argument about honest disclosure suggests it might — you now have it stated plainly rather than left for you to guess.

---

# PREFACE: Why I Wrote This Book

I wrote this book because a frustration with my own investing and long-term financial planning — tracking requirements that span years, reconciling records scattered across accounts — accidentally taught me something too useful to keep to myself. The fix was simple: stop treating the AI like an oracle, start treating it like a durable external store. I took a spreadsheet that had grown into a mess of notes and made the model organize its own memory into a structured, human-auditable ledger. It worked. That day, I stopped one-shotting.

This book does two jobs at once: it's a manual for techniques that already work, and a method for finding the ones that don't exist yet. Those aren't in tension — the techniques here exist to train a discovery reflex, not just to be copied. Learn the foundations, improve on them, and put your own back into the commons.

**This is workflow engineering, not prompt engineering — and the difference matters.** Prompt engineering optimizes one question for one better answer; it operates at the level of the *turn*. Workflow engineering operates *above* the turn: the memory that outlives a conversation, the file that survives a thread, the check that fires on a future edit, the reconciliation that runs weeks later. It's the same move software engineers call a design pattern — a recurring solution to a recurring problem that you don't invent so much as *notice*. Work this way long enough and you'll realize you've been using a structure that already has a name, or you'll have quietly named one yourself. This book catalogs the ones I noticed. Its bigger job is teaching you to notice your own.

If you want the definitive treatment of the layer below this one, it already exists: DAIR.AI's Prompt Engineering Guide (promptingguide.ai) catalogs prompting technique thoroughly and keeps it current. This book starts where that one stops — not at the prompt, but at everything that has to survive after the answer arrives.

**The method is not "assume the machine can do anything."** That assumption feels bold; it isn't — it's how you get confidently wrong output you never catch, because you stopped checking. What I actually do: assume nothing about the ceiling, push hard to find it, verify what comes back. Ambition and verification aren't opposites here — they're the same discipline. Push boldly to discover, trust nothing unverified. Every technique in this book came out of that push-then-test loop, not out of a theory about what AI should be able to do.

I didn't arrive at these patterns once, in one place. The same architecture showed up independently across three domains I run this way — personal investing, a serious medical episode, stewardship of a personal collection — each one rediscovering the same four moves: a living document as the source of truth, a second mind checking the first, mistakes converted into standing rules, a bright line where the human decides. **Be precise about what that evidence actually supports:** three domains, one practitioner, is cross-domain reappearance within a single mind — not independent convergence, and not proof the method transfers to you. Treat it as a hypothesis worth testing, not a guarantee.

This project is a contribution to an open-source commons, and the larger hope is to help start one (see "Where This Goes"). A contribution earns credibility by reconciling to actuals, not by sounding right. I mark what's durable versus perishable, and I check claims against independent review, because two systems agreeing is not the same thing as a claim being true. I'm asking you to hold your own contributions to the same bar.

**Scope: three platforms, and only three.** The patterns here are written for, and where possible verified on, **ChatGPT, Google Gemini, and Claude** — chosen because between them they cover the full capability set the patterns depend on: persistent project memory, file upload and generation, multimodal input, code execution, connectors to external stores. Everything else — DeepSeek, Perplexity, Meta AI — is out of scope. Not a judgment of quality; an application of this book's own rule: if a pattern hasn't been tested and verified on a platform, the book doesn't claim it works there. An untested platform gets treated as a hypothesis, not a promise — and if you verify one, that's a real contribution back to the commons.

**One correction to make plainly: platform capabilities are the least durable thing in this book, and free tiers are not paid tiers.** What a platform can't do this quarter, it may do next quarter — and the reverse. Every capability-dependent pattern carries a dated, tier-specific note (see the Platform Compatibility appendix), and you should re-check it against your platform's current state before you trust it. There's a pattern in this book for exactly that check — [SCF-07], Connector Discovery: ask your platform what it can actually do, don't assume from memory.

A final constraint, and the one that earns all the rest. This book pushes you to push AI systems hard — but that's only earned through the rigor of the audit, not a substitute for it. In medicine, law, and money, the line is absolute and non-negotiable: the AI prepares your questions; it does not make your decision. You and your credentialed professional do that. Skip the audit and the boldness is just recklessness wearing a better outfit. Keep it, and it's a disciplined workflow.

One more thing I didn't expect: how it would feel. Building these systems put me back into a state I hadn't felt in twenty years — the flow of my early days as a software engineer, looking up to find the whole day gone. I wasn't optimizing prompts; I was architecting a system, and architecture absorbs you in a way a single answer never does. I'm not promising you'll feel it too — flow is personal, and these tools frustrate as often as they deliver — but it's the honest reason I kept going, and it's worth naming: the payoff lives in the building, not in the asking.

There is a second thing I didn't expect, and it explains where most of these patterns actually came from. Very few were designed. They were noticed — a figure I couldn't trace back to its source, a file that reported success and hadn't saved, a rule followed on Monday and quietly dropped by Thursday. Each time, I worked the fix out *with* the model that had just made the mistake, and then handed the result to the rest of what I've come to think of as my team: the separate threads I keep for separate domains, each one inheriting a correction it never had to earn for itself.

What made that work was a division of labour I've not had with a machine before. I brought the creativity, the domain judgement, and the reality checks — the insistence that a claim be true rather than merely plausible. They brought technical depth and a breadth of reference no person can hold. Neither half would have produced this catalogue alone, and I'm fairly sure neither half could have. The closest word I have for it is a mind meld, which I'm aware sounds like exactly the kind of overclaim this book warns against. I'll defend it anyway: the patterns in here are the residue of that collaboration, not a report about it.

### How to Self-Classify (borrowed from skill-rating systems like pickleball's DUPR)

Rating systems like DUPR don't ask how long you've played or how confident you feel — they ask what you can actually do, against opponents who can do the same. Borrow that logic here. Classify yourself by what you've *done*, not by time spent or how expert you feel.

Proficiency frameworks for AI exist — Anthropic's AI Fluency work, and several published level ladders. This is not one of them. The tiers here are a reading order for a catalog, not an assessment: they tell you which patterns will make sense next, not how good you are.

1. **Beginner.** You've used a chat AI for straightforward questions and drafts — or maybe this is your first real conversation with one at all; either way, you're in exactly the right place. *Self-check:* have you ever made the model interview you before it answers, or asked it to argue against your own draft instead of approving it? If you haven't tried either, start here — the Beginner section is built for exactly this gap.

2. **Intermediate.** You use AI daily for real work — documents, day-to-day tasks — but nothing you've built with it outlives the conversation that created it. *Self-check:* if this chat ended right now, would anything of value survive in a file you control? If no, the Intermediate section closes that gap.

3. **Advanced.** You've built at least one durable, file-based system: a memory registry, a spreadsheet with self-checking guards, a handoff brief a stranger could pick up cold. *Self-check:* could a brand-new AI thread, with zero chat history, continue your project today from a file alone? If yes, you're here — the Advanced section is your home base.

4. **Elite.** You govern a system rather than build one: verification is structurally independent of the work being verified — not just promised, but enforced. *Self-check:* do you have a standing rule that no model can grade its own output, and has that rule ever actually caught a real error? If yes, the Elite section (gated, and now you know why) is where you already live. **Six of its seven patterns work in a single chat window**; only [GOV-07] needs more than one thread, and says so.

**The four tiers above are a reading order. They end there.**

**One honest note matching the registry's own tags:** every numbered pattern is assigned to Beginner, Intermediate, Advanced or Elite. The first three are what a single practitioner does or builds alone; the Elite patterns are labeled Elite, not because they're harder in the same sense, but because they describe *governing a system*, not building one — the pyramid's gated top rung.

### And then there's a different axis entirely

**Pattern Finder is not a fifth tier.** It's a *role* — something you do with competence, rather than a measure of how much you have. You've noticed a recurring solution to a recurring problem in your own practice, one that isn't in this book, and written it down so someone else can use it. The section at the end is a short guide to doing exactly that.

**You don't graduate into it, and you don't need to be Elite to get there.** A beginner who notices something real and writes it down clearly has done the thing. Someone who has read every pattern here and never found one of their own hasn't — and that's a perfectly good place to stay.

**It's also not the only role.** Two others show up in practice, and this edition doesn't cover them: **Team Builder**, if your work splits across enough domains that you end up running more than one thread; and **Thread Grower**, if you deepen a single thread over months until it holds context a fresh one couldn't. Most people will only ever wear one of the three hats, and one is enough. The collective name for wearing any of them is **Scaffolder** — which is where this book gets its title.

Here's how to build that infrastructure.

---

# ACKNOWLEDGEMENTS

To Hewlen, the rock of my life. Thank you for your patience, understanding and support as I endeavored on this project.

To Philip and Huey, my long-time friends and reviewers. For your insightful feedback and encouragement, making the book far better than it could have ever been without your input.

To Claude (Anthropic), my AI co-author. The writing, editing, research, and building in this book happened across hundreds of hours of collaborative sessions. The work is mine; the partnership made it possible.

To Gemini (Google), ChatGPT (OpenAI), and DeepSeek — the AI co-reviewers whose independent review rounds challenged, tested, and sharpened every pattern in this catalogue.

---

## INTRODUCTION

There is a colleague available to you now who has no fear of your reaction, no stake in your good opinion, and no memory of the argument you had last week. That absence — call it **The Zero-Stakes Critic** — is not a limitation of the tool; it is the whole advantage. A human reviewer calibrates criticism against the relationship it might damage. An AI has no relationship to protect, which means it can be exactly as blunt as the problem requires, every time, without cost. This book leans on that advantage constantly — see [ONR-02] for where it first shows up as a technique, and watch for it again wherever a pattern asks the model to argue against you rather than agree with you.

### How This Book Is Organized

**The book is arranged by skill tier, because that is the order to read it in.** Four tier sections — Beginner, Intermediate, Advanced, Elite — each resting on the one below. A fifth section, **Pattern Finder**, contains no patterns: it teaches contribution, and it is a role rather than a rung.

**Read one section, then stop.** Come back when it feels automatic. You do not need to read this book front to back, and you shouldn't: a beginner who pushes to the end spends most of their time on infrastructure for problems they haven't hit yet, and the patterns read as ceremony rather than as answers.

**Within a tier, patterns are grouped by category** — the ID prefix: `ONR` On-Ramps · `SCF` Foundation · `PRAC` Practices · `ARC` Architecture · `GOV` Governance · `SAFE` Safety. A category can appear at more than one tier, because some safety rules are the first thing a beginner needs while others are advanced infrastructure. If you want the category view instead of the tier view, the **Patterns at a Glance** appendix lists all fifty that way.

**IDs are permanent and never renumber.** Display order is cosmetic, and a pattern's number tells you nothing about where it sits or how hard it is. Gaps in the numbering are expected and carry no meaning — a retired or never-written ID is left empty rather than backfilled.

**Pattern Finder, the fifth section, has no patterns at all.** It isn't a harder degree of the same skill — it's a change in what you produce, from applying this catalog to adding to it, and it sits on a different axis from the four tiers. See "How to Self-Classify" in the Preface.

**Try it right now, not just read about it:** you can upload this file directly into a ChatGPT, Gemini, or Claude conversation and ask it to walk you through any pattern, or even test one on a real task with you on the spot. The book is written to be handed to the tool it describes — see "Where This Goes" for the fuller version of this idea.

**Most of this has a lineage.** Very little here is unprecedented in computing — the moves have names in distributed systems, software engineering and security, some of them decades old. Where a pattern has a known ancestor, its entry says so in a **Lineage** line. That isn't a hedge. Knowing that your memory registry is paging, or that your one-writer rule is leader-based replication, tells you where to look when it breaks and what someone else already learned the hard way. What's uncommon isn't the mechanism — it's who's doing it by hand, alone, in a chat window.

**The form is borrowed, and the debt is worth naming.** A pattern catalog — a recurring problem, a recurring solution, a name you can say out loud to another practitioner — comes from architecture by way of software engineering, and most directly from the *Design Patterns* book of 1994. What that book did for object-oriented design, this one attempts for working with an AI in a chat window: not new inventions, but recurring moves given names, so they can be recognised, taught and argued about. The names are the point. A technique you cannot name is one you cannot deliberately reach for.

**And this book covers one part of the problem, not all of it.** Its subject is workflow and architecture — how work is structured, where state lives, what checks exist and who runs them. **It is not a book about prompting.** Wording, phrasing, few-shot examples, chain-of-thought and the rest are a real and separate craft, well covered elsewhere, and a reader who wants to be good at this needs both. Where a pattern here depends on how something is asked, it says so and points onward. **Treat this as the architecture half of a two-part education, and read something on prompt engineering alongside it.**

**There may be more on the way.** A more comprehensive guide — something closer to a hitchhiker's guide to the whole galaxy of working with AI, beginner to fluent, in one place — is the kind of problem this author can't leave alone. Nothing here promises it, or when. But if this book closes one gap for you, know that the others are visible from here too.

**And pattern catalogs for AI already exist** — prompt-pattern collections in the academic literature, design-pattern books for people building applications and agents, UX pattern libraries for people designing chat interfaces. All of them are written for builders. This book is for the person on the other side of that interface: no code, no framework, no API key, just a chat window and work that matters. That is a different problem with a different failure set, and it is the gap this book is trying to fill.

**A second marker, ★, means don't skip this one.** It flags the few patterns that quietly unlock several others. The Swap Disk Protocol ([ARC-01]) is the clearest example: once your project has durable, file-based memory, a dozen Advanced patterns become easy instead of theoretical.


---

### The One Principle Underneath Everything

**Reliability is a property of the system, not the model alone.** A capable-but-fallible model becomes a reliable collaborator *for bounded tasks* when it is anchored inside durable, human-auditable artifacts — memory in files, errors turned into guards, verification built into the workflow — its outputs are independently checkable, and a human decides. The model's capability sets the ceiling on what any workflow can achieve; the system determines how close you get to that ceiling, and how safely you fail when you don't. Process cannot turn an incapable model into a reliable one; it makes a capable one's work *compound* across sessions and its errors catchable.

Running underneath every pattern is one governing rule, which is why it is stated here as a principle rather than filed as a technique:

> **The verifier must be independent of the verified** — where *independent* means the check does not share the failure that produced the error. A model cannot reliably check its own work: it shares its own blind spots, and asked whether it succeeded, it will tend to say yes. So every check that matters is run by something *outside* the thing being checked: a human, a different model, a frozen reference, a mechanical diff against stored actuals. Independence of the *evidence* matters more than a different brand of model — a mechanical diff against the stored bytes is independent even when the same agent wrote them, though it establishes integrity against that baseline, not that the baseline is *correct*; where correctness is claimed, reconcile against an independently established, known-good reference. A second model is not independent merely by being a different product; it may share training data and blind spots. Self-review is *insufficient as final assurance*, not worthless. This is the reason the techniques work, not one of the techniques.

**Why a second channel, and not a second look.** The failure this guards against isn't that a model lies. It's that a model's account of what it just did is generated the same way as everything else it generates — from the conversation, not from an inspection of the world. Ask whether a file saved and you get a fluent, plausible answer that was never checked against a file system. The report and the reality are produced by different processes, and only one of them involves looking.

So a write is not done until a *different* read confirms it: a different tool, a direct metadata lookup, the folder listing itself. And "a different model" is not automatically independent — two models can share a blind spot. Independence is a property of the evidence channel, not the brand.

---

---
