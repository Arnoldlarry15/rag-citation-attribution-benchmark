import re
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class AttributionItem:
    sentence_id: int
    sentence_text: str
    cited_keys: List[str]
    is_valid_attribution: bool
    precision_score: float

@dataclass
class AttributionReport:
    total_sentences: int
    attributed_sentences: int
    attribution_coverage: float
    overall_precision: float
    items: List[AttributionItem] = field(default_factory=list)

    def print_report(self):
        print("="*65)
        print("RAG CITATION ATTRIBUTION BENCHMARK REPORT")
        print("="*65)
        print(f"Total Sentences Analyzed  : {self.total_sentences}")
        print(f"Attributed Sentences      : {self.attributed_sentences}")
        print(f"Attribution Coverage Rate : {self.attribution_coverage * 100:.1f}%")
        print(f"Mean Citation Precision   : {self.overall_precision * 100:.1f}%")
        print("="*65)

class CitationAttributionBenchmark:
    """Measures sentence-level attribution accuracy and span overlap in RAG outputs."""

    def evaluate_text(self, generated_text: str, source_corpus: Dict[str, str]) -> AttributionReport:
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", generated_text.strip()) if s.strip()]
        items = []
        attributed_count = 0
        total_prec = 0.0

        for idx, sent in enumerate(sentences, start=1):
            cits = re.findall(r"\[(.*?)\]", sent)
            if cits:
                attributed_count += 1
                valid_cits = [c for c in cits if c in source_corpus]
                if valid_cits:
                    s_words = set(re.findall(r"\w+", sent.lower()))
                    matches = 0
                    for vc in valid_cits:
                        doc_words = set(re.findall(r"\w+", source_corpus[vc].lower()))
                        matches += len(s_words.intersection(doc_words))
                    prec = min(1.0, matches / (len(s_words) * len(valid_cits))) if s_words else 1.0
                    is_valid = prec > 0.35
                else:
                    prec = 0.0
                    is_valid = False
            else:
                cits = []
                prec = 0.0
                is_valid = False

            total_prec += prec
            items.append(AttributionItem(
                sentence_id=idx,
                sentence_text=sent,
                cited_keys=cits,
                is_valid_attribution=is_valid,
                precision_score=prec
            ))

        tot = len(sentences)
        coverage = (attributed_count / tot) if tot else 0.0
        mean_p = (total_prec / attributed_count) if attributed_count else 0.0

        return AttributionReport(
            total_sentences=tot,
            attributed_sentences=attributed_count,
            attribution_coverage=coverage,
            overall_precision=mean_p,
            items=items
        )
