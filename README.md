# NanoGPT + Math: Direct Preference Optimization

## Project Overview
This project aims to build a math training dataset and fine-tune a NanoGPT model to solve simple arithmetic problems with reasoning. We utilize **Direct Preference Optimization (DPO)** to align the model's outputs with a specific format and reasoning capability.

The goal is to teach the model to reply in the format:
> `PROMPT The answer is A because B is C`

Where:
- **PROMPT**: The arithmetic or algebraic question (e.g., `98/x=14,x=?`).
- **A**: The Answer.
- **B**: The Reasoning.
- **C**: The Answer (reconfirmed).

## Methodology
 The team settled on generating datasets with familiar mathematical patterns (e.g. multiply by 10, commutative property, etc.) this allows DPO to pick up patterns better, thus improving model's performance. 

The model is fine-tuned using the **AdamW** optimizer and **CosineAnnealingLR** scheduler.

No additional fine-tuning method was introduced, other then the DPO method provided by the assignment authors.

## Installation and Usage
1.  **Install Dependencies**:
    ```bash
    pip install matplotlib torch numpy transformers datasets tiktoken wandb tqdm
    ```

2.  **Pretrained Model**:
    Please download the pretrained NanoGPT model on QA data from the [link](https://drive.google.com/file/d/1gIZw-HAB-tHtEYCmNugwlIV7R3WsgjjZ/view?usp=sharing), and place it into the folder `./sft`!

3.  **Run the Project**:
    The main training and evaluation logic is contained within the Jupyter Notebooks in the `dpo/` directory (e.g., `dpo/dpo.ipynb`).