#!/usr/bin/env bash
# ==============================================================================
# Multi-Agent Lifecycle Orchestrator with Session Isolation
# Pipeline: Planner -> Plan Reviewer -> Coder (Executor) -> Code Reviewer
# ==============================================================================

set -euo pipefail

TASKS_DIR="tasks"
CURRENT_LINK="${TASKS_DIR}/current"
CURRENT_FILE="${TASKS_DIR}/current_session.txt"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

mkdir -p "$TASKS_DIR"

log_step() {
  echo -e "\n${BLUE}================================================================${NC}"
  echo -e "${PURPLE}$1${NC}"
  echo -e "${BLUE}================================================================${NC}\n"
}

get_current_session() {
  if [ -f "$CURRENT_FILE" ] && [ -s "$CURRENT_FILE" ]; then
    cat "$CURRENT_FILE" | tr -d '\r\n'
  elif [ -L "$CURRENT_LINK" ]; then
    basename "$(readlink "$CURRENT_LINK")"
  else
    echo ""
  fi
}

set_current_session() {
  local session_name="$1"
  mkdir -p "${TASKS_DIR}/${session_name}"
  echo "$session_name" > "$CURRENT_FILE"
  ln -sfn "$session_name" "$CURRENT_LINK"
}

resolve_session() {
  local requested="${1:-}"
  if [ -n "$requested" ]; then
    echo "$requested"
  else
    local curr
    curr="$(get_current_session)"
    if [ -n "$curr" ]; then
      echo "$curr"
    else
      local new_sess
      new_sess="$(date +%Y%m%d_%H%M%S)"
      set_current_session "$new_sess"
      echo "$new_sess"
    fi
  fi
}

list_sessions() {
  echo -e "\n${BLUE}Available Task Sessions in ${TASKS_DIR}/:${NC}"
  local curr
  curr="$(get_current_session)"
  for d in "${TASKS_DIR}"/*; do
    if [ -d "$d" ] && [ ! -L "$d" ]; then
      local bname
      bname="$(basename "$d")"
      if [ "$bname" = "$curr" ]; then
        echo -e "  * ${GREEN}${bname}${NC} (ACTIVE)"
      else
        echo -e "    ${bname}"
      fi
    fi
  done
  echo ""
}

switch_session() {
  local target="${1:-}"
  if [ -z "$target" ]; then
    echo -e "${RED}[ERROR] Must specify session name to switch to.${NC}"
    list_sessions
    exit 1
  fi
  if [ ! -d "${TASKS_DIR}/${target}" ]; then
    echo -e "${RED}[ERROR] Session directory does not exist: ${TASKS_DIR}/${target}${NC}"
    list_sessions
    exit 1
  fi
  set_current_session "$target"
  echo -e "${GREEN}[OK] Switched active session to: ${target}${NC}"
}

new_session() {
  local name="${1:-$(date +%Y%m%d_%H%M%S)}"
  # Sanitize name
  name="$(echo "$name" | tr ' /' '_-')"
  if [ -d "${TASKS_DIR}/${name}" ]; then
    echo -e "${YELLOW}[NOTE] Session ${name} already exists. Switching to it.${NC}"
  else
    mkdir -p "${TASKS_DIR}/${name}"
    echo -e "${GREEN}[OK] Created new session directory: ${TASKS_DIR}/${name}${NC}"
  fi
  set_current_session "$name"
  echo -e "${GREEN}[OK] Active session set to: ${name}${NC}"
}

check_plan_exists() {
  local s_dir="$1"
  if [ ! -f "${s_dir}/plan.md" ]; then
    echo -e "${RED}[ERROR] Plan file not found: ${s_dir}/plan.md${NC}"
    echo "Please run Phase 1 (Planner) first or create ${s_dir}/plan.md."
    exit 1
  fi
}

check_plan_approval() {
  local s_dir="$1"
  check_plan_exists "$s_dir"
  local rev_file="${s_dir}/plan_review.md"
  if [ ! -f "$rev_file" ]; then
    echo -e "${RED}[ERROR] Plan review file not found: ${rev_file}${NC}"
    echo "The Plan Reviewer must audit ${s_dir}/plan.md and issue an APPROVED verdict before coding."
    exit 1
  fi

  if grep -q "VERDICT: APPROVED" "$rev_file" || grep -q "\*\*APPROVED\*\*" "$rev_file"; then
    echo -e "${GREEN}[OK] Plan in ${s_dir} is APPROVED by Plan Reviewer.${NC}"
  else
    echo -e "${RED}[BLOCKED] Plan in ${s_dir} has NOT been approved by Plan Reviewer!${NC}"
    echo "Review contents of ${rev_file} and revise ${s_dir}/plan.md with the Planner."
    exit 1
  fi
}

phase_planner() {
  local session_name="$1"
  local s_dir="${TASKS_DIR}/${session_name}"
  set_current_session "$session_name"

  log_step "PHASE 1: PLANNER (The Architect) [Session: ${session_name}]"
  echo -e "${CYAN}Profile & Effort Allocation:${NC}"
  echo "  - Recommended Model: 'pro'"
  echo "  - Thinking / Reasoning Effort: HIGH (1.00)"
  echo "  - Focus: Deep structural analysis, dependency tree, atomic TDD task design"
  echo ""
  echo "Target Plan File: ${s_dir}/plan.md"
  echo "Instructions:"
  echo " - Break down requirements into atomic, bottom-up tasks."
  echo " - Formulate explicit TDD tests and verification commands."
  echo " - Output execution blueprint to ${s_dir}/plan.md."
}

phase_plan_reviewer() {
  local session_name="$1"
  local s_dir="${TASKS_DIR}/${session_name}"
  check_plan_exists "$s_dir"

  log_step "PHASE 2: PLAN REVIEWER (The Adversarial Gatekeeper) [Session: ${session_name}]"
  echo -e "${CYAN}Profile & Effort Allocation:${NC}"
  echo "  - Recommended Model: 'pro'"
  echo "  - Thinking / Reasoning Effort: HIGH (1.00 / Maximum Adversarial Scrutiny)"
  echo "  - Focus: Circular dependency detection, reference integrity, stripping slop"
  echo ""
  echo "Auditing Plan File: ${s_dir}/plan.md"
  echo "Verification parameters:"
  echo "  1. Dependency Analysis (bottom-up order)"
  echo "  2. Reference Integrity (verify components exist)"
  echo "  3. Scope Contraction (strip slop & over-engineering)"
  echo "  4. Testability Matrix (concrete verification commands)"
  echo ""
  echo "Review output target: ${s_dir}/plan_review.md"
  echo "Must conclude with either **APPROVED** or **REJECTED**."
}

phase_coder() {
  local session_name="$1"
  local s_dir="${TASKS_DIR}/${session_name}"
  check_plan_approval "$s_dir"

  log_step "PHASE 3: CODER (The Builder / TDD Executor) [Session: ${session_name}]"
  echo -e "${CYAN}Profile & Effort Allocation:${NC}"
  echo "  - Recommended Model: 'flash' (or inherit)"
  echo "  - Thinking / Reasoning Effort: MEDIUM (0.50 - 0.70 / High Velocity)"
  echo "  - Focus: Fast Red-Green-Refactor cycles, local unit tests, minimal diffs"
  echo ""
  echo "Plan verified! Proceeding with TDD implementation loop for ${s_dir}/plan.md:"
  echo "  1. RED: Write failing test matching blueprint."
  echo "  2. GREEN: Implement minimal production code to pass test."
  echo "  3. REFACTOR: Clean up without breaking tests."
  echo "  4. Check off completed tasks in ${s_dir}/plan.md."
}

phase_code_reviewer() {
  local session_name="$1"
  local s_dir="${TASKS_DIR}/${session_name}"

  log_step "PHASE 4: CODE REVIEWER (Architecture, Design Systems, Best Practices & Security) [Session: ${session_name}]"
  echo -e "${CYAN}Profile & Effort Allocation:${NC}"
  echo "  - Recommended Model: 'pro'"
  echo "  - Thinking / Reasoning Effort: HIGH (0.90 - 1.00 / Deep Audit)"
  echo "  - Focus: Architecture decisions, design systems, best practices, OWASP security"
  echo ""
  echo "Inspecting git diff and test results against: ${s_dir}/plan.md"
  git status -s
  echo ""
  echo "Pillars evaluated:"
  echo "  1. Architecture Decisions & System Boundaries (layering, decoupling, multi-provider isolation)"
  echo "  2. Design Systems & Software Engineering Best Practices (component reuse, typing, error hierarchy, SOLID)"
  echo "  3. Security & Vulnerability Auditing (OWASP, auth guards, injection vectors, secret leaks, whitelisting)"
  echo "  4. Correctness, Integrity & Test Quality (plan conformance, test coverage, edge cases, zero regressions)"
  echo ""
  echo "Audit report target: ${s_dir}/code_review.md"
  echo "Must conclude with either **APPROVED** or **CHANGES REQUESTED**."
}

status() {
  local session_name="$1"
  local s_dir="${TASKS_DIR}/${session_name}"

  echo -e "\n${BLUE}Multi-Agent Pipeline Status & Effort Matrix [Session: ${session_name}]:${NC}"
  echo "------------------------------------------------------------"
  printf "%-16s | %-8s | %-12s | %-16s\n" "Agent" "Model" "Effort" "Status"
  echo "------------------------------------------------------------"

  local p_status="Pending"
  [ -f "${s_dir}/plan.md" ] && p_status="Created"
  printf "%-16s | %-8s | %-12s | %-16s\n" "1. Planner" "pro" "HIGH (1.00)" "$p_status"

  local pr_status="Missing"
  local rev_file="${s_dir}/plan_review.md"
  if [ -f "$rev_file" ]; then
    if grep -q "VERDICT: APPROVED" "$rev_file" || grep -q "\*\*APPROVED\*\*" "$rev_file"; then
      pr_status="APPROVED"
    else
      pr_status="REJECTED"
    fi
  fi
  printf "%-16s | %-8s | %-12s | %-16s\n" "2. Plan Reviewer" "pro" "HIGH (1.00)" "$pr_status"

  local c_status="Awaiting Plan"
  [ "$pr_status" = "APPROVED" ] && c_status="Ready / Active"
  printf "%-16s | %-8s | %-12s | %-16s\n" "3. Coder" "flash" "MEDIUM (0.6)" "$c_status"

  local cr_status="Pending"
  local cr_file="${s_dir}/code_review.md"
  if [ -f "$cr_file" ]; then
    if grep -q "VERDICT: APPROVED" "$cr_file" || grep -q "\*\*APPROVED\*\*" "$cr_file"; then
      cr_status="APPROVED"
    else
      cr_status="CHANGES REQ"
    fi
  fi
  printf "%-16s | %-8s | %-12s | %-16s\n" "4. Code Reviewer" "pro" "HIGH (1.00)" "$cr_status"
  echo "------------------------------------------------------------"
  echo "Active Session Directory: ${s_dir}"
  echo ""
}

CMD="${1:-status}"
SESS_ARG="${2:-}"

case "$CMD" in
  new)
    new_session "$SESS_ARG"
    ;;
  list)
    list_sessions
    ;;
  switch)
    switch_session "$SESS_ARG"
    ;;
  plan)
    SESSION="$(resolve_session "$SESS_ARG")"
    phase_planner "$SESSION"
    ;;
  review-plan)
    SESSION="$(resolve_session "$SESS_ARG")"
    phase_plan_reviewer "$SESSION"
    ;;
  code)
    SESSION="$(resolve_session "$SESS_ARG")"
    phase_coder "$SESSION"
    ;;
  review-code)
    SESSION="$(resolve_session "$SESS_ARG")"
    phase_code_reviewer "$SESSION"
    ;;
  check)
    SESSION="$(resolve_session "$SESS_ARG")"
    check_plan_approval "${TASKS_DIR}/${SESSION}"
    ;;
  status)
    SESSION="$(resolve_session "$SESS_ARG")"
    status "$SESSION"
    ;;
  *)
    echo "Usage: $0 {new|list|switch|plan|review-plan|code|review-code|check|status} [session-name]"
    exit 1
    ;;
esac
