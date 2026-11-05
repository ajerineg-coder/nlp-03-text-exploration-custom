"""Smoke test for Addie's custom fraud text exploration."""

import runpy

import matplotlib.pyplot as plt


def test_corpus_has_token_and_context_features(monkeypatch, tmp_path):
    """Verify the custom fraud corpus and text analysis."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(plt, "show", lambda: plt.close("all"))

    result = runpy.run_module("nlp.nlp_corpus_explore", run_name="__main__")

    assert len(result["corpus"]) == 12
    assert set(result["top_per_category_dict"]) == {
        "check_fraud",
        "wire_fraud",
        "account_takeover",
    }
    assert result["tokenize"]("Suspicious WIRE, transfer!") == [
        "suspicious",
        "wire",
        "transfer",
    ]
    assert ("wire", "instructions") in result["bigrams_list"]
    assert "instructions" in result["co_occurrence_dict"]["wire"]
