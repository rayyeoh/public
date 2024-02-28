import re
import pandas as pd
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig

tokenizer = AutoTokenizer.from_pretrained("gtfintechlab/FOMC-RoBERTa", do_lower_case=True, do_basic_tokenize=True)
model = AutoModelForSequenceClassification.from_pretrained("gtfintechlab/FOMC-RoBERTa", num_labels=3)
config = AutoConfig.from_pretrained("gtfintechlab/FOMC-RoBERTa")
classifier = pipeline('text-classification', model=model, tokenizer=tokenizer, config=config, framework="pt")

def get_hawkish_dovish_classification(results):
	if results['label'] == 'LABEL_0':
		return 'Dovish'
	elif results['label'] == 'LABEL_1':
		return 'Hawkish'
	elif results['label'] == 'LABEL_2':
		return 'Neutral'

# This is the text release of the Jan 31, 2024 FOMC statement
# Source: https://www.federalreserve.gov/newsevents/pressreleases/monetary20240131a.htm
statement = """Recent indicators suggest that economic activity has been expanding at a solid pace. Job gains have moderated since early last year but remain strong, and the unemployment rate has remained low. Inflation has eased over the past year but remains elevated.
The Committee seeks to achieve maximum employment and inflation at the rate of 2 percent over the longer run. The Committee judges that the risks to achieving its employment and inflation goals are moving into better balance. The economic outlook is uncertain, and the Committee remains highly attentive to inflation risks.
In support of its goals, the Committee decided to maintain the target range for the federal funds rate at 5-1/4 to 5-1/2 percent. In considering any adjustments to the target range for the federal funds rate, the Committee will carefully assess incoming data, the evolving outlook, and the balance of risks. The Committee does not expect it will be appropriate to reduce the target range until it has gained greater confidence that inflation is moving sustainably toward 2 percent. In addition, the Committee will continue reducing its holdings of Treasury securities and agency debt and agency mortgage-backed securities, as described in its previously announced plans. The Committee is strongly committed to returning inflation to its 2 percent objective.
In assessing the appropriate stance of monetary policy, the Committee will continue to monitor the implications of incoming information for the economic outlook. The Committee would be prepared to adjust the stance of monetary policy as appropriate if risks emerge that could impede the attainment of the Committee's goals. The Committee's assessments will take into account a wide range of information, including readings on labor market conditions, inflation pressures and inflation expectations, and financial and international developments"""

sentences = re.split(r'(?<=[.!?])\s+', statement)
df = pd.DataFrame(sentences, columns=['Sentence'])
df['Results'] = classifier(sentences, batch_size=128, truncation="only_first")
df['SENTIMENT'] = df['Results'].apply(get_hawkish_dovish_classification)
df.to_markdown('sentiment.md', index=False)
print(df)
grouped_df = df.groupby('SENTIMENT').size()
print('='*50)
print(grouped_df)

# Citation :
#
# @inproceedings{shah-etal-2023-trillion,
#     title = "Trillion Dollar Words: A New Financial Dataset, Task {\&} Market Analysis",
#     author = "Shah, Agam  and
#       Paturi, Suvan  and
#       Chava, Sudheer",
#     booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
#     month = jul,
#     year = "2023",
#     address = "Toronto, Canada",
#     publisher = "Association for Computational Linguistics",
#     url = "https://aclanthology.org/2023.acl-long.368",
#     doi = "10.18653/v1/2023.acl-long.368",
#     pages = "6664--6679",
#     abstract = "Monetary policy pronouncements by Federal Open Market Committee (FOMC) are a major driver of financial market returns. We construct the largest tokenized and annotated dataset of FOMC speeches, meeting minutes, and press conference transcripts in order to understand how monetary policy influences financial markets. In this study, we develop a novel task of hawkish-dovish classification and benchmark various pre-trained language models on the proposed dataset. Using the best-performing model (RoBERTa-large), we construct a measure of monetary policy stance for the FOMC document release days. To evaluate the constructed measure, we study its impact on the treasury market, stock market, and macroeconomic indicators. Our dataset, models, and code are publicly available on Huggingface and GitHub under CC BY-NC 4.0 license.",
# }
