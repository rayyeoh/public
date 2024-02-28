Toy model to classify FOMC text and interpretation based on fine-tuned FOMC-RoBERTa as published on https://huggingface.co/gtfintechlab/FOMC-RoBERTa
Text released for the Jan 31, 2024 FOMC statement (https://www.federalreserve.gov/newsevents/pressreleases/monetary20240131a.htm) was inputted 
and results tabulated into a markdown file. 
Final output tabulated each sentence's sentiment based on the classifier. 

| Sentence                                                                                                                                                                                                                    | Results                                           | SENTIMENT   |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------|:------------|
| Recent indicators suggest that economic activity has been expanding at a solid pace.                                                                                                                                        | {'label': 'LABEL_1', 'score': 0.9977574944496155} | Hawkish     |
| Job gains have moderated since early last year but remain strong, and the unemployment rate has remained low.                                                                                                               | {'label': 'LABEL_1', 'score': 0.9948988556861877} | Hawkish     |
| Inflation has eased over the past year but remains elevated.                                                                                                                                                                | {'label': 'LABEL_1', 'score': 0.9985118508338928} | Hawkish     |
| The Committee seeks to achieve maximum employment and inflation at the rate of 2 percent over the longer run.                                                                                                               | {'label': 'LABEL_2', 'score': 0.973000705242157}  | Neutral     |
| The Committee judges that the risks to achieving its employment and inflation goals are moving into better balance.                                                                                                         | {'label': 'LABEL_2', 'score': 0.9994924068450928} | Neutral     |
| The economic outlook is uncertain, and the Committee remains highly attentive to inflation risks.                                                                                                                           | {'label': 'LABEL_1', 'score': 0.9869159460067749} | Hawkish     |
| In support of its goals, the Committee decided to maintain the target range for the federal funds rate at 5-1/4 to 5-1/2 percent.                                                                                           | {'label': 'LABEL_2', 'score': 0.7037272453308105} | Neutral     |
| In considering any adjustments to the target range for the federal funds rate, the Committee will carefully assess incoming data, the evolving outlook, and the balance of risks.                                           | {'label': 'LABEL_2', 'score': 0.9997367262840271} | Neutral     |
| The Committee does not expect it will be appropriate to reduce the target range until it has gained greater confidence that inflation is moving sustainably toward 2 percent.                                               | {'label': 'LABEL_2', 'score': 0.9180444478988647} | Neutral     |
| In addition, the Committee will continue reducing its holdings of Treasury securities and agency debt and agency mortgage-backed securities, as described in its previously announced plans.                                | {'label': 'LABEL_0', 'score': 0.9168940782546997} | Dovish      |
| The Committee is strongly committed to returning inflation to its 2 percent objective.                                                                                                                                      | {'label': 'LABEL_1', 'score': 0.9758880734443665} | Hawkish     |
| In assessing the appropriate stance of monetary policy, the Committee will continue to monitor the implications of incoming information for the economic outlook.                                                           | {'label': 'LABEL_2', 'score': 0.9997928738594055} | Neutral     |
| The Committee would be prepared to adjust the stance of monetary policy as appropriate if risks emerge that could impede the attainment of the Committee's goals.                                                           | {'label': 'LABEL_2', 'score': 0.9995238780975342} | Neutral     |
| The Committee's assessments will take into account a wide range of information, including readings on labor market conditions, inflation pressures and inflation expectations, and financial and international developments | {'label': 'LABEL_2', 'score': 0.9996886253356934} | Neutral     |

==================================================
SENTIMENT
Dovish     1
Hawkish    5
Neutral    8
