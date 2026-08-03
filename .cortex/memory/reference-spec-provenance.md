# Spec provenance (opencode API)

- Tracking surface: `spec/openapi-opencode.json` - copy of anomalyco/opencode `packages/sdk/openapi.json` at a release tag. Currently v1.18.11 (commit a1ab489e, 2026-07-30; sha256 `5bbd6493a1a488ef4294889341c896e420f814ecea95822100aaa9f3f95ab2d1` after stripping x-codeSamples).
- Re-pull per release: fetch `https://raw.githubusercontent.com/anomalyco/opencode/<tag>/packages/sdk/openapi.json`, strip `x-codeSamples`, record tag + commit next to the file.
- `.stats.yml`: `openapi_spec_url` + `openapi_spec_hash` record a legacy Stainless generation (23 paths / 26 ops, camelCase operationIds, md5 `4ff9376cf9634e91731e63fe482ea532`). Historical record only; regeneration via Stainless with that input cannot produce the 188-op surface.
- Docs sources (opencode.ai/changelog, opencode.ai/docs) derive from the same generated spec.
