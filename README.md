## CRISPE: Semantic-Guided Execution Planning and Dynamic Reasoning for Enhancing Code Coverage Prediction

While LLMs excel in understanding source code and descriptive texts for tasks like code generation, code completion, etc., they exhibit weaknesses in predicting dynamic program behavior, such as code coverage and runtime error detection, which typically require program execution. Aiming to advance the capability of LLMs in reasoning and predicting the program behavior at runtime, we present CRISPE (short for Coverage Rationalization and Intelligent Selection ProcedurE), a novel approach for code coverage prediction that guides an LLM in simulating program execution via an execution plan based on two key factors: (1) program semantics of each statement type, and (2) the observation of current set of covered statements at the current “execution” step relative to all feasible code coverage options. We frame code coverage prediction as semantic-guided execution planning through the steps, using these feasible coverage options to determine whether the LLM is heading in the right direction. We enhance the traditional generative task with the retrieval-based framework on feasible options of code coverage. Our experiments on real-world data show that CRISPE achieves high
accuracy in code coverage prediction in both exact-match and statement-match coverage metrics, improving over the baseline approaches. We also show that with semantic-guiding and dynamic reasoning from CRISPE, the LLM generates more correct planning steps. To demonstrate CRISPE’s usefulness, we used it in the downstream task of predicting runtime error(s) for the given inputs of incomplete code snippets.

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
2. Add the necessary paths required for prompting with crispe in model/pipeline.py
3. Add the API keys and endpoints in model/gpt_interaction.py
4. Run the 'model/pipeline.py' file 
