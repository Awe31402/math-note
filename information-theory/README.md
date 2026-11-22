# 消息理論 隨堂筆記（陳伯寧，NYCU OCW）

課本：Alajaji & Chen, *An Introduction to Single-User Information Theory* (Springer, 2018)。任務說明見 [BRIEF.md](BRIEF.md)，進度見 [PROGRESS.md](PROGRESS.md)。

| 集 | 講次 | 主題 |
|---|---|---|
| 01 | Lec01 Overview: The philosophy behind information theory | [Shannon 1948 論文、四個定理、參考書](01-overview-philosophy-of-information-theory.md) |
| 02 | Lec02 Chapter 1:Introduction | [Shannon 的思路、entropy、兩大編碼定理的想法](02-introduction-information-entropy-coding-theorems.md) |
| 03 | Lec03 Appendix A:Overview on Suprema and Limits A.1-A.4 | [mutual information 的直覺、supremum 與 infimum](03-suprema-and-limits.md) |
| 04 | Lec04 Review A.1-A.4, A.5 Equivalence | [數列極限、limsup / liminf、等價敘述](04-review-suprema-limits-equivalence.md) |
| 05 | Lec05 Appendix B:Overview in Probability and Random Processes… | [σ-field、機率空間、隨機變數、隨機過程](05-probability-random-processes-overview.md) |
| 06 | Lec06 B.3 Statistical properties of random sources | [T-invariant、ergodic、stationary、Markov source](06-statistical-properties-random-sources.md) |
| 07 | Lec07 B.5 Ergodicity and law of large numbers, B.6 Central limit theorem… | [收斂模式、大數法則、CLT、Jensen、KKT](07-ergodicity-law-of-large-numbers-clt.md) |
| 08 | Lec08 Chapter 2：Information Measures for Discrete Systems: 2.1.1 Self-information... | [self-information、entropy、chain rule、mutual information](08-self-information-entropy-mutual-information.md) |
| 09 | Lec09 2.4 Data processing inequality, 2.5 Fano’s inequality | [entropy 名字由來、DPI、Fano 不等式](09-data-processing-fano-inequality.md) |
| 10 | Lec10 2.6 Divergence and variational distance | [divergence、refinement、variational distance、Pinsker](10-divergence-variational-distance.md) |
| 11 | Lec11 2.7 Convexity/concavity of information measures, 2.8 Fundamentals … | [資訊量的凸性、Neyman–Pearson、Chernoff–Stein](11-convexity-information-measures-hypothesis-testing.md) |
| 12 | Lec12 Chapter 3：Lossless Data Compression: 3.1 Principles of data compression | [block code、AEP、source coding theorem、entropy rate](12-lossless-data-compression-principles-aep.md) |
| 13 | Lec13 3.3 Variable-Length Code for Lossless Data Comp.3.3.1 Non-singular Codes… | [變長碼、uniquely decodable、Kraft、prefix code](13-variable-length-codes-kraft-inequality.md) |
| 14 | Lec14 3.3.3 Examples of Binary Prefix Codes | [Huffman、Shannon–Fano–Elias、Fano code](14-binary-prefix-codes-huffman-shannon-fano-elias.md) |
| 15 | Lec15 3.3.4 Universal Lossless Variable-Length Codes | [universal code：adaptive Huffman、Lempel–Ziv](15-universal-lossless-codes.md) |
| 16 | Lec16 Chapter 4:Data Transmission and Channel Capacity: 4.3 Block codes… | [資料傳輸原理、DMC、block code、jointly typical set](16-block-codes-dmc-channel-capacity-1.md) |
| 17 | Lec17 4.3 Block codes for data transmission over DMCs(2/3) | [operational capacity、channel coding theorem、random coding](17-channel-coding-theorem-achievability.md) |
| 18 | Lec18 4.3 Block codes for data transmission over DMCs(3/3) | [channel coding converse、information density、三個區域](18-channel-coding-converse-fano.md) |
| 19 | Lec19 4.5 Calculating channel capacity, 4.5.1 Symmetric, Weakly Symmetric… | [算 capacity：對稱通道與 KKT 條件](19-calculating-channel-capacity-symmetric-kkt.md) |
| 20 | Lec20 4.4 Example of Polar Codes for the BEC | [回顧 KKT、polar code（BEC）](20-polar-codes-bec.md) |
| 21 | Lec21 4.6 Lossless joint source-channel coding and Shannon’s separation principle | [lossless joint source-channel coding、separation principle](21-joint-source-channel-separation.md) |
| 22 | Lec22 Chapter 5：Differential Entropy and Gaussian Channels: 5.1 Differential entropy | [連續 source 的 entropy 無限大、differential entropy](22-differential-entropy-1.md) |
| 23 | Lec23 5.1 Differential entropy, 5.2 Joint , cond. diff. entrop., diverg. , mutual info | [joint/conditional differential entropy、divergence、MI、高斯最大](23-differential-entropy-joint-divergence-mutual-info.md) |
| 24 | Lec24 5.3 AEP for continuous memoryless sources, 5.4 Capacity for discrete… | [連續 AEP、capacity-cost function、Gaussian channel](24-continuous-aep-gaussian-channel-capacity.md) |
| 25 | Lec25 5.5 Capacity of Uncorrelated Parallel Gaussian Chan | [高斯雜訊最難對付、fading、平行高斯通道 water-filling](25-parallel-gaussian-channels-water-filling.md) |
| 26 | Lec26 5.6 Capacity of correlated parallel Gaussian channels, 5.7 Non-Gaussian discrete-time... | [相關平行高斯、MIMO、entropy power、band-limited AWGN](26-correlated-parallel-gaussian-non-gaussian.md) |
| 27 | Lec27 Chapter 6：Lossy Data Compression and Transmission, 6.1.1 Motivation… | [有損壓縮動機、distortion measure、R(D) 定義](27-lossy-compression-motivation-distortion.md) |
| 28 | Lec28 6.3 Rate-distortion theorem AEP for distortion typical set Shannon’s lossy source… | [Rate–distortion theorem（Shannon 第三定律）](28-rate-distortion-theorem.md) |
| 29 | Lec29 6.4 Calculation of the rate-distortion function, 6.4.2 Rate distortion func… | [計算 R(D)：二元 source、高斯 source](29-rate-distortion-calculation.md) |
| 30 | Lec30 Chapter 6：Lossy Data Compression and Transmission, 6.5 Lossy joint source-channel… | [有損 joint source–channel coding、Shannon limit（上）](30-lossy-joint-source-channel-coding.md) |
| 31 | Lec31 6.6 Shannon limit of communication systems(2/2) | [Shannon limit（下）、第一部分總結、information spectrum 預告](31-shannon-limit-communication-systems.md) |
| 32 | Lec32 Preface and Introduction: Chapter 1:Generalized Information Measures… | [廣義資訊量：spectrum、quantile、inf／sup rate](32-generalized-information-measures.md) |
| 33 | Lec33 Chapter 2:General Data Compression Theorems | [一般 source 的固定長度壓縮定理](33-general-data-compression-theorems.md) |
| 34 | Lec34 Chapter 3:Measure of Randomness for Stochastic Processes | [隨機性量度 resolvability、不定長度壓縮](34-measure-of-randomness-stochastic-processes.md) |
| 35 | Lec35 Chapter 4:Channel Coding Theorems and Approximations of Output Statistics for… | [任意通道的 channel coding theorem、output statistics](35-channel-coding-theorems-output-statistics.md) |
