from __future__ import annotations

import subprocess
import sys
from datetime import datetime
from pathlib import Path
import os


PROJECT_ROOT = Path(__file__).resolve().parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
DIAGNOSTICS_DIR = PROJECT_ROOT / "outputs" / "diagnostics"
DIAGNOSTICS_DIR.mkdir(parents=True, exist_ok=True)

SCRIPT_ORDER = [
    "01_load_and_audit_data.py",
    "02_column_mapping.py",
    "03_data_cleaning.py",
    "04_collection_control_gap.py",
    "05_uncollected_waste_hotspots.py",
    "06_future_infrastructure_pressure.py",
    "07_urban_rural_collection_gap.py",
    "08_organic_treatment_mismatch.py",
    "09_policy_performance_mismatch.py",
    "10_data_visibility_analysis.py",
    "11_city_country_mismatch.py",
    "14_macro_to_micro_extension.py",
    "15_substitution_scenario_tests.py",
    "12_compare_research_directions.py",
    "13_make_figures.py",
    "18_paper_ready_analytical_upgrades.py",
    "16_figure_design_review.py",
    "17_quality_validation_and_memos.py",
    "19_figure_quality_curation.py",
]


def main() -> None:
    log_path = DIAGNOSTICS_DIR / "pipeline_run_log.txt"
    with log_path.open("w", encoding="utf-8") as log:
        log.write(f"WAW3 pipeline started: {datetime.now().isoformat(timespec='seconds')}\n")
        log.write("Existing generated outputs may be overwritten by scripts inside outputs/.\n")
        print("Existing generated outputs may be overwritten by scripts inside outputs/. Raw data will not be modified.")

        for script_name in SCRIPT_ORDER:
            script_path = SCRIPTS_DIR / script_name
            if not script_path.exists():
                message = f"SKIPPED missing script: {script_name}"
                print(message)
                log.write(message + "\n")
                continue
            print(f"\nRunning {script_name}...")
            log.write(f"\nRunning {script_name}\n")
            completed = subprocess.run(
                [sys.executable, str(script_path)],
                cwd=str(PROJECT_ROOT),
                capture_output=True,
                text=True,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            log.write(completed.stdout)
            if completed.stderr:
                log.write("\nSTDERR:\n" + completed.stderr)
            if completed.returncode != 0:
                warning = f"WARNING: {script_name} exited with code {completed.returncode}; pipeline will continue."
                print(warning)
                log.write(warning + "\n")
                (DIAGNOSTICS_DIR / f"{script_name.replace('.py', '')}_pipeline_error.txt").write_text(
                    completed.stderr or completed.stdout or warning,
                    encoding="utf-8",
                )
            else:
                stale_error = DIAGNOSTICS_DIR / f"{script_name.replace('.py', '')}_pipeline_error.txt"
                if stale_error.exists():
                    stale_error.unlink()
                print(f"Completed {script_name}.")
                log.write(f"Completed {script_name}.\n")

        log.write(f"\nWAW3 pipeline finished: {datetime.now().isoformat(timespec='seconds')}\n")
    print(f"\nPipeline complete. Log saved to {log_path}")


if __name__ == "__main__":
    main()
