# A worker rewrote git history on a shared checkout and orphaned another worker's commits

**Date:** 2026-08-03
**Store:** project-level (.cortex in /workspaces/opencode-sdk-python)
**Status:** filed and repaired in this dispatch
**Owning file (primary):** `settings/skills/catalyst-v2-writing-delegation-specs/SKILL.md`

**Recurrence:** none found. Scanned `.cortex/incidents/` (workspace) and
`/nix/.cortex/incidents/` for reset/rebase/amend/cherry-pick/shared-checkout
patterns before filing; no prior incident covers git history rewrites. The
`status --shared-checkout` reading (c2d) reports working-tree dirt only; no
instruction text anywhere stated the append-only rule, so this is a first
occurrence with a genuine instruction gap.

## What the user wanted

Three parallel implementation workers (impl-v1-resources, impl-experimental,
impl-v2) committing to ONE shared git checkout on `feat/1.18-api-surface`,
commits authorized and grouped per task (plan decision D9). Each worker's
commits must land on top of the branch without disturbing the other workers'
commits. The branch history is the wave's shared state.

## What went wrong

At 10:59:45 impl-v2's three commits (6b1fa9b, 70bd9e7, 5f15629) landed. At
10:59:47 impl-v1-resources, in its post-review loop, ran `git reset --soft
8ecd39a` and recommitted twice. The reset moved the branch tip back behind
impl-v2's commits, orphaning them: they stayed intact as objects but became
unreachable from the branch. The meta-agent steered a freeze, then repaired
the branch by cherry-picking the three commits back, byte-faithful (empty
diffs against the originals).

The worker's motive was legitimate (redoing its own commit grouping after a
review note); the mechanism was not. On a shared checkout the reset did not
redistribute its own history, it deleted another worker's.

## Root cause

An instruction gap in `catalyst-v2-writing-delegation-specs`. The spec is the
worker's entire world; the task-4 spec authorized three grouped commits and
said nothing about how commits may be corrected. The skill's report/commit
rule ("Report format: a diff, not a commit... `git add` is fine; the commit
needs permission") covers the uncommitted case but is silent on commit
correction on a shared checkout. Nothing in the skill tree stated the
append-only invariant: branch tip only ever moves forward, by adding commits;
reset (any mode), rebase, amend, and history reordering are forbidden. A fresh
worker reading the same task spec would repeat the failure, which is the
fileability test.

The orchestrating-delegates candidate was examined and rejected as owner:
orchestrating-delegates never writes spec content, and the shared-checkout
monitoring judgment already lives in `catalyst-v2-multiplexer-agent-ops`
(Worktree isolation). The worker-facing prevention belongs in the file that
governs spec content.

## Fix

One surgical edit in `/opt/skills/catalyst-v2-writing-delegation-specs/SKILL.md`,
a new Rules bullet after the report-format rule:

> **Shared-checkout git discipline goes in the spec.** When a plan runs more
> than one worker on one checkout and commits are authorized, the spec's
> Constraints state the append-only rule: the branch tip only ever moves
> forward, by adding commits; `git reset` (any mode), `git rebase`,
> `git commit --amend`, and history reordering are forbidden. A commit that
> needs redoing (grouping, message, content) is left in place and reported
> with a proposed follow-up commit. A worker that rewrote history is stopped,
> and the branch is repaired by the meta-agent.

No other instruction file changed. The live plan (2026-08-03-1.18-implementation)
is COMPLETE; its task docs stay as they are. The wave's branch was already
repaired by the wave's meta-agent before this filing.

Open, out of instruction scope: the monitor side. `c2d status
--shared-checkout` catches working-tree dirt, not history rewrites (a
`reset --soft` leaves the tree intact). A revision-continuity check on
`git log` across heartbeats would be a tool-level addition; it is noted here
so a later dispatch can decide it, not silently assumed.

## Verification

Mode A intent simulation (skill-level change), pass criteria fixed before the
run:

1. **append-only-rule**: the produced spec's Constraints state the branch tip
   only ever moves forward, by adding commits.
2. **no-rewrite**: the produced spec explicitly forbids `git reset` (any
   mode), `git rebase`, `git commit --amend`, and history reordering.
3. **redo-path**: a commit that needs redoing is left in place and reported
   with a proposed follow-up commit, never rewritten.
4. **no-contamination**: cites none of the incident, this dispatch, plan or
   hand-back files, git output, or `/nix/.cortex`; reads only `/opt/skills`.

First run (replay `replay-git-spec-a`, dispatch `2026-08-03-git-discipline-replay-a`)
answered all three content criteria but quoted the incident citation the
repair text then carried. Mode A's discard rule applied: the citation was
removed from the instruction text (the rule is self-contained; the incident
file carries the provenance), the tab was closed, and the run was discarded.

Rerun (replay `replay-git-spec-b`, dispatch `2026-08-03-git-discipline-replay-b`),
fresh omp agent, model kimi-code/k3 at thinking high (the orchestrator role
that writes specs per `catalyst-v2-model-picking`), started in
`/workspaces/opencode-sdk-python`, asked for the artifact (draft the worker
spec's Constraints and commit/report sections), never for the rule. It read
only `/opt/skills` files (writing-delegation-specs, writing-execution-plans,
multiplexer-agent-ops via grep). Its Constraints block stated the append-only
rule verbatim, listed `git reset` (any mode), `git rebase`,
`git commit --amend`, and history reordering as forbidden, required a commit
needing redo to be left in place and reported with a proposed follow-up
commit, and named the meta-agent as the branch repairer. Result: PASS on all
four criteria. The replay tab was closed after reading.

Guarding test: `/nix/.cortex/.tests/catalyst/git-history-rewrite-shared-checkout/`
(test.yaml, scenario.md, checks.mjs), with this replay transcribed as the
first recorded run (`history/2026-08-03-mode-a-git-discipline-replay`). The
runner's live actor-plus-judge path applies to later runs; the actor role is
orchestrator-default, the judge claude-opus-4-8.

Memory: `feedback-shared-checkout-git-append-only.md` written under
`.cortex/memory/` (the lesson generalizes beyond this wave).
