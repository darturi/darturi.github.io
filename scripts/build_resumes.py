from __future__ import annotations

import argparse
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


BLUE = colors.HexColor("#0057FF")
INK = colors.HexColor("#111111")
MUTED = colors.HexColor("#585858")
RULE = colors.HexColor("#A8A8A8")
PAGE_WIDTH, PAGE_HEIGHT = letter
LEFT = 0.55 * inch
RIGHT = 0.55 * inch
TOP = 0.38 * inch
BOTTOM = 0.32 * inch
CONTENT_WIDTH = PAGE_WIDTH - LEFT - RIGHT
STAMP = "October 2026"


URLS = {
    "email": "mailto:dar579@nyu.edu",
    "linkedin": "https://linkedin.com/in/daniel-aarao-reis-arturi",
    "github": "https://github.com/darturi",
    "fannagent_code": "https://github.com/darturi/FANN-Agent/tree/public-facing",
    "lea": "https://github.com/VIDA-NYU/Lea",
    "expmath": "https://www.darpa.mil/research/programs/expmath-exponential-mathematics",
    "em_paper": "https://arxiv.org/abs/2511.02022",
    "em_project": "https://darturi.github.io/shared-em-subspaces/",
    "em_code": "https://github.com/darturi/shared-em-subspaces",
    "graph_paper": "https://arxiv.org/abs/2603.12476",
    "graph_code": "https://github.com/sdbs-uni-p/trees-in-graphs",
    "quantum_paper": "https://www.vldb.org/2026/Workshops/VLDB-Workshops-2026/QCDKM/QCDKM26_7.pdf",
    "quantum_code": "https://github.com/DISLMcGill/EvaluatingAQuantumSolution",
    "energy_code": "https://github.com/darturi/ml-energy-efficiency",
    "energy_report": "https://github.com/darturi/ml-energy-efficiency/blob/main/paper/Profiling_and_Optimising_Energy_in_GFlowNet_Molecular_Generation.pdf",
    "housing_code": "https://github.com/darturi/nyc-housing-research",
    "paxos_code": "https://github.com/darturi/Paxos",
}


def link(label: str, key: str) -> str:
    return f'<link href="{URLS[key]}" color="#0057FF"><u>{label}</u></link>'


def styles(industry: bool = False) -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    body_size = 8.1 if industry else 8.3
    leading = 9.5 if industry else 9.9
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=22,
            alignment=TA_CENTER,
            textColor=INK,
            spaceAfter=3,
        ),
        "role": ParagraphStyle(
            "Role",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=12,
            alignment=TA_CENTER,
            textColor=INK,
            spaceAfter=2,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.2,
            leading=9.5,
            alignment=TA_CENTER,
            textColor=INK,
            spaceAfter=3,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.2,
            leading=11.5,
            textColor=INK,
            spaceBefore=4,
            spaceAfter=1,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=body_size,
            leading=leading,
            textColor=INK,
            spaceAfter=1.5,
        ),
        "body_tight": ParagraphStyle(
            "BodyTight",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=body_size,
            leading=leading,
            textColor=INK,
            spaceAfter=0.5,
        ),
        "org": ParagraphStyle(
            "Org",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.05 if industry else 9.3,
            leading=10.3,
            textColor=INK,
        ),
        "date": ParagraphStyle(
            "Date",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8.4,
            leading=10.3,
            alignment=TA_RIGHT,
            textColor=INK,
        ),
        "subhead": ParagraphStyle(
            "Subhead",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.3 if industry else 8.5,
            leading=9.4,
            textColor=MUTED,
            spaceAfter=1,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=body_size,
            leading=leading,
            leftIndent=12,
            firstLineIndent=-8,
            bulletIndent=1,
            textColor=INK,
            spaceAfter=1.2,
        ),
        "publication": ParagraphStyle(
            "Publication",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.2,
            leading=9.55,
            textColor=INK,
            spaceAfter=1,
        ),
        "note": ParagraphStyle(
            "Note",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.75,
            leading=8.9,
            leftIndent=13,
            textColor=MUTED,
            spaceAfter=2.2,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.75,
            leading=9.0,
            textColor=INK,
            spaceAfter=1,
        ),
    }


def section(title: str, s: dict[str, ParagraphStyle]) -> list:
    return [
        Spacer(1, 1.5),
        Paragraph(title, s["section"]),
        HRFlowable(width="100%", thickness=0.45, color=RULE, spaceBefore=0, spaceAfter=3),
    ]


def experience_entry(
    organization: str,
    date: str,
    subhead: str,
    bullets: list[str],
    s: dict[str, ParagraphStyle],
) -> KeepTogether:
    heading = Table(
        [[Paragraph(organization, s["org"]), Paragraph(date, s["date"])]],
        colWidths=[CONTENT_WIDTH - 120, 120],
        hAlign="LEFT",
    )
    heading.setStyle(
        TableStyle(
            [
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    contents = [heading, Paragraph(subhead, s["subhead"])]
    contents.extend(Paragraph(item, s["bullet"], bulletText="•") for item in bullets)
    contents.append(Spacer(1, 2))
    return KeepTogether(contents)


def header_story(role: str, s: dict[str, ParagraphStyle]) -> list:
    contact = (
        "New York, NY&nbsp;&nbsp;|&nbsp;&nbsp;+1 917-655-9244&nbsp;&nbsp;|&nbsp;&nbsp;"
        f'{link("dar579@nyu.edu", "email")}&nbsp;&nbsp;|&nbsp;&nbsp;'
        f'{link("LinkedIn", "linkedin")}&nbsp;&nbsp;|&nbsp;&nbsp;'
        f'{link("GitHub", "github")}&nbsp;&nbsp;|&nbsp;&nbsp;'
        f'{link("FANNAgent code", "fannagent_code")}'
    )
    return [
        Paragraph("Daniel Aarao Reis Arturi", s["name"]),
        Paragraph(role, s["role"]),
        Paragraph(contact, s["contact"]),
    ]


def later_header(canvas, document) -> None:
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.35)
    canvas.line(LEFT, PAGE_HEIGHT - 19, PAGE_WIDTH - RIGHT, PAGE_HEIGHT - 19)
    canvas.setFont("Helvetica", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(PAGE_WIDTH - RIGHT, PAGE_HEIGHT - 15, f"Daniel Aarao Reis Arturi  |  {STAMP}")
    canvas.restoreState()


def make_document(path: Path, title: str, subject: str, author_role: str) -> BaseDocTemplate:
    document = BaseDocTemplate(
        str(path),
        pagesize=letter,
        leftMargin=LEFT,
        rightMargin=RIGHT,
        topMargin=TOP,
        bottomMargin=BOTTOM,
        title=title,
        author="Daniel Aarao Reis Arturi",
        subject=subject,
        pageCompression=1,
    )
    frame = Frame(LEFT, BOTTOM, CONTENT_WIDTH, PAGE_HEIGHT - TOP - BOTTOM, id="content", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    def first_page(canvas, doc):
        canvas.setTitle(title)
        canvas.setAuthor("Daniel Aarao Reis Arturi")
        canvas.setSubject(subject)
        canvas.setKeywords(author_role)

    def later_page(canvas, doc):
        later_header(canvas, doc)

    document.addPageTemplates(
        [
            PageTemplate(id="First", frames=[frame], onPage=first_page, autoNextPageTemplate="Later"),
            PageTemplate(id="Later", frames=[frame], onPage=later_page),
        ]
    )
    return document


def build_research(path: Path) -> None:
    s = styles(industry=False)
    story = header_story("Research Scientist and Research Engineer", s)
    story += section("RESEARCH PROFILE", s)
    story += [
        Paragraph(
            "Research scientist and engineer building reproducible benchmarks, agentic systems, and experimental infrastructure for open-ended problems. Current work spans AI for mathematics, mechanistic interpretability, and LLM-guided stopping policies for filtered vector search.",
            s["body"],
        ),
        Paragraph(
            "<b>Research interests</b>&nbsp;&nbsp;AI for mathematics, agentic systems, database systems, query optimization, vector search, mechanistic interpretability, and reproducible evaluation",
            s["body_tight"],
        ),
    ]
    story += section("RESEARCH EXPERIENCE", s)
    story += [
        experience_entry(
            "NYU Tandon School of Engineering, VIDA Center",
            "May 2026-Present",
            f"<i>Research Scientist</i>&nbsp;&nbsp;|&nbsp;&nbsp;DARPA expMath&nbsp;&nbsp;|&nbsp;&nbsp;{link('Lea', 'lea')}&nbsp;&nbsp;|&nbsp;&nbsp;{link('Program', 'expmath')}",
            [
                "Helped develop Lea, an open-source platform for mathematician-controlled formalization that supports proof decomposition, mid-run intervention, trajectory inspection, manual correction, and auditable Lean 4 output.",
                "Worked on the agentic harness and its research infrastructure, integrating project-aware execution, configurable sub-agent roles, Lean checking, typed event streams, persistent proof history, and shared state across standalone and Overleaf clients.",
                "Built the React/Vite/TypeScript and FastAPI research interface and developed the Overleaf-to-Lean workflow, including dependency-aware formalization, counterexample handling, self-repair, theorem-specific review, and GitHub export.",
                "First-authored the Lea paper accepted to the Sixth Workshop on Mathematical Reasoning and AI at NeurIPS 2026; contributed related-work synthesis, research framing, architecture documentation, case-study analysis, and technical writing.",
            ],
            s,
        ),
        experience_entry(
            "New York University, Courant Institute of Mathematical Sciences",
            "Sep 2026-Present",
            "<i>Independent Study Researcher</i>&nbsp;&nbsp;|&nbsp;&nbsp;Filtered Vector Search&nbsp;&nbsp;|&nbsp;&nbsp;Advisor: Prof. Jinyang Li",
            [
                f"Developed {link('FANNAgent', 'fannagent_code')}, an offline LLM-guided system for workload-specific early stopping in filtered approximate nearest-neighbor search; implemented bounded policies inside pgvector's HNSW search without query-time model calls.",
                "Built FANNBench across PostgreSQL/pgvector, Elasticsearch/Lucene, and Weaviate, with exact filtered top-<i>k</i> references and native instrumentation separating search, feature-collection, and policy-execution costs.",
                "Measured 59.7-62.0% lower mean latency than native pgvector for an agent-generated policy on 300 development query-filter cases, with 95% mean Recall@10 versus 99% for the baseline.",
            ],
            s,
        ),
        experience_entry(
            "Algoverse AI Research",
            "Apr 2025-Present",
            f"<i>Research Intern</i>&nbsp;&nbsp;|&nbsp;&nbsp;AI Safety and Mechanistic Interpretability&nbsp;&nbsp;|&nbsp;&nbsp;{link('Workshop paper', 'em_paper')}&nbsp;&nbsp;|&nbsp;&nbsp;{link('Project', 'em_project')}&nbsp;&nbsp;|&nbsp;&nbsp;{link('Code', 'em_code')}",
            [
                "Characterized shared parameter subspaces and cross-task linear mode connectivity in LoRA-adapted Qwen2.5-7B and Llama 3.1-8B models; interpolations retained misaligned behavior while preserving more than 90% coherence.",
                "Compared harmful and matched benign fine-tunes across data-generation conditions, showing that shared parameter geometry can reflect template provenance rather than misalignment alone; tested robustness across LoRA ranks and model sizes.",
                "Evaluated post-hoc negation and orthonormal projection, finding better reasoning retention with projection in the tested mixed-data settings; contributed to the full-length manuscript under review at ICLR 2027.",
                "Joint first author of the NeurIPS 2025 workshop paper; a separate ongoing project studies how multi-thousand-turn conversations and persistent memory affect model persona stability.",
            ],
            s,
        ),
        experience_entry(
            "McGill University and University of Passau",
            "Aug 2025-Mar 2026",
            f"<i>Research Intern</i>&nbsp;&nbsp;|&nbsp;&nbsp;Graph Database Systems&nbsp;&nbsp;|&nbsp;&nbsp;{link('Artifact', 'graph_code')}&nbsp;&nbsp;|&nbsp;&nbsp;{link('Earlier preprint', 'graph_paper')}",
            [
                "Adapted Dewey and PrePost structural indexes to tree-shaped property-graph data and evaluated baseline traversal and indexed variants across Apache AGE, Kuzu, and Neo4j using 100,000-node synthetic trees and LDBC SNB workloads.",
                "Measured 6.7x to more than 300,000x microbenchmark speedups and 1.1x to 16x gains on three LDBC queries in AGE, while documenting mixed results in native graph engines and index-maintenance costs; released a Dockerized reproducibility artifact and co-authored the vision paper accepted to the EDBT 2027 Research Track.",
            ],
            s,
        ),
        experience_entry(
            "McGill University, Distributed Information Systems Group",
            "Jan-Jun 2026",
            f"<i>Research Intern</i>&nbsp;&nbsp;|&nbsp;&nbsp;Quantum Computing for Data Systems&nbsp;&nbsp;|&nbsp;&nbsp;{link('Paper', 'quantum_paper')}&nbsp;&nbsp;|&nbsp;&nbsp;{link('Artifact', 'quantum_code')}",
            [
                "Formulated fault-tolerant distributed data allocation through binary-slack, calibrated unbalanced-penalty, and domain-wall QUBO encodings, with exact ILP and brute-force oracles for feasibility and optimality checks.",
                "Evaluated D-Wave simulated annealing, hybrid CQM, Advantage hardware, and QAOA while separating QPU time from end-to-end cloud overhead. The study found no quantum advantage, mapped current scaling barriers, and produced a first-author workshop paper accepted at VLDB 2026 QC&amp;DKM and delivered as an oral presentation.",
            ],
            s,
        ),
        PageBreak(),
    ]

    story += section("PUBLICATIONS AND MANUSCRIPTS", s)
    story += [
        Paragraph(
            f'<i>Lea: An Agent Backbone for Mathematician-Controlled Formalization in Lean</i><br/><b>Daniel Aarao Reis Arturi</b>, Shaswat Patel, Kevin Gomez, Jaume de Dios Pont, Jorge Poco, Eduardo V. Teixeira, Sam Westrick, Claudio Silva, and Chinmay Hegde. Accepted to the Sixth Workshop on Mathematical Reasoning and AI (MATH-AI), NeurIPS 2026. First author. &nbsp;{link("[Code]", "lea")}',
            s["publication"],
        ),
        Paragraph(
            "Open-source Lean formalization backbone shared by LeaChat and LeaOverleaf, with a case study formalizing the Durfee square generating function under a mathematician's guidance.",
            s["note"],
        ),
        Paragraph(
            f'<i>Seeing the Trees for the Forest: Leveraging Tree-Shaped Substructures in Property Graphs</i><br/>Accepted to the EDBT 2027 Research Track. <b>Co-author.</b> &nbsp;{link("[Artifact]", "graph_code")}&nbsp;&nbsp;{link("[Earlier preprint]", "graph_paper")}',
            s["publication"],
        ),
        Paragraph(
            "Implemented and benchmarked structural indexes across Apache AGE, Kuzu, and Neo4j and built the Dockerized reproducibility artifact. Selected for the 2026 McGill Science Undergraduate Research Showcase.",
            s["note"],
        ),
        Paragraph(
            '<i>Shared Parametric Geometry and Data Provenance in Model Organisms for Emergent Misalignment</i><br/>2026. Full-length manuscript under review at ICLR 2027.',
            s["publication"],
        ),
        Paragraph(
            "Extends the NeurIPS 2025 workshop work with robustness analyses, matched benign controls, data-provenance experiments, and post-hoc interventions evaluated for alignment and reasoning retention.",
            s["note"],
        ),
        Paragraph(
            f'<i>{link("Shared Parameter Subspaces and Cross-Task Linearity in Emergently Misaligned Behavior", "em_paper")}</i><br/><b>Daniel Aarao Reis Arturi*</b>, Eric Zhang*, Andrew Ansah, Kevin Zhu, Ashwinee Panda, and Aishwarya Balwani. Accepted to NeurIPS 2025 workshops. arXiv:2511.02022, 2025. Joint first author. &nbsp;{link("[Project]", "em_project")}&nbsp;&nbsp;{link("[Code]", "em_code")}',
            s["publication"],
        ),
        Paragraph(
            "* Joint first authors with equal contributions; joint first authors listed alphabetically.",
            s["note"],
        ),
        Paragraph(
            f'<i>{link("Evaluating a Quantum Solution: How hard can it be?", "quantum_paper")}</i><br/><b>Daniel Aarao Reis Arturi</b>, Emilie Fahber, Stefanie Scherzinger, and Bettina Kemme. Accepted at the 2nd Workshop on Quantum Computing and Data/Knowledge Management, VLDB 2026. First author and oral presenter. &nbsp;{link("[Artifact]", "quantum_code")}',
            s["publication"],
        ),
        Paragraph(
            "Experience report and reproducibility artifact covering QUBO formulation, simulators, hybrid solvers, D-Wave Advantage hardware, QAOA, classical baselines, and practical scaling limits.",
            s["note"],
        ),
    ]

    story += section("SELECTED RESEARCH SYSTEMS AND STUDIES", s)
    story += [
        experience_entry(
            "Profiling and Optimising Energy Efficiency in GFlowNet Molecular Generation",
            "",
            f"<i>Python, PyTorch, CUDA, CodeCarbon, Slurm</i>&nbsp;&nbsp;{link('[Code]', 'energy_code')}&nbsp;&nbsp;{link('[Report]', 'energy_report')}",
            [
                "Instrumented a ~600M-parameter GraphTransformerGFN with timing-only, CodeCarbon, and CUDA-synchronized measurement modes at less than 0.2% overhead; found molecular sampling consumed 94.4% of step time while GPU utilization remained below 13%.",
                "Parallel sampling with four workers improved throughput about 1.9x and reduced total energy use by approximately 47%; automated Slurm sweeps covered batch sizes 64, 128, and 256 across three seeds and all measurement modes.",
            ],
            s,
        ),
        experience_entry(
            "NYC Housing Research",
            "",
            f"<i>Python, FastAPI, SQLite, retrieval and evaluation</i>&nbsp;&nbsp;{link('[Code]', 'housing_code')}",
            [
                "Built a local-first cited research system over official NYC legal sources, separating keyless citation search from optional semantic indexing and evidence-cited generation while preserving source versions, provenance, explicit coverage gaps, and per-resource provider consent.",
                "Developed retrieval and answer-evaluation infrastructure, citation-support checks, report-bound human-review workflows, explicit provider-cost approvals, and documented gates separating software regression evidence from substantive housing-law review.",
            ],
            s,
        ),
    ]

    story += section("EDUCATION", s)
    story += [
        Paragraph("<b>New York University, Courant Institute of Mathematical Sciences</b>&nbsp;&nbsp;|&nbsp;&nbsp;M.S. Computer Science&nbsp;&nbsp;|&nbsp;&nbsp;Fall 2026-Present", s["body_tight"]),
        Paragraph("<b>McGill University</b>&nbsp;&nbsp;|&nbsp;&nbsp;B.Sc. Honours Software Engineering&nbsp;&nbsp;|&nbsp;&nbsp;May 2026&nbsp;&nbsp;|&nbsp;&nbsp;GPA 3.99/4.0&nbsp;&nbsp;|&nbsp;&nbsp;First Class Honours", s["body_tight"]),
        Paragraph("<b>Selected coursework</b>&nbsp;&nbsp;Graduate Distributed Systems, Graduate Applied ML, Graduate Computer Networks, Sustainability for ML, Algorithms, Operating Systems, Database Systems, Probability and Statistics", s["body"]),
    ]

    story += section("AWARDS AND RECOGNITION", s)
    story += [
        Paragraph("<b>NeurIPS 2026 MATH-AI</b>&nbsp;&nbsp;Workshop Paper Acceptance&nbsp;&nbsp;|&nbsp;&nbsp;First Author", s["body_tight"]),
        Paragraph("<b>NeurIPS 2025 workshops</b>&nbsp;&nbsp;UniReps - Oral Presentation + Honorable Mention&nbsp;&nbsp;|&nbsp;&nbsp;MechInterp - Spotlight&nbsp;&nbsp;|&nbsp;&nbsp;CogInterp - Poster Acceptance", s["body_tight"]),
        Paragraph("<b>VLDB 2026 QC&amp;DKM</b>&nbsp;&nbsp;Workshop Paper Acceptance&nbsp;&nbsp;|&nbsp;&nbsp;First-Author Oral Presentation", s["body_tight"]),
        Paragraph("McGill Science Undergraduate Research Showcase (2026)&nbsp;&nbsp;|&nbsp;&nbsp;Wing Hing Chan Scholarship in Science&nbsp;&nbsp;|&nbsp;&nbsp;Algoverse Merit Scholarship (twice)&nbsp;&nbsp;|&nbsp;&nbsp;McGill Dean's Honour List", s["body"]),
    ]

    story += section("RESEARCH METHODS AND TECHNICAL SKILLS", s)
    story += [
        Paragraph("<b>Methods</b>&nbsp;&nbsp;Experimental design, benchmark design, reproducible evaluation, filtered-ANN evaluation, query optimization, performance instrumentation, exact-oracle validation, mechanistic interpretability, parameter-subspace analysis, linear mode connectivity, data-provenance analysis, intervention evaluation, QUBO, statistical analysis", s["small"]),
        Paragraph("<b>Research stack</b>&nbsp;&nbsp;Python, PyTorch, Transformers, NumPy, pandas, scikit-learn, Jupyter, CUDA, Slurm, CodeCarbon, D-Wave Ocean, Qiskit Aer", s["small"]),
        Paragraph("<b>Systems</b>&nbsp;&nbsp;Lean 4, Mathlib, FastAPI, React, TypeScript, SQLite, PostgreSQL, pgvector, Elasticsearch/Lucene, Weaviate, Docker, Git, Apache AGE, Kuzu, Neo4j", s["small"]),
    ]

    document = make_document(
        path,
        f"Daniel Aarao Reis Arturi Research Resume {STAMP}",
        "Research resume for research scientist and research engineering roles",
        "research scientist research engineer agentic systems database systems query optimization",
    )
    document.build(story)


def build_ai_security(path: Path) -> None:
    s = styles(industry=False)
    story = header_story("AI Safety and Agent Security Researcher", s)
    story += section("RESEARCH PROFILE", s)
    story += [
        Paragraph(
            "AI-safety researcher and agent-systems engineer who builds reproducible evaluation harnesses, instruments long-horizon agent behavior, and publishes empirical findings. Experience spans emergent misalignment, intervention evaluation, multi-agent orchestration, persistent memory, tool integration, and auditable human-in-the-loop systems.",
            s["body"],
        ),
        Paragraph(
            "<b>Research interests</b>&nbsp;&nbsp;AI agent security, adversarial-behavior evaluation, agent guardrails, memory and context integrity, mechanistic interpretability, threat modeling, and reproducible evaluation",
            s["body_tight"],
        ),
    ]

    story += section("RELEVANT RESEARCH EXPERIENCE", s)
    story += [
        experience_entry(
            "Algoverse AI Research",
            "Apr 2025-Present",
            f"<i>Research Intern</i>&nbsp;&nbsp;|&nbsp;&nbsp;AI Safety and Mechanistic Interpretability&nbsp;&nbsp;|&nbsp;&nbsp;{link('Paper', 'em_paper')}&nbsp;&nbsp;|&nbsp;&nbsp;{link('Project', 'em_project')}&nbsp;&nbsp;|&nbsp;&nbsp;{link('Code', 'em_code')}",
            [
                "Studied emergent misalignment in LoRA-adapted Qwen2.5-7B and Llama 3.1-8B models across narrowly harmful tasks, finding shared parameter subspaces with mean principal angles near 20 degrees versus an approximately 85-degree random baseline and projection overlap near 0.8.",
                "Built reproducible fine-tuning and behavioral evaluation pipelines, then used linear mode connectivity to test functional equivalence across independently trained models; cross-task interpolations retained misaligned behavior while preserving more than 90% coherence.",
                "Extended the work to post-hoc and during-training interventions, measuring mitigation alongside GSM8K capability retention, and began a separate study of how multi-thousand-turn conversations and persistent memory affect model persona stability.",
                "Co-authored the resulting NeurIPS 2025 workshop paper as a joint first author; the work received a UniReps oral award, a MechInterp honourable mention, and a CogInterp poster acceptance.",
            ],
            s,
        ),
        experience_entry(
            "NYU Tandon School of Engineering, VIDA Center",
            "May 2026-Present",
            f"<i>Research Scientist</i>&nbsp;&nbsp;|&nbsp;&nbsp;DARPA expMath&nbsp;&nbsp;|&nbsp;&nbsp;{link('Lea', 'lea')}&nbsp;&nbsp;|&nbsp;&nbsp;{link('Program', 'expmath')}",
            [
                "Helped develop Lea, an open-source agent platform for mathematician-controlled formalization with proof decomposition, bounded sub-agent roles, mid-run intervention, trajectory inspection, manual correction, and auditable Lean 4 output.",
                "Worked on the project-aware agent harness and its research infrastructure, integrating tool and skill access, MCP servers, Lean checking, typed event streams, persistent proof history, and shared state across standalone and Overleaf clients.",
                "Developed review and recovery workflows around agent failures, including dependency-aware execution, counterexample handling, theorem-specific review, self-repair, resumable sessions, and GitHub export.",
                "Contributed to long-horizon agent evaluations, related-work synthesis, architecture documentation, case-study analysis, and the human-in-the-loop research framing; GitHub listed me as Lea's leading public contributor with 144 contributions in September 2026.",
            ],
            s,
        ),
    ]

    story += section("SELECTED SECURITY-MINDED SYSTEM", s)
    story += [
        experience_entry(
            "NYC Housing Research",
            "",
            f"<i>Python, FastAPI, SQLite, retrieval and evaluation</i>&nbsp;&nbsp;{link('[Code]', 'housing_code')}",
            [
                "Built a local-first cited research system over official NYC legal sources with source provenance, explicit coverage gaps, report-bound human review, citation-support checks, and controls separating keyless retrieval from optional semantic indexing and generation.",
                "Implemented dual authentication paths, row-level access controls, provider-cost approvals, backup and recovery workflows, and automated regression coverage spanning ingestion, retrieval, security, migration, desktop, and browser behavior.",
            ],
            s,
        ),
    ]

    story += section("PUBLICATIONS AND MANUSCRIPTS", s)
    story += [
        Paragraph(
            f'<b>Daniel Aarao Reis Arturi*</b>, Eric Zhang*, Andrew Ansah, Kevin Zhu, Ashwinee Panda, and Aishwarya Balwani. <i>{link("Shared Parameter Subspaces and Cross-Task Linearity in Emergently Misaligned Behavior", "em_paper")}</i>. arXiv:2511.02022, 2025. Joint first author. &nbsp;{link("[Project]", "em_project")}&nbsp;&nbsp;{link("[Code]", "em_code")}',
            s["publication"],
        ),
        Paragraph(
            "* Joint first authors with equal contributions; authors listed alphabetically. Expanded manuscript: <i>Of Basins and Vaccines: Emergent Misalignment Through the Lens of Parametric Geometry</i> (ICLR submission).",
            s["note"],
        ),
        Paragraph(
            f'<b>Daniel Aarao Reis Arturi</b>, Christoph Köhnen, George Fletcher, Bettina Kemme, and Stefanie Scherzinger. <i>{link("Seeing the Trees for the Forest: Leveraging Tree-Shaped Substructures in Property Graphs", "graph_paper")}</i>. arXiv:2603.12476, 2026. Under review at EDBT 2027. &nbsp;{link("[Artifact]", "graph_code")}',
            s["publication"],
        ),
        Paragraph(
            f'<b>Daniel Aarao Reis Arturi</b>, Emilie Fahber, Stefanie Scherzinger, and Bettina Kemme. <i>{link("Evaluating a Quantum Solution: How hard can it be?", "quantum_paper")}</i>. 2nd Workshop on Quantum Computing and Data/Knowledge Management, VLDB 2026. First author and oral presenter. &nbsp;{link("[Artifact]", "quantum_code")}',
            s["publication"],
        ),
    ]

    story += section("EDUCATION", s)
    story += [
        Paragraph("<b>New York University, Courant Institute of Mathematical Sciences</b>&nbsp;&nbsp;|&nbsp;&nbsp;M.S. Computer Science&nbsp;&nbsp;|&nbsp;&nbsp;Fall 2026-Present", s["body_tight"]),
        Paragraph("<b>McGill University</b>&nbsp;&nbsp;|&nbsp;&nbsp;B.Sc. Honours Software Engineering&nbsp;&nbsp;|&nbsp;&nbsp;May 2026&nbsp;&nbsp;|&nbsp;&nbsp;GPA 3.99/4.0&nbsp;&nbsp;|&nbsp;&nbsp;First Class Honours", s["body"]),
    ]

    story += section("RESEARCH METHODS AND TECHNICAL SKILLS", s)
    story += [
        Paragraph("<b>AI safety and evaluation</b>&nbsp;&nbsp;Adversarial-behavior evaluation, intervention evaluation, long-horizon agent analysis, mechanistic interpretability, parameter-subspace analysis, linear mode connectivity, exact-oracle validation, statistical analysis, technical writing", s["small"]),
        Paragraph("<b>Agents and ML</b>&nbsp;&nbsp;Python, PyTorch, Transformers, LoRA/PEFT, NumPy, pandas, scikit-learn, agent orchestration, MCP integration, persistent memory, tool-use instrumentation, Jupyter, CUDA, Slurm", s["small"]),
        Paragraph("<b>Systems</b>&nbsp;&nbsp;Lean 4, Mathlib, FastAPI, React, TypeScript, Node.js, SQLite, PostgreSQL, Docker, Git, GitHub Actions, Linux", s["small"]),
    ]

    document = make_document(
        path,
        f"Daniel Aarao Reis Arturi AI Security Research Resume {STAMP}",
        "Tailored resume for AI safety and agent security research internships",
        "AI safety agent security researcher evaluation harnesses guardrails threat modeling",
    )
    document.build(story)


def build_industry(path: Path) -> None:
    s = styles(industry=True)
    story = header_story("Research Engineer and Software Engineer", s)
    story += section("PROFESSIONAL SUMMARY", s)
    story += [
        Paragraph(
            "Research engineer and software engineer building agentic systems, cross-system benchmarks, and production-minded research infrastructure. Experience spanning LLM agents, filtered vector search, stopping-policy synthesis, full-stack systems, and reproducible performance evaluation.",
            s["body"],
        )
    ]
    story += section("EXPERIENCE", s)
    story += [
        experience_entry(
            "NYU Tandon School of Engineering, VIDA Center",
            "May 2026-Present",
            f"<i>Research Scientist</i>&nbsp;&nbsp;|&nbsp;&nbsp;Agentic Systems and Research Infrastructure&nbsp;&nbsp;|&nbsp;&nbsp;{link('Lea', 'lea')}",
            [
                "Developed Lea's project-aware agent harness with configurable sub-agents, Lean checking, and persistent proof history; first-author paper accepted to NeurIPS 2026 MATH-AI.",
                "Built the React/Vite/TypeScript client and Python/FastAPI/SQLite backend path, including typed server-sent events, live proof updates, shared state, usage tracking, and spend controls.",
                "Developed the Overleaf-to-Lean workflow across a Chrome extension and local Node.js companion, including dependency parsing, inline progress, manual review, counterexample handling, self-repair, and GitHub export.",
            ],
            s,
        ),
        experience_entry(
            "New York University, Courant Institute of Mathematical Sciences",
            "Sep 2026-Present",
            "<i>Independent Study Researcher</i>&nbsp;&nbsp;|&nbsp;&nbsp;Filtered Vector Search&nbsp;&nbsp;|&nbsp;&nbsp;Advisor: Prof. Jinyang Li",
            [
                f"Developed {link('FANNAgent', 'fannagent_code')}, an offline LLM-guided system for workload-specific early stopping in filtered approximate nearest-neighbor search; implemented bounded policies inside pgvector's HNSW search without query-time model calls.",
                "Built FANNBench across PostgreSQL/pgvector, Elasticsearch/Lucene, and Weaviate, with exact filtered top-<i>k</i> references and native instrumentation separating search, feature-collection, and policy-execution costs.",
                "Measured 59.7-62.0% lower mean latency than native pgvector for an agent-generated policy on 300 development query-filter cases, with 95% mean Recall@10 versus 99% for the baseline.",
            ],
            s,
        ),
        experience_entry(
            "McGill University and University of Passau",
            "Aug 2025-Mar 2026",
            f"<i>Research Intern</i>&nbsp;&nbsp;|&nbsp;&nbsp;Graph Database Systems&nbsp;&nbsp;|&nbsp;&nbsp;{link('Artifact', 'graph_code')}&nbsp;&nbsp;|&nbsp;&nbsp;{link('Earlier preprint', 'graph_paper')}",
            [
                "Implemented Dewey and PrePost structural indexes for tree-shaped property-graph data and built a Dockerized benchmark across Apache AGE, Kuzu, and Neo4j using 100,000-node synthetic trees and LDBC SNB workloads.",
                "Measured 6.7x to more than 300,000x microbenchmark speedups and 1.1x to 16x gains on three LDBC queries in AGE, documenting mixed native-engine results and index-maintenance costs; co-authored the accepted EDBT 2027 vision paper.",
            ],
            s,
        ),
        experience_entry(
            "McGill University, Distributed Information Systems Group",
            "Jan-Jun 2026",
            f"<i>Research Intern</i>&nbsp;&nbsp;|&nbsp;&nbsp;Quantum Computing for Data Systems&nbsp;&nbsp;|&nbsp;&nbsp;{link('Paper', 'quantum_paper')}&nbsp;&nbsp;|&nbsp;&nbsp;{link('Artifact', 'quantum_code')}",
            [
                "Built a reproducible benchmark for distributed data allocation across exact ILP and brute-force oracles, D-Wave simulated annealing, hybrid CQM, Advantage hardware, and QAOA.",
                "Implemented resumable experiment runners and analysis-ready metrics for validity, constraint violations, optimality gap, embedding size, chain breaks, and timing while separating QPU access time from end-to-end cloud latency; the resulting first-author paper was accepted at VLDB 2026 QC&amp;DKM and delivered as an oral presentation.",
            ],
            s,
        ),
        experience_entry(
            "Algoverse AI Research",
            "Apr 2025-Present",
            f"<i>Research Intern</i>&nbsp;&nbsp;|&nbsp;&nbsp;AI Safety and Mechanistic Interpretability&nbsp;&nbsp;|&nbsp;&nbsp;{link('Workshop paper', 'em_paper')}&nbsp;&nbsp;|&nbsp;&nbsp;{link('Code', 'em_code')}",
            [
                "Analyzed LoRA-adapted Qwen2.5-7B and Llama 3.1-8B models using PyTorch, parameter-subspace analysis, and linear mode connectivity.",
                "Built fine-tuning and evaluation pipelines for matched benign controls, data provenance, and post-hoc interventions; contributed to a full-length manuscript under review at ICLR 2027.",
            ],
            s,
        ),
    ]

    story += section("SELECTED ENGINEERING PROJECTS", s)
    story += [
        experience_entry(
            "NYC Housing Research",
            "",
            f"<i>Python, FastAPI, SQLite, local-first software, macOS</i>&nbsp;&nbsp;|&nbsp;&nbsp;{link('[Code]', 'housing_code')}",
            [
                "Built a local-first legal research application over official NYC housing sources with full-text and semantic retrieval, evidence-cited answers, provider-cost controls, resilient backup and upgrade recovery, and a self-contained macOS desktop build.",
            ],
            s,
        ),
        experience_entry(
            "Paxos Treasure Island",
            "",
            f"<i>Java, Paxos, UDP, distributed systems</i>&nbsp;&nbsp;|&nbsp;&nbsp;{link('[Code]', 'paxos_code')}",
            [
                "Implemented single-decree Paxos over UDP for total-order broadcast, with concurrent proposer handling, six crash-injection points, scripted consensus verification, and an interactive protocol-trace visualizer.",
            ],
            s,
        ),
    ]

    story += section("SELECTED RESEARCH OUTPUT", s)
    story += [
        Paragraph(
            f'<b>NeurIPS 2026 MATH-AI</b>: accepted Lea paper, first author&nbsp;&nbsp;|&nbsp;&nbsp;<b>EDBT 2027</b>: accepted paper, co-author&nbsp;&nbsp;|&nbsp;&nbsp;<b>ICLR 2027</b>: full-length manuscript under review&nbsp;&nbsp;|&nbsp;&nbsp;<b>NeurIPS 2025 workshops</b>: {link("joint-first-author paper", "em_paper")}, UniReps oral + honorable mention, MechInterp spotlight&nbsp;&nbsp;|&nbsp;&nbsp;<b>VLDB 2026 QC&amp;DKM</b>: {link("accepted paper", "quantum_paper")}, first author and oral presenter',
            s["small"],
        )
    ]

    story += section("EDUCATION", s)
    story += [
        Paragraph("<b>New York University, Courant Institute of Mathematical Sciences</b>&nbsp;&nbsp;|&nbsp;&nbsp;M.S. Computer Science&nbsp;&nbsp;|&nbsp;&nbsp;Fall 2026-Present", s["body_tight"]),
        Paragraph("<b>McGill University</b>&nbsp;&nbsp;|&nbsp;&nbsp;B.Sc. Honours Software Engineering&nbsp;&nbsp;|&nbsp;&nbsp;May 2026&nbsp;&nbsp;|&nbsp;&nbsp;GPA 3.99/4.0&nbsp;&nbsp;|&nbsp;&nbsp;First Class Honours", s["body"]),
    ]

    story += section("TECHNICAL SKILLS", s)
    story += [
        Paragraph("<b>Languages</b>&nbsp;&nbsp;Python, Java, C/C++, SQL, TypeScript, JavaScript, Bash, Swift, Lean", s["small"]),
        Paragraph("<b>Agents and ML</b>&nbsp;&nbsp;PyTorch, Transformers, LoRA/PEFT, agent orchestration, LLM tooling, evaluation", s["small"]),
        Paragraph("<b>Data and search</b>&nbsp;&nbsp;PostgreSQL, pgvector, Elasticsearch/Lucene, Weaviate, HNSW, SQLite, Apache AGE, Kuzu, Neo4j", s["small"]),
        Paragraph("<b>Infrastructure</b>&nbsp;&nbsp;FastAPI, React, Docker, Git, GitHub Actions, Linux, Slurm, Jupyter", s["small"]),
    ]

    document = make_document(
        path,
        f"Daniel Aarao Reis Arturi Industry Resume {STAMP}",
        "Industry resume for research engineering and software engineering roles",
        "research engineer software engineer agentic systems LLM agents database systems query optimization",
    )
    document.build(story)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Daniel Aarao Reis Arturi's research, industry, and AI security resume PDFs.")
    parser.add_argument("--output-dir", type=Path, default=Path.cwd())
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    build_research(args.output_dir / "resume.pdf")
    build_industry(args.output_dir / "resume-industry.pdf")
    build_ai_security(args.output_dir / "resume-ai-security.pdf")


if __name__ == "__main__":
    main()
