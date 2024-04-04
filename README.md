# ViMGuard
The first automated, multi-modal approach to Video Misinformation Guarding.

ViMGuard leverages a three-step system: Claim Detection, Claim Extraction, and Claim Verification. In Claim Detection, Vidoe and Audio MAE are used to determine if there is a claim in the input video. If a claim is detected, the video is then passed through Claim Extraction, in which Claims made in the video are isolated with natural language processing. In Claim Verification, these claims are fact-checked with a Retrieval Augmented Generation (RAG) system.

## Audio + Video MAE
MAE is a self-supervised learning task designed to improve the performance of audio classification models. Video and Audio MAE were used in the Claim Detection task of ViMGuard.

## RAG
Retrieval Augmented Generation is a system in which external information is fed to a LLM. This process mitigates hallucination and allows the LLM to speak on current events. RAG was utilized for the Claim Verification portion of ViMGuard.

# Benchmarking
The 'Benchmarking' folder contains the models that ViMGuard was benchmarked against (Google ClaimReview, UTA's Claim Buster and a GPT-4 fact-checker)
