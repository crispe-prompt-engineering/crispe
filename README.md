## CRISPE: Enhancing Code Coverage Prediction Through Semantic-Guided Execution Planning and Dynamic Reasoning

Given the limited time, developers often focus on executing only the highest quality test cases to ensure the most critical functionalities are tested. This includes 
prioritizing and executing test cases based on the source code or recent code changes – which further improves the efficiency of the testing process. However, executing
the code and computing the code coverage is resource-intensive and impossible - in cases where only code snippets are available (e.g., in server-side scenarios). Thus, we observe a need for predicting code coverage without actual execution. Such a process can also be leveraged to enable an efficient test-case prioritization. Current state-of-the-art code coverage prediction approaches are driven by learning execution semantics via pre-training, or utilizing the reasoning capabilities of large language models (LLMs). Yet, they still suffer from a low accuracy, mainly due to error propagation and inadequate reasoning about program semantics. In this paper, we present CRISPE (short for Coverage Rationalization and Intelligent Selection ProcedurE), a novel approach for code coverage prediction that guides an LLM in simulating program execution
via an execution plan based on two key factors: (1) program semantics of each statement type, and (2) the observation of current set of covered statements at the current “execution” step relative to all feasible code coverage options. Our experiments demonstrate that CRISPE achieves a high accuracy, with up to 54.54% in Exact-Match and 84.55% in Statement-Match metrics, outperforming the baselines by 7.26% and 33.69% higher in both metrics, respectively.

### Dataset
All data for reproducing the results is available in the final_dataset.json file.

The dataset for CRISPE has been tested on a subset derived from [FixExal](https://arxiv.org/abs/2206.07796)

### Folder Structure 
```

├── crispe
│   ├── model
│   │    ├──prompts
│   │    ├──gpt_interaction.py
│   │    ├──focc.py
│   │    ├──pipeline.py
│   ├── responses
│   │    ├──crispe_responses.json
│   │    ├──baseline_responses.json
│   ├── dataset.json
│   └── README.md
```

## Procedure to predict the code coverage for given target program using CRISPE

1. Clone the official github repository for CRISPE
```
git clone https://github.com/crispe-prompt-engineering/crispe
```
2. Add the necessary paths required for prompting woth crispe in model/pipeline.py
3. Add the API keys and endpoints in model/gpt_interaction.py
4. Run the 'model/pipeline.py' file 
