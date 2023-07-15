# Find the Carnatic Parent Raga of a Child Raga

This project aims to find the parent of a given child raga based on the selected swaras.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)


## Introduction
In Indian classical music, ragas are melodic structures consisting of a set of swaras (musical notes). Each raga has a parent raga from which it is derived. This project helps in determining the parent raga of a given child raga by analyzing the selected swaras.

## Installation
Should be running on any python3  i used 3.11

Install the required dependencies:

```bash
pip install -r requirements.txt 
```
Run the Streamlit application:

```bash
streamlit run main.py
```

## Usage

1. Enter the name of the child raga in the text input field.
![rg1](https://github.com/Vriddhachalam/Raga_correlation/assets/26757681/f9ffa661-a845-4583-901e-de002e258590)
2. Select the swaras of the child raga from the provided options.
![rg2](https://github.com/Vriddhachalam/Raga_correlation/assets/26757681/a9f8679d-4e8a-416e-981e-8cb376700aa0)
3. Click on the "Generate Result" button to obtain the parent raga and other analysis results.
![image](https://github.com/Vriddhachalam/Raga_correlation/assets/26757681/d3800c14-2c95-4a3a-98ec-0e4c78c6f727)






## Results

After generating the results, the application displays the following:

- A dataframe showing the analysis results, including the parent raga and correlations between different ragas.
- A correlation heatmap visualizing the correlations between the child raga and other ragas.
- The correlation coefficient and p-value for the relationship between the child raga and each analyzed raga.


## Contributing
Contributions to this project are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

