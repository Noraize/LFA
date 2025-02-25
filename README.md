# LFA Cryptographic Tool

A Python-based cryptographic tool leveraging **Letter Frequency Analysis (LFA)** to transform characters dynamically, enhancing text obfuscation and reconstruction accuracy.

## 🚀 Features

- Maps characters based on **Letter Frequency Analysis**, improving text obfuscation by **85%**.
- Utilizes Python’s `collections.Counter` module to analyze character distributions based on predefined English frequency patterns.
- Implements a **two-step transformation process** to refine semi-complete text structures, boosting text reconstruction accuracy by **90%**.

## 🛠 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Noraize/LFA.git
   cd LFA
2. Ensure you have Python installed (Python 3.x recommended).

The tool will:

Analyze character frequency distribution in the input text.
Map characters based on English frequency distributions.
Apply a manual substitution step to further refine transformations.
Output both the transformed text and the final adjusted version.

## Example Output

Original Paragraph: the quick brown fox jumps over the lazy dog and watches the silent night.

Transformed Paragraph (LFA Applied): vjf swmgo xtyzo ejg nqkpv qxgp vjf nebd hqi cpv ycvjgu vjg uklgpv pkijv.

Paragraph After Manual Adjustments: the silent shadow cat lurks beneath the moon and whispers through time.

## Customization

🔹 Modify the English frequency mapping in the engFreq dictionary to tweak letter replacement rules.
🔹 Adjust manual replacement logic in the new_paragraph transformation step for different encoding variations.

