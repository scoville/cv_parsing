# Japanese CV Parser
This PR is to implement test on Japanese cv parser created through Azure content understanding. 

To open `test_cv_parsing_speed_and_cost.ipynb`, 

1. please run command below to start Jupyter lab 
```bash
uv run --with jupyter jupyter lab
```
2. In Jupter lab, click `test_cv_parsing_speed_and_cost.ipynb`

To run `test_cv_parsing.py` to try cv parser,
1. please run below 
```bash 
uv run python test_cv_parsing.py
```

## Performance and cost comparsion among different version of Azure content understanding api

| api version | LLM | analyser id  | speed (per 2-page pdf) | cost (per 2-page pdf) | quality (per 2-page pdf)| speed (per 2-page docx) | cost (per 2-page docx) | quality (per 2-page docx)| speed (per 2-page xlsx) | cost (per 2-page xlsx) | quality (per 2-page xlsx)|
| :--- | :---: | :---: | ---: | :--- | :---: | ---: | :--- | :---: | ---: | :--- | :---: |
| 2025-11-01 | gpt-5 |cv_parser_test_lk | 22.5 s ± 1.05 s | $0.0357 | high | 12.7 s ± 98.6 ms | $0.021 | very low | 13.6 s ± 2.18 s |  $0.0231 | very low |
| 2026-06-01-preview | gpt-5|cv_parser_preview_api_2026_06_01| **19.9 s ± 1.52 s** | $0.0438 | high | 11 s ± 1.58 s | $0.0272 | high | 10.1 s ± 1.05 s | $0.029 | high |
| 2026-06-01-preview | gpt-5-mini |cv_parser_preview_api_2026_06_01_gpt5_mini| 20.8 s ± 4.34 s | $0.0213 | low | 13.7 s ± 1.34 s | $0.0072 | medium | 14.1 s ± 1.49 s | $0.0104 | medium |