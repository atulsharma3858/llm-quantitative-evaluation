
# LLM Quantitative Evaluation

## Overview
This project demonstrates a structured, evaluation-driven approach to assessing Large Language Model (LLM) outputs using reproducible prompt configurations.

The goal is to move beyond trial-and-error prompting and apply **quantitative evaluation metrics** to compare model behavior in an enterprise-style workflow.

---

## Problem Statement
Organizations increasingly rely on LLMs for decision-support tasks such as resume screening and job matching.  
However, LLM outputs must be **evaluated systematically** for relevance, consistency, and factual grounding.

This project evaluates LLM responses for **resume-to-job relevance scoring**.

---

## Methodology
- Prompt configurations are stored as version-controlled `.prompt.yml` files
- Each prompt defines:
  - Model parameters
  - System instructions
  - Test inputs
- Outputs are evaluated using quantitative criteria:
  - **Relevance**
  - **Groundedness**
  - **Consistency**

The workflow is designed to be compatible with **GitHub Models–style evaluation pipelines**.

---

## Prompt Configuration
Prompt files are located in the `prompts/` directory.

Example:
- `resume_matcher.prompt.yml`
  - Scores resume–job fit on a 0–100 scale
  - Identifies matching skills
  - Provides justification for the score

---

## Evaluation Metrics
- **Relevance**: Alignment between resume skills and job requirements
- **Groundedness**: Whether conclusions are supported by provided inputs
- **Consistency**: Stability of outputs across similar inputs

---

## Key Takeaways
- Prompt engineering should be treated as an **optimization problem**
- Quantitative metrics improve reliability and reproducibility
- Structured evaluation reduces risk when deploying LLMs in production workflows

---

## Future Work
- Compare multiple LLMs side-by-side
- Add batch test cases
- Export evaluation results for statistical analysis
