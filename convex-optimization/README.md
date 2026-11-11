# EE364A 凸最佳化 隨堂筆記

Stanford EE364A Convex Optimization I（2023，Stephen Boyd）。課本 Boyd & Vandenberghe《Convex Optimization》（`bv_cvxbook.pdf`，PDF 頁碼 = 書頁 + 14）。任務說明見 [BRIEF.md](BRIEF.md)，進度見 [PROGRESS.md](PROGRESS.md)。

| 部分 | 集數 | 課本 |
|---|---|---|
| 課程介紹 | 01 | 第 1 章 |
| 理論：凸集、凸函數 | 02–05 | 第 2–3 章 |
| 理論：凸最佳化問題、問題類別、向量最佳化 | 05–07 | 第 4 章 |
| 理論：對偶 | 07–09 | 第 5 章 |
| 應用：近似、統計、幾何 | 09–12 | 第 6–8 章 |
| 演算法：數值線性代數、Newton 法 | 12–15 | 附錄 C、第 9–10 章 |
| 演算法：內點法 | 15–17 | 第 11 章 |
| ℓ1 方法、凸基數問題、總結 | 17–18 | 課本無專章 |

| # | 主題 | 筆記 |
|---|---|---|
| 01 | 課程介紹與總覽 | [01-introduction](01-introduction.md) |
| 02 | 凸集 | [02-convex-sets](02-convex-sets.md) |
| 03 | 分離超平面、對偶錐、凸函數 | [03-convex-functions](03-convex-functions.md) |
| 04 | 凸函數（二）：組合規則、共軛、擬凸 | [04-convex-functions-2](04-convex-functions-2.md) |
| 05 | 對數凹函數、凸最佳化問題 | [05-convex-optimization-problems](05-convex-optimization-problems.md) |
| 06 | 問題類別：LP、QP、SOCP、GP、SDP | [06-problem-classes](06-problem-classes.md) |
| 07 | 向量最佳化、Lagrange 對偶函數 | [07-vector-optimization-duality](07-vector-optimization-duality.md) |
| 08 | 對偶問題、強對偶、KKT、敏感度 | [08-duality](08-duality.md) |
| 09 | 重新表述與對偶、範數與懲罰近似 | [09-duality-2-approximation](09-duality-2-approximation.md) |
| 10 | 訊號重建、強健近似、統計估計 | [10-approximation-and-statistics](10-approximation-and-statistics.md) |
| 11 | 實驗設計、外接與內接橢球、中心 | [11-statistics-and-geometry](11-statistics-and-geometry.md) |
| 12 | 線性判別、放置問題、數值線性代數入門 | [12-geometric-problems](12-geometric-problems.md) |
| 13 | 稀疏分解、區塊消去、梯度法 | [13-numerical-linear-algebra](13-numerical-linear-algebra.md) |
| 14 | 最陡下降、Newton 法、自和諧 | [14-newton-method](14-newton-method.md) |
| 15 | 等式約束最小化、不可行起點 Newton 法 | [15-equality-constrained-minimization](15-equality-constrained-minimization.md) |
| 16 | 對數障礙、中心路徑、障礙法、Phase I | [16-interior-point-methods](16-interior-point-methods.md) |
| 17 | 障礙法複雜度、廣義不等式、凸基數問題 | [17-barrier-method-complexity](17-barrier-method-complexity.md) |
| 18 | ℓ1 啟發式、秩問題、課程總結 | [18-l1-methods-and-wrap-up](18-l1-methods-and-wrap-up.md) |
