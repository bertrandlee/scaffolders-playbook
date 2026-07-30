# Licensing

This repository contains two different kinds of material under two different
licences. The distinction matters: a content licence applied to build tooling makes
the tooling unusable by the people most likely to improve it.

## The book — CC BY-NC 4.0

Everything under `manuscript/`, and the built files attached to Releases, is
licensed **Creative Commons Attribution–NonCommercial 4.0 International**.

Share it, adapt it, fork it for non-commercial purposes with credit. The grant is
irrevocable.

**Internal use within organisations is expressly permitted** — copy, circulate and
use this book for training, onboarding and reference inside your organisation,
commercial or otherwise, at no charge and without seeking permission. What the
NonCommercial term withholds is *selling* the book, or selling a work derived from
it.

Full text: `LICENSE`

## The build tooling — [MIT or Apache-2.0: OWNER DECISION PENDING]

Everything under `build/` — the assembler, the regression suite, the declared
expectations, the accessibility post-processor — is licensed permissively so that
anyone can reuse or improve it without the NonCommercial restriction attaching to
their own work.

Full text: `LICENSE-CODE`

## Why the split

The NonCommercial term protects the book from being resold. It was never intended
to stop a developer borrowing the test harness, and applying it to code would do
exactly that. Contributions to `build/` are far more likely to come from people
working inside commercial organisations than contributions to the manuscript.

## Contributions

By submitting, you agree your contribution is offered under the licence covering the
part of the repository it touches — CC BY-NC 4.0 for manuscript content, the
permissive licence for build tooling.
