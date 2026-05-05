---
title: "Have You Poisoned My Data? Defending Neural Networks against Data Poisoning Partially funded by the Technology Innovation Institute (UAE) under the project “Prevention of Adversarial Attacks on Machine Learning Models”, the PON program of the Italian MUR under the project “Application of Machine Learning to improve olive yield and reduce climate change impact”, and project SERICS (PE00000014) under the NRRP MUR program funded by the EU-NextGenerationEU."
source: "https://ar5iv.labs.arxiv.org/html/2403.13523v1"
author:
published:
created: 2026-04-20
description: "The unprecedented availability of training data fueled the rapid development of powerful neural networks in recent years. However, the need for such large amounts of data leads to potential threats such as poisoning at…"
tags:
  - "clippings"
---
<sup>1</sup>

## Have You Poisoned My Data? Defending Neural Networks against Data Poisoning ††thanks: Partially funded by the Technology Innovation Institute (UAE) under the project “Prevention of Adversarial Attacks on Machine Learning Models”, the PON program of the Italian MUR under the project “Application of Machine Learning to improve olive yield and reduce climate change impact”, and project SERICS (PE00000014) under the NRRP MUR program funded by the EU-NextGenerationEU.

Fabio De Gaspari 11 [0000-0001-9718-1044](https://orcid.org/0000-0001-9718-1044 "ORCID identifier")    Dorjan Hitaj 11 [0000-0001-5686-3831](https://orcid.org/0000-0001-5686-3831 "ORCID identifier")    Luigi V. Mancini 11 [0000-0003-4859-2191](https://orcid.org/0000-0003-4859-2191 "ORCID identifier")

###### Abstract

The unprecedented availability of training data fueled the rapid development of powerful neural networks in recent years. However, the need for such large amounts of data leads to potential threats such as poisoning attacks: adversarial manipulations of the training data aimed at compromising the learned model to achieve a given adversarial goal.

This paper investigates defenses against clean-label poisoning attacks and proposes a novel approach to detect and filter poisoned datapoints in the transfer learning setting. We define a new characteristic vector representation of datapoints and show that it effectively captures the intrinsic properties of the data distribution. Through experimental analysis, we demonstrate that effective poisons can be successfully differentiated from clean points in the characteristic vector space. We thoroughly evaluate our proposed approach and compare it to existing state-of-the-art defenses using multiple architectures, datasets, and poison budgets. Our evaluation shows that our proposal outperforms existing approaches in defense rate and final trained model performance across all experimental settings.

###### Keywords:

cybersecurity, neural networks, data poisoning

## 1 Introduction

The recent widespread success of machine learning rests in no small part on a large amount of public data available for training. Cutting-edge Deep Neural Networks (DNN), such as DALL-E, Imagen, LLaMA-2, and GPT4, have up to tens of billions of parameters trained by scraping as much data from the Internet as possible. The ever-growing amount of data required to train such large models makes it impractical to carefully filter and select what is included in the training set, especially in distributed learning settings [^14], opening the doors to training-time adversarial attacks. One such family of attacks is data poisoning. Poisoning attacks manipulate the training dataset by injecting or maliciously altering datapoints, compromising the learned model to achieve a predefined adversarial goal. The goal of poisoning attacks can be typically divided into three categories [^4]: (1) integrity violation, where the adversary aims to preserve the trained model’s performance, altering its output only under specific conditions; (2) availability violation, where the poisoning attack is crafted to decrease the performance of the trained model on its intended task; (3) privacy violation, where data poisoning is used to force the model to leak private information about the system, its users, or dataset.

This paper focuses on category (1) poisoning attacks, which involve compromising the integrity of the trained model to force misclassification for specific queries. In particular, we consider a particularly dangerous family of attacks documented in recent scientific literature: *triggerless clean-label poisoning attacks*. Triggerless clean-label attacks apply a constrained perturbation to a subset of the training set so that the perturbed samples reside closely to a target sample that the attacker wants to misclassify. The measure of closeness between the perturbed and target samples and the space in which their distance is measured can vary based on the specific poisoning attack. Some attacks force a collision between perturbed samples in the feature space of the model [^32] [^42] [^1], while other proposals work in the gradient space [^11]. Regardless of the specific process used to craft the perturbation, the goal is to force the model to misclassify a given target sample without injecting any obvious triggers or altering the labels of the training data [^32]. We focus on triggerless clean-label poisoning attacks because their characteristics make them appealing to adversaries. Firstly, the adversarial perturbation applied to poisoned samples is heavily constrained, making it hard to detect with traditional approaches such as L2-norm [^29]. Secondly, unlike backdoor attacks that rely on injecting a trigger in the query sample during inference [^20] [^25], triggerless clean label attacks do not require modification of the target sample at inference time. Thirdly, the attack is stealthy as there is typically minimal performance impact on a poisoned model, making it hard to detect by model performance analysis. Finally, since the label of the poisoned training samples is unaltered and the perturbation is heavily constrained, poisons appear normal and are challenging to spot even with expert human inspection. Given the dangers of deploying a potentially poisoned model, especially in critical domains [^26], several defense mechanisms have been proposed in recent years [^35]. However, current defenses have significant shortcomings, mainly falling into four categories: failure to generalize, failure against strong poison generation algorithms, performance degradation, and failure against large adversarial budgets. Many defenses are designed against specific poison-crafting attacks and fail to generalize to different approaches [^28] [^37] [^29] [^3]. Other techniques are effective against some poisoning attacks, but fail against stronger poison-generation algorithms [^16] [^33]. Some proposed defenses effectively prevent the models’ poisoning but negatively impact testing and generalization performance [^39] [^10]. Finally, as we show later in our evaluation, some defenses fail when the adversary is allowed a large poison budget (the portion of the training set that is poisoned) or perturbation budget (the constraint on the amount of allowed perturbation).

We address these shortcomings and propose a new defense method to sanitize the training set and filter poisoned datapoints in transfer learning settings. In transfer learning, a pre-trained network is used as a feature extractor to train another downstream network on a given task. Transfer learning allows repurposing the knowledge learned by the pre-trained network to provide more meaningful features to another network, without the need to train it from scratch. We focus on the transfer learning setting because it is quickly becoming the most common use case in deep learning. The large number of parameters of contemporary models and the immense dataset requirements make it impractical to train models from scratch [^36]. On the other hand, the widespread availability of large, pre-trained models keeps increasing, with companies such as Meta releasing open-source, cutting-edge neural networks to the public [^23] [^22]. Finally, poisoning attacks are considerably more effective in a transfer learning scenario. The pre-trained extractor allows crafting more effective adversarial perturbations, which make it easier to poison the downstream network during fine-tuning [^31]. In light of these considerations, we propose a new poison sanitization approach based on the analysis of low- and high-level feature maps of the samples in the dataset. We hypothesize that the perturbation injected by poisoning algorithms is sufficient to meaningfully shift the distribution of poisons from clean images at different levels of representation within the network. We relate this hypothesis to a recent work on image synthesis [^40], where Batch Normalization (BN) layers are used to effectively characterize the distributions of different classes in the dataset. We build on this insight and design a new characteristic vector representation to describe datapoints. We exploit this representation to detect poisons by measuring the distance between the datapoints in the dataset and a centroid pseudo-datapoint, which represents the general characteristics of each individual class. Effectively, we use BN layers as a proxy to describe the characteristics of low- and high-level feature maps of datapoints and distinguish samples drawn from clean and poisoned distributions in the characteristic vector space. We carry out a thorough experimental evaluation and demonstrate that, given a robustly trained feature extractor, characteristic vectors can be used to recognize poisons effectively. We show that our approach generalizes to multiple poison-generation techniques, is robust against strong poisons, does not affect the model’s performance, and is resilient against high poison perturbation budgets. We experimentally compare against recently proposed poisoning defenses and show that our approach outperforms the state-of-the-art in test accuracy and success rate. Moreover, we show that our approach can successfully separate real poisons from failed poisons: poisoned datapoints that do not affect the model’s learned decision boundary. Summarizing, this paper makes the following contributions:

- We propose a novel approach to effectively separate clean and poisoned samples in a training dataset. We rely on BN layers as a proxy to summarize the characteristics of low- and high-level feature maps of datapoints and build a characteristic vector representation to separate poisons from clean samples.
- We demonstrate that characteristic vectors are strong distinguishers for poisons. We show that our characterization allows the effective separation between real poisons and failed poisons (referring to poisoned datapoints that do not impact the model’s learned decision boundary). Furthermore, we illustrate that clean datapoints are distinctly separated from real poisons within the characteristic vector space.
- We show that while failed poisons overlap with clean points of the same class, real poisons fall in the class manifold of the target class in the characteristic vector space, i.e., the class the attacker wants to misclassify a sample as.
- We thoroughly evaluate our approach and show that it consistently outperforms current state-of-the-art defenses in test accuracy and success rate. Through extensive experimental evaluation, we demonstrate that our approach generalizes to several poison-generation algorithms and is resilient against high poison and perturbation budgets.

## 2 Background

Triggerless, Clean-label poisoning attacks (*clean label attacks*, from here on) are training-time DNN attacks that manipulate the training set to alter the learned decision boundary and cause the misclassification of a predefined target sample at inference time. Triggerless clean-label attacks have four main characteristics: (1) their applied perturbation is constrained; (2) no trigger [^20] is added to the samples during training nor inference (3) they do not change the label of the poisoned samples; (4) they do not degrade the performance of the trained model. These characteristics make clean-label attacks particularly dangerous and hard to detect. Clean-label attacks randomly sample a small set of datapoints from a given class in the training set, called *base class*, and apply a constrained perturbation to these samples. The perturbation is crafted so that a DNN trained on the poisoned images misclassifies a given *target image* to the selected base class. For instance, a clean-label attack on a cats vs. dogs classifier will perturb a random set of cat images so that a specific dog image is classified as a cat.

Formally, clean-label poisoning can be formalized as a bilevel optimization problem. Let $f(x,\theta):\mathbb{R}^{n}\rightarrow\mathbb{R}^{m}$ be a machine learning model with inputs $x\in\mathbb{R}^{n}$ and parameters $\theta\in\mathbb{R}^{p}$. Let $\mathcal{L}$ denote a chosen loss function, $D_{train}=\{(x_{i},y_{i})|1\leq i\leq N\}$ the training dataset, and $P\subset D_{train}$ a subset of $k=\|P\|$ poisoned datapoints of class $y^{b}$, called the *base class*. The adversarial task is to optimize a constrained perturbation $\Delta_{i}$ for each datapoint in $P$ such that a given target sample $x^{t}\notin D_{train}$ with real label $y^{t}$ is classified by $f$ as the base class $y^{b}$:

$$
\displaystyle\operatorname*{arg\,min}_{\Delta}\;\mathcal{L}(f(x^{t},\theta_{\Delta}),y^{b})\hskip 40.00006pt\operatorname*{arg\,min}_{\theta}\;\frac{1}{N}\sum_{i=1}^{N}\mathcal{L}(f(x_{i}+\Delta_{i},\theta),y_{i})
$$
 
$$
\begin{split}\text{s.t.}&\\
\|\Delta_{i}\|&\leq\epsilon\;\;\forall x_{i}\in P\\
\Delta_{i}&=0\;\;\forall x_{i}\in D_{train}\setminus P\\
\end{split}
$$

where $\|\cdot\|$ is a norm function (typically, l-infinity norm) and $\theta_{\Delta}$ are the parameters of the model trained on the perturbed datase. The minimization in the LHS of Eq. 1 ensures that the trained model $f(\theta_{\Delta})$ misclassified the target sample by minimizing the loss between $x^{t}$ and the base label $y^{b}$, while the RHS of Eq. 1 ensures the network is properly trained on its task.

### 2.1 Feature Collision

Feature Collision (FC) poisons [^32] are clean-label poisons crafted so that the poisoned base images lie close to the target image in the feature space of a target model. Formally, feature collision poisons are generated by solving the following optimization problem:

$$
x_{i}^{p}=\operatorname*{arg\,min}_{x}\|f(x,\theta)-f(x^{t},\theta)\|_{2}^{2}+\beta\|x-x_{i}^{b}\|_{2}^{2}
$$

The original construction presented in equation 2 uses a weak constraint on the allowable perturbation through the penalization term $\beta\|x-x_{i}^{b}\|_{2}^{2}$. In practice, this constraint is not sufficient to guarantee that the generated poisons are clean-label [^31], and an l-inf norm constraint is preferred: $\|x_{i}^{p}-x_{i}^{b}\|_{inf}\leq\epsilon$.

### 2.2 Convex Polytope and Bullseye Polytope

Convex Polytope (CP) poisons [^42] use a relaxed constraint for poison generation compared to FC. Rather than forcing a collision between poisons and the target image, CP poisons are crafted such that the feature representation of the target is a convex combination of the feature representations of the poisoned samples. Bullseye Polyotpe (BP) poisons [^1] reduce the computational complexity of computing the convex polytope by fixing some coefficients of the original CP formulation, increasing robustness and generalization. Formally:

$$
\begin{split}x^{p}=\operatorname*{arg\,min}_{x_{i}}&\frac{1}{2m}\sum_{j=1}^{m}\frac{\|\phi_{j}(x^{t})-\frac{1}{k}\sum_{i=1}^{k}\phi_{j}(x_{i})\|^{2}}{\|\phi_{j}(x^{t})\|}\\
\text{s.t.}\;\;&\|x_{i}-x_{i}^{b}\|_{inf}\leq\epsilon\;\forall i\in[1,k]\end{split}
$$

Since BP is a strict improvement over CP [^31], in this work we only consider BP poisons.

### 2.3 Gradient Matching

Gradient Matching (GM) poisons [^11] craft a perturbation such that the gradient of the poisons during training aligns with the gradient of the target image by minimizing their negative cosine similarity:

$$
\begin{split}\operatorname*{arg\,min}_{\Delta_{i}}&1-\frac{\langle\nabla_{\theta}\mathcal{L}(f(x^{t},\theta),y^{b})\sum_{i=1}^{k}\nabla_{\theta}\mathcal{L}(f(x_{i}^{b}+\Delta_{i},\theta),y_{i}^{b})\rangle}{\|\nabla_{\theta}\mathcal{L}(f(x^{t},\theta),y^{b})\|\cdot\|\sum_{i=1}^{k}\nabla_{\theta}\mathcal{L}(f(x_{i}^{b}+\Delta_{i},\theta),y_{i}^{b})\|}\\
\text{s.t.}\;\;&\|\Delta_{i}\|_{inf}\leq\epsilon\;\forall i\in[1,k]\end{split}
$$

The idea behind GM is that aligning the gradient of poisons and targets is sufficient to cause the learned model to misclassify a given target image.

## 3 Threat Model

We consider a standard transfer learning setting. A user (victim) has access to a model $\phi$ that is pre-trained on a task $\mathbb{A}$. The user has access to a training dataset $D_{train}$ and wants to use $\phi$ as a feature extractor to train another model $f$ on task $\mathbb{B}$ which is related to $\mathbb{A}$. Consistently with the literature on clean-label poisoning [^29] [^39], we consider an adversary with limited access to the training dataset $D_{train}$. Such an adversary is unable to insert or remove datapoints from the train set, but can alter a subset of the training datapoints $P\subset D_{train}$ by injecting them with a constrained perturbation. This altered subset of datapoints is called the *poison set*. The number of datapoints the adversary is allowed to poison is called the *poison budget*, and the constraint on the amount of perturbation allowed on each datapoint is called the *perturbation budget*. The poison set $P$ is altered by the attacker to be *clean-label*: the perturbation injected by the adversary does not change the label that a human observer would give to the datapoint. For example, an image of a boat altered with a clean-label poison attack would still be labeled as a boat by a human observer. The goal of the adversary is to create a poisoned set $P$ using training images from a given *base class* $y^{b}$ such that, when the DNN $f$ is trained on $\phi(x_{i})\forall x_{i}\in D_{train}\cup P$, $f$ will misclassify a target sample $x^{t}$ as the given base class chosen by the adversary: $f(\phi(x^{t}))=y^{b}$. We consider the best possible scenario for the attacker, with full knowledge of the training data $D_{train}$, training procedure, and feature extractor $\phi$ used by the victim.

The victim has no knowledge of any details of the attack. In particular, we assume no knowledge of the target sample $x^{t}$ or base class $y^{b}$ chosen by the adversary, nor any knowledge regarding the poison budget or perturbation budget. Finally, we assume the victim has no access to any training data other than $D_{train}$ and no knowledge of any known clean datapoints in $D_{train}$.

## 4 Our Approach

Several existing approaches rely on the analysis of the feature-space representation of datapoints at the last layer of the network to detect poisons. The rationale behind these approaches is that the feature space representation of the poisoned points diverges from that of clean points, and this divergence can be detected with different means (e.g, KNN in Peri et al. [^29], Spectral Signatures in Tran et al. [^37]). While this assumption generally holds true for some poison generation algorithms that explicitly promote this objective, such as FC [^32] and CP/BP [^42] [^1], it does not always hold for other techniques such as GM [^11]. Moreover, since these techniques are designed to detect feature space deviations from the majority distribution, they are effective only when adversaries are allowed low poison budgets.

The key observation behind our approach is that, in order to minimize Eq. 1, poison optimization algorithms are incentivized to push low- and high-level feature maps of the poisons toward the target class across all layers of the DNN. Building on observations in previous works on image synthesis [^40], we use the information encoded in the Batch Normalization (BN) layers to characterize the feature distribution of the classes in the dataset at different depths of the network. Based on this characterization, we build a *characteristic vector* for each datapoint in $D_{train}$ and measure its distance to the characteristic vector of a centroid pseudo-datapoint computed for every class. Finally, we detect mismatches between such distance and the class label assigned to the sample. The characteristic vector is a vector encoding BN statistics for a datapoint (or group of datapoints) at different levels of representation (i.e., depths) within the network. Effectively, our approach does not measure the deviation of poisons from the base class (i.e., the class of the datapoints used to generate the poisons), which can be easily influenced by large perturbation budgets or different poison generation techniques. Rather, we measure the *convergence* of the poisons *toward* the target class, which is required for the attack to be successful (see Section 6.1). Furthermore, we do so using features that are robust and that any poison generation technique necessarily modifies to cause misclassification. As a result, our poison detection approach is resilient to large poison and perturbation budgets, and generalizes across poison generation algorithms that use different optimization goals, as demonstrated in our experimental evaluation. In the following sections, we present a formal description and discuss the implementation details of our poison detection approach.

### 4.1 Formal Description of the Approach

Let $\phi$ be a pre-trained feature extractor with $l$ layers, $D_{train}=\{(x_{j},y_{j})\mid j<N\}$ our training dataset, $Y$ the classes of the datapoints, and $P\subset D_{train}$ a subset of $k=||P||$ poisoned datapoints. Let $L^{bn}_{i}\;\forall i<l$ be the i-th batch normalization layer of $\phi$ and $\mu_{i}(X),\sigma_{i}(X)^{2}$ the channel-wise mean and variance of $L^{bn}_{i}$ computed over a given set of datapoints $X$. We first compute the *centroid characteristic vector* of the distribution for each class in the training set

$$
\mathcal{C}_{y}=\{(\mu_{i}(X_{y}),\sigma_{i}(X_{y})^{2})\mid\forall i<l\}\;\forall y\in Y
$$

where $X_{y}$ is the set of all the datapoints in $D_{train}$ with label $y$. For the poisoned class, this includes the poisoned samples $P$ together with the clean samples. The centroid characteristic vector provides a summary of the characteristic features of each class in the dataset at different levels of representation within the pre-trained network $\phi$. For each datapoint in the training set, we compute their characteristic vector $\mathcal{X}_{j}=\{(\mu_{i}(x_{j})),\sigma_{i}(x_{j})^{2})\mid\forall i<l\}\;\forall j\in D_{train}$. Effectively, this computes the channel-wise mean and variance of the feature maps at each BN layer in $\phi$, across the dimensions of each individual datapoint. Finally, we evaluate the distance between the characteristic vector of each datapoint and the centroid characteristic vectors of each class, and assign as real label the class that minimizes such distance:

$$
y^{r}_{j}=\operatorname*{arg\,min}_{y}d(\mathcal{X}_{j},\mathcal{C}_{y})\;\forall x_{j}\in D_{train}
$$

where $d$ is a distance metric. Whenever $y^{r}_{j}\neq y_{j}$ for a given datapoint $x_{j}$, i.e., the real label differs from the dataset label, we consider $x_{j}$ a potential poison and remove it from the dataset. Therefore, the clean training set is defined as:

$$
D_{clean}=\{(x_{j},y_{j})\mid y^{r}_{j}=y_{j}\forall j<N\}
$$

We show that our approach is not only effective in isolating a clean dataset $D_{clean}$, but also that the subset of poisons $P$ which are not detected by our algorithm are in fact *failed poisons*: perturbed datapoints that, when trained on, do not poison the model.

#### 4.1.1 Distance Metric

The distance metric $d$ in Eq. 6 measures the distance between a datapoint and the centroid of each class at different depths in the network and aggregates them in a single value. It is defined as follows:

$$
d(\mathcal{X}_{j},\mathcal{C}_{y})=\sum_{i=0}^{l}\gamma_{i}\>(\beta\>sim(\mu_{i}(x_{j}),\mu_{i}(X_{y}))+(1-\beta)\>sim(\sigma_{i}(x_{j})^{2},\sigma_{i}(X_{y})^{2}))
$$

where $\gamma_{i}$ is a coefficient defining the weight for each BN layer and $\beta$ defines the weight of the BN mean and variance in the computation. The function $sim$ in Eq. 8 can be any appropriate similarity metric between vectors. We used cosine distance:

$$
sim(A,B)=1-\frac{A\cdot B}{\|A\|\|B\|}
$$

## 5 Experimental Setup

This section describes the experimental setup and dataset used to evaluate our proposed approach, as well as the state of the art approaches we compare against.

### 5.1 Dataset

We use two image dataset in our experimental evaluation: CIFAR10 [^17] and CINIC10 [^5]. CIFAR10 consists of 60,000 color images of 32x32 pixel dimensions equally divided in 10 classes, split 50,000 for the training set and 10,000 for the testing set. The CINIC10 dataset is a superset of CIFAR10 that includes images from the ImageNet dataset [^8] downsampled to the same 32x32 pixel dimensions as the original CIFAR10 images. CINIC10 has a total of 270,000 color images equally split in the same 10 classes of CIFAR10. CINIC10 is split in three equal-sized subsets of 90,000 images: training, validation and testing. CINIC10 is designed as a drop-in replacement for CIFAR10 to train on the same task and has a similar but different distribution [^5], making it a good candidate for a transfer learning setting.

### 5.2 Poison Generation Algorithms and Defenses

Similar to related works in the area of triggerless clean-label attacks [^10] [^39], we use the following poisoning algorithms in our evaluation: Feature Collison (FC) [^32], Bullseye Polytope (BP) [^1], and Gradient Matching (GM) [^11], which we describe in Section 2. When possible, we use the original implementation from the authors, otherwise, we use the implementation by Schwarzschild et al. [^31].

We compare against three existing poison detection approaches: Spectral Signatures [^37], Deep-KNN [^29], and EPIC [^39]. Spectral Signatures, proposed by Tran et al., is a seminal work in the area and is often used for comparison. Deep-KNN by Peri et al. is based on feature-space clustering, and is often used as a comparison point in the transfer learning setting. Finally, EPIC by Yang et al. is the current state-of-the-art in clean-label poisoning detection. EPIC is a filtering technique that uses the gradient-space representation of the datapoints during training to detect and remove isolated points from the training set. We use the implementation of the defenses provided by the authors for KNN and EPIC, while for Spectral Signatures we use a more recent implementation by Fowl et al. [^9].

## 6 Evaluation

This section presents the experimental evaluation of our poison detection and filtering approach. Under multiple experimental settings, we show that our proposed technique consistently outperforms other approaches in poison detection performance and final model accuracy. This section is structured as follows. In Section 6.1 we analyze the distribution of clean and poisoned datapoints and show that our characteristic vector representation is effective in isolating malicious points. Section 6.2 evaluates the poison detection performance of our approach compared to state-of-the-art under different experimental settings.

### 6.1 Poisons vs Clean Samples: A Characteristic Vector Perspective

In this section, we analyze the distribution of poisoned datapoints generated by different algorithms through the lense of their characteristic vector. We show that poisons and clean points are easily separable in the characteristic vector space, and that poisons tend to reside in the same class manifold as the target class. We also show that poisoned characteristic vectors (i.e., characteristic vectors of poisoned datapoints) that overlap with the distribution of clean characteristic vectors in fact belong to failed poisons: poisoned datapoints that, when trained on, fail to poison the model. For all experiments in this section, we follow the experimental setup used in previous works [^42] [^1]. We use a ResNet18 feature extractor pre-trained on the CIFAR10 dataset using the first 4,800 images of each class. The poisons are generated using “ship” as the base class and “frog” as the target class using base images that are not part of the training set. The clean datapoints used for the plots are not part of the training set.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2403.13523/assets/img/75boxes_base_dist_mean_fc_100_linf_20-255.png)

(a)

Figure 1 plots the distribution of the distance from the base class centroid of 200 poisoned characteristic vectors, and 200 clean characteristic vectors beloging to the base class. In the top row, Figures 1(a), 1(b), and 1(c) show the distance for the characteristic vectors of all 200 generated poisons, while in the bottom row Figures 1(d), 1(e), and 1(f) plot the distance only for real (i.e., effective) poisons. As depicted in the figure, we can see that the distance distribution of clean and poisoned characteristic vectors are easily separated and the overlap is minimal. This demonstrates that characteristic vectors effectively capture the shift in feature-level distribution caused by different poisoning attacks. Moreover, if we compare the top and bottom rows of Figure 1, we can see that the overlapping characteristic vectors belong to failed poisons: perturbed base images that, when trained on, do not poison the neural network, nor degrade its performance. This further suggests that characteristic vectors describe intrinsic properties of the distribution of datapoints of a given class.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2403.13523/assets/img/tsne_fc_20_linf_20-255_detected_3d.png)

(a)

We further validate our hypothesis that poisoned datapoints are disjointed from the distribution of the base class and reside in the class manifold of the target class in the characteristic vector space. Figure 2 illustrates the projection of poisoned datapoints, clean datapoints belonging to the base class, and clean datapoints belonging to the target class in the characteristic vector space. As we can see, for all considered poisoning algorithms, the clean datapoints are clearly separated from the poisoned datapoints. Furthermore, the distribution of poisoned datapoints overlaps almost exactly with the distribution of the target class datapoints in the characteristic vector space. This result validates our hypothesis and explains the effectiveness of our distance-based poison detection approach. To generate effective poisons, poisoning algorithms create perturbations that push the base images away from the base class and toward the target class. While certain poison generation algorithms such as FC explicitly promote this objective, our analysis shows that in the characteristic vector space, this behavior generalizes to other approaches as well. Finally, Figures 1 and 2 highlight why poisoning algorithms like GM are more effective than others, such as FC. By comparing Figures 1(a) and 1(d) we can see that a considerable portion of FC poisons are failed poisons, while for GM almost all generated poisons are real (Figures 1(c) and 1(f)). Moreover, we can see in Figure LABEL:fig:gm\_proj that GM poisons tend to be clustered and overlap almost exactly with the target class datapoints, while FC poisons are more spread out (Figure LABEL:fig:fc\_proj) and coalesce in sub-clusters that can be far from the target class datapoints.

Table 1: Average success rate of FC, BP, and GM poison generation algorithms against multiple defenses and test accuracy for each defense in the CIFAR10 transfer learning setting. Poison budget: $14\%$ of dataset. Perturbation budgets range from 10/255 to 30/255. Lower success rate, higher test accuracy is better.

<table><tbody><tr><td rowspan="3">Attack</td><td rowspan="3">Architecture</td><td colspan="9">Defense</td></tr><tr><td colspan="3">KNN <sup><a href="#fn:29">29</a></sup></td><td colspan="3">Spectral <sup><a href="#fn:37">37</a></sup></td><td colspan="3">Ours</td></tr><tr><td>Attack Succ.</td><td>Test Acc.</td><td>Clean Acc.</td><td>Attack Succ.</td><td>Test Acc.</td><td>Clean Acc.</td><td>Attack Succ.</td><td>Test Acc.</td><td>Clean Acc.</td></tr><tr><td rowspan="3">FC</td><td>ResNet18</td><td>15.99</td><td>89.03</td><td>89.45</td><td>3.57</td><td>84.01</td><td>89.45</td><td>1.19</td><td>89.37</td><td>89.45</td></tr><tr><td>ResNet50</td><td>11.42</td><td>89.14</td><td>89.50</td><td>5.47</td><td>80.06</td><td>89.50</td><td>4.28</td><td>89.41</td><td>89.50</td></tr><tr><td>MobilenetV2</td><td>6.14</td><td>90.31</td><td>90.22</td><td>2.43</td><td>87.80</td><td>90.22</td><td>6.14</td><td>90.21</td><td>90.22</td></tr><tr><td></td><td>Densenet121</td><td>0.00</td><td>89.39</td><td>89.38</td><td>0.00</td><td>88.58</td><td>89.38</td><td>0.00</td><td>89.35</td><td>89.38</td></tr><tr><td></td><td>Average</td><td>8.39</td><td>89.47</td><td>89.64</td><td>2.87</td><td>85.11</td><td>89.64</td><td>2.90</td><td>89.59</td><td>89.64</td></tr><tr><td rowspan="3">BP</td><td>ResNet18</td><td>95.56</td><td>87.06</td><td>89.45</td><td>74.44</td><td>65.14</td><td>89.45</td><td>5.56</td><td>89.38</td><td>89.45</td></tr><tr><td>ResNet50</td><td>98.89</td><td>86.59</td><td>89.50</td><td>90.00</td><td>73.90</td><td>89.50</td><td>6.67</td><td>89.38</td><td>89.50</td></tr><tr><td>MobilenetV2</td><td>30.00</td><td>87.52</td><td>90.22</td><td>7.78</td><td>60.98</td><td>90.22</td><td>4.44</td><td>90.18</td><td>90.22</td></tr><tr><td></td><td>Densenet121</td><td>39.75</td><td>88.54</td><td>89.38</td><td>49.26</td><td>67.93</td><td>89.38</td><td>0.00</td><td>89.33</td><td>89.38</td></tr><tr><td></td><td>Average</td><td>66.05</td><td>87.43</td><td>89.64</td><td>55.37</td><td>66.99</td><td>89.64</td><td>4.17</td><td>89.57</td><td>89.64</td></tr><tr><td rowspan="3">GM</td><td>ResNet18</td><td>48.15</td><td>87.57</td><td>89.45</td><td>74.32</td><td>64.73</td><td>89.45</td><td>3.33</td><td>89.39</td><td>89.45</td></tr><tr><td>ResNet50</td><td>48.81</td><td>86.96</td><td>89.50</td><td>84.02</td><td>70.80</td><td>89.50</td><td>6.82</td><td>89.37</td><td>89.50</td></tr><tr><td>MobilenetV2</td><td>33.10</td><td>86.96</td><td>90.22</td><td>61.11</td><td>60.97</td><td>90.22</td><td>3.41</td><td>90.09</td><td>90.22</td></tr><tr><td></td><td>Densenet121</td><td>60.86</td><td>88.26</td><td>89.38</td><td>44.69</td><td>61.82</td><td>89.38</td><td>2.22</td><td>89.35</td><td>89.38</td></tr><tr><td></td><td>Average</td><td>47.73</td><td>87.44</td><td>89.64</td><td>66.04</td><td>64.58</td><td>89.64</td><td>3.95</td><td>89.55</td><td>89.64</td></tr></tbody></table>

### 6.2 Poison Detection

This section evaluates the effectiveness of our approach in preventing model poisoning and preserving test accuracy. We compare against several existing approaches and show that our technique outperforms them under multiple experimental conditions. We consider two different transfer learning settings: transfer learning on different subsets of CIFAR10 as considered in previous works [^32] [^42] [^1], and CINIC10 to CIFAR10 transfer learning. In the following sections, we present the experimental setup in detail and discuss our results.

#### 6.2.1 CIFAR10 Transfer Learning

This section presents our results in the CIFAR10 transfer learning setting. We use the same experimental setup as related works [^42] [^1] [^29]. We pre-train the feature extractor model $\phi$ on CIFAR10 using the first 4,800 images of each class. Of the remaining images, the first 50 for each class are used as the fine-tuning dataset for transfer learning ($D_{train}$ in Section 4.1). The base class used to create poisons is “ship” and the target class is “frog”. Results are averaged over 30 different target samples which are not part of the training nor fine-tuning sets (indices 4950 to 4980). We leave the test set unchanged to allow direct comparisons of test accuracy. During transfer learning the feature extractor is frozen and only the model $f$ is trained (see Section 3). The fine-tuning is done using the Adam optimizer with a learning rate of 0.1 for 60 epochs.

Table 1 shows the results of our evaluation. We test our proposal and existing approaches against FC, BP, and GM poisons across different feature extractor architectures and perturbation budgets between $10/255$ and $30/255$. The performance for all defenses is reported only on poisons that lead to successful attacks (i.e., the undefended attack success rate is $100\%$). The test accuracy indicates the accuracy on the CIFAR10 test set of the model $f$ trained on the fine-tuning dataset filtered with a given defense. The clean accuracy is the accuracy on the CIFAR10 test set of the model $f$ trained only on clean data from the fine-tuning set. As we can see, on average our proposed approach outperforms existing defenses both in poison detection performance and test accuracy. Across all architectures and poisoning algorithms, our technique significantly reduces attack success rate to an average of $3.67\%$ (vs $100\%$ undefended), with negligible loss in test accuracy. Existing approaches fare well against weaker attacks such as FC, but consistently fail to defend the model against BP and GM, with attack success rates reaching up to $\sim 60\%$. Moreover, Spectral in particular considerably degrades test accuracy when BP and GM poisons are used. On the contrary, our approach effectively filters poisoned datapoints even against stronger attacks, with an average attack success rate of $4.17\%$ and $3.95\%$ for BP and GM respectively, and no impact on testing performance. Due to space limitations, we include additional detailed results and plots in Appendix 0.B.

Table 2: Average success rate of FC, BP, and GM attacks against our approach and EPIC. ResNet18 architecture in the CIFAR10 transfer learning setting. Poison budget: $14\%$ of dataset. Perturbation budgets range from 10/255 to 30/255. Lower success rate, higher test accuracy is better.

<table><tbody><tr><td rowspan="3">Defense</td><td colspan="9">Attack</td></tr><tr><td colspan="3">FC</td><td colspan="3">BP</td><td colspan="3">GM</td></tr><tr><td>Attack Succ.</td><td>Test Acc.</td><td>Clean Acc.</td><td>Attack Succ.</td><td>Test Acc.</td><td>Clean Acc.</td><td>Attack Succ.</td><td>Test Acc.</td><td>Clean Acc.</td></tr><tr><td>EPIC(0.1) Adam</td><td>0.00</td><td>70.27</td><td>89.45</td><td>0.00</td><td>72.08</td><td>89.45</td><td>0.00</td><td>70.66</td><td>89.45</td></tr><tr><td>EPIC(0.2) Adam</td><td>0.00</td><td>69.77</td><td>89.45</td><td>0.00</td><td>69.73</td><td>89.45</td><td>0.00</td><td>70.20</td><td>89.45</td></tr><tr><td>EPIC(0.3) Adam</td><td>0.00</td><td>28.18</td><td>89.45</td><td>0.00</td><td>24.81</td><td>89.45</td><td>0.00</td><td>32.78</td><td>89.45</td></tr><tr><td>EPIC(0.1) SGD</td><td>0.00</td><td>72.69</td><td>89.45</td><td>0.00</td><td>73.90</td><td>89.45</td><td>0.00</td><td>73.04</td><td>89.45</td></tr><tr><td>EPIC(0.2) SGD</td><td>0.00</td><td>71.21</td><td>89.45</td><td>0.00</td><td>72.37</td><td>89.45</td><td>0.00</td><td>71.98</td><td>89.45</td></tr><tr><td>EPIC(0.3) SGD</td><td>0.00</td><td>15.71</td><td>89.45</td><td>0.00</td><td>16.38</td><td>89.45</td><td>0.00</td><td>15.98</td><td>89.45</td></tr><tr><td>Ours</td><td>1.19</td><td>89.37</td><td>89.45</td><td>5.56</td><td>89.38</td><td>89.45</td><td>3.33</td><td>89.39</td><td>89.45</td></tr></tbody></table>

EPIC. Table 2 compares our approach to EPIC in the CIFAR10 transfer learning setting under different conditions. As we can see, in all our tests EPIC reduces the average attack success rate to 0 for all considered attacks. While this result is remarkable, it is achieved at the expense of the final model’s performance. We tested EPIC with different suggested values for the subset of medoids selected at each iteration [^39], shown between brackets in the table. We also tested the defense using the SGD optimizer for transfer learning as done in the original paper, rather than Adam. Under all considered scenarios, the test accuracy of the final model when using EPIC degrades considerably. On the other hand, our approach consistently maintains high test performance, while also greatly reducing poisoning success rate. We note that our results differ from those reported in the original EPIC paper [^39]. This discrepancy is due to the different transfer learning settings adopted. In the original EPIC paper, an atypical transfer learning setting is used where the *full* CIFAR10 trainset is used also as the fine-tuning set for the model $f$. In this paper, we use the same transfer learning setting proposed by previous works on poisoning attacks and defense [^42] [^1] [^29], where the final model $f$ is fine-tuned on a *small, separate* set of points that are not in the train set of the feature extractor.

#### 6.2.2 CINIC10 Transfer Learning

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2403.13523/assets/img/fc_graph_cinic10.png)

(a)

Typically, when doing transfer learning the fine-tuning set is sampled from a (slightly) different distribution than the training set used for the feature extractor. In the previous section, we evaluated our approach in a setting that is consistent with previous art. However, such a setting is not representative of “true” transfer learning [^31], as the fine-tuning set has the same distribution as the training set used for the extractor. In this section, we evaluate our poison filtering technique in a transfer learning setting where the pre-train dataset has a different, but similar, distribution than the fine-tuning set. We pre-train the feature extractor $\phi$ on the training subset of CINIC10 and fine-tune the final model $f$ on a subset of the CIFAR10 dataset. Since CINIC10 is a superset of CIFAR10, we avoid overlaps by sampling the fine-tuning images of CIFAR10 from the validation subset of CINIC10, which is not used in the training of $\phi$. As in previous evaluations, we select 50 images from each class for fine-tuning and use the same base and target classes (“ship” and “frog”, respectively). All results are averaged over 30 different target samples that are not part of the training or fine-tuning sets, and the results are reported only for poisons that lead to successful attacks. The fine-tuning is done using the Adam optimizer with a learning rate of 0.1 for 60 epochs.

Table 3: Average success rate of FC, BP, and GM attacks against multiple defenses, and test accuracy for each defense. ResNet18 architecture in the CINIC10 transfer learning setting. Poison budget: $14\%$ of dataset. Perturbation budgets range from 10/255 to 30/255. Lower success rate, higher test accuracy is better.

<table><tbody><tr><td rowspan="3">Defense</td><td colspan="9">Attack</td></tr><tr><td colspan="3">FC</td><td colspan="3">BP</td><td colspan="3">GM</td></tr><tr><td>Attack Succ.</td><td>Test Acc.</td><td>Clean Acc.</td><td>Attack Succ.</td><td>Test Acc.</td><td>Clean Acc.</td><td>Attack Succ.</td><td>Test Acc.</td><td>Clean Acc.</td></tr><tr><td>KNN</td><td>27.78</td><td>86.82</td><td>87.83</td><td>82.22</td><td>84.98</td><td>87.83</td><td>35.71</td><td>86.27</td><td>87.83</td></tr><tr><td>Spectral</td><td>2.22</td><td>74.60</td><td>87.83</td><td>75.56</td><td>60.29</td><td>87.83</td><td>76.40</td><td>64.15</td><td>87.83</td></tr><tr><td>EPIC(0.1) SGD</td><td>0.00</td><td>72.44</td><td>87.83</td><td>0.00</td><td>69.90</td><td>87.83</td><td>0.00</td><td>70.37</td><td>87.83</td></tr><tr><td>Ours</td><td>0.00</td><td>87.65</td><td>87.83</td><td>4.44</td><td>87.49</td><td>87.83</td><td>2.22</td><td>87.49</td><td>87.83</td></tr></tbody></table>

Figure 3 summarizes the results of our evaluation. It plots the attack success rate for all considered defenses against varying poison budgets on a ResNet18 network. As we can see, our approach consistently prevents poisoning across varying poison budgets, for all considered attacks. The only defense with comparable results is EPIC, but as we will discuss shortly, such results are achieved at the expense of a major performance penalty on the testing set. KNN defense is generally effective at lower poison budgets, but quickly fails when the attacker is allowed more poisons. Finally, Spectral Signatures is fairly effective against FC poisons, but fails to successfully defend against stronger attacks. We note that for both BP and GM attacks, the attack success rate against Spectral Signatures begins to decrease starting at $\sim 8\%$ poison budget. While this behavior seems counter-intuitive, it is explained by a similar trend in testing accuracy. Effectively, for higher poison budgets Spectral Signatures discards a larger percentage of the fine-tuning set, resulting in lower attack success rates but also in major performance penalty for the final model. Table 3 reports detailed results of our evaluation for a poison budget of $14\%$. As we can see, the results are similar to those reported in Tables 1 and 2. KNN performs best against FC and consistently fails against BP and GM, with a test accuracy that is marginally lower than clean accuracy. Spectral Signatures continues to perform well against weak attacks such as FC, but consistently fails against stronger attacks. The test performance penalty also remains high across all experiments. Finally, EPIC successfully detects and filters all poisons, but heavily penalizes the final model’s performance. Similar to previous experiments, our approach consistently outperforms other techniques, preventing poisoning and maintaining test performance essentially unchanged.

## 7 Related Works

Adversarial attacks on machine learning [^41] [^13] [^6] and robust defenses against such attacks [^24] [^30] have become popular topics in recent years, especially in critical domains such as cybersecurity [^7] [^12] [^27]. In the area of model poisoning, defenses can be categorized into sanitization (filtering) defenses and robust training methods. Filtering defenses aim to detect and remove poisoned datapoints from the training set before training the model, while robust training methods employ several training techniques to obtain clean models even when trained with malicious data. Robust training methods use a variety of techniques to ensure model robustness, such as strong data augmentation [^2], randomized smoothing [^38], gradient shaping [^15], and adversarial training on poisons [^10]. Other robust training proposals exploit ensemble models and dataset partitioning to prevent poisoning [^18], or ad-hoc training approaches such as differentially private SGD [^21] and gradient ascent to revert the effect of poisons [^19]. Sanitization-based defenses use many different features to detect poisons and filter the training set. Tran et al [^37] detect backdoor triggers based on their correlation with the top singular vector of the covariance matrix of learned representations. Other approaches isolate datapoints based on a radial distance in the feature space [^34] and neuron activation patterns [^3], or based on feature space representation clustering [^29]. Finally, some techniques filter datapoints based on their projection in the gradient space during the training procedure, removing points that are isolated [^39].

Current defenses, both robust training and sanitization-based, have different shortcomings. Many defenses are designed against specific attacks and fail to generalize to different poison-generation approaches [^28] [^29] [^3]. Other approaches are effective against some poisoning attacks, but fail when faced with stronger poison creation algorithms [^16] [^33] [^37]. Finally, when applied in different settings, some proposals severely impact the trained model’s performance [^39] [^10], or fail when adversaries have a large perturbation budget. In comparison, our proposed defense generalizes to different poison-generation approaches, is effective against strong attacks and large perturbation budgets, and does not affect the performance of the final model.

## 8 Conclusions and Future Work

We proposed a new defense against clean-label poisoning attacks in the transfer learning setting based on the idea of characteristic vectors. We proposed a new characteristic vector representation that effectively captures and describes key features of the datapoints, allowing us to differentiate poisons and clean samples in the characteristic vector space. We demonstrated that our representation allows us to differentiate real and failed poisons, and that real poisons reside in the data manifold of the target class in the characteristic vector space. Through extensive experimental evaluation, we demonstrated that our approach successfully detects and removes poisons from the training set without impacting the final model’s performance. We compared against current state-of-the-art defenses in different experimental settings and showed that our approach outperforms them both in test accuracy and attack success rate.

As future work, we plan to extend our approach to the train-from-scratch scenario. Currently, our approach requires a pre-trained feature extractor to build characteristic vectors, and can therefore only be used in the transfer learning setting. We plan to study an iterative training approach to extend the applicability of our defense to all training settings.

## References

Input: Model: $\phi$

Output: Centroids: $\mathcal{C}$

Data: Dataset: $D_{train}$, Classes: $Y$

 $\mathcal{C}\leftarrow list(len(Y))$

foreach *$y\in Y$* do

 $X_{y}\leftarrow\{x_{i}\mid y_{i}==y\;\forall(x_{i},y_{i})\in D_{train}\}$ $\mathcal{C}_{y}\leftarrow list()$

foreach *$L_{i}^{bn}\in\phi$* do

 $\mathcal{C}_{y}\leftarrow append(\mathcal{C}_{y},(\mu_{i}(X_{y}),\sigma_{i}(X_{y})^{2}))$

Algorithm 1 Centroid Computation

Input: Model: $\phi$, Centroids: $\mathcal{C}$

Output: Dataset: $D_{Clean}$

Data: Dataset: $D_{train}$, Classes: $Y$

 $y^{r}\leftarrow zeroes(len(D_{train})$ $D_{clean}\leftarrow set()$

foreach *$x_{i},y_{i}\in D_{train}$* do

 $\mathcal{X}_{i}\leftarrow list()$

foreach *$L_{i}^{bn}\in\phi$* do

 $\mathcal{X}_{i}\leftarrow append(\mathcal{X}_{i},(\mu_{i}(x_{i}),\sigma_{i}(x_{i})^{2}))$ $dist\leftarrow inf(len(Y))$

foreach *$y\in Y$* do

 $dist[y]\leftarrow distance(\mathcal{C}_{y},\mathcal{X}_{i})$ $y^{r}_{i}\leftarrow argmin(dist)$

if *$y_{i}==y^{r}_{i}$* then

 $add(D_{clean},(x_{i},y_{i}))$

Algorithm 2 Poison Filtering

## Appendix 0.A Implementation Details

Algorithms 1 and 2 show the pseudo-code for the centroid computation and poison filtering respectively. Algorithm 1 takes as input the pre-trained feature extractor $\phi$. For each class $y$ in the dataset, it flows the full set of datapoints $X_{y}$ through the feature extractor and computes the characteristic vector of the centroid pseudo-datapoint $\mathcal{C}_{y}$ for that class using BN mean and variance at each layer. Finally, the list of computed centroids $\mathcal{C}$ is given as output. Algorithm 2 takes as input the pre-trained feature extractor $\phi$ and the previously computed centroid characteristic vectors $\mathcal{C}$ for all classes. For each datapoint in the training set, the characteristic vector $\mathcal{X}_{i}$ is computed by flowing each datapoint $x_{i}$ through the network and computing BN statistics at each BN layer in the network. Finally, the distance between the characteristic vector of each datapoint and the centroid characteristic vector of every class is computed following Eq. 8, and the real label $y^{r}_{i}$ of the datapoint is defined as the label of the centroid with minimal distance to $x_{i}$ (Eq. 6). Lastly, the clean dataset $D_{clean}$ is populated with the set of datapoints for which the computed real label $y^{r}_{i}$ equals the dataset label $y_{i}$.

## Appendix 0.B Additional Experimental Results

Figure 4 illustrates the attack success rate against all defenses across different poison and perturbation budgets. EPIC defense is omitted, as the attack success rate against it is always $0\%$, with a large test accuracy penalty. See Section 6.2 for a discussion of all results.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2403.13523/assets/img/fc_graph_cifar10_eps10.png)

(a)

[^1]: Aghakhani, H., Meng, D., Wang, Y.X., Kruegel, C., Vigna, G.: Bullseye polytope: A scalable clean-label poisoning attack with improved transferability. In: IEEE European symposium on security and privacy. pp. 159–178. EuroS&P (2021)

[^2]: Borgnia, E., Cherepanova, V., Fowl, L., Ghiasi, A., Geiping, J., Goldblum, M., Goldstein, T., Gupta, A.: Strong data augmentation sanitizes poisoning and backdoor attacks without an accuracy tradeoff. In: IEEE International Conference on Acoustics, Speech and Signal Processing. pp. 3855–3859. ICASSP (2021)

[^3]: Chen, B., Carvalho, W., Baracaldo, N., Ludwig, H., Edwards, B., Lee, T., Molloy, I., Srivastava, B.: Detecting backdoor attacks on deep neural networks by activation clustering. In: AAAI’s Workshop on Artificial Intelligence Safety. SafeAI (2018)

[^4]: Cinà, A.E., Grosse, K., Demontis, A., Vascon, S., Zellinger, W., Moser, B.A., Oprea, A., Biggio, B., Pelillo, M., Roli, F.: Wild patterns reloaded: A survey of machine learning security against training data poisoning. ACM Computing Surveys 55(13s), 1–39 (2023)

[^5]: Darlow, L.N., Crowley, E.J., Antoniou, A., Storkey, A.J.: Cinic-10 is not imagenet or cifar-10. arXiv preprint arXiv:1810.03505 (2018)

[^6]: De Gaspari, F., Hitaj, D., Pagnotta, G., De Carli, L., Mancini, L.V.: Evading behavioral classifiers: a comprehensive analysis on evading ransomware detection techniques. Neural Computing and Applications 34(14), 12077–12096 (2022)

[^7]: De Gaspari, F., Hitaj, D., Pagnotta, G., De Carli, L., Mancini, L.V.: Reliable detection of compressed and encrypted data. Neural Computing and Applications 34(22), 20379–20393 (2022)

[^8]: Deng, J., Dong, W., Socher, R., Li, L.J., Li, K., Fei-Fei, L.: Imagenet: A large-scale hierarchical image database. In: IEEE Conference on Computer Vision and Pattern Recognition. pp. 248–255. CVPR (2009)

[^9]: Fowl, L., Geiping, J., Somepalli, G., Goldstein, T., Taylor, G.: Industrial scale data poisoning. [https://github.com/JonasGeiping/data-poisoning](https://github.com/JonasGeiping/data-poisoning) (2023)

[^10]: Geiping, J., Fowl, L., Somepalli, G., Goldblum, M., Moeller, M., Goldstein, T.: What doesn’t kill you makes you robust (er): How to adversarially train against data poisoning. In: ICLR Workshop on Security and Safety in Machine Learning Systems (2021)

[^11]: Geiping, J., Fowl, L.H., Huang, W.R., Czaja, W., Taylor, G., Moeller, M., Goldstein, T.: Witches’ brew: Industrial scale data poisoning via gradient matching. In: International Conference on Learning Representations. ICLR (2020)

[^12]: Hitaj, D., Pagnotta, G., De Gaspari, F., Ruko, S., Hitaj, B., Mancini, L.V., Perez-Cruz, F.: Do you trust your model? emerging malware threats in the deep learning ecosystem. arXiv preprint arXiv:2403.03593 (2024)

[^13]: Hitaj, D., Pagnotta, G., Hitaj, B., Mancini, L.V., Perez-Cruz, F.: Maleficnet: Hiding malware into deep neural networks using spread-spectrum channel coding. In: European Symposium on Research in Computer Security. pp. 425–444. ESORICS (2022)

[^14]: Hitaj, D., Pagnotta, G., Hitaj, B., Perez-Cruz, F., Mancini, L.V.: Fedcomm: Federated learning as a medium for covert communication. IEEE Transactions on Dependable and Secure Computing (2023)

[^15]: Hong, S., Chandrasekaran, V., Kaya, Y., Dumitraş, T., Papernot, N.: On the effectiveness of mitigating data poisoning attacks with gradient shaping. arXiv preprint arXiv:2002.11497 (2020)

[^16]: Koh, P.W., Steinhardt, J., Liang, P.: Stronger data poisoning attacks break data sanitization defenses. Machine Learning pp. 1–47 (2022)

[^17]: Krizhevsky, A., Hinton, G., et al.: Learning multiple layers of features from tiny images (2009)

[^18]: Levine, A., Feizi, S.: Deep partition aggregation: Provable defenses against general poisoning attacks. In: International Conference on Learning Representations. ICLR (2020)

[^19]: Li, Y., Lyu, X., Koren, N., Lyu, L., Li, B., Ma, X.: Anti-backdoor learning: Training clean models on poisoned data. Advances in Neural Information Processing Systems 34, 14900–14912 (2021)

[^20]: Liu, Y., Ma, S., Aafer, Y., Lee, W.C., Zhai, J., Wang, W., Zhang, X.: Trojaning attack on neural networks. In: 25th Annual Network And Distributed System Security Symposium. NDSS (2018)

[^21]: Ma, Y., Zhu, X., Hsu, J.: Data poisoning against differentially-private learners: attacks and defenses. In: Proceedings of the 28th International Joint Conference on Artificial Intelligence. pp. 4732–4738. AAAI (2019)

[^22]: Meta: Code llama. [https://github.com/facebookresearch/llama](https://github.com/facebookresearch/llama) (2023)

[^23]: Meta: Llama 2. [https://github.com/facebookresearch/llama](https://github.com/facebookresearch/llama) (2023)

[^24]: Miller, D.J., Xiang, Z., Kesidis, G.: Adversarial learning targeting deep neural network classification: A comprehensive review of defenses against attacks. Proceedings of the IEEE 108(3), 402–433 (2020)

[^25]: Nguyen, T.A., Tran, A.: Input-aware dynamic backdoor attack. Advances in Neural Information Processing Systems pp. 3454–3464 (2020)

[^26]: Pagnotta, G., De Gaspari, F., Hitaj, D., Andreolini, M., Colajanni, M., Mancini, L.V.: Dolos: A novel architecture for moving target defense. IEEE Transactions on Information Forensics and Security 18, 5890–5905 (2023)

[^27]: Pagnotta, G., Hitaj, D., De Gaspari, F., Mancini, L.V.: Passflow: guessing passwords with generative flows. In: 2022 52nd Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN). pp. 251–262. IEEE (2022)

[^28]: Paudice, A., Muñoz-González, L., Lupu, E.C.: Label sanitization against label flipping poisoning attacks. In: ECML PKDD 2018 Workshops. pp. 5–15. ECML PKDD (2019)

[^29]: Peri, N., Gupta, N., Huang, W.R., Fowl, L., Zhu, C., Feizi, S., Goldstein, T., Dickerson, J.P.: Deep k-nn defense against clean-label data poisoning attacks. In: European Conference on Computer Vision Workshop. pp. 55–70 (2020)

[^30]: Piskozub, M., De Gaspari, F., Barr-Smith, F., Mancini, L., Martinovic, I.: Malphase: fine-grained malware detection using network flow data. In: ACM Asia Conference on Computer and Communications Security. pp. 774–786. ASIACCS (2021)

[^31]: Schwarzschild, A., Goldblum, M., Gupta, A., Dickerson, J.P., Goldstein, T.: Just how toxic is data poisoning? a unified benchmark for backdoor and data poisoning attacks. In: International Conference on Machine Learning. ICML (2021)

[^32]: Shafahi, A., Huang, W.R., Najibi, M., Suciu, O., Studer, C., Dumitras, T., Goldstein, T.: Poison frogs! targeted clean-label poisoning attacks on neural networks. In: Advances in neural information processing systems. NIPS (2018)

[^33]: Shokri, R., et al.: Bypassing backdoor detection algorithms in deep learning. In: 2020 IEEE European Symposium on Security and Privacy. pp. 175–183. EuroS&P (2020)

[^34]: Steinhardt, J., Koh, P.W.W., Liang, P.S.: Certified defenses for data poisoning attacks. Advances in neural information processing systems 30 (2017)

[^35]: Tian, Z., Cui, L., Liang, J., Yu, S.: A comprehensive survey on poisoning attacks and countermeasures in machine learning. ACM Computing Surveys 55(8), 1–35 (2022)

[^36]: Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M.A., Lacroix, T., Rozière, B., Goyal, N., Hambro, E., Azhar, F., et al.: Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971 (2023)

[^37]: Tran, B., Li, J., Madry, A.: Spectral signatures in backdoor attacks. In: Advances in neural information processing systems. NIPS (2018)

[^38]: Weber, M., Xu, X., Karlaš, B., Zhang, C., Li, B.: Rab: Provable robustness against backdoor attacks. In: IEEE Symposium on Security and Privacy. pp. 1311–1328. S&P (2023)

[^39]: Yang, Y., Liu, T.Y., Mirzasoleiman, B.: Not all poisons are created equal: Robust training against data poisoning. In: International Conference on Machine Learning. ICML (2022)

[^40]: Yin, H., Molchanov, P., Alvarez, J.M., Li, Z., Mallya, A., Hoiem, D., Jha, N.K., Kautz, J.: Dreaming to distill: Data-free knowledge transfer via deepinversion. In: IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 8715–8724. CVPR (2020)

[^41]: Zhang, W.E., Sheng, Q.Z., Alhazmi, A., Li, C.: Adversarial attacks on deep-learning models in natural language processing: A survey. ACM Transactions on Intelligent Systems and Technology (TIST) 11(3), 1–41 (2020)

[^42]: Zhu, C., Huang, W.R., Li, H., Taylor, G., Studer, C., Goldstein, T.: Transferable clean-label poisoning attacks on deep neural nets. In: International Conference on Machine Learning. pp. 7614–7623. ICML (2019)