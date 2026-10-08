from rag_attribution import CitationAttributionBenchmark

def test_attribution_benchmark():
    corpus = {"D1": "PostgreSQL uses MVCC for transaction isolation."}
    bench = CitationAttributionBenchmark()
    res = bench.evaluate_text("PostgreSQL implements MVCC for isolation [D1].", corpus)
    assert res.total_sentences == 1
    assert res.attributed_sentences == 1
    assert res.items[0].is_valid_attribution is True
