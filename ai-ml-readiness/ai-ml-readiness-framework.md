# AI/ML Cloud Readiness Framework

**Version:** 2.0  
**Authors:** AI Architects — Microsoft, Google Cloud, AWS  
**Aligned To:** Microsoft AI Cloud · AWS Generative AI · Google Cloud Vertex AI

---

## Overview

This framework guides enterprise organizations through assessing, planning, and implementing **Artificial Intelligence (AI) and Machine Learning (ML)** workloads on cloud platforms. It covers traditional ML, MLOps, and **Generative AI (GenAI)** — including Large Language Models (LLMs) — across **Azure**, **AWS**, and **Google Cloud Platform**.

---

## AI/ML Readiness Assessment

### Dimension 1: Data Readiness

| # | Question | Score (1–5) |
|---|---|---|
| 1.1 | Is there a centralized data platform (data lake/lakehouse/warehouse) in place? | |
| 1.2 | Is data catalogued with metadata, lineage, and quality controls? | |
| 1.3 | Is PII/sensitive data identified and governed (masking, tokenization)? | |
| 1.4 | Are data pipelines automated and observable (ETL/ELT)? | |
| 1.5 | Is data accessible to AI/ML teams within defined governance boundaries? | |

### Dimension 2: Platform & Infrastructure Readiness

| # | Question | Score (1–5) |
|---|---|---|
| 2.1 | Is there a dedicated ML platform or workspace (Azure ML, SageMaker, Vertex AI)? | |
| 2.2 | Is GPU/accelerator compute available for model training? | |
| 2.3 | Is there a model registry and experiment tracking tool (MLflow, Vertex Experiments)? | |
| 2.4 | Are feature stores available for structured feature management? | |
| 2.5 | Is there a CI/CD pipeline adapted for ML model lifecycle (MLOps)? | |

### Dimension 3: Skills & Organization

| # | Question | Score (1–5) |
|---|---|---|
| 3.1 | Are data scientists, ML engineers, and AI product owners in place? | |
| 3.2 | Is there a responsible AI policy and ethics review process? | |
| 3.3 | Is there ML/AI literacy across business stakeholders? | |
| 3.4 | Are AI use cases prioritized and tied to business outcomes? | |

### Dimension 4: Governance & Responsible AI

| # | Question | Score (1–5) |
|---|---|---|
| 4.1 | Is there a Responsible AI framework (fairness, explainability, privacy)? | |
| 4.2 | Are AI models documented (model cards, training data provenance)? | |
| 4.3 | Is there a process for bias detection and mitigation? | |
| 4.4 | Are AI compliance requirements assessed (EU AI Act, NIST AI RMF)? | |

---

## Cloud AI/ML Platform Comparison

| Capability | Azure | AWS | Google Cloud |
|---|---|---|---|
| **ML Platform** | Azure Machine Learning | Amazon SageMaker | Vertex AI |
| **GenAI / LLM API** | Azure OpenAI Service (GPT-4, DALL-E) | Amazon Bedrock (Claude, Titan, Llama) | Vertex AI (Gemini Pro/Ultra) |
| **Foundation Model Access** | OpenAI GPT-4, Llama, Phi-3 | Anthropic Claude, Meta Llama, Amazon Titan | Google Gemini, PaLM, third-party via Vertex |
| **Notebook/IDE** | Azure ML Notebooks, VS Code | SageMaker Studio | Vertex AI Workbench, Colab Enterprise |
| **Feature Store** | Azure ML Feature Store | SageMaker Feature Store | Vertex AI Feature Store |
| **Model Registry** | Azure ML Model Registry | SageMaker Model Registry | Vertex AI Model Registry |
| **Training (GPU)** | NC/ND-series VMs (A100, H100) | P3, G4, P4de instances (A100, H100) | A2 (A100), A3 (H100) VMs |
| **Inference (Managed)** | Azure ML Managed Online Endpoints | SageMaker Real-Time Inference | Vertex AI Prediction |
| **Batch Inference** | Azure ML Batch Endpoints | SageMaker Batch Transform | Vertex AI Batch Prediction |
| **MLOps CI/CD** | Azure DevOps / GitHub Actions + Azure ML | CodePipeline / SageMaker Pipelines | Cloud Build + Vertex AI Pipelines |
| **Vector Search (RAG)** | Azure AI Search + Cognitive Search | Amazon OpenSearch (k-NN) + Kendra | Vertex AI Search / Matching Engine |
| **Data Processing (Scale)** | Azure Synapse, Databricks on Azure | AWS Glue, EMR, Databricks on AWS | Dataflow, Dataproc, Databricks on GCP |
| **BI / Analytics** | Power BI | Amazon QuickSight | Looker / Looker Studio |

---

## Generative AI (GenAI) Architecture Patterns

### Pattern 1: Retrieval-Augmented Generation (RAG)

The most common enterprise GenAI pattern — grounds LLM responses in proprietary data.

```
User Query
    │
    ▼
[Embedding Model] → [Vector Database] ← [Document Ingestion Pipeline]
                           │                   (Azure AI Search /
                           ▼                    AWS OpenSearch /
                    [Top-K Retrieval]            GCP Matching Engine)
                           │
                           ▼
               [LLM Prompt (Query + Context)] → [LLM API]
                                                     │
                                                     ▼
                                              [Grounded Response]
```

**Azure RAG Stack:** Azure OpenAI + Azure AI Search + Azure Blob Storage + Prompt Flow  
**AWS RAG Stack:** Amazon Bedrock + Amazon OpenSearch / Kendra + S3 + Bedrock Agents  
**GCP RAG Stack:** Vertex AI Gemini + Vertex AI Search + Cloud Storage + Agent Builder

### Pattern 2: Fine-Tuning

Custom-train a foundation model on proprietary data for domain-specific accuracy.

**When to Fine-Tune vs. RAG:**
- Use **RAG** when: information is dynamic, large corpus, factual Q&A, low latency acceptable
- Use **Fine-Tuning** when: specific tone/format, domain jargon, classification tasks, high-volume inference

**Fine-Tuning Tools:**
- Azure: Azure OpenAI fine-tuning (GPT-3.5-turbo, Ada), Azure ML + LoRA
- AWS: Amazon Bedrock fine-tuning (Claude, Titan), SageMaker JumpStart fine-tuning
- GCP: Vertex AI supervised fine-tuning (Gemini), Vertex AI model tuning

### Pattern 3: AI Agents & Agentic Workflows

LLMs equipped with tools (functions, APIs, databases) to autonomously complete multi-step tasks.

**Frameworks:**
- **LangChain / LangGraph** — Multi-step orchestration (all clouds)
- **Semantic Kernel** — Microsoft's SDK for AI orchestration (Azure-first)
- **Amazon Bedrock Agents** — Native agentic framework on AWS
- **Vertex AI Agent Builder** — Google's agent development platform
- **AutoGen** — Microsoft Research multi-agent framework

**Components:**
- LLM backbone (reasoning and planning)
- Tool calling (APIs, databases, code execution)
- Memory (short-term: context window; long-term: vector database)
- Orchestration layer (LangGraph, Semantic Kernel)

---

## MLOps Maturity Model

| Level | Description | Practices |
|---|---|---|
| **L0 – Manual** | Manual, script-based ML | Jupyter notebooks, no versioning, no CI/CD |
| **L1 – ML Pipeline Automation** | Automated training pipeline | ML pipelines, experiment tracking, model registry |
| **L2 – CI/CD for ML** | Continuous delivery of models | Automated retraining, A/B testing, canary deployments |
| **L3 – Full MLOps** | Continuous deployment + monitoring | Real-time monitoring, drift detection, auto-retraining |

**Target:** Enterprise production systems should achieve **L2 minimum**, targeting **L3** for critical AI workloads.

---

## Responsible AI Framework

### Microsoft Responsible AI Principles (Applied to All Clouds)

| Principle | Description | Implementation |
|---|---|---|
| **Fairness** | AI systems treat all people equitably | Bias testing (Fairlearn, What-If Tool) |
| **Reliability & Safety** | Systems perform safely and as intended | Model validation, testing, red-teaming |
| **Privacy & Security** | Protect people's data and privacy | Data minimization, differential privacy |
| **Inclusiveness** | Designed for all people | Accessibility testing, diverse training data |
| **Transparency** | Understandable and explainable decisions | SHAP, LIME, model cards |
| **Accountability** | Human oversight and governance | AI governance board, model cards, audit trails |

**Regulatory Compliance:**
- **EU AI Act** — Risk-based classification; high-risk AI requires conformity assessment
- **NIST AI RMF 1.0** — Govern, Map, Measure, Manage
- **ISO/IEC 42001** — AI Management Systems standard

---

## AI/ML Security Considerations

| Risk | Mitigation |
|---|---|
| **Prompt Injection** | Input validation, system prompt hardening, output filtering |
| **Data Poisoning** | Training data provenance, anomaly detection in training sets |
| **Model Exfiltration** | Access controls on model registry, API rate limiting, logging |
| **PII in Training Data** | Data scanning (Azure Purview, AWS Macie, GCP DLP) before training |
| **LLM Output Hallucination** | RAG grounding, human review for high-stakes outputs, confidence scoring |
| **Third-Party Model Risk** | Model provenance verification, private deployment (not shared API) |

---

## AI/ML Cloud Certification Path

| Role | Azure | AWS | GCP |
|---|---|---|---|
| AI Fundamentals | AI-900 | AWS Cloud Practitioner | Cloud Digital Leader |
| ML Engineer | DP-100 (Azure ML) | MLA-C01 | Professional ML Engineer |
| AI Engineer | AI-102 | AWS AI Practitioner | Professional ML Engineer |
| Data Engineer | DP-203 | DEA-C01 | Professional Data Engineer |

---

*See also: [Multi-Cloud Strategy](../frameworks/multi-cloud/multi-cloud-strategy.md) | [Security Framework](../security/security-compliance-framework.md) | [GCP Migration Guide](../frameworks/gcp/gcp-migration-guide.md)*
