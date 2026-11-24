# EE274 資料壓縮 隨堂筆記

Stanford EE274 Data Compression: Theory and Applications（2023 秋），講者 Tsachy Weissman、Shubham Chandak、Pulkit Tandon，第 18 集客座 Kedar Tatwawadi。課本 Cover & Thomas《Elements of Information Theory》2nd ed.（PDF 頁碼 = 書頁 + 26）；投影片在 `_work/slides/`。任務說明見 [BRIEF.md](BRIEF.md)，進度見 [PROGRESS.md](PROGRESS.md)。

| 部分 | 集數 | 課本 |
|---|---|---|
| 無損：基礎（前綴碼、Kraft、熵） | 01–03 | 第 2、5 章 |
| 無損：熵編碼器（Huffman、AEP、算術編碼、ANS） | 04–07 | 第 3、5、13 章；ANS 課本無 |
| 無損：非 iid（條件熵、context 模型、LLM、LZ77） | 08–10 | 第 2、4、13 章 |
| 有損：基礎（量化、率失真、轉換編碼） | 11–14 | 第 10 章；DCT 課本無 |
| 有損：應用（JPEG、學習式壓縮、人的感知、影片） | 15–18 | 課本無 |

| # | 主題 | 筆記 |
|---|---|---|
| 01 | 課程介紹、固定長度碼、變長碼、期望碼長 | [01-course-intro-lossless-basics](01-course-intro-lossless-basics.md) |
| 02 | 唯一可解碼、前綴碼、樹、Shannon 碼 | [02-prefix-free-codes](02-prefix-free-codes.md) |
| 03 | Kraft 不等式、熵、KL 散度、主定理 | [03-kraft-inequality-entropy](03-kraft-inequality-entropy.md) |
| 04 | 最佳前綴碼條件、Huffman、查表解碼 | [04-huffman-codes](04-huffman-codes.md) |
| 05 | AEP、典型集合、不匹配壓縮、典型 Huffman 碼 | [05-asymptotic-equipartition-property](05-asymptotic-equipartition-property.md) |
| 06 | 算術編碼、碼長 ≤ log(1/p)+2、重新縮放 | [06-arithmetic-coding](06-arithmetic-coding.md) |
| 07 | 對稱記數系統、rANS、串流 rANS、tANS | [07-ans](07-ans.md) |
| 08 | 平穩、Markov、條件熵、熵率 | [08-conditional-entropy](08-conditional-entropy.md) |
| 09 | context-based 算術編碼、自適應、MDL、LLM 壓縮 | [09-context-based-ac-llm-compression](09-context-based-ac-llm-compression.md) |
| 10 | 通用壓縮、LZ77、Kac 引理、實務建議 | [10-lz-universal-compression](10-lz-universal-compression.md) |
| 11 | 失真、量化、向量量化、Lloyd/k-means | [11-lossy-compression-quantization](11-lossy-compression-quantization.md) |
| 12 | 互資訊、率失真定理、Bernoulli 與高斯 | [12-mutual-information-rate-distortion](12-mutual-information-rate-distortion.md) |
| 13 | 反向注水、轉換編碼、正交轉換、KLT | [13-gaussian-rd-transform-coding](13-gaussian-rd-transform-coding.md) |
| 14 | Gauss–Markov KLT、DCT、音訊壓縮器 | [14-transform-coding-in-practice](14-transform-coding-in-practice.md) |
| 15 | 2D-DCT、JPEG 流程、BPG | [15-image-compression-jpeg-bpg](15-image-compression-jpeg-bpg.md) |
| 16 | 非線性轉換、量化與機率模型的繞法、MNIST 示範 | [16-learnt-image-compression](16-learnt-image-compression.md) |
| 17 | 人眼、YCbCr、4:2:0、SSIM/LPIPS/VMAF、RDP | [17-humans-and-compression](17-humans-and-compression.md) |
| 18 | I/P/B 畫面、運動補償、學習式影片編碼、課程總結 | [18-video-compression](18-video-compression.md) |
