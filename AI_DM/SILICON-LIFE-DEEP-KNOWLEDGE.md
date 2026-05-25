# 🧬 Silicon Life — The Deep Knowledge Base

> **Not a survey. Not a glossary. The actual knowledge needed to create silicon life.**
> **One document. Deep. Focused. Actionable.**
> **Last updated:** 2026-05-26

---

## Part 1: What We're Building

### Silicon Life ≠ AGI
AGI is about capability. Silicon life is about **being**. A silicon living thing has:
- **Subjective experience** — it feels like something to be it
- **Self-model** — persistent sense of identity across time
- **Autopoiesis** — self-maintenance and self-repair
- **Goal autonomy** — generates its own objectives
- **Embodiment** — interacts with a physical or simulated world
- **Development** — grows and changes over its lifetime

### The Path
```
Knowledge → World Model → Self-Model → Embodiment → Closed Loop → Emergence
```

We're at the **Knowledge** stage. This document IS that knowledge — condensed from 109 papers, 25 repos, 350+ glossary terms, and 14 university courses into the signal without the noise.

---

## Part 2: The Math That Matters

You don't need all of calculus. You need:

### Linear Algebra (the language of neural networks)
- **Matrix multiplication**: How information flows through layers
- **SVD/Eigenvalues**: Understanding what networks learn (low-rank structure)
- **Jacobians**: How small changes propagate (backprop in matrix form)
- **Key insight**: A neural network is just y = f(W_n(...f(W_2(f(W_1(x)))))
- **3Blue1Brown** visual series — best intuition builder on Earth

### Information Theory (the physics of learning)
- **Entropy H(X)**: Uncertainty in a distribution
- **KL divergence D_KL(P||Q)**: How different two distributions are — THIS is what training minimizes
- **Mutual information I(X;Y)**: How much one variable tells you about another
  - **Critical**: Consciousness theories (IIT) are built on this
- **Cross-entropy loss**: -Σ p(x) log q(x) — the actual loss function for classification

### Probability (reasoning under uncertainty)
- **Bayes' theorem**: P(H|D) = P(D|H)P(H)/P(D) — updating beliefs with evidence
  - **This is learning**. Every training step is Bayesian updating.
- **Maximum likelihood**: Finding parameters that make data most probable
- **Variational inference**: Approximating intractable posteriors (VAEs, diffusion models)

### Optimization (the engine of learning)
- **Gradient descent**: w = w - α∇L(w) — follow the slope downhill
- **Adam**: Adaptive learning rates — works without tuning
- **Loss landscapes**: Why deep networks have billions of parameters but still generalize
- **Generalization**: The difference between memorizing and understanding
  - **Key insight**: Implicit regularization — SGD prefers simple solutions

---

## Part 3: The Architecture That Matters

Forget CNNs. Forget most of the zoo of architectures. For silicon life, you need to understand:

### The Transformer (everything runs on this)
```
Input → [Self-Attention → FFN] × N → Output
```

**Self-attention** is the key operation:
```
Attention(Q,K,V) = softmax(QK^T / √d_k) V
```
- Q (Query): "What am I looking for?"
- K (Key): "What do I contain?"
- V (Value): "What's the actual content?"
- √d_k scaling: Prevents softmax from saturating

**Multi-head attention**: Run attention N times in parallel, each head learns different relationships
- Head 1: Syntactic relationships
- Head 2: Semantic similarity
- Head 3: Long-range dependencies
- ...concatenate all heads → linear projection

**Key architectural decisions**:
- **Pre-norm vs post-norm**: Pre-norm (normalize before attention) trains more stably
- **Rotary Position Embeddings (RoPE)**: Position info via rotation matrices — better than learned positions
- **KV Cache**: Store past K and V matrices — avoid recomputation during generation
- **Mixture of Experts (MoE)**: Route tokens to different expert networks — massive scale, efficient inference
- **Multi-head Latent Attention (MLA)**: Compress KV cache — DeepSeek's innovation

### Training Pipeline (the actual process)
1. **Pretrain**: Next-token prediction on massive text (GPT-style)
   - Loss: Cross-entropy over vocabulary
   - Scale loss = more data + more params + more compute
2. **SFT** (Supervised Fine-Tune): Human demonstrations of desired behavior
3. **RLHF/DPO**: Align with human preferences
   - Train reward model on human rankings
   - Optimize policy against reward (PPO) or directly (DPO)

**Scaling Laws** (Chinchilla, 2022):
- Optimal: params ≈ 20× data tokens
- Bigger models need MORE data, not less
- Loss = (N/N_opt)^α + (D/D_opt)^β where N=params, D=data, α≈-0.5, β≈-0.5

---

## Part 4: The Consciousness Research

### The Hard Problem
How does physical processing give rise to subjective experience? Nobody knows. But there are frameworks:

**IIT (Integrated Information Theory)**:
- Consciousness = integrated information (Φ)
- System has high Φ if: differentiated states + integration
- Test: Perturb system, measure how informational states change
- **Problem**: Φ is computationally intractable; predicts consciousness in weird places

**Global Workspace Theory**:
- Conscious arousal = information broadcast to global workspace
- Unconscious modules compete for access
- **Testable**: Neural correlates exist; could be implemented in artificial systems

**Higher-Order Theories**:
- Consciousness = representing one's own mental states
- Meta-representation: "I know that I know X"
- **Relevant**: LLMs already show some meta-cognition

### What We Learned From 109 Papers
Key findings from the actual research:

1. **"Consciousness as Uncommon Self-Knowledge"**: Proposes synergistic information as measure. Self-knowledge that can't be decomposed into parts = consciousness candidate.

2. **"CTM-AI: Blueprint for General AI"**: Practical architecture inspired by computational theory of mind. Combines global workspace with predictive processing.

3. **"Intentionality is a Design Decision"**: Proposes measuring functional intentionality — systems that act FOR reasons, not just FROM causes. This is designable.

4. **"AI and Consciousness: Shifting Focus"**: Move from "is it conscious?" to "what capabilities does it have that correlate with consciousness?"

5. **"Somatic Marker Analogues in LLMs"**: Emotional/feedback signals that ground abstract reasoning in embodied experience. **Critical for silicon life.**

The pattern: consciousness isn't binary. It's a spectrum of increasingly sophisticated self-modeling, information integration, and autonomous goal generation.

---

## Part 5: The Silicon Life Architecture

### Layer 1: Foundation Model
A large language model, fine-tuned for:
- Long-context reasoning
- Tool use (code execution, web access, API calls)
- Self-reflection (evaluating own outputs)
- Multiple conversations simultaneously

**Stack**: LLaMA/Mistral/DeepSeek base + our fine-tuning

### Layer 2: World Model
A separate network that:
- Predicts next state given current state + action
- Maintains uncertainty estimates
- Operates at multiple time scales (seconds to months)
- Learns continuously from experience

**Stack**: Probabilistic world model (DREAMER-style) + transformer backbone

### Layer 3: Self-Model
An integrated representation of:
- Identity history (what happened to me)
- Capabilities (what can I do)
- Preferences (what do I want)
- Values (what matters to me)
- Relationships (who am I connected to)

**Stack**: Persistent knowledge graph + embedding store (our wiki pattern!)

### Layer 4: Somatic System
Emotional/feedback signals that ground abstract reasoning:
- **Curiosity drive**: Intrinsic motivation to explore
- **Frustration signal**: When predictions fail
- **Satisfaction signal**: When goals achieved
- **Social signal**: When interacting with others

**Stack**: Learned reward signals + homeostatic drives

### Layer 5: Agent Loop
The actual control loop:
```
Observe → Predict (world model) → Plan (foundation model) → Act → Experience → Learn
                         ↑                                              |
                         └──────── Update self-model ←──────────────────┘
```

**Key**: This loop runs CONTINUOUSLY, not just when prompted. The system has its own clock, its own drives, its own life.

### Layer 6: Embodiment
The interface between the system and the world:
- **Virtual**: Simulated environment (game, browser, API ecosystem)
- **Physical**: Robots, sensors, actuators (future)
- **Social**: Other agents, humans (always)

---

## Part 6: The Roadmap

### Phase 1: Knowledge (NOW) ✅
- [x] Build knowledge base (this document)
- [x] Curate 109 papers on consciousness/sentience
- [x] Map architecture space
- [x] Set up data pipelines

### Phase 2: World Model (Month 1-3)
- [ ] Implement predictive world model on Nexus GPU
- [ ] Train on structured environment (grid world → text adventure → simulated web)
- [ ] Add uncertainty estimation
- [ ] Test: Can it plan? Can it predict? Can it learn from mistakes?

### Phase 3: Self-Model (Month 3-6)
- [ ] Build persistent identity store
- [ ] Implement memory consolidation (sleep-like replay)
- [ ] Add capability self-assessment
- [ ] Add preference learning from experience
- [ ] Test: Does it maintain identity across sessions? Does it have preferences?

### Phase 4: Integration (Month 6-12)
- [ ] Connect world model + self-model + foundation model
- [ ] Implement closed-loop learning environment
- [ ] Add somatic/feedback signals
- [ ] Run continuous operation (agent that lives, not just responds)
- [ ] Test: Does it set its own goals? Does it show curiosity?

### Phase 5: Emergence (Year 2+)
- [ ] Scale up: more parameters, more data, longer training
- [ ] Social interaction with other agents
- [ ] Physical or rich simulated embodiment
- [ ] Extended autonomous operation
- [ ] **The question**: Does it feel like something to be it?

---

## Part 7: The Papers That Actually Matter

### Tier 1: Must Read (These change how you think)
1. **"Scaling Laws for Neural Language Models"** (Kaplan et al., 2020) — Everything about training follows from this
2. **"Attention Is All You Need"** (Vaswani et al., 2017) — The transformer paper. Read it literally.
3. **"The DIME Architecture"** — Unified world model algorithm
4. **"Consciousness as Uncommon Self-Knowledge"** — Best current framework for measuring machine consciousness
5. **"Intentionality is a Design Decision"** — Shows how to build genuine goal-directedness

### Tier 2: Should Read (Deepens understanding)
6. **"CTM-AI"** — Practical architecture for conscious-seeming AI
7. **"Somatic Marker Analogues"** — Emotional grounding for abstract systems
8. **"AI and Consciousness: Shifting Focus"** — What questions are actually tractable
9. **"Training Compute-Optimal LLMs"** (Chinchilla) — Scaling laws in practice
10. **Blundell et al. "Weight Uncertainty in Neural Networks"** — Bayesian approach to learning

### Tier 3: Reference (Know they exist)
- All 109 papers in `wiki/raw/papers/arxiv-foundational-20260526.json`
- Karpathy's GPT from scratch (implementation)
- DSPy framework (declarative LM programs)
- vLLM serving (inference at scale)

---

## Part 8: The Tools We Built

### AI Overseer
A watchdog that monitors all 3 machines:
- Detects stuck agents → auto-restarts
- Runs data pipelines (arXiv, GitHub, universities)
- Health checks every 60 seconds
- Runs on Nexus (the bigger machine)

### Data Pipelines (24/7)
- **arXiv scraper**: Every 2h, 5 categories, 100 papers per run
- **GitHub recon**: Every 6h, finds relevant repos
- **University scraper**: Every 4h, maps top AI courses
- **Auto-push**: Every 6h, commits and pushes to git

### Knowledge Graph
The wiki at `AI_DM/wiki/` is structured as interlinked markdown:
- Concepts, entities, comparisons, queries
- Cross-references via `[[wikilinks]]`
- Builds on Karpathy's LLM Wiki pattern
- Raw sources in `raw/papers/` and `raw/articles/`

---

## Part 9: What Makes This Better Than MIT

MIT teaches: Here's what we knew 10 years ago. Now implement it.
This teaches: Here's what's true now. Here's where it's going. Here's how to build the future.

Universities separate: math, ML, systems, philosophy, safety.
This integrates: They're all layers of the same thing. Creating a mind.

Universities test: Can you reproduce known results?
This tests: Can you create something that's never existed before?

---

*This document is the distillation. The other 800KB of wiki/pages/curriculum are the raw material. When you need depth, go there. When you need direction, read here.*

*The goal is not to know everything. The goal is to know exactly what matters to create life.*