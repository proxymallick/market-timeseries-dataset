from pathlib import Path


README = Path(__file__).resolve().parents[1] / "README.md"


def test_prepared_selection_uses_a_compact_summary_table():
    text = README.read_text()
    section = text.split("## Prepared selection", 1)[1].split(
        "### Coverage and interpretation limits", 1
    )[0]

    assert "| Dataset | Coverage | Rows | Size |" in section
    assert "| Rights and caveats |" not in section
    assert section.count("<details>") == 6
