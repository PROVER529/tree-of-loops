from pathlib import Path

CANDIDATES = {
    "candidate_a_minimal_patch": "Minimal patch strategy",
    "candidate_b_test_first": "Test-first strategy",
    "candidate_c_refactor": "Refactor strategy",
    "candidate_d_safety_first": "Safety-first strategy",
}

BASE_DIR = Path("demo_runs")


def main() -> None:
    BASE_DIR.mkdir(exist_ok=True)

    for folder_name, strategy in CANDIDATES.items():
        candidate_dir = BASE_DIR / folder_name
        candidate_dir.mkdir(exist_ok=True)

        readme = candidate_dir / "README.md"
        readme.write_text(
            f"# {folder_name}\n\n"
            f"Strategy: {strategy}\n\n"
            "This folder represents one isolated candidate loop.\n",
            encoding="utf-8",
        )

    print(f"Created {len(CANDIDATES)} candidate folders in {BASE_DIR}/")


if __name__ == "__main__":
    main()
