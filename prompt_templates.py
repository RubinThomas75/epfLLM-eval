# Define the multiple-choice string template using string formatting
multiple_choice_template = """
Answer the following multiple-choice question. The last line of your response should be of the following format: 'Answer: $LETTER' (without quotes), where LETTER is one of A, B, C, or D. Think step by step before answering.

Example 1:
Q: What is the first-line treatment for hypertension?
A) Diuretics
B) Beta-blockers
C) ACE inhibitors
D) Calcium channel blockers
Answer: A

Example 2:
Q: What is the treatment for type 2 diabetes?
A) Insulin therapy
B) Metformin
C) Statins
D) Diuretics
Answer: B

Now, answer the following question:
{prompt}
Answer:
""".strip()
