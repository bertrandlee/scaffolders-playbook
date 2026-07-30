# The Scaffolder's Playbook

**Beyond Prompt Engineering to Workflow Architecture**

Fifty patterns for working with AI at the level serious practitioners actually
operate — without any technical prerequisites beyond a chat window and curiosity.

Free. Forkable. Built to grow.

---

## What this is

Most people use AI as a question-answering machine. This book shows you how to use
it as a system — one with memory, discipline, and a clear human in charge.

Prompt engineering optimises one question for one better answer. It operates at the
level of the *turn*. This book operates above the turn: the memory that outlives a
conversation, the file that survives a thread, the check that fires on a future
edit, the reconciliation that runs weeks later.

The patterns are organised by the skill they require and the problem they solve —
from a technique you can try in a single conversation, to architectures that outlive
individual threads and survive across months of real use.

## Who it is for

Someone working *alongside* an AI in a chat window. No code, no framework, no API
key.

Pattern catalogues for AI already exist — prompt-pattern collections in the academic
literature, design-pattern books for people building applications and agents, UX
pattern libraries for people designing chat interfaces. All of them are written for
builders. This one is for the person on the other side of that interface.

If you want the layer *below* this one, it already exists and is excellent:
[DAIR.AI's Prompt Engineering Guide](https://www.promptingguide.ai/). This book
starts where that one stops.

## Read it

| Format | Best for |
|---|---|
| PDF | reading straight through, printing |
| EPUB | e-readers, phones; each pattern is its own section |
| DOCX | commenting, tracked changes |

Download from [Releases](../../releases). Built files are attached to each release
rather than committed to the repository, so a fork gives you editable source rather
than a PDF you cannot change.

**Or hand it to the tool it describes.** Upload the file into a ChatGPT, Gemini or
Claude conversation and ask it to walk you through any pattern, or to test one with
you on a real task.

## Source layout

The manuscript is sharded. The shard set is canonical — not the built files.

```
manuscript/
  shard_00_frontmatter_*.md    title, licence, preface, introduction
  shard_01_beginner_*.md
  shard_02_intermediate_*.md
  shard_03_advanced_*.md
  shard_04_elite_*.md
  shard_99_appendices_*.md     index, platform compatibility, further reading
  MANIFEST_*.md                names the live shard set and the control total
build/
  assemble_*.py                shards -> build source
  build_tests.py               regression suite
  build_expectations.json      declared expectations the tests assert against
```

**Resolve the manuscript through the MANIFEST, never by guessing at filenames.**
Shard files carry a date and revision; the MANIFEST names which revision is live and
states the expected byte total.

## Contributing

The real product is not the fifty patterns. It is the reflex: work with these tools
long enough and with enough discipline, and you will notice your own recurring
solutions to your own recurring problems.

When you do, [write them up](CONTRIBUTING.md). There is a bar, and it is deliberately
awkward — a pattern with no stated limit is a sales pitch, not a technique.

## Licence

Content is licensed **CC BY-NC 4.0**. Share it, adapt it, fork it for non-commercial
purposes with credit.

**Internal use within organisations is expressly permitted** — copy it, circulate it,
use it for training and onboarding inside your company, commercial or otherwise, at
no charge and without asking. What the NonCommercial term withholds is *selling* the
book, or selling a work derived from it.

See [LICENSE](LICENSE) for the full grant. The Creative Commons grant is irrevocable.

## A word on what this book claims

Platform capabilities are the least durable content here, and they are dated and
marked as such. Every capability-dependent pattern carries a note saying when it was
checked. Re-check before you rely on it.

Where a pattern has known prior art, its entry says so. Very little here is
unprecedented in computing — what is uncommon is who is doing it by hand, alone, in
a chat window.
