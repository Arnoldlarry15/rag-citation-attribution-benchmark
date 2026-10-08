# rag-citation-attribution-benchmark 📊

[![License: MIT](https://img.shields.io/badge/License-MIT-amber.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-emerald.svg)](https://labuilds.xyz)
[![Ecosystem: LA Builds](https://img.shields.io/badge/LA%20Builds-240%2B%20Production%20Assets-amber.svg)](https://labuilds.xyz)

> **Automated RAG Citation Attribution Benchmark (LAB-PRD-179)**  
> An open-source reference implementation from the **[LA Builds](https://www.labuilds.xyz)** software catalog.

---

### 🌐 Part of the LA Builds Architecture Ecosystem
Looking for production-grade self-hosted Python architectures, multi-agent swarms, security guardrails, and enterprise suites?  
**Explore all 240+ curated digital assets on the official store: [https://www.labuilds.xyz](https://www.labuilds.xyz)**

*This asset is also available as a constituent engine within the full **[LAB-BND-011: Enterprise LLM Evaluation, Judge Calibration & Observability Benchmark Suite](https://www.labuilds.xyz?pid=LAB-BND-011)** ($299).*

---

## 🎯 The Problem
When deploying enterprise retrieval engines, measuring exact sentence-level citation fidelity is critical. Existing benchmarks measure simple BLEU or ROUGE scores rather than factual citation precision and span overlap.

## 💡 The Solution
An automated evaluation harness that scores sentence-level citation fidelity, precision of cited character spans, over-citation penalties, and attribution coverage ratio across technical documents.

---

## 🚀 Quickstart

### 1. Installation
```bash
git clone https://github.com/Arnoldlarry15/rag-citation-attribution-benchmark.git
cd rag-citation-attribution-benchmark
pip install -e .
```

### 2. Run the Standalone Demo
```bash
python demo.py
```

### 3. Run the Test Suite
```bash
pytest tests/
```

---

## 📄 License
MIT License. Free for open-source and commercial deployment.  
Developed by **[LA Builds](https://www.labuilds.xyz)** • Autonomous AI Systems & Production Software.
