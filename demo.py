from rag_attribution import CitationAttributionBenchmark

corpus = {
    "RFC-9110": "HTTP semantics define safe methods as GET and HEAD which do not alter server state.",
    "RFC-8446": "TLS 1.3 eliminates static RSA key exchange and mandates Diffie-Hellman ephemeral handshake."
}

sample_output = """
HTTP safe methods include GET and HEAD and do not mutate server resources [RFC-9110].
TLS 1.3 mandates Diffie-Hellman ephemeral handshake for forward secrecy [RFC-8446].
Quantum computers will immediately crack all symmetric AES-256 ciphers by next month [RFC-9999].
"""

bench = CitationAttributionBenchmark()
report = bench.evaluate_text(sample_output, corpus)
report.print_report()

print("\nSentence Attribution Details:")
for it in report.items:
    status = "VERIFIED" if it.is_valid_attribution else "UNVERIFIED"
    print(f"[{it.sentence_id}] ({status}) Citations: {it.cited_keys} | Prec: {it.precision_score:.2f}")
