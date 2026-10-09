# Candidate sources

This skill is project-specific to Daniel Aarao Reis Arturi's professional portfolio. This reference locates the living evidence; it is not a frozen biography. Read the current files before selecting claims.

When installed at `.agents/skills/cover-letter/`, the project root is three directories above `SKILL.md`, or four above this reference. Resolve paths relative to the installed files, not the shell's working directory.

## Source order

1. Use explicit user corrections and a newly supplied resume or application-specific materials first.
2. The project's [resume.pdf](../../../../resume.pdf) is the principal local career record. [resume-industry.pdf](../../../../resume-industry.pdf) offers an engineering-oriented presentation of that record.
3. [index.html](../../../../index.html) contains the portfolio's detailed contribution statements, project limitations, and external evidence links. Read these details as well as summary cards.
4. [scripts/build_resumes.py](../../../../scripts/build_resumes.py) contains readable text used to generate the resumes. It is useful for locating evidence; investigate material discrepancies with the PDF instead of assuming the generator is newer. Drafting a letter does not require running it or overwriting resumes.
5. [PRODUCT.md](../../../../PRODUCT.md) records the portfolio's positioning and truthfulness commitments. Use it to guide presentation, not to establish undocumented achievements.

If the relevant source is unavailable, use other supplied evidence and ask only for facts that materially affect the letter. Keep unverified claims out of the draft.

## Find relevant passages

Use targeted searches rather than loading the whole portfolio. These are navigation hints, not a requirement to include any particular experience:

| Topic | Search anchors in `index.html` |
| --- | --- |
| Lea and the VIDA role | `nyu-expmath`, `lea`, `lea-paper`, `My Contribution`, `Research Evaluation` |
| Retrieval and application engineering | `nyc-housing-rag`, `Research Workflow`, `Release Status` |
| Agent-guided vector search and evaluation | `nyu-fann-research`, `fannbench` |
| LLM behavior and interpretability | `algoverse`, `iclr-em-paper`, `neurips-paper` |
| Database and systems research | `mcgill-graph`, `mcgill-graph-paper`, `mcgill-quantum`, `vldb-quantum` |
| Performance and distributed systems projects | `ml-sustainability`, `mosaic-exchange`, `Paxos` |
| Education | `edu-nyu`, `edu-mcgill` |

In `scripts/build_resumes.py`, search `build_research`, `build_industry`, `build_ai_security`, `EDUCATION`, and `URLS` to find the relevant presentation and supporting links. Contact details appear in `header_story`.

## Preserve qualifications

- Check employment and education dates, publication venues and statuses, authorship, and numerical results in the current record. Distinguish accepted work, work under review, and ongoing evaluation.
- Keep benchmark results tied to the measured engine, workload, baseline, and conditions. An implementation alone does not establish a performance gain.
- Check detailed project status before using claims about production use, release readiness, user adoption, or validation. Citation checks in a legal-information application do not establish substantive legal accuracy.
- Respect statements such as helped develop, built a particular subsystem, joint first author, and co-author. Describe Daniel's contribution precisely.
- Use external papers and repositories linked from the portfolio when further detail is necessary; employer knowledge does not verify candidate experience.

The user's cover-letter requirements are encoded in `SKILL.md`: official employer research, verified personal evidence, concise natural writing, a separate cited explanation, and explicit separation of company statements from interpretations. A particular employer's research or an earlier letter is not a standing rule for future applications.
