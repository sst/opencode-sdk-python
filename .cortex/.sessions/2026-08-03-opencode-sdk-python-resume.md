# Orchestrator compact-resume — opencode-sdk-python, 2026-08-03 (final)

Session: catalyst v2 orchestrator (omp, deepseek-v4-flash thinking max) for the Walzen Group fork
of the Stainless-generated opencode Python SDK. Repo /workspaces/opencode-sdk-python.
Branch feat/1.18-api-surface. ALL wave work committed (12 commits, see below); nothing pushed.
Kit tree: /nix/.cortex/ (skills live at /opt/skills). Roster: orchestrator only, no wave in flight.

## Branch state (feat/1.18-api-surface, 12 commits, append-only, no push)
7100070 uv.lock migration | 0fcbbf4 de-Stainless | c010afa subagent_depth | 86bf9c6 flake.nix |
8ecd39a experimental (16 ops) | 2876d48/051131c/bf6fc95 global_/tool/worktree (12 ops) |
1ec5a4a/da0cf15/a1cfdb8 v2 (61 ops: AddressingParams ext, subpackage, tests) |
4cf0597 wiring + api.md | fec2a78 pyright test fix | 8cb982c api.md LF + .direnv ignore |
d79a023 spec-faithful (subagent_depth on global.config.update, with_raw_response) |
4732f2e Python 3.13 + mypy-under-nix fix.

## Whole-change state (verified by wave metas, orchestrator audited)
Baseline failures only (pre-existing at 1247e99): 2 pytest (u2028 SSE test_streaming
special_new_line sync+async), 2 mypy/pyright errors in _models.py (pydantic drift: venv 2.13.4
vs requirements-dev.lock 2.10.3). Everything else green on Python 3.13; mypy runs bare under
nix (flake wraps it with --python-executable .venv/bin/python).

## Open issues (user decisions pending)
1. 2 mypy findings: RESOLVED (commit 5feae1f, verified: bare nix mypy = 2 baseline only).
2. Dev-tool venv recipe: RESOLVED (commit 39fe91d, CONTRIBUTING With Nix subsection).
3. list_models: RESOLVED - user approved not re-landing; v2.model.list covers it.
4. Push branch / open PR: held, user's call.
5. Kit: models.yaml default RESOLVED - defaults to /opt/skills/catalyst-v2-model-picking/models.yaml
   (alongside its skill); suite 77 tests / 76 pass. Kit: 1 remaining same-family failure -
   dispatch.test.mjs imports /nix/settings/skills/catalyst-v2-dispatch/test/helpers/harness.mjs
   (nonexistent); harness lives at /opt/skills/... - fold into kit consolidation. Kit: 6 guarding
   tests await kit consolidation. Kit: docs/catalyst-skills.md row (host-side).
6. Audit report: delivered at .cortex/reports/2026-08-03-opencode-1.18-audit-report.md.
7. System note: worker briefs tell omp workers to report via c2d steer, but worker sessions have
   no c2d device / no meta hub peer - reports reached the meta as in-terminal relays instead.
   Worked, but check the worker report channel if it recurs (candidate improvement).

## Delivered today (all verified)
- Audit report (v1.18.11 surface): .cortex/reports/2026-08-03-opencode-1.18-audit-report.md
- flake.nix dev toolchain; uv.lock current format; de-Stainless sweep; 89-op coverage (global_,
  tool, worktree, experimental, v2); subagent_depth everywhere; cleanup wave (LF, .direnv,
  faithfulness, 3.13).
- Skill/tool system: A2A:/A2U: channel markers; steer composer-hold (c2d refuses delivery over a
  live draft); kit-vs-project store split; append-only git rule for shared-checkout workers;
  meta liveness probe-and-verify (META QUIESCENT classification); testing-skill split
  (catalyst-v2-testing -> catalyst-v2-self-testing; NEW catalyst-v2-testing codifies test-first,
  post-fix tests 'dishonest'); Mode A replay no-write rule (isolated worktree).

## Incidents filed today (kit store /nix/.cortex/incidents/)
2026-08-03-report-delivery, report-style, meta-retirement-misdiagnosis, steer-composer-interference,
memory-store-placement, replay-contamination-shared-checkout, skill-content-duplicated-in-memory.
Project store: 2026-08-03-git-history-rewrite-shared-checkout. All repaired + replay-verified + guarding tests.

## Skill-vs-memory rule (incident 2026-08-03-skill-content-duplicated-in-memory)
A directive codified in a catalyst skill is never restated in memory; memory may carry a
pointer until the skill lands it, then the entry is removed or reduced to a pointer. The
skill is the single home. Owning skill: catalyst-v2-in-repo-agent-memory; guarding test
skill-content-duplicated-in-memory.

## Standing conventions
A2A:/A2U: markers (steer vs user-relay); unmarked user-channel = user input, claimed relays held
for provenance; system records -> /nix/.cortex/, project records -> project .cortex/; steer
refused over live composer drafts (quarantine hand-backs to .cortex/reports/handbacks/); workers
append-only git; meta liveness = probe-and-verify (never two metas); test-first with recorded red
run; user-facing deliverables -> .cortex/reports/ with writing-docs pass; i-have-adhd + humanizer.

## Memory
Project: .cortex/memory/ (project-2026-08-03-flake-uv-audit.md, reference-spec-provenance.md).
Kit: /nix/.cortex/memory/ (project-2026-08-03-catalyst-conventions.md, feedback-* files).

## Next actions
1. Present open items to the user (above) and take their calls.
2. Optional follow-up dispatch: mypy findings fix + CONTRIBUTING venv recipe (one small wave).
3. Kit consolidation dispatch (guarding tests move + CATALYST_MODELS_YAML doc + catalyst-skills.md
   row) when the user wants kit cleanup.
4. Push/PR on the user's go.
