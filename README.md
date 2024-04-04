a# ViMGuard
The first automated, multi-modal approach to Video Misinformation Guarding.

ViMGuard leverages a three-step system: Claim Detection, Claim Extraction, and Claim Verification. In Claim Detection, Vidoe and Audio MAE are used to determine if there is a claim in the input video. If a claim is detected, the video is then passed through Claim Extraction, in which Claims made in the video are isolated with natural language processing. In Claim Verification, these claims are fact-checked with a Retrieval Augmented Generation (RAG) system.

## Audio + Video MAE
These folders contain the code used to train our Audio and Video MAE models. Code is a mix of original code and code taken from Facebook Research. 

## RAG
This folder contains the code used to create the RAG database utilized by ViMGuard and process RAG inputs. Sources that were utilized in our final database include Wikipedia, Bing News, and Google Claims.

## Benchmarking
This folder contains the models that ViMGuard was benchmarked against (Google ClaimReview, UTA's Claim Buster and a GPT-4 fact-checker)
