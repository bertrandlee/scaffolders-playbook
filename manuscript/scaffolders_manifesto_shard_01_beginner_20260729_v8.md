# BEGINNER

*Ten patterns, readable in one sitting. Every one can be used within a single conversation, with no persistent project infrastructure — though a few use ordinary upload, image or voice features.*

**Read this section and stop.** When these feel automatic — when you make the model interview you before it answers without having to remember to — come back for Intermediate. There is no benefit to reading further before then, and some cost: the later sections describe infrastructure that only makes sense once you have hit the problems it solves.

### The Interview Primitive
*Try asking it to interview you first.*
*(cross-reference: `[ONR-01]` · **Beginner**)*

Ask "plan a family trip to Japan" and you get a generic, tourist-trap itinerary built on surface assumptions. Before you let the model answer anything real, make it interview *you* first.

- **Analogy:** A good tailor measures you before cutting the cloth; a bad one hands you something off the rack and calls it fitted.
- **Benefit:** Surfaces the gaps in your own thinking — a budget you forgot to mention, a mobility limit, a dietary need — before you've committed to a plan built on a wrong guess. Costs one extra reply; saves redoing the whole thing.
- **Apply:** End your first prompt with *"Before you answer, ask me the top three clarifying questions you need to tailor this to my situation."*
- **Guardrail:** The model organizes your options; you know your life. You keep authority over the decision.
- **Related:** → Structured Elicitation Before Action

### The Adversarial Framing Shift
*Ask it to tear your draft apart, not approve it.*
*(cross-reference: `[ONR-02]` · **Beginner**)*

Drafting a hard email — pushing back on an unreasonable deadline — the instinct is to paste it and ask "does this sound okay?" Because these tools are trained to be helpful and polite, they'll tell you it does. In a high-stakes moment, an assistant that always agrees is a liability.

- **Analogy:** Ask a friend "does this look okay?" and you get "yes." Ask "what would my harshest critic say?" and you get it while you can still fix it.
- **Benefit:** Trades one uncomfortable moment (reading a critique of your own draft) for catching a tone problem or a misread before it reaches the person who'll actually judge you on it.
- **Apply:** *"Critique this aggressively. Don't tell me why it works — tell me what's wrong, what I've missed, and how it could backfire."*
- **Guardrail:** It spots tone and logic gaps; it doesn't know your workplace politics or your manager's temperament. It's a peer reviewer, not the decider.
- **Related:** → Active Interrogation & Steering

### The Blind-Spot Inquiry
*Ask what you forgot to ask.*
*(cross-reference: `[ONR-03]` · **Beginner**)*

Applying for a permit, prepping for a specialist appointment — the real danger isn't the question you asked badly, it's the one you never thought to ask at all. An AI answers exactly what you type; it won't volunteer the gap in your plan unless you make it hunt for one.

- **Analogy:** A good doctor answers the question you asked, then the one you didn't know to ask.
- **Benefit:** Turns everything the model has seen before — thousands of similar situations — into a checklist built for your blind spots specifically, not just the ones you knew to ask about.
- **Apply:** *"Thinking about everything we've discussed, what important questions or hidden risks should I raise with my specialist that I haven't thought of?"*
- **Guardrail:** The boundary that matters most in daily use: this prepares you for your professional, it does not replace them. Describe your situation in general terms; keep identifying numbers out.
- **Related:** → Active Interrogation & Steering

### Direct Grounding: Don't Explain — Show
*Show it the document instead of describing it.*
*(cross-reference: `[ONR-04]` · **Beginner**)*

"I have a bank statement with a $50 late fee, but I don't know why" hands the model a memory of a document instead of the document — and memory misreads dates, skips fine print, drops the one line that mattered. Stop summarizing what you think you saw. Show it the original.

- **Analogy:** Describing a rash over the phone versus showing the doctor — one is your memory of the thing, the other is the thing.
- **Benefit:** Removes an entire category of error at the source — the model reasons from the real document instead of your recollection of it, so its answer can't be wrong for a reason you introduced.
- **Apply:** Photograph or upload the actual page. *"Read this directly and tell me why I was charged this fee; highlight the exact rule on the page."*
- **Guardrail:** Redact account numbers, NRIC, address before uploading. The AI explains; you decide what to do — and if it matters, read the part it points to yourself to confirm.
- **Related:** → Explicit Source-Grounding

### Multi-Modal Equity: Talk to the Tool
*Speak to it when typing is the barrier.*
*(cross-reference: `[ONR-05]` · **Beginner**)*

For someone who isn't comfortable typing, or whose first language isn't the interface's, the keyboard itself is the barrier — not the technology behind it. Someone in a hospital, working through a health plan written in an unfamiliar language, can simply speak instead: describe the situation, ask the question, hear the answer back.

- **Analogy:** An office that only takes written forms turns away anyone who finds writing hard. One with a counter you can talk to serves everybody.
- **Benefit:** Opens the tool to exactly the people who need it most and are least served by a keyboard-first design — non-typists, non-native speakers, anyone for whom syntax was never the point.
- **Apply:** Use the voice feature in your own language: *"I'll speak to you in [language]; explain these terms to me simply."*
- **Guardrail:** Speaking to the AI is the same as typing to it — your words are still sent and stored. Don't say more than you need to, and not where others can overhear. A preparation tool, not a clinician.
- **Related:** *(none yet — its natural parent, deliberate modality/language routing, isn't its own pattern; flagged as a possible future entry)*

### Encryption Is Not the Answer
*Protect the account, not the file.*
*(cross-reference: `[SCF-10]` · **Beginner**)*

Worried about AI and privacy, the instinct is to reach for encryption. But you can't use data you can't decrypt — and encryption does nothing against the actual threat: someone who steals your login. To them, you're already unlocked.

- **Analogy:** A wall safe does nothing if the burglar walks in wearing your face and knows the combination.
- **Benefit:** Redirects real effort from a comforting non-solution to the two things that actually reduce risk — account security and data minimization.
- **Apply:** Protect the account, not the file. Strong, unique passwords; two-factor or passkeys; and above all, hand over less data in the first place.
- **Guardrail:** This isn't "encryption is useless" in general; it's "encryption is the wrong answer to *this* fear." A stolen, authenticated session walks straight past it.

### Email Is the Master Key
*Your inbox opens every other lock you own.*
*(cross-reference: `[SCF-11]` · **Beginner**)*

You connect an AI assistant to your calendar without a second thought — then, without thinking much harder, do the same for your inbox. That second connection is categorically different: email is the password-reset channel for *every other account you own*, so an assistant with email access effectively holds the keys to everything else too.

- **Analogy:** Lending your house key is one thing. Lending the cabinet where every other key hangs is another.
- **Benefit:** Protects the one account whose compromise cascades into all the others, by treating it as categorically different from the rest.
- **Apply:** Think of connector access as a sensitivity gradient: Calendar < Cloud Storage < Email. Grant the least that does the job.
- **Guardrail:** Deliberately *not* connecting your email is a feature, not a limitation. The convenience you give up is small; the blast radius you close off is your whole digital life.

### The Data Ingestion Boundary
*Decide what never gets typed or uploaded in the first place.*
*(cross-reference: `[SAFE-01]` · **Beginner**)*

The excitement of "just upload the document" or "just speak to it" has to arrive paired with an instinct for what *not* to hand over in the first place. You control what goes into the box.

- **Analogy:** You don't hand over the whole wallet to prove you're over eighteen — you show one card.
- **Benefit:** Prevents a leak at its only fully preventable point — before it's ever typed or uploaded — rather than trying to contain it afterward.
- **Apply:** Redact identifying detail — passwords, full NRIC, account numbers, other people's private data — before pasting or uploading. Share only the part needed for the question.
- **Guardrail:** This is a Beginner rule precisely because Direct Grounding and Multi-Modal Equity send beginners toward uploading documents and speaking aloud — the boundary has to arrive with the capability.

### Temporal Drift Verification
*Give it today's date instead of trusting its memory.*
*(cross-reference: `[SAFE-03]` · **Beginner**)*

A model's training cutoff means it will answer a "what's current" question with total confidence and total staleness, and give no visible sign of which one it's doing.

- **Analogy:** Asking someone just back from a year off-grid what the weather's like. Confident answer; last year's weather.
- **Benefit:** Catches an entire class of confidently-wrong answers before they're acted on, for the cost of one extra instruction.
- **Apply:** For anything current, supply today's date and tell the model to search rather than answer from memory. *"Today is [date]. Don't answer this from memory — search, and tell me the date on whatever source you use."*
- **Guardrail:** A Beginner rule because one-shot users often don't know a cutoff exists.

### Time-Grounding: The Clock It Doesn't Have
*Never let it guess what day it is.*
*(cross-reference: `[SAFE-04]` · **Beginner** — new in this edition)*

This is Temporal Drift Verification's sibling, and the distinction matters: that pattern is about *stale knowledge* (the model doesn't know what changed since training). This one is about the *clock itself*. A base model has no clock of its own; the product wrapped around it may or may not supply one — a device time zone, a system-injected date, a live search tool. Which of those you have is not visible from inside the conversation, and web searches often return cached pages rather than fresh ones. When the model can't establish the date, it doesn't stop. It fabricates a plausible one.

- **Analogy:** A stopped clock still has hands. It still points somewhere. It looks exactly like a working one until you check it against something else.
- **Benefit:** Kills an entire class of confident, invisible staleness — the wrong date that looks exactly like a right one.
- **Apply:** For anything time-sensitive, never accept a bare answer. Give it today's date yourself, or make it show you the dated source it's reading. Verify the date, the time zone and the freshness channel rather than assuming any one of them exists or is correct. If it can't produce one, treat the time as unknown. *"Before you answer: what is today's date, and how do you know it? If you can't establish it from a dated source, say so instead of estimating."*
- **Guardrail:** The dangerous case isn't the obvious error. It's the *roughly-correct* fabrication, because occasional accuracy builds false trust. One good guess earns three unearned ones.
- **Related:** → Temporal Drift Verification (its sibling)

---
