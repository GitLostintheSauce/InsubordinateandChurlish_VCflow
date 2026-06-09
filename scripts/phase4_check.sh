#!/usr/bin/env bash
# Phase-4 static QA check. Run from repo root.
# Verifies: JS parses, Phase-4 anchors exist, semantic-color tokens aren't overloaded.
# Does NOT do live browser QA — open the URL yourself and hard-refresh.
set -u
cd "$(dirname "$0")/.."

pass=0; fail=0
ok()   { echo "  ✓ $1"; pass=$((pass+1)); }
bad()  { echo "  ✗ $1"; fail=$((fail+1)); }
F=index.html

echo "[1/4] JS parse (JavaScriptCore)"
awk '/<script>$/{f=1;next} /<\/script>/{f=0} f' "$F" > /tmp/vcflow_check.js
result=$(osascript -l JavaScript -e 'ObjC.import("Foundation"); var s=$.NSString.stringWithContentsOfFileEncodingError("/tmp/vcflow_check.js",4,null).js; try{new Function(s);"PARSE OK"}catch(e){"ERR: "+e}' 2>/dev/null)
[[ "$result" == "PARSE OK" ]] && ok "JS parses" || bad "JS parse failed: $result"

echo "[2/4] Phase-4 anchors present"
grep -q 'id="headline-insights"'        "$F" && ok "insights section in HTML"           || bad "insights section missing"
grep -q 'id="insightsGrid"'             "$F" && ok "insights grid mount point"          || bad "grid mount missing"
grep -q 'const INSIGHTS = \['           "$F" && ok "INSIGHTS array defined"             || bad "INSIGHTS missing"
grep -q 'function renderInsights()'     "$F" && ok "renderInsights() defined"           || bad "renderInsights missing"
grep -q '^  renderInsights();'          "$F" && ok "renderInsights() called in renderAll" || bad "renderInsights not called"
cards=$(awk '/const INSIGHTS = \[/,/^\];/' "$F" | grep -c '^  {big:')
[[ "$cards" -ge 8 && "$cards" -le 12 ]] && ok "insight card count = $cards (8–12)" || bad "card count $cards out of 8–12 range"

echo "[3/4] Critique-driven polish landed"
grep -q 'state = {scale:"linear"'           "$F" && ok "default chart scale = linear"     || bad "default scale not linear"
grep -q 'data-scale="linear" class="on"'    "$F" && ok "Linear toggle marked active in HTML" || bad "Linear button not active in HTML"
grep -q '~\$93B'                            "$F" && ok "concentration KPI in hero"        || bad "concentration KPI missing from hero"
! grep -q '<div class="value">56%</div>'    "$F" && ok "weak 56% KPI removed"             || bad "old 56% KPI still in hero"
grep -q -- '--Biotech:#e879d4'              "$F" && ok "Biotech recolored (magenta)"      || bad "Biotech still on old color"
grep -q -- '--Defense:#9ca0a8'              "$F" && ok "Defense recolored (steel)"        || bad "Defense still on old color"
grep -q '"Biotech":"#e879d4"'               "$F" && ok "JS COLOR Biotech matches CSS"     || bad "JS COLOR Biotech mismatch"
grep -q '"Defense":"#9ca0a8"'               "$F" && ok "JS COLOR Defense matches CSS"     || bad "JS COLOR Defense mismatch"

echo "[4/4] Semantic color tokens not overloaded by any sector"
! grep -Eq '^    --(AI|Fintech|Biotech|Climate|Web3|Defense):#ff7575' "$F" && ok "no sector uses --danger red"    || bad "a sector still uses #ff7575"
! grep -Eq '^    --(AI|Fintech|Biotech|Climate|Web3|Defense):#ffd76b' "$F" && ok "no sector uses --warn yellow"   || bad "a sector still uses #ffd76b"

echo
echo "Summary: $pass passed, $fail failed"
[[ "$fail" -eq 0 ]] || exit 1
echo
echo "Static checks clean. Next: live QA."
echo "  python3 -m http.server 8000   # then hard-refresh http://localhost:8000"
echo "  Verify: insight grid renders 12 cards · Overview opens linear · KPI #2 reads \$93B ·"
echo "          Biotech is magenta and Defense is steel in every chart · no console errors · 375px width OK"
