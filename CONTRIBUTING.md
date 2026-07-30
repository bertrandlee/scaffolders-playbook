# Contributing a pattern

This book teaches you to notice recurring solutions to recurring problems in your own
practice, and then to write them down well enough that a stranger can use them. This
is where you send them.

**The bar is deliberately awkward.** Most submissions that fail, fail on evidence or
on the guardrail — not on the idea.

---

## Before you write anything: four checks

**1. Is it actually yours, or is it already named?**
Search first. Much of what feels novel in a consumer-chat workflow has decades of
prior art in software engineering, distributed systems or security. Finding the
lineage makes your write-up *stronger* — you can point at the established version and
say *this is that, applied here*. Claiming novelty you do not have is the fastest way
to lose a careful reader.

**2. Does it survive abstraction?**
Strip out everything specific to you — your tools, your files, your project — and
check the shape still stands. Then state what it genuinely requires: *needs a file you
control*, *needs a second model*, *needs somewhere two threads can both read*. If you
cannot name the prerequisites you have a configuration, not a pattern.

Beginner and Intermediate patterns hold to a harder bar: they must work in a bare
chat window with nothing but the conversation.

**3. Would it survive an adversary?**
Hand the write-up to a *different* model than the one you built it with and instruct
it to attack — find where it breaks, which claim is too strong, which guardrail is
missing. Then note the ceiling: two models agreeing is weaker evidence than it feels,
because they may share training data and therefore blind spots. Before submitting, add
at least one channel that is not another model — repeated real use, a mechanical test,
a comparison against primary sources, or a domain expert.

**4. Has it actually worked, more than once?**
This is where most submissions fail. The question splits, because two kinds of pattern
earn their place two different ways.

- **A technique you deliberately deploy** — name **two occasions**, real tasks and not
  demonstrations, where you reached for this and it changed the outcome.
- **A diagnostic** — nobody reaches for one; you notice afterwards that you failed to
  apply it. So name **two occasions where failing to do this changed the outcome, and
  one where catching it did.**

If you can only think of the time you invented it, you have a **hypothesis**. Submit it
labelled as one. A clearly labelled hypothesis is a useful contribution. A hypothesis
dressed as a tested pattern is the thing this book keeps warning about.

---

## The template

Copy this into your pull request or issue.

```markdown
### [Pattern name]
*One-line summary, framed as an instruction.*

**Tier:** Beginner | Intermediate | Advanced | Elite
**Family:** On-Ramps | Foundation | Practices | Architecture | Governance | Safety
**Status:** tested pattern | labelled hypothesis

**Prerequisites** (one line — what a reader must have for this to work at all)

**The problem.** The recurring friction, concrete enough that a reader recognises
their own version of it. One or two sentences.

**Analogy** (optional, but it is the fastest way to make a pattern land — and it
tells you whether you understand the shape or only the mechanics)

**Benefit.** What you get, and what it costs you if you skip it.

**Apply.** How to actually do it, specific enough to act on. If a prompt is part of
it, include the prompt verbatim. Not every pattern has one — a pattern you *build*
(a file convention, a way of writing) does not, and inventing a prompt for it
misrepresents what it is.

**Guardrail.** Where it fails. What it does *not* protect against. The honest
ceiling. **This field is the one most people skip and the one that makes a pattern
trustworthy.** If you cannot fill it in, you have not tested the pattern hard enough
— go use it until it fails, then write down how.

**Evidence.** Per check 4 above. State which form applies and give the occasions.

**Lineage.** If it has a known ancestor, name it. A specific document needs a URL
*you verified yourself* — never a citation copied from someone else's summary.
A canonical concept (version control, late binding, leader election) needs no URL.
"No lineage" is a valid answer.
```

---

## What gets rejected, and why

- **No guardrail.** The most common failure. A pattern with no stated limit reads as
  a sales pitch.
- **Evidence from demonstrations rather than real tasks.** Building an example to
  prove the pattern is not the same as the pattern having changed an outcome.
- **Requires infrastructure a reader cannot reasonably have.** Especially at Beginner
  and Intermediate tier.
- **A citation nobody checked.** A real, prestigious, checkable document that answers
  a *different* question is more dangerous than a fabricated one, because it survives
  a reader who checks only the title.
- **Novelty claims.** Say "uncommon in this context, well established in that one."

Rejection is usually "not yet" rather than "no." The most common fix is to go use the
thing until it breaks, then come back with the guardrail.

## Corrections and stale content

Platform capabilities are the most perishable content in this book. If a dated
capability note has gone stale, that is a genuinely useful contribution — open an
issue with the platform, the tier, what you observed, and the date you checked.
State whether you tested it or read it in documentation. Those are different claims.

## Licence for contributions

By submitting, you agree your contribution may be published under the same terms as
the book (CC BY-NC 4.0), with credit.
