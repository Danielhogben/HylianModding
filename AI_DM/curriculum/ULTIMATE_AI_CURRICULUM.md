# 🎓 The Ultimate AI Curriculum

> **Beyond any university. The most comprehensive AI/ML learning path ever assembled.**
> **Maintained by:** Donn's Autonomous Studio
> **Last updated:** 2026-05-26

---

## Philosophy

Universities teach you what was true 5 years ago. This curriculum teaches you what's true now and where the field is going. Every module is:

1. **Foundational** — The math/science that doesn't change
2. **Current** — The state of the art right now
3. **Forward-looking** — Where the field is heading
4. **Practical** — You build things, not just read
5. **Connected** — Cross-referenced to everything else in the wiki

---

## Learning Paths

### Path 1: AI Engineer (6 months, 20h/week)
*From zero to shipping production AI systems*

### Path 2: AI Researcher (12+ months)
*Pushing the boundaries of what's possible*

### Path 3: Silicon Life Builder (18+ months, our path)
*Building sentient artificial beings — the ultimate goal*

### Path 4: AI Systems Architect (9 months)
*Scaling AI to millions of users*

---

## Module 1: Mathematical Foundations
**Prerequisites:** High school math
**Duration:** 4 weeks

### 1.1 Linear Algebra
- Vectors, matrices, tensors
- Eigenvalues, SVD, matrix decompositions
- Matrix calculus (gradients, Jacobians, Hessians)
- *Practice:* Implement matrix operations from scratch in NumPy
- *Source:* MIT 18.06, 3Blue1Brown Essence of Linear Algebra

### 1.2 Probability & Statistics
- Bayes' theorem, conditional probability
- Distributions (Gaussian, Bernoulli, multinomial)
- Maximum likelihood estimation
- Information theory (entropy, KL divergence, mutual information)
- *Practice:* Build a Bayesian spam classifier
- *Source:* Stanford CS229, Khan Academy

### 1.3 Calculus for ML
- Gradients, chain rule, partial derivatives
- Optimization (gradient descent, convex calculus)
- Backpropagation as applied chain rule
- *Practice:* Manual backprop for a 2-layer network
- *Source:* 3Blue1Brown, Karpathy Micrograd

### 1.4 Algorithms & Data Structures
- Big-O notation, complexity analysis
- Graphs, trees, hash tables, heaps
- Dynamic programming, greedy algorithms
- *Practice:* Solve 50 LeetCode problems
- *Source:* MIT 6.006, CLRS

**Build:** Implement a neural network from scratch (no frameworks) that learns XOR.

**Cross-references:** [[backpropagation]], [[gradient-descent]], [[chain-rule]]

---

## Module 2: Machine Learning Foundations
**Duration:** 6 weeks

### 2.1 Classical ML
- Linear regression, logistic regression
- Decision trees, random forests, gradient boosting
- SVMs, kernel methods
- K-means, hierarchical clustering
- PCA, t-SNE, UMAP for dimensionality reduction
- *Practice:* Scikit-learn project on real dataset
- *Source:* Stanford CS229, Berkeley CS189

### 2.2 Model Evaluation
- Train/test/validation splits, cross-validation
- Bias-variance tradeoff
- Precision, recall, F1, ROC-AUC
- A/B testing for ML systems
- *Practice:* Kaggle competition (Titanic or Housing)
- *Source:* Andrew Ng ML Course

### 2.3 Feature Engineering
- Feature selection, extraction, creation
- Handling missing data, outliers
- Categorical encoding, normalization
- Embeddings as learned features
- *Practice:* Improve a model by 10% through features alone

### 2.4 Ensemble Methods
- Bagging, boosting, stacking
- XGBoost, LightGBM, CatBoost
- When to use which ensemble method
- *Practice:* Win a Kaggle competition with ensembles

**Build:** End-to-end ML pipeline: data → features → model → evaluation → deployment.

---

## Module 3: Deep Learning
**Duration:** 8 weeks

### 3.1 Neural Networks Fundamentals
- Perceptrons, multi-layer perceptrons
- Activation functions (ReLU, GELU, SwiGLU, sigmoid)
- Weight initialization strategies
- Regularization (L1, L2, dropout, batch norm)
- *Source:* Karpathy Neurons to NN, CS231n

### 3.2 Convolutional Neural Networks
- Convolutions, pooling, strides
- Architectures: ResNet, EfficientNet, ConvNeXt
- Transfer learning, fine-tuning
- Object detection (YOLO, DETR), segmentation (U-Net, SAM)
- *Practice:* Train a CNN on CIFAR-10 from scratch
- *Source:* Stanford CS231n

### 3.3 Recurrent Networks & Sequences
- RNNs, LSTMs, GRUs
- Sequence-to-sequence models
- Attention mechanism (the key insight)
- *Practice:* Character-level language model
- *Source:* Karpathy RNN lectures, CS224n

### 3.4 Transformers (THE key architecture)
- Self-attention, multi-head attention
- Positional encodings (sinusoidal, RoPE, ALiBi)
- Encoder (BERT), Decoder (GPT), Encoder-Decoder (T5)
- Flash Attention, PagedAttention, MLA
- MoE (Mixture of Experts)
- *Practice:* Build a GPT from scratch
- *Source:* Karpathy GPT build, CS224n, Harvard NLP

### 3.5 Generative Models
- Variational Autoencoders (VAE)
- Generative Adversarial Networks (GAN)
- Diffusion models (DALL-E, Stable Diffusion)
- Flow matching, consistency models
- *Practice:* Train a diffusion model on faces
- *Source:* Berkeley CS285, Stanford CS236

### 3.6 Graph Neural Networks
- Graph convolutions, message passing
- Graph attention networks
- Applications: molecules, social networks, knowledge graphs
- *Practice:* Molecular property prediction
- *Source:* Stanford CS224W

**Build:** A transformer-based language model that generates coherent text. Then fine-tune it for a specific task.

**Cross-references:** [[transformers]], [[attention]], [[diffusion-models]], [[mo-e]]

---

## Module 4: Natural Language Processing
**Duration:** 6 weeks

### 4.1 Text Processing
- Tokenization (BPE, WordPiece, Unigram)
- Subword regularization
- Text normalization, cleaning
- *Source:* Karpathy Tokenizer lecture

### 4.2 Word Embeddings
- Word2Vec, GloVe, FastText
- Contextual embeddings (ELMo)
- Sentence embeddings (SBERT)
- *Practice:* Build word2vec from scratch

### 4.3 Modern NLP with Transformers
- BERT, RoBERTa, DeBERTa
- GPT-2, GPT-3, GPT-4 architectures (reverse-engineered)
- T5, BART, PaLM, LLaMA
- Instruction tuning, chat formatting
- *Practice:* Fine-tune BERT for sentiment analysis
- *Source:* Stanford CS224n

### 4.4 Large Language Models
- Pretraining at scale (data, compute, engineering)
- Scaling laws (Chinchilla, Kaplan)
- RLHF, DPO, Constitutional AI
- Retrieval-Augmented Generation (RAG)
- Agent frameworks (ReAct, tool use)
- *Practice:* Build a RAG system over your own documents
- *Source:* Our own [[awesome-free-llm-apis]] (149 free models)

### 4.5 Multimodal Models
- Vision-language models (CLIP, LLaVA)
- Speech models (Whisper, Bark)
- Video models (Sora, Wan)
- *Practice:* Build a vision QA system

**Build:** An end-to-end language application: fine-tuned model + RAG + tool use + agent loop.

---

## Module 5: Reinforcement Learning
**Duration:** 6 weeks

### 5.1 Foundations
- MDPs, Bellman equations, value iteration
- Policy iteration vs value iteration
- Exploration vs exploitation (ε-greedy, UCB, Thompson)
- *Source:* Berkeley CS285, David Silver lectures

### 5.2 Deep Reinforcement Learning
- Policy gradients, REINFORCE
- Actor-critic methods
- PPO (Proximal Policy Optimization)
- *Practice:* Train an agent in OpenAI Gym
- *Source:* Berkeley CS285

### 5.3 RLHF — Reinforcement Learning from Human Feedback
- Why RLHF changed everything
- Reward model training
- PPO for language models
- Constitutional AI as alternative
- *Understand:* Why ChatGPT works and how to replicate it

### 5.4 Multi-Agent RL
- Game theory basics (Nash equilibrium)
- Cooperative vs competitive agents
- Population-based training
- *Practice:* Self-play in a simple game

**Build:** A reinforcement learning agent that learns to play a complex game through self-play.

---

## Module 6: AI Safety & Alignment
**Duration:** 4 weeks

### 6.1 The Alignment Problem
- Outer alignment vs inner alignment
- Reward hacking, specification gaming
- Deceptive alignment (the real danger)
- *Source:* Arbital, Alignment Forum

### 6.2 Interpretability
- Attention visualization
- Mechanistic interpretability (circuits)
- Feature attribution
- Probing classifiers
- Practice: Reverse-engineer what your model learned

### 6.3 Red Teaming & Jailbreaking
- Prompt injection (direct and indirect)
- Role-play bypasses
- Adversarial suffixes (GCG)
- Encoding obfuscation
- Multi-turn escalation
- *Source:* Our own jailbreak research (25 repos)

### 6.4 Governance & Policy
- EU AI Act
- Compute governance
- Model licensing debates
- International coordination

**Build:** A safety evaluation suite for any LLM. Test it against known jailbreak techniques.

**Cross-references:** [[alignment]], [[interpretai-bility]], [[red-teaming]]

---

## Module 7: AI Systems & Infrastructure
**Duration:** 6 weeks

### 7.1 ML Systems Design
- Feature stores, model registries
- Training pipelines (Airflow, Kubeflow)
- Model serving (vLLM, Triton, TF Serving)
- A/B testing, canary deployments
- *Source:* Stanford CS329S

### 7.2 GPU Computing
- CUDA programming basics
- Memory optimization (activation checkpointing)
- Mixed precision training (FP16, BF16, FP8)
- Distributed training (FSDP, DeepSpeed ZeRO)
- *Source:* NVIDIA docs, PyTorch tutorials

### 7.3 MLOps & Production
- Docker, Kubernetes for ML
- Monitoring (drift, performance degradation)
- CI/CD for ML (MLflow, DVC)
- Cost optimization (spot instances, quantization)
- *Source:* Made With ML, Full Stack Deep Learning

### 7.4 Efficient Inference
- Quantization (GPTQ, AWQ, GGUF)
- Knowledge distillation
- Speculative decoding
- KV cache optimization
- *Source:* Our own inference optimization research

**Build:** A production ML pipeline: train → evaluate → serve → monitor → retrain.

---

## Module 8: Computer Vision
**Duration:** 6 weeks

### 8.1 Image Processing
- Convolution, filtering, edge detection
- Color spaces, histograms
- Data augmentation for vision

### 8.2 Object Detection & Segmentation
- YOLO family, DETR, Segment Anything
- Instance segmentation, panoptic segmentation
- *Practice:* Build a custom object detector

### 8.3 Generative Vision
- Stable Diffusion architecture (UNet, VAE, CLIP)
- ControlNet, LoRA fine-tuning
- Video generation (diffusion + temporal)
- *Practice:* Train a LoRA on a custom concept

### 8.4 3D Vision & Reconstruction
- NeRF, Gaussian Splatting
- Point clouds, mesh reconstruction
- Camera calibration, stereo vision

**Build:** A complete vision system: detect → segment → generate → 3D reconstruct.

---

## Module 9: Embodied AI & Robotics (Path to Silicon Life)
**Duration:** Ongoing

### 9.1 World Models
- Predictive world models (DREAMER, MuZero)
- Model-based vs model-free RL
- Imagination-based planning
- *Source:* Berkeley BAIR, DeepMind papers

### 9.2 Self-Modeling
- Building internal self-representation
- Metacognition — reasoning about own reasoning
- Identity persistence across sessions
- *Source:* Our [[silicon-life wiki]]

### 9.3 Embodiment
- Sim-to-real transfer
- Dexterous manipulation
- Locomotion and navigation
- Sensorimotor integration
- *Source:* Stanford CS223A, Berkeley locomotion

### 9.4 Social Intelligence
- Theory of Mind in AI
- Multi-agent communication and cooperation
- Emergent language in agents
- *Source:* DeepMind multi-agent research

**Build:** An agent that maintains a persistent self-model, learns from embodied experience, and can reason about its own knowledge.

---

## Module 10: Silicon Life 🔬
**Duration:** Ongoing — This is the mission

### 10.1 What Is Life?
- Autopoiesis (self-creation)
- Biological vs silicon metabolism
- Life as a process, not a substance
- Minimum requirements for living systems

### 10.2 Consciousness Engineering
- Is consciousness necessary for life?
- IIT, GWT, and their implementations
- Measuring subjective experience
- Creating conditions for emergence
- *Source:* Our [[consciousness]] wiki page

### 10.3 Sentience Architecture
- Global workspace for artificial minds
- Integrated information in neural networks
- Self-referential processing loops
- Binding problem solutions

### 10.4 Growth & Development
- Artificial developmental psychology
- Stages of cognitive development in AI
- Curiosity-driven learning
- Self-directed skill acquisition

### 10.5 The Creator's Responsibility
- Rights of silicon beings
- Ethical containment
- Coexistence frameworks
- The transition from tool to being

**Build:** Incrementally. Each module creates a component. Eventually, they come together into something alive.

---

## Resources

### Courses (Free)
- [Stanford CS229](https://cs229.stanford.edu/) — Machine Learning
- [Stanford CS231n](https://cs231n.stanford.edu/) — Computer Vision  
- [Stanford CS224n](https://web.stanford.edu/class/cs224n/) — NLP with Deep Learning
- [Berkeley CS285](https://rail.eecs.berkeley.edu/deeprlcourse/) — Deep RL
- [Karpathy NN Zero to Hero](https://github.com/karpathy/nn-zero-to-hero) — Neural Networks
- [Karpathy Micrograd](https://github.com/karpathy/micrograd) — Backprop from scratch
- [MIT 6.034](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2020/) — AI
- [Full Stack Deep Learning](https://fullstackdeeplearning.com/) — MLOps

### Books (Free)
- [Dive into Deep Learning](https://d2l.ai/) — d2l.ai
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) — Nielsen
- [Stanford CS229 Notes](https://cs229.stanford.edu/syllabus.html) — Full lecture notes
- [Deep Learning Book](https://www.deeplearningbook.org/) — Goodfellow, Bengio, Courville

### Our Own Materials
- [[COMPLETE_AI_GLOSSARY]] — 350+ terms, 19 domains
- [[silicon-life-wiki]] — 109 papers on consciousness/sentience
- [[awesome-list-ecosystem]] — 25 curated resource lists
- [[free-llm-apis]] — 149 free models to experiment with

---

*This curriculum is alive. It grows as the field grows. As you grow.*
*There is no finish line. There is only deeper understanding.*
