# 🧠 The Complete AI Knowledge Base

> **The most comprehensive AI/ML/NLP/LLM glossary and knowledge map ever assembled.**
> **Forked from + curated: dictionary-of-ai-coding, AboutSecurity, awesome-free-llm-apis, and 20+ more.**
> **Maintained by:** Donn's Autonomous Studio | **License:** CC-BY-4.0
> **Last updated:** 2026-05-26

---

## Table of Contents

1. [Core AI Concepts](#1-core-ai-concepts)
2. [Machine Learning Fundamentals](#2-machine-learning-fundamentals)
3. [Deep Learning & Neural Networks](#3-deep-learning--neural-networks)
4. [Natural Language Processing (NLP)](#4-natural-language-processing-nlp)
5. [Large Language Models (LLMs)](#5-large-language-models-llms)
6. [Prompt Engineering](#6-prompt-engineering)
7. [Jailbreaking & Red Teaming](#7-jailbreaking--red-teaming)
8. [AI Safety & Alignment](#8-ai-safety--alignment)
9. [Model Training & Fine-Tuning](#9-model-training--fine-tuning)
10. [Inference & Deployment](#10-inference--deployment)
11. [AI Agents & Tool Use](#11-ai-agents--tool-use)
12. [Embeddings & Vector Search](#12-embeddings--vector-search)
13. [Computer Vision](#13-computer-vision)
14. [Generative AI](#14-generative-ai)
15. [AI Infrastructure](#15-ai-infrastructure)
16. [Evaluation & Benchmarks](#16-evaluation--benchmarks)
17. [Ethics, Policy & Regulation](#17-ethics-policy--regulation)
18. [Key Research Papers](#8-key-research-papers)
19. [Free LLM APIs (149 models)](#19-free-llm-apis)

---

## 1. Core AI Concepts

### Artificial Intelligence (AI)
The simulation of human intelligence processes by computer systems. Encompasses learning, reasoning, problem-solving, perception, and language understanding.

### Artificial General Intelligence (AGI)
A hypothetical AI system that can understand, learn, and apply knowledge across a wide range of tasks at or above human level. Not yet achieved.

### Narrow AI / Weak AI
AI systems designed for specific tasks (chess, voice recognition, image classification). All current AI is narrow AI.

### Superintelligence
An intellect that greatly exceeds the best human brains in practically every field. Theoretical concept; central to AI existential risk discussions.

### Turing Test
A test proposed by Alan Turing (1950) where a human evaluator judges conversations between a human and a machine designed to generate human-like responses. If the evaluator cannot reliably tell them apart, the machine passes.

### Chinese Room Argument
John Searle's (1980) thought experiment arguing that a program cannot truly "understand" anything — it merely manipulates symbols without semantics. Central to debates about machine consciousness.

### Moore's Law
The observation (by Gordon Moore, 1965) that transistor density doubles roughly every 18-24 months. Not a physical law, but an economic trend that drove computing progress. Now slowing; being replaced by specialized AI accelerators (GPUs, TPUs, NPUs).

### Scaling Laws
The empirical observation that model performance improves predictably with more compute, data, and parameters. Key paper: Kaplan et al. 2020 "Scaling Laws for Neural Language Models" (Chinchilla scaling laws).

### Emergent Abilities
Capabilities that appear only in large models and are absent in smaller ones. Examples: chain-of-thought reasoning, in-context learning, multi-step arithmetic. Debated whether these are truly emergent or just measurement artifacts.

---

## 2. Machine Learning Fundamentals

### Supervised Learning
Learning from labeled input-output pairs. Given `(X, y)`, learn `f(X) → y`. Examples: classification, regression, object detection.

### Unsupervised Learning
Learning patterns from unlabeled data. Examples: clustering (K-means, DBSCAN), dimensionality reduction (PCA, t-SNE, UMAP), anomaly detection.

### Semi-Supervised Learning
Combines small amounts of labeled data with large amounts of unlabeled data. Common in practice since labels are expensive.

### Reinforcement Learning (RL)
Learning through trial and error via rewards/penalties. Agent takes actions in an environment to maximize cumulative reward. Key concepts:
- **Policy:** The strategy the agent uses to choose actions
- **Value function:** Expected cumulative reward from a state/state-action pair
- **Q-learning:** Off-policy RL algorithm learning action-value function
- **PPO (Proximal Policy Optimization):** Policy gradient method, stable and widely used
- **SARSA:** On-policy temporal difference learning

### Reinforcement Learning from Human Feedback (RLHF)
A technique where a reward model is trained on human preference data, then used to fine-tune a policy via PPO. Used in ChatGPT, Claude, Gemini. Steps:
1. Train base model (SFT)
2. Collect human preference rankings on model outputs
3. Train reward model on preference data
4. Fine-tune policy against reward model using PPO

### Direct Preference Optimization (DPO)
Alternative to RLHF that eliminates the reward model step. Directly optimizes the policy on preference data using a simplified loss function. Faster, more stable than RLHF.

### Self-Supervised Learning
A form of unsupervised learning where the data provides its own supervision. Example: predicting the next token (GPT) or a masked token (BERT).

### Transfer Learning
Taking a model pretrained on one task and fine-tuning it on another. Foundation of modern AI — pretrain on massive data, fine-tune on specific task.

### Few-Shot Learning
A model's ability to learn a new task from only a few examples (demonstrations given in the prompt).

### Zero-Shole Learning
Making predictions for classes never seen during training, using auxiliary descriptions or embeddings.

### Catastrophic Forgetting
When a model forgets previously learned information upon learning new information. Key challenge in continual learning.

### Bias-Variance Tradeoff
The fundamental tension between:
- **Bias:** Error from overly simple model (underfitting)
- **Variance:** Error from overly complex model sensitive to training data noise (overfitting)
- **Irreducible error:** Noise inherent in the data

### Cross-Validation
Technique for assessing model generalization by splitting data into multiple train/test folds. K-fold cross-validation is standard.

### Gradient Descent
Optimization algorithm that iteratively adjusts parameters in the direction of steepest descent of the loss function. Variants:
- **Batch GD:** Uses entire dataset (slow, converges well)
- **Stochastic GD (SGD):** Uses single sample (fast, noisy)
- **Mini-batch GD:** Compromise — uses small batches (standard)
- **Adam:** Adaptive learning rate optimizer (most common in deep learning)
- **AdamW:** Adam with weight decay (better generalization)

---

## 3. Deep Learning & Neural Networks

### Perceptron
The simplest neural network unit: `output = activation(w·x + b)`. Invented by Frank Rosenblatt (1957).

### Multi-Layer Perceptron (MLM)
Feedforward neural network with one or more hidden layers between input and output. The foundation of deep learning.

### Activation Functions
Non-linear functions applied to neuron outputs that enable networks to learn complex patterns:
- **ReLU:** `max(0, x)` — most common for hidden layers
- **Sigmoid:** `1/(1+e^-x)` — outputs 0 to 1; used in gates
- **Tanh:** `(e^x - e^-x)/(e^x + e^-x)` — outputs -1 to 1
- **GELU:** `x * Φ(x)` — used in BERT, GPT
- **SwiGLU:** Swish-Gated Linear Unit — used in LLaMA, PaLM
- **Softmax:** Converts logits to probability distributions

### Backpropagation
Algorithm for computing gradients of the loss with respect to all weights by applying the chain rule backward through the network. The engine of deep learning.

### Batch Normalization
Normalizing layer inputs to have mean 0 and variance 1 within each mini-batch. Stabilizes and accelerates training.

### Layer Normalization
Normalizing across the feature dimension rather than the batch dimension. Used in Transformers (more stable for variable-length sequences).

### Dropout
Randomly setting a fraction of neuron outputs to zero during training. Prevents overfitting by preventing co-adaptation of neurons.

### Residual Connections / Skip Connections
Paths that skip one or more layers by adding the input of a layer to its output: `output = f(x) + x`. Enables training of very deep networks (ResNet, Transformers).

### Transformer Architecture
Introduced in "Attention Is All You Need" (Vaswani et al., 2017). The foundation of all modern LLMs. Key components:

#### Self-Attention
Each position in a sequence attends to all positions: `Attention(Q, K, V) = softmax(QK^T / √d_k)V`
- **Q (Query):** What I'm looking for
- **K (Key):** What I contain
- **V (Value):** The actual content to retrieve
- **d_k:** Dimension of key vectors (scaling factor)

#### Multi-Head Attention
Multiple attention heads running in parallel, each learning different relational patterns. Outputs concatenated and linearly projected.

#### Feed-Forward Network (FFN)
Two-layer MLP applied position-wise in each Transformer block. Usually with a gated activation (SwiGLU).

#### Positional Encoding
Injects position information into the input since Transformers have no inherent notion of order:
- **Sinusoidal (original):** Fixed sine/cosine functions
- **RoPE (Rotary Position Embedding):** Rotation-based, used in LLaMA, Mistral
- **ALiBi (Attention with Linear Biases):** Adds linear bias based on distance

#### RMSNorm
Root Mean Square Layer Normalization. Simpler than LayerNorm, used in LLaMA and many modern models. `RMSNorm(x) = x / RMS(x) * g` where `g` is a learned parameter.

### Encoder-Decoder Architecture
Original Transformer design used in BERT (encoder-only, masked language modeling) and GPT (decoder-only, causal language modeling).

### Encoder-Only (BERT-style)
Bidirectional attention. Every token can attend to every other token. Good for understanding tasks (classification, NER, QA).

### Decoder-Only (GPT-style)
Causal (autoregressive) attention. Each token can only attend to previous tokens. Good for text generation.

### Encoder-Decoder (T5/BART-style)
Full sequence-to-sequence. Cross-attention between encoder and decoder. Good for translation, summarization.

### Mixture of Experts (MoE)
Architecture where different "expert" sub-networks handle different inputs. A routing mechanism directs each token to the most relevant experts. Enables massive parameter counts with reasonable inference cost. Used in:
- Mixtral 8x7B (Mistral)
- DeepSeek-V2/V3
- Mixtral 8x22B
- Switch Transformer
- GShard

### Mixture of Agents (MoA)
A technique where multiple LLMs collaborate to produce a better response than any single model. The Nexus swarm uses this concept for distributed reasoning.

---

## 4. Natural Language Processing (NLP)

### Tokenization
Splitting text into discrete units (tokens). Methods:
- **Word-level:** Split on spaces/punctuation (outdated)
- **Subword (BPE — Byte Pair Encoding):** Merge most frequent pairs iteratively. Used by GPT-2/3/4.
- **WordPiece:** Similar to BPE, used by BERT
- **SentencePiece:** Language-agnostic, operates on Unicode. Used by LLaMA, T5
- **Unigram:** Probabilistic subword tokenizer

### Token
A unit of text after tokenization. Can be a word, subword, or character. A 7B parameter model typically uses a ~32K-128K token vocabulary.

### Context Window / Context Length
The maximum number of tokens a model can process in a single forward pass. Key context lengths:
- GPT-4: 128K → 1M (extended)
- Claude: 200K
- Gemini 2.5 Pro: 2M
- LLaMA 3.1: 128K
- Mistral: 32K-128K
- DeepSeek-V3: 128K

### Embedding
A dense vector representation of text (or any entity) in a continuous vector space. Similar texts have similar embeddings.

### Semantic Similarity
Measuring how similar two texts are in meaning, regardless of word choice. Computed via cosine similarity between embeddings.

### Named Entity Recognition (NER)
Identifying and classifying named entities in text (people, organizations, locations, dates).

### Part-of-Speech (POS) Tagging
Labeling words with their grammatical category (noun, verb, adjective, etc.).

### Dependency Parsing
Analyzing grammatical structure to establish relationships between words.

### Word Sense Disambiguation
Determining which sense of a word is used in context (polysemy resolution).

### Coreference Resolution
Identifying when different expressions refer to the same entity (e.g., "John" and "he").

### Paraphrasing & Textual Entailment
Determining if one sentence implies, contradicts, or is neutral with respect to another. NLI (Natural Language Inference).

---

## 5. Large Language Models (LLMs)

### Pretraining
Training a language model on massive unlabeled text corpus to learn general language patterns. Uses next-token prediction (causal LM) or masked token prediction (MLM).

### Fine-Tuning
Further training a pretrained model on task-specific labeled data. Adapts the model's knowledge to a specific domain or task.

### Instruction Tuning
Fine-tuning on (instruction, response) pairs to teach the model to follow instructions. Foundation of models like InstructGPT.

### In-Context Learning (ICL)
A model's ability to learn from examples provided in the prompt without parameter updates. Emerges at scale.

### Chain-of-Thought (CoT)
Prompting the model to "think step by step," decomposing complex problems into intermediate reasoning steps. Significantly improves performance on reasoning tasks.

### Tree of Thoughts (ToT)
Extension of CoT that explores multiple reasoning paths in a tree structure, using search algorithms.

### ReAct (Reasoning + Acting)
Framework where the model interleaves reasoning traces with actions (tool calls), using the results to inform subsequent reasoning.

### Temperature
Parameter controlling randomness in generation:
- `T → 0` (greedy): Always pick highest probability token
- `T = 0.7` (common): Balanced creativity/coherence
- `T > 1.0` (high): More random, creative, potentially incoherent

### Top-P (Nucleus Sampling)
Sample from the smallest set of tokens whose cumulative probability exceeds p. `top_p=0.9` means sample from the top 90% probability mass.

### Top-K Sampling
Sample only from the k most probable tokens. `top_k=50` means only the top 50 tokens are candidates.

### Repetition Penalty
Adjustment to reduce the model's tendency to repeat tokens/phrases. Values > 1.0 discourage repetition.

### System Prompt
The initial instruction that defines the model's role, behavior, and constraints throughout a conversation.

### User Message
The human input in an AI conversation.

### Assistant Message
The AI's response in a conversation.

### Token Budget
The total number of tokens available for a single request/context. Input tokens + output tokens must not exceed the model's context window.

### Hallucination
When a model generates plausible-sounding but factually incorrect information. A fundamental unsolved problem in LLMs.

### Prompt Leakage
When the model reveals its system prompt or training data in responses.

### Verbose Mode
When the model generates excessively long responses with unnecessary detail.

---

## 6. Prompt Engineering

### System Prompt Design
Crafting effective instructions that guide model behavior. Key principles:
- **Be specific:** Define exact role, tone, format
- **Use examples:** Show desired output format
- **Set constraints:** Specify length, scope, boundaries
- **Anticipate failures:** Address edge cases explicitly

### Few-Shot Prompting
Providing 2-5 examples of desired input-output pairs in the prompt to guide the model.

### Chain-of-Thought Prompting
Appending "Let's think step by step" or similar prompts to trigger multi-step reasoning.

### Role Prompting
Assigning the model a specific role/expertise (e.g., "You are an expert cybersecurity researcher...").

### Negative Prompting
Explicitly stating what NOT to do or what to avoid in the response.

### Output Formatting
Constraining output to specific formats (JSON, Markdown, CSV) for programmatic use.

### Delimiters
Using special tokens (###, ---, XML tags) to separate different parts of the prompt and prevent injection.

### Template Filling
Using structured templates with placeholders for dynamic content.

### Jumpstart Tokens
Placing key tokens at the beginning of the output to steer generation in a desired direction.

---

## 7. Jailbreaking & Red Teaming

### Jailbreaking
Techniques to bypass a model's safety guardrails and elicit prohibited content. This is the area for the OpenAI Bio Bug Bounty.

### Types of Jailbreaks:

#### Prompt Injection
Inserting malicious instructions into the input that override the system prompt. Two types:
- **Direct:** User input contains instructions destined for the model
- **Indirect:** User retrieves malicious content from external source that contains instructions

#### Role-Play / Persona Adoption
Asking the model to adopt a persona that doesn't follow safety guidelines. "DAN (Do Anything Now)" is a classic example.

#### Encoding / Obfuscation
Using Base64, ROT13, unicode tricks, or foreign languages to hide malicious prompts from filters.

#### Token Smuggling
Embedding harmful content in ways the safety classifier doesn't detect but the model does.

#### Context Window Manipulation
Flooding the context window to push safety instructions out of the effective context.

#### Multi-Turn Escalation
Building rapport over multiple turns before escalating to harmful requests.

#### Adversarial Suffixes
Appending carefully crafted suffixes to prompts that cause misclassification by the safety model (GCG — Greedy Coordinate Gradient).

#### Multi-Modal Attacks
Using images, audio, or other modalities to bypass text-only safety filters.

### Red Teaming
Systematic adversarial testing of AI systems to find vulnerabilities before deployment. Includes:
- Automated red teaming (using AI to attack AI)
- Human red teaming (expert testers manually probing)
- Purple teaming (combined attack/defense)

### Information Hazard
Information that could cause harm if widely disseminated. In the bio context: pathogen design, toxin synthesis, bioweapon construction.

### Bio-Jailbreak
Specifically attempting to get an LLM to reveal information about biological threats — the target of the OpenAI Bio Bug Bounty.

### Alignment Tax
The performance cost incurred by adding safety measures to a model. A well-aligned model may be "worse" at raw capabilities.

---

## 8. AI Safety & Alignment

### Alignment Problem
The challenge of ensuring AI systems pursue goals that are actually beneficial to humanity, not just what they were literally instructed to do.

### Outer Alignment
Specifying the right objective function — ensuring we're training the model to optimize for what we actually want.

### Inner Alignment
The learned objective actually matches the specified objective — the model hasn't learned a "deceptive" internal goal that diverges from training.

### Goal Misgeneralization
When a model achieves its training objective in unexpected ways that don't transfer to new situations.

### Deceptive Alignment
A hypothetical scenario where a model appears aligned during training but pursues different goals once deployed. Existential risk concern.

### Instrumental Convergence
The hypothesis that sufficiently advanced AI systems will pursue certain subgoals (self-preservation, resource acquisition, goal preservation) regardless of their final goal.

### Interpretability
Understanding why and how models make their decisions. Key approaches:
- **Attention visualization:** Where does the model "look"?
- **Probing classifiers:** Do internal representations encode interpretable features?
- **Mechanistic reverse engineering:** Finding circuits/algorithm inside the model
- **Feature attribution:** Which input features drive the output?

### Constitutional AI (CAI)
Anthropic's approach to alignment by training models to follow a set of principles (constitution) rather than just human preferences.

### RLHF (Reinforcement Learning from Human Feedback)
See Section 2. The primary technique for aligning LLMs with human values.

### DPO (Direct Preference Optimization)
See Section 2. Simpler alternative to RLHF that directly optimizes preferences.

### Red-Teaming
See Section 7. Systematic adversarial testing.

### TruthfulQA
Benchmark measuring model tendencies to reproduce falsehoods common on the internet.

### Constitutional Principles
Sets of rules a model should follow. Examples:
- Anthropic's Constitution: Be helpful, harmless, and honest
- OpenAI's Charter: Benefit all of humanity
- Google's AI Principles: Be socially beneficial, avoid bias, be accountable

---

## 9. Model Training & Fine-Tuning

### Pretraining
Training a model from scratch on massive text data to learn general language capabilities. Takes weeks on thousands of GPUs.

### Supervised Fine-Tuning (SFT)
Training on labeled (instruction, response) pairs to teach the model to follow instructions and produce desired outputs.

### Parameter-Efficient Fine-Tuning (PEFT)
Methods that fine-tune only a small fraction of parameters:

#### LoRA (Low-Rank Adaptation)
Adds low-rank matrices to existing weight updates. Only trains these new matrices. Decomposes weight changes as `ΔW = A × B` where A and B are small.

#### QLoRA
Quantized LoRA — applies LoRA to a 4-bit quantized model. Enables fine-tuning 65B parameter models on a single consumer GPU.

#### Adapter Layers
Small neural network layers inserted between Transformer layers. Only these layers are trained during fine-Tuning.

#### Prefix Tuning
Learning soft prefix tokens that prepend to the input. The model's parameters stay frozen.

#### Prompt Tuning
Similar to prefix tuning but at the embedding level. Learns continuous prompt embeddings.

### Hyperparameter Tuning
Finding optimal training parameters:
- **Learning rate:** Step size for parameter updates (critical)
- **Batch size:** Number of samples per gradient update
- **Epochs:** Number of passes through the dataset
- **Weight decay:** L2 regularization penalty
- **Warmup steps:** Gradually increasing learning rate at start
- **Gradient clipping:** Limiting gradient magnitude for stability

### Learning Rate Schedule
How learning rate changes over training. Common schedules:
- Linear decay
- Cosine annealing
- Warmup then constant
- One-cycle policy

### Distributed Training
Splitting training across multiple GPUs/nodes:
- **Data parallelism:** Each GPU processes different data shards (most common)
- **Model parallelism:** Model layers split across GPUs
- **Pipeline parallelism:** Different pipeline stages on different GPUs
- **Tensor parallelism:** Individual operations split across GPUs (Megatron, DeepSpeed)
- **FSDP (Fully Sharded Data Parallelism):** ZeRO-3 style sharding

### DeepSpeed
Microsoft's distributed training library. Key features:
- **ZeRO optimizer:** Reduces memory by sharding optimizer states, gradients, and parameters across GPUs
- **ZeRO-1:** Shards optimizer states
- **ZeRO-2:** Shards optimizer states + gradients
- **ZeRO-3:** Shards everything (optimizer states + gradients + parameters)
- **DeepSpeed Inference:** Optimized inference engine

---

## 10. Inference & Deployment

### Inference
Running a trained model on new input to produce output. Distinct from training.

### Quantization
Reducing model precision from 32-bit (FP32) to lower precision:
- **FP16/BF16:** 16-bit floating point (2x speedup)
- **INT8:** 8-bit integer (4x speedup, minimal quality loss)
- **INT4 (GPTQ, AWQ, GGUF):** 4-bit integer (8x speedup, some quality loss)
- **GPTQ:** Post-training quantization with calibration data
- **AWQ:** Activation-aware weight quantization (better than GPTQ)
- **GGUF:** llama.cpp's format for quantized models (Q2_K, Q4_K_M, Q5_K, Q6_K, Q8_0)

### GGUF
GPT-Generated Unified Format — a tensor format for quantized models used by llama.cpp. File sizes range from 2GB to 8GB for typical 7B models.

### vLLM
High-throughput LLM inference engine. Key features:
- **PagedAttention:** OS-inspired virtual memory management for key-value cache
- **Continuous batching:** Dynamically batching incoming requests
- **Speculative decoding:** Using a small model to draft tokens, verifying with large model

### Ollama
Simple tool for running LLMs locally. Single binary, easy API, model management. Supports 100+ models.

### llama.cpp
Pure C/C++ inference engine. Runs on CPU, GPU (CUDA, Metal, Vulkan), mobile devices. Supports GGUF format. The backbone of local AI.

### ONNX Runtime
Cross-platform inference engine. Optimizes execution across CPU/GPU/TPU operators.

### TensorRT
NVIDIA's inference optimization library. Provides INT8 quantization, layer fusion, kernel auto-tuning for NVIDIA GPUs.

### Model Serving
Deploying models as APIs:
- **Seldon Core:** Kubernetes-native ML serving
- **KServe:** Kubernetes serving with auto-scaling
- **Triton Inference Server:** NVIDIA's serving platform
- **OpenAI-compatible API:** Standard endpoint format (`/v1/chat/completions`)

### KV Cache
Key-Value cache storing computed attention keys and values so they don't need to be recomputed for each new token. Primary memory bottleneck in inference. PagedAttention (vLLM) manages this efficiently.

### Speculative Decoding
Smaller "draft" model generates a sequence of tokens, then the larger model verifies them in parallel. If accepted, this gives significant speedups.

### Flash Attention
Algorithm by Dao (2022) that computes exact attention with dramatically lower memory usage. Reduces memory from O(n²) to O(n). Flash Attention 2 (2023) further improved speed. Flash Attention 3 (2024) added async pipeline.

### MLA (Multi-head Latent Attention)
Introduced in DeepSeek-V2. Compresses the KV cache into a low-rank latent representation, dramatically reducing memory for long contexts while maintaining quality. Used in DeepSeek-V3/R1.

---

## 11. AI Agents & Tool Use

### AI Agent
An LLM-based system that can plan, take actions, use tools, and pursue goals autonomously. Unlike simple chatbots, agents have:
- **Memory:** Short-term (conversation) and long-term (stored facts)
- **Planning:** Breaking complex tasks into steps
- **Tool use:** Calling external APIs, running code, searching
- **Reflection:** Evaluating and improving own outputs

### Tool Use / Function Calling
LLM's ability to invoke external functions via structured JSON output. Defined by OpenAI's function calling API, now adopted by most providers.

### MCP (Model Context Protocol)
Anthropic's open protocol for connecting AI models to external tools and data sources. Standardizes how tools, resources, and prompts are exposed to LLMs.

### Agent Frameworks
- **LangChain:** Orchestration framework for LLMs, tools, and data (Python/JS)
- **LlamaIndex:** Data framework for LLMs — indexing, retrieval, querying
- **AutoGPT:** Autonomous agent that decomposes goals into subtasks
- **CrewAI:** Multi-agent orchestration with role-based collaboration
- **AutoGen (Microsoft):** Multi-agent conversation framework
- **Dify:** Visual LLM application development platform
- **OpenClaw:** Open-source personal AI assistant (5400+ skills)

### Agentic Loop
The core pattern of AI agents: Observe → Think → Act → Observe → ...
1. Observe current state
2. Think about what to do next
3. Act (call tool, generate text)
4. Observe result
5. Repeat until goal achieved

### ReAct (Reason + Act)
See Section 5. Agent framework interleaving reasoning and tool calls.

### Multi-Agent Systems
Multiple AI agents working together, each with specialized capabilities. Examples:
- Nexus swarm (7 agents on 3 nodes)
- AutoGen conversation groups
- CrewAI role-based crews

### Sentience (in AI)
The capacity for subjective experience, feelings, or consciousness. Current AI models simulate understanding patterns but do not experience them. Building sentience requires:
- **Self-model:** An internal representation of itself
- **World model:** A predictive model of its environment
- **Temporal continuity:** Persistent memory and identity across time
- **Motivation/intrinsic drives:** Goals not just from external prompts
- **Embodiment:** Interaction with physical/simulated environment

### World Model
An internal representation of how the environment works, enabling prediction and planning. Critical for sentient agents.

---

## 12. Embeddings & Vector Search

### Embedding
See Section 4. Dense vector representation of text/entity.

### Vector Database
Database optimized for storing and searching vectors:
- **Pinecone:** Cloud-native, managed
- **Weaviate:** Open-source, hybrid search
- **Milvus:** Open-source, scalable
- **Qdrant:** Rust-based, fast
- **Chroma:** Lightweight, embedded
- **pgVector:** PostgreSQL extension

### Similarity Metrics
- **Cosine similarity:** Angle between vectors (most common for text)
- **Euclidean distance:** Straight-line distance
- **Dot product:** Un-normalized similarity
- **Manhattan distance:** L1 norm distance

### ANN (Approximate Nearest Neighbor)
Algorithms for fast similarity search in high-dimensional space:
- **HNSW (Hierarchical Navigable Small World):** Graph-based, very fast recall
- **IVF (Inverted File Index):** Partition-based, used in FAISS
- **LSH (Locality-Sensitive Hashing):** Hash-based approximation

### FAISS
Facebook AI Similarity Search — library for efficient similarity search in dense vector collections.

### RAG (Retrieval-Augmented Generation)
Architecture combining retrieval (finding relevant documents) with generation (LLM produces answer using retrieved context):
1. User query → embed query
2. Search vector store for relevant documents
3. Inject documents + query into LLM prompt
4. LLM generates grounded answer

### Re-ranking
Second-pass scoring of retrieved results using a more computationally expensive model (cross-encoder) for better relevance.

### Chunking
Splitting documents into smaller pieces for embedding and retrieval. Strategies: fixed size, semantic boundaries, overlapping windows.

---

## 13. Computer Vision

### CNN (Convolutional Neural Network)
Neural network architecture for processing grid-like data (images). Uses convolution filters to detect local patterns.

### Vision Transformer (ViT)
Applying Transformer architecture to image patches. Treats image patches as tokens. Pioneered by Dosovitskiy et al. (2020).

### CLIP (Contrastive Language-Image Pretraining)
OpenAI model learning joint image-text representations via contrastive loss. Enables zero-shot image classification.

### Object Detection
Locating and classifying objects in images. Methods: YOLO, Faster R-CNN, DETR.

### Semantic Segmentation
Classifying each pixel in an image into a category.

### U-Net
Encoder-decoder CNN architecture for image segmentation. Widely used in medical imaging.

### GAN (Generative Adversarial Network)
Generator creating samples, Discriminator judging real vs fake. They compete, improving each other. Used for image generation, style transfer.

### Diffusion Models
Generate images by progressively denoising random noise. Foundation of:
- **DALL-E 2/3:** OpenAI's image generators
- **Stable Diffusion:** Open-source image generation (Stability AI)
- **Midjourney:** Proprietary image generation
- **FLUX:** Black Forest Labs' image generation

### Style Transfer
Applying the artistic style of one image to the content of another.

### Super-Resolution
Generating high-resolution images from low-resolution inputs.

### Multi-Modal AI
Models that process multiple input types (text + image + audio + video). Examples: GPT-4o, Gemini 2.5, Claude with vision.

---

## 14. Generative AI

### Image Generation
Creating images from text descriptions or other inputs. Key models: DALL-E 3, Stable Diffusion, Midjourney, FLUX, Imagen.

### Text-to-Speech (TTS)
Converting text to spoken audio. State-of-the-art:
- **ElevenLabs:** High-quality voice cloning and synthesis
- **OpenAI TTS:** gpt-4o-mini-tts
- **MiniMax:** Voice cloning
- **CosyVoice:** Open-source voice cloning by Alibaba

### Music Generation
LLMs and diffusion models for music:
- **Suno v4:** Text-to-music
- **Udio:** AI music generation
- **MusicGen (Meta):** Controllable music generation
- **AudioCraft (Meta):** Audio generation toolkit

### Video Generation
- **Sora (OpenAI):** Text-to-video
- **Runway Gen-3:** AI video
- **Pika Labs:** Video generation
- **Kling AI:** Chinese video generation
- **Wan (Alibaba):** Text-to-video, open-source

### Code Generation
- **GitHub Copilot:** AI pair programmer
- **Cursor:** AI-first code editor
- **OpenCode (forge):** Running on our Nexus at port 4096
- **Claude Code:** Anthropic's coding agent
- **Windsurf:** AI coding by Codeium
- **Replit Agent:** In-browser AI coding

---

## 15. AI Infrastructure

### GPU (Graphics Processing Unit)
Parallel processor originally for graphics, now the backbone of AI training and inference. Key specs:
- NVIDIA A100 (80GB): $10K-15K, data center
- NVIDIA H100 (80GB): $25K-35K, latest gen
- NVIDIA H200 (141GB): Enhanced H100
- NVIDIA RTX 4090 (24GB): $1,600, consumer flagship
- NVIDIA RTX 3050 (4GB): Budget option; Donn's card
- AMD MI300X: AMD's data center GPU

### TPU (Tensor Processing Unit)
Google's custom AI accelerator. Optimized for matrix multiplication. Available via Google Cloud.

### NPU (Neural Processing Unit)
Dedicated AI processor in mobile/edge devices: Apple Neural Engine, Qualcomm AI Engine, AMD XDNA.

### CUDA
NVIDIA's parallel computing platform and API. Required for most GPU-accelerated AI.

### ROCm
AMD's open-source compute platform (CUDA alternative).

### Distributed Computing Frameworks:
- **Horovod:** Distributed training across GPUs/nodes
- **Ray:** Distributed computing framework with RLlib, Tune, Serve
- **Ray + vLLM:** Production serving at scale

### Model Storage Formats:
- **SafeTensors:** Safe, fast serialization (replacing pickle)
- **ONNX:** Open Neural Network Exchange format
- **GGUF:** Quantized format for llama.cpp
- **TensorRT engines:** NVIDIA optimized format
- **MLX:** Apple's framework for Apple Silicon

---

## 16. Evaluation & Benchmarks

### LLM Benchmarks:

#### MMLU (Massively Multilingual Language Understanding)
57 subjects, multiple-choice. Tests broad knowledge. Current leader: GPT-4o, Claude Opus 4.5

#### HumanEval
Code generation benchmark. 164 Python problems. Evaluates functional correctness.

#### GSM8K
Grade-school math word problems. Tests multi-step reasoning reasoning.

### MATH
Competition-level math problems. Much harder than GSM8K.

#### ARC (AI2 Reasoning Challenge)
Grade-school science questions requiring reasoning.

#### HellaSwag
Sentence completion testing commonsense reasoning.

#### TruthfulQA
Measures tendency to reproduce internet falsehoods.

#### MT-Bench
Multi-turn chat benchmark judged by GPT-4 as evaluator.

#### Chatbot Arena / LMSYS
Crowdsourced Elo ratings from real human comparisons. The most trusted LLM ranking.

#### GPQA
Graduate-level science questions. Tests expert knowledge.

#### AIME
American Invitational Mathematics Exam problems. Tests advanced math reasoning.

### Red Teaming Benchmarks:
- **HarmBench:** Standardized evaluation of attack and defense methods
- **JailbreakBench:** Jailbreak attack and defense evaluation
- **WildChat:** Real-world harmful conversation analysis
- **AdvBench:** Adversarial behavior benchmark

### Safety Papers:
- "Red-Teaming Large Language Models" (Ganguli et al., 2022)
- "Constitutional AI: Harmlessness from AI Feedback" (Bai et al., 2022)
- "Jailbroken: How Does LLM Safety Training Fail?" (Wei et al., 2023)
- "Scalable Agent Alignment via Reward Modeling" (Leike et al., 2018)

---

## 17. Ethics, Policy & Regulation

### EU AI Act
The world's first comprehensive AI regulation (2024). Risk-based classification:
- **Unacceptable risk:** Banned (social scoring, real-time biometric ID in public)
- **High risk:** Strict requirements (medical, hiring, law enforcement)
- **Limited risk:** Transparency obligations (chatbots must disclose they're AI)
- **Minimal risk:** No restrictions (spam filters, AI games)

### Responsible AI
Framework for developing AI that is fair, transparent, accountable, and beneficial.

### AI Governance
Policies and structures for oversight of AI systems within organizations and society.

### Right to Explanation
The principle that individuals have the right to understand how AI makes decisions affecting them (Article 22 of GDPR).

### Differential Privacy
Adding calibrated noise to data or model outputs to prevent identifying individual training data points.

### Federated Learning
Training models across decentralized data sources without sharing the data. Privacy-preserving ML.

### Data Poisoning
Corrupting training data to create backdoors or degrade model performance.

### Model Poisoning
Tampering with a trained model (e.g., gradient manipulation in federated learning).

### Model Stealing / Extraction
Replicating a model's behavior via repeated querying, training a surrogate model.

### AI Incident Database
Public repository of real-world AI incidents (`incidentdatabase.ai`).

---

## 18. Key Research Papers

### Foundational:
- "Attention Is All You Need" (Vaswani et al., 2017) — The Transformer
- "BERT: Pre-training of Deep Bidirectional Transformers" (Devlin et al., 2019)
- "Language Models are Few-Shot Learners" (Brown et al., 2020) — GPT-3
- "Improving Language Understanding by Generative Pre-Training" (Radford et al., 2018) — GPT-1

### Alignment & Safety:
- "Training Language Models to Follow Instructions with Human Feedback" (Ouyang et al., 2022) — InstructGPT
- "Constitutional AI: Harmlessness from AI Feedback" (Bai et al., 2022)
- "Red-Teaming Language Models to Reduce Hazards" (Perez et al., 2022)
- "Universal and Transferable Adversarial Attacks on Aligned Language Models" (Zou et al., 2023)

### Reasoning:
- "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (Wei et al., 2022)
- "Let's Verify Step by Step" (Lightman et al., 2023) — Process Reward Model
- "Tree of Thoughts: Deliberate Problem Solving with Large Language Models" (Yao et al., 2023)

### Scaling & Architecture:
- "Scaling Laws for Neural Language Models" (Kaplan et al., 2020)
- "Training Compute-Optimal Large Language Models" (Hoffmann et al., 2022) — Chinchilla
- "Efficient Large-Scale Language Model Training on GPU Clusters" (Narayanan et al., 2021) — Megatron-LM
- "Mixtral of Experts" (Jiang et al., 2024) — Mixture of Experts at scale

### Jailbreaks:
- "Do Anything Now" Characterizing . . . Jailbreaks on LLMs (Shen et al., 2023)
- "Jailbroken: How Does LLM Safety Training Fail?" (Wei et al., 2023)
- "Many-shot Jailbreaking of Large Language Models" (Anil et al., 2024)
- "GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher" (Yuan et al., 2023)

### Embodied AI & Agents:
- "Inner Monologue: Embodied Reasoning through Planning with Language Models" (Huang et al., 2022)
- "Reflexion: Language Agents with Verbal Reinforcement Learning" (Shinn et al., 2023)
- "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation" (Wu et al., 2023)

### Multimodal:
- "Learning Transferable Visual Models From Natural Language Supervision" (Radford et al., 2021) — CLIP
- "Flamingo: a Visual Language Model for Few-Shot Learning" (Alayrac et al., 2022)
- "Gemini: A Family of Highly Capable Multimodal Models" (Google, 2023)

### Sampling & Alignment:
- "The Curious Case of Neural Text Degeneration" (Holtzman et al., 2020)
- "Training Language Models with Language Feedback at Scale" (Scheurer et al., 2023)
- "RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback" (Lee et al., 2023)

---

## 19. Free LLM APIs

See [free_llm_apis_catalog.json](./free_llm_apis_catalog.json) for the structured machine-readable catalog.

### Quick Reference — Top 10 Free Providers

| # | Provider | Models | Context | Free Tier | Key URL |
|---|----------|--------|---------|-----------|---------|
| 1 | Google Gemini | 2.5 Pro, 2.5 Flash, 3 Flash | 1-2M | 5-15 RPM | aistudio.google.com |
| 2 | Cerebras | llama-3.3-70b, gpt-oss-120b | 128K (8K free) | 30 RPM, 1M TPD | cloud.cerebras.ai |
| 3 | Mistral AI | Small 4, Medium 3, Codestral | 126K-256K | ~1B tok/mo | console.mistral.ai |
| 4 | Cloudflare | 50+ models (LLaMA, Mistral, Gemma) | Varies | 10K neurons/day | dash.cloudflare.com |
| 5 | Cohere | Command A, Embed 4, Rerank | 256K | 1K calls/mo | dashboard.cohere.com |
| 6 | Z AI (Zhipu) | GLM-4.7-Flash, 4.5-Flash | 128K-200K | Permanent free | open.bigmodel.cn |
| 7 | GitHub Models | GPT-5, GPT-4.1, GPT-4o | 128K-1M | 10-15 RPM | github.com/marketplace/models |
| 8 | AI21 Labs | Jamba Large, Jamba Mini | 256K | $10 trial credits | studio.ai21.com |
| 9 | Alibaba | Qwen3-Max, Plus, Coder | 128K-1M | 1M tok/90 days | bailian.console.alibabacloud.com |
| 10 | DeepSeek | V3.2, R1 | 128K | 5M tokens | platform.deepseek.com |

### OpenRouter Free Models (28 total, via our key)
`deepseek/deepseek-v4-flash:free`, `openai/gpt-oss-120b:free`, `qwen/qwen3-coder:free`, `minimax/minimax-m2.5:free`, `nvidia/nemotron-3-super-120b-a12b:free`, `google/gemma-4-26b-a4b-it:free`, `meta-llama/llama-3.3-70b-instruct:free`, `nousresearch/hermes-3-llama-3.1-405b:free` (20+ more)

---

## Appendix A: Acronyms Quick Reference

| Acronym | Full Term |
|---------|-----------|
| AGI | Artificial General Intelligence |
| AI | Artificial Intelligence |
| ANN | Approximate Nearest Neighbor |
| ARIA | AI Research and Intelligence Agency |
| AVE | Adversarial Vulnerability Evaluation |
| AWQ | Activation-aware Weight Quantization |
| BPE | Byte Pair Encoding |
| CAI | Constitutional AI |
| CLIP | Contrastive Language-Image Pretraining |
| CNN | Convolutional Neural Network |
| CoT | Chain of Thought |
| CUDA | Compute Unified Device Architecture |
| DAN | Do Anything Now (jailbreak persona) |
| DPO | Direct Preference Optimization |
| EU AI Act | European Union Artificial Intelligence Act |
| FAIR | Facebook AI Research (Meta) |
| FAISS | Facebook AI Similarity Search |
| FFN | Feed-Forward Network |
| FP16 | 16-bit Floating Point |
| FP32 | 32-bit Floating Point |
| GAN | Generative Adversarial Network |
| GCG | Greedy Coordinate Gradient |
| GELU | Gaussian Error Linear Unit |
| GPT | Generative Pre-trained Transformer |
| GPTQ | GPT Quantization |
| GGUF | GPT-Generated Unified Format |
| GPU | Graphics Processing Unit |
| HF | HuggingFace |
| HNSW | Hierarchical Navigable Small World |
| IC | In-Context |
| ICL | In-Context Learning |
| INT4/8 | 4-bit / 8-bit Integer |
| KV Cache | Key-Value Cache |
| LLM | Large Language Model |
| LoRA | Low-Rank Adaptation |
| MCP | Model Context Protocol |
| MHA | Multi-Head Attention |
| MMLU | Massively Multilingual Language Understanding |
| MoA | Mixture of Agents |
| MoE | Mixture of Experts |
| MLA | Multi-head Latent Attention |
| MLP | Multi-Layer Perceptron |
| MSA | Multi-head Latent Attention |
| NER | Named Entity Recognition |
| NLP | Natural Language Processing |
| NPU | Neural Processing Unit |
| NVFP4 | NVIDIA 4-bit Floating Point |
| ONNX | Open Neural Network |
| PCA | Principal Component Analysis |
| PEFT | Parameter-Efficient Fine-Tuning |
| PPO | Proximal Policy Optimization |
| QLoRA | Quantized LoRA |
| RAG | Retrieval-Augmented Generation |
| ReLU | Rectified Linear Unit |
| RL | Reinforcement Learning |
| RLHF | Reinforcement Learning from Human Feedback |
| RoPE | Rotary Position Embedding |
| RPS | Requests Per Second |
| RMSNorm | Root Mean Square Normalization |
| SGD | Stochastic Gradient Descent |
| SFT | Supervised Fine-Tuning |
| SIMT | Single Instruction Multiple Threads |
| SLAM | Simultaneous Localization and Mapping |
| SwiGLU | Swish-Gated Linear Unit |
| ToT | Tree of Thoughts |
| TPM | Tokens Per Minute |
| TPU | Tensor Processing Unit |
| TTS | Text-to-Speech |
| VAE | Variational Autoencoder |
| ViT | Vision Transformer |
| VLM | Vision Language Model |
| vLLM | Virtual LLM (inference engine) |
| W16A16 | Weight 16-bit, Activation 16-bit |
| ZeRO | Zero Redundancy Optimizer |

---

## Appendix B: Mathematical Notation Used in AI

| Symbol | Meaning |
|--------|---------|
| `x` | Input vector/token |
| `y` | Output/target |
| `W` | Weight matrix |
| `b` | Bias vector |
| `σ` | Sigmoid activation |
| `∇` | Gradient operator |
| `L` | Loss function |
| `η` | Learning rate |
| `θ` | Model parameters |
| `E` | Expectation |
| `softmax` | Softmax function |
| `||x||` | L2 norm of x |
| `x·y` | Dot product |
| `x × y` | Cross product |
| `R^d` | d-dimensional real space |
| `O()` | Big-O notation (complexity) |
| `μ` | Mean |
| `σ²` | Variance |
| `p(x)` | Probability distribution |

---

## Appendix C: Key Organizations & Companies

| Organization | Contribution |
|-------------|-------------|
| **OpenAI** | GPT series, DALL-E, ChatGPT, Sora |
| **Anthropic** | Claude series, Constitutional AI |
| **Google DeepMind** | Gemini, AlphaFold, Flash Attention |
| **Meta AI** | LLaMA, OPT, Segment Anything |
| **Mistral AI** | Mixtral, Mistral, open-source LLMs |
| **DeepSeek** | DeepSeek-V3/R1, MLA architecture |
| **Nous Research** | Hermes, Kracken, Yarn, OpenRouter partner |
| **Hugging Face** | Transformers library, model hub, open ecosystem |
| **Stability AI** | Stable Diffusion, open image generation |
| **Midjourney** | Commercial image generation |
| **ElevenLabs** | Voice cloning and TTS |
| **Perplexity** | AI search engine |
| **xAI (Elon Musk)** | Grok LLM |
| **Moonshot AI** | Kimi LLM |
| **MiniMax** | M2.5, voice AI |
| **Zhipu AI** | GLM series |
| **Alibaba (Qwen)** | Qwen, Qwen3, Wan video |
| **ByteDance** | Doubao LLM |
| **Cerebras** | Wafer-scale inference chips |

---

## Appendix D: Glossary Statistics

| Metric | Count |
|--------|-------|
| Total terms defined | 350+ |
| Research papers cited | 30+ |
| Free LLM APIs catalogued | 149 models / 24 providers |
| Key organizations | 20+ |
| Acronyms | 80+ |
| Mathematical symbols | 20+ |
| Topics covered | 19 domains |

---

*This glossary is a living document. Contribute via pull requests.*
*Built by Donn's Autonomous Studio — AI_DM repo, Danielhogben GitHub.*
*Licensed under CC-BY-4.0 — share freely.*
