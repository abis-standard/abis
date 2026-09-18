#!/usr/bin/env bash
# M229D-009 — Public-safe protected test vector marker enforcement
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
FAIL=0

MARKERS=(
  "protected_golden_vectors"
  "counsel_derived_test_cases"
  "patent_embodiment_fixtures"
  "private_simulator_scenario_internals"
  "SYNTHETIC_PROTECTED_TEST_VECTOR"
)

while IFS= read -r -d '' file; do
  rel="${file#${ROOT}/}"
  case "$rel" in
    scripts/disclosure/check-test-vector-markers.sh)
      continue
      ;;
  esac
  case "$rel" in
    docs/*|assets/*|*.md)
      ;;
    *)
      continue
      ;;
  esac
  for marker in "${MARKERS[@]}"; do
    if grep -qF "$marker" "$file" 2>/dev/null; then
      FAIL=1
    fi
  done
done < <(find "${ROOT}" -type f ! -path '*/.git/*' -print0)

if [[ "${FAIL}" -eq 1 ]]; then
  echo "M229D-009 BLOCK: Disclosure policy violation." >&2
  exit 1
fi

echo "M229D-009 PASS"
exit 0
