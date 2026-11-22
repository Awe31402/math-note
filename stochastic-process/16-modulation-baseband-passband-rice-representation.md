---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 16
lecture: Lec 10-3 Random Walks and Other Applications — Modulation (1/3)
date: 待補
video: https://youtu.be/qTKcT61ea1k
notes: Papoulis & Pillai 4th ed. §10-3 Modulation（式 (10-125)–(10-141)，pp. 463–465；Rice's representation 開頭，p. 465）
---

# 第 16 集 · Lec 10-3 (1/3)：調變——$a\cos\omega_0t-b\sin\omega_0t$ 何時 WSS、基頻與射頻的全對稱系統、頻譜關係、Rice 表示法的出發點 [▶ 影片](https://youtu.be/qTKcT61ea1k)

← 上一集：[15](15-discrete-time-processes-sampling-schur-paley-wiener.md) ｜ [總目錄](README.md) ｜ 下一集：[17](17-rice-optimal-hilbert-center-frequency-instantaneous-frequency-fm.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 16 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（57:56，whisper large-v3-turbo）＋ Papoulis §10-3（pp. 463–466）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「調變」→「條片」，「Hilbert transform」→「Hilbert and Fong／Cuberton Phone／Huberton Form」，「Rice's representation」→「Rice／Rise Representation／Rise Reputation」，「wide-sense stationary」→「Widescent／Ysin／Wisen／wise and／y-sense stationary」，「jointly WSS」→「join the rising station」，「穩態」→「穩泰」，「zero mean」→「0 mean／G0面／肌肉命」（「肌肉面穩泰」= zero-mean WSS），「false」→「Phalos」，「lemma」→「Lama」，「Neyman–Pearson」→「Newman Pearson」，「實部／虛部」→「十步／時步／虛步」，「實數」→「時數」，「射頻」→「社頻／色頻」，「基頻」→「g頻／基屏」，「載波」→「載坡／載播」，「展頻（通訊）」→「斬頻通訊」，「aliasing」→「Alien 型／A 連形」，「奇對稱」→「G 對稱」，「偶對稱」→「O 對稱」，「頻域」→「斗面」，「autocorrelation」→「autochrome／autoclin／autocorine／autocoration function」，「complex conjugate」→「complete conjugate」，「narrowband」→「Narrowband」，「all-pass」→「all-path」。以下一律用正確的字。

> **接上一集**：第 9 章是基本概念：隨機過程是函數映射、各種重要性質、我們要造 WSS 訊號、基本定理、均方意義。準備好之後進入第 10 章。§10-1 Random Walks、§10-2 Poisson Points and Shot Noise 從通訊角度比較次要，跳過；直接講 §10-3 **調變** (modulation)。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 課本 p. 463 那句話：單獨看是錯的](#1-課本-p-463-那句話單獨看是錯的)
- [2. 定理：何時 $X(t)=A\cos\omega_0t-B\sin\omega_0t$ 是 WSS](#2-定理何時-xtacosomega_0t-bsinomega_0t-是-wss)
  - [2.1 敘述（把條件寫完整）](#21-敘述把條件寫完整)
  - [2.2 反例：少了前提就不對](#22-反例少了前提就不對)
  - [2.3 證明](#23-證明)
  - [2.4 心得：射頻訊號的自相關也是高頻](#24-心得射頻訊號的自相關也是高頻)
- [3. 基頻、射頻與「虛部到哪裡去了」](#3-基頻射頻與虛部到哪裡去了)
- [4. 通訊是全對稱系統](#4-通訊是全對稱系統)
- [5. 整個系統鎖在一起：一個穩態，全部穩態](#5-整個系統鎖在一起一個穩態全部穩態)
- [6. 複數訊號的自相關：實部是自相關、虛部是互相關](#6-複數訊號的自相關實部是自相關虛部是互相關)
- [7. 頻譜關係](#7-頻譜關係)
- [8. Rice 表示法的出發點](#8-rice-表示法的出發點)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 第 10 章安排 | [▶ 00:00](https://youtu.be/qTKcT61ea1k?t=0) | 無 |
| WSS 條件、反例、證明 | [▶ 01:36](https://youtu.be/qTKcT61ea1k?t=96) | 式 (10-125)–(10-128)，pp. 463–464 |
| 複數表示、全對稱 | [▶ 17:07](https://youtu.be/qTKcT61ea1k?t=1027) | 式 (10-129)–(10-134)，p. 464 |
| 自相關、頻譜關係 | [▶ 31:55](https://youtu.be/qTKcT61ea1k?t=1915) | 式 (10-135)–(10-141)，pp. 464–465 |
| Rice 表示法 | [▶ 45:00](https://youtu.be/qTKcT61ea1k?t=2700) | p. 465 |

老師說【口頭】：調變大家修數位通訊都學了很多，這裡用不同的方式陳述；而且會讓你知道 **Hilbert 轉換**有另一個數學上的意義——數位通訊時直接給定義（為了做分析），這裡會給它最直觀的物理意義：**Rice 表示法**。

---

## 1. 課本 p. 463 那句話：單獨看是錯的

[▶ 01:36](https://youtu.be/qTKcT61ea1k?t=96) 通訊訊號都長成這個形式：基頻的隨機過程 $A(t)$、$B(t)$ 分別乘 $\cos\omega_0t$、$\sin\omega_0t$ 送出去，天線打出去的訊號是 $X(t)$，我們希望它非常穩定（WSS）。

課本說（p. 463）：$X(t)$ 是 WSS **若且唯若** $A$、$B$ 的自相關、互相關「很平衡」：
$$R_{AA}(\tau)=R_{BB}(\tau),\qquad R_{AB}(\tau)=-R_{BA}(\tau)\qquad\text{(10-126)}.$$

老師說【口頭】：看到這句話要產生疑問——**單獨看它不完全正確**，反方向 (converse) 是錯的。不是作者寫錯，而是它的前提寫在別處：§10-3 第一行「Given two real **jointly WSS** processes $a(t)$ and $b(t)$ **with zero mean**」。前後文離太遠（像三天前講了前提、三天後才講下文），讀的時候要一口氣看完，不要斷章取義。老師寫書喜歡把條件寫在 lemma 裡，雖然囉嗦，但對讀者才嚴謹。將來回來當教授的同學，要看懂這種前後關係。

---

## 2. 定理：何時 $X(t)=A\cos\omega_0t-B\sin\omega_0t$ 是 WSS

### 2.1 敘述（把條件寫完整）

> **引理**：設 $A(t)$、$B(t)$ 是**零平均、聯合 WSS** 的實數過程。則
> $$X(t)=A(t)\cos\omega_0t-B(t)\sin\omega_0t\ \text{是 WSS}\iff R_{AA}(\tau)=R_{BB}(\tau),\ R_{AB}(\tau)=-R_{BA}(\tau).$$
> 此時
> $$R_{XX}(\tau)=R_{AA}(\tau)\cos\omega_0\tau+R_{AB}(\tau)\sin\omega_0\tau\qquad\text{(10-128)}.$$

【課本補充】(10-125)：也可寫成 $X(t)=r(t)\cos[\omega_0t+\varphi(t)]$，$r=\sqrt{A^2+B^2}$ 是**振幅調變** (amplitude modulation)，$\tan\varphi=B/A$ 是**相位調變** (phase modulation)。

### 2.2 反例：少了前提就不對

[▶ 07:13](https://youtu.be/qTKcT61ea1k?t=433) 不加「$A,B$ 聯合 WSS」的前提，「$X$ 是 WSS ⇒ 平衡條件」就是 false。老師的反例思路：把 $A$、$B$ 代成特定的函數，讓 $X\equiv0$。$X$ 永遠是 0，當然是 WSS；但 $R_{AA}$、$R_{BB}$ 根本不是 $t_1-t_2$ 的函數，談不上平衡條件。

以下**不是逐字稿內容**，是依這個思路補的具體例子（老師沒唸出用了哪兩個函數）：取隨機變數 $Z$，令 $A(t)=Z\sin\omega_0t$、$B(t)=Z\cos\omega_0t$。則
$$X(t)=Z(\sin\omega_0t\cos\omega_0t-\cos\omega_0t\sin\omega_0t)=0,$$
但 $R_{AA}(t_1,t_2)=E[Z^2]\sin\omega_0t_1\sin\omega_0t_2$ 不只跟 $t_1-t_2$ 有關。

### 2.3 證明

**⇐（if part）**：大學部通訊原理、研究所數位通訊一直重複做這件事，因為基本、觀念重要——要造穩態訊號一定要有這個概念。

1. 平均：$E[X]=E[A]\cos\omega_0t-E[B]\sin\omega_0t=0$，常數。（**不要忘了檢查平均**。）
2. 自相關（$X$ 是實數，不用共軛）：代入相乘，$A,B$ 聯合 WSS 所以只跟時間差有關，用三角公式就證完。

**⇒（converse）** [▶ 09:48](https://youtu.be/qTKcT61ea1k?t=588)：$X$ 是 WSS，自相關不能隨 $t$ 改變。

**Step 1：** 展開 $E[X(t+\tau)X(t)]$，有 $\cos\cos$、$\cos\sin$、$\sin\cos$、$\sin\sin$ 四項。

**Step 2：** 老師的口訣【口頭】：**通訊上碰到兩個三角函數相乘，一定要變成單一的三角函數**：$\cos A\cos B=\frac12[\cos(A+B)+\cos(A-B)]$。整理後：
$$2E[X(t+\tau)X(t)]=\left[R_{AA}+R_{BB}\right]\cos\omega_0\tau+\left[R_{AB}-R_{BA}\right]\sin\omega_0\tau$$
$$+\left[R_{AA}-R_{BB}\right]\cos\omega_0(2t+\tau)-\left[R_{AB}+R_{BA}\right]\sin\omega_0(2t+\tau)\qquad\text{(10-127)}.$$
（這裡 $R$ 能寫成只有 $\tau$，正是因為前提 $A,B$ 聯合 WSS。）

**Step 3：** 有的項只跟 $\tau=t_1-t_2$ 有關，有的跟 $2t+\tau=t_1+t_2$（絕對時間）有關。WSS 不能跟 $t_1+t_2$ 有關，所以後兩項的係數要是 0（多元一次聯立方程式）：
$$R_{AA}=R_{BB},\qquad R_{AB}=-R_{BA}.$$ ∎

代回 Step 2，前兩項各變兩倍，和 $\frac12$ 消掉，就得到 (10-128)。

老師說：這個結果每本講調變的書都有，就像每本 detection 的書都有 Neyman–Pearson lemma：證明簡單，但它確立了重要的觀念。

### 2.4 心得：射頻訊號的自相關也是高頻

[▶ 14:33](https://youtu.be/qTKcT61ea1k?t=873)

- 結構和基本定理很像：$X=A\cos-B\sin$，自相關也是 $R_{AA}$ 乘 $\cos$ 加 $R_{AB}$ 乘 $\sin$。
- 天線打出去的 $X$ 的自相關**完全由 $A$、$B$ 的自相關決定**。
- $A$、$B$ 是**基頻**（例如 3100 Hz 的聲音），$X$ 是**射頻**（例如 1.8 GHz）。兩者差一個頻率的調變。
- 所以 **$R_{XX}(\tau)$ 也是高頻**，在同一個頻率（1.8 GHz）快速震盪。畫出自相關就猜得出它是基頻還是射頻訊號。（看功率頻譜當然也看得出來；現在告訴你從自相關也看得出來。）

---

## 3. 基頻、射頻與「虛部到哪裡去了」

[▶ 17:07](https://youtu.be/qTKcT61ea1k?t=1027)

用 $\cos$ 送出去的當**實部**、$\sin$ 送出去的當**虛部**——虛數 (imaginary) 本來就是想像出來的，方便分析。

> **複數基頻訊號**：$W(t)=A(t)+jB(t)$。
> **射頻訊號**：$X(t)=\text{Re}\left[W(t)e^{j\omega_0t}\right]$。

老師說【口頭】：這是通訊非常重要的公式。他有學生畢業後回來，第一個就問：「你還寫不寫得出基頻和射頻的關係？」學通訊的一定要馬上寫出來：**基頻訊號乘複數載波，取實部就打出去**。

**這門課的問題**：既然是 random process 的數學課，就問：取了實部，**虛部跑哪裡去了**？
$$\text{Im}\left[W(t)e^{j\omega_0t}\right]=A(t)\sin\omega_0t+B(t)\cos\omega_0t.$$
操作上用不到它，但數學上它存在。它有什麼物理意義？

**記號**（老師要大家記住：$X,Y,Z$ 都是高頻，$W$ 是低頻）：

| 記號 | 意義 |
|---|---|
| $W=A+jB$ | 基頻複數訊號 |
| $Z=We^{j\omega_0t}=X+jY$ | 高頻複數訊號 |
| $X=\text{Re}\,Z$ | 天線真正打出去的訊號（實際看得到） |
| $Y=\text{Im}\,Z$ | 想像中的訊號（直接丟掉不送） |

【課本補充】式 (10-129)、(10-132)–(10-134)，p. 464。課本把 $Y(t)=B(t)\cos\omega_0t+A(t)\sin\omega_0t$ 叫 $X$ 的**對偶過程** (dual process)。反過來：
$$A(t)=X(t)\cos\omega_0t+Y(t)\sin\omega_0t,\qquad B(t)=Y(t)\cos\omega_0t-X(t)\sin\omega_0t.$$

---

## 4. 通訊是全對稱系統

[▶ 21:13](https://youtu.be/qTKcT61ea1k?t=1273)

- **傳送**：$W$ 乘 $e^{j\omega_0t}$ 得 $Z$，取實部 $X$ 送出（虛部 $Y$ 濾掉，但它存在）。
- **接收**：把 $Z$ 乘 $e^{-j\omega_0t}$（負的載波）拉回基頻，取實部、虛部就是 $A$、$B$。
- 兩邊完全一樣，差別只在載波一個正、一個負。**沒有雜訊時，傳送端和接收端完全對稱**。

老師的例子【口頭】：

- 傳統通訊：訊號乘 $\cos2\pi f_ct$ 打出去（前面先濾乾淨），接收端再乘一次 $\cos2\pi f_ct$、經過低通濾波器就回來了。
- 3G 展頻通訊：傳送端乘 $p(t)$，接收端再乘 $p(t)$，$p^2=1$。自己乘自己是 1 的函數很受歡迎，因為能「傳收不分」。
- 那為什麼實際上接收端比較複雜？**因為有雜訊**。接收端要做 channel estimation、equalization、濾雜訊、detection／estimation……所以接收技術比較難。

**每個操作都是線性的**：乘 $e^{j\omega_0t}$ 是線性（時變）系統；取實部也是線性的。所以基本定理、Theorem 9-2 都能用：要知道輸入輸出自相關的關係，就把輸入的自相關當輸入送進系統兩次（例如「取實部」取兩次）。

---

## 5. 整個系統鎖在一起：一個穩態，全部穩態

[▶ 25:48](https://youtu.be/qTKcT61ea1k?t=1548)

**$W$ 零平均 WSS ⇒ $Z$ 零平均 WSS**：

- 老師先說「線性系統輸入 WSS、輸出就 WSS，根本不用證」——隨即自我修正：那是**時不變**線性系統的性質；乘 $e^{j\omega_0t}$ 是**時變**的，要另外證。（他謝謝同學提醒。）
- 證明：用時變版的基本定理（第 11 集）——時變因子可以拆成 $h(\tau)$ 和 $e^{j\omega_0t}$ 相乘。這裡 $h(\tau)=\delta(\tau)$，時變部分是載波：
$$R_{ZZ}(t+s,t)=E\left[W(t+s)e^{j\omega_0(t+s)}W^*(t)e^{-j\omega_0t}\right]=e^{j\omega_0s}R_{WW}(s).$$
  $e^{j\omega_0t}$ 和 $e^{-j\omega_0t}$ 消掉，只跟 $s$ 有關。

**反過來**：$Z$ 零平均 WSS ⇒ $W=Ze^{-j\omega_0t}$ 零平均 WSS（同樣理由）。

**$Z$ WSS ⇒ $X,Y$ 聯合零平均 WSS**：取實部、虛部是**時不變**的線性操作。

**$W$ WSS ⇔ $A,B$ 聯合零平均 WSS**：同理。

> **Observation**：$A,B$（聯合零平均 WSS）、$W$、$Z$、$X,Y$（聯合零平均 WSS）——**只要有一個穩態，其他全部穩態；有一個不穩，全部不穩**。整個系統鎖在一起 (locked)。

這就是為什麼課本 §10-3 第一行「假設 $A,B$ 聯合零平均 WSS」那句話這麼重要：一假設，整個系統都穩了。

而且 $X,Y$ 也要**平衡**：
$$R_{XX}(\tau)=R_{YY}(\tau),\qquad R_{XY}(\tau)=-R_{YX}(\tau)\qquad\text{(10-130)}.$$
這跟後面 $Y$ 的角色有關：實際上不送 $Y$，但想像中的 $Y$ 要和 $X$ 完全平衡。

【課本補充】(10-131)：$R_{XY}(\tau)=R_{AB}(\tau)\cos\omega_0\tau-R_{AA}(\tau)\sin\omega_0\tau$。

---

## 6. 複數訊號的自相關：實部是自相關、虛部是互相關

[▶ 31:55](https://youtu.be/qTKcT61ea1k?t=1915) 基頻對基頻：$W$ 和 $A,B$ 的關係（等於把 $\omega_0$ 代 0，沒有載波的直接傳輸）。照定義算：
$$R_{WW}(\tau)=E\left[(A(t+\tau)+jB(t+\tau))(A(t)-jB(t))\right]=R_{AA}+R_{BB}+j\left(R_{BA}-R_{AB}\right)=2R_{AA}(\tau)-2jR_{AB}(\tau).$$
（四項中有兩對相等，所以有係數 2。）

- 係數 2 不用太在意：有的書會刻意加 $\frac12$ 消掉，這本書照定義就不調整；系統裡加一個 gain 就調掉了。
- 要記得的觀念：**複數訊號的自相關，實部是實部自己的自相關，虛部是實部和虛部之間的互相關。**

高頻完全對稱（$Z=X+jY$）：
$$R_{ZZ}(\tau)=2R_{XX}(\tau)-2jR_{XY}(\tau),\qquad R_{ZZ}(\tau)=e^{j\omega_0\tau}R_{WW}(\tau).$$

【課本補充】式 (10-135)–(10-137)，p. 465。

---

## 7. 頻譜關係

[▶ 35:37](https://youtu.be/qTKcT61ea1k?t=2137) 一般書（數位通訊）講的是：**基頻頻譜 $S_{WW}$ 和射頻頻譜 $S_{XX}$ 的關係**。

> $$S_{XX}(\omega)=\frac14\left[S_{WW}(\omega-\omega_0)+S_{WW}(-\omega-\omega_0)\right],$$
> $$S_{XY}(\omega)=\frac{j}{4}\left[S_{WW}(\omega-\omega_0)-S_{WW}(-\omega-\omega_0)\right].$$

**直觀理解**【口頭】：

- $X$ 是實數訊號 → 自相關是實數 → 頻譜一定**左右對稱**（偶函數）。
- $W$ 是複數訊號 → 頻譜一般**不對稱**。$Z$ 也是複數，也不對稱。
- 怎麼從不對稱造出對稱？把 $\omega$ 和 $-\omega$ 疊加：$S_{ZZ}(\omega)+S_{ZZ}(-\omega)$，代 $\omega$ 或 $-\omega$ 都一樣，保證對稱。
- $S_{XY}$ 是「相減」，所以是**奇對稱**（對原點對稱）。一般比較少注意到：**穩態系統的實部、虛部之間的互頻譜一定是奇函數**。

**aliasing 的提醒** [▶ 39:17](https://youtu.be/qTKcT61ea1k?t=2357)：大部分時候假設沒有 aliasing（嚴格窄頻 narrowband）。同學常畫成：把基頻頻譜往右拉、往左拉，形狀不變。但若基頻頻譜不對稱、載波頻率又不夠高，往左那一份是 $S_{WW}(-\omega-\omega_0)$（翻轉過的），會和往右那一份**疊加**，改變形狀。真正的訊號外面從來不是 0，只是很小，所以這個等號裡的「加」是真的加。老師說考試會故意考這個。

**證明**（三個式子）：

1. $S_{ZZ}(\omega)=2S_{XX}(\omega)-2jS_{XY}(\omega)$（由 $R_{ZZ}=2R_{XX}-2jR_{XY}$）。
2. 把 $\omega$ 換 $-\omega$：$X$ 實數 → $S_{XX}$ 偶；$R_{XY}(-\tau)=R_{YX}(\tau)$ 且 $R_{YX}=-R_{XY}$，所以 $R_{XY}$ 是奇函數 → $S_{XY}$ 奇。得 $S_{ZZ}(-\omega)=2S_{XX}(\omega)+2jS_{XY}(\omega)$。
3. $S_{ZZ}(\omega)=S_{WW}(\omega-\omega_0)$（乘載波 = 頻域平移）。

1 + 2 消掉虛部 → $S_{XX}$；2 − 1 消掉實部 → $S_{XY}$。 ∎

【課本補充】式 (10-138)–(10-141)，p. 465：$S_{XX}$、$S_{ZZ}$ 是實數且非負；$B_{XY}(\omega)=-jS_{XY}(\omega)$ 是實數、奇函數，$|B_{XY}(\omega)|\le S_{XX}(\omega)$；$4S_{XX}(\omega)=S_{ZZ}(\omega)+S_{ZZ}(-\omega)$，$4jS_{XY}(\omega)=S_{ZZ}(-\omega)-S_{ZZ}(\omega)$。

【課本補充】**單邊帶** (single sideband，p. 465)：若 $B(t)=\hat{A}(t)$（$A$ 的 Hilbert 轉換），平衡條件自動滿足，$S_{WW}(\omega)=4S_{AA}(\omega)U(\omega)$（只剩正頻率），所以 $|\omega|<\omega_0$ 時 $S_{XX}(\omega)=0$。

---

## 8. Rice 表示法的出發點

[▶ 45:00](https://youtu.be/qTKcT61ea1k?t=2700) 老師說：一般大學設計是先修 random process 再修數位通訊；很多同學反過來，也有好處——你已經知道常常加一個 $Y$、做 Hilbert 轉換是為了分析。現在問：**Hilbert 轉換的物理意義是什麼？** 答案是 **Rice 表示法**。

**情境**：傳送端 $X=A\cos\omega_0t-B\sin\omega_0t$ 是穩態的（$A,B$ 穩態且能量平衡）。接收端從天線收到一個高頻的 $X(t)$（收很多次，知道它的統計特性），要**解調**回基頻。

- 你必須知道載波（1.8 GHz 還是 2.4 GHz），要拿掉它；還要回復基頻的實部、虛部。但你**完全不知道**這些。
- 你只知道：系統是穩態的，所以解回來的也要穩態。
- 接收端的 $\omega_0$ 一定要和傳送端一樣嗎？不見得：送 1.8 GHz，可以用 1.81 GHz 解。解回來是什麼？這就是 Rice 問的問題。（手機和基地台的震盪頻率本來就可能差一點點，不一定同步。）

> **Rice 表示法** (Rice's representation)：給任何**零平均 WSS** 的 $X(t)$，**存在**常數 $\omega_0$ 和過程 $A(t)$、$B(t)$，使
> $$X(t)=A(t)\cos\omega_0t-B(t)\sin\omega_0t\quad\text{（均方意義下相等）}.$$

- 接收端只看到 $X$，沒看到傳送端用的 $\omega_0$、$A$、$B$；硬去找一組 $\omega_0,A,B$ 重建 $X$，重建出來和 $X$ 一模一樣。
- 「等號」是**均方相等**：兩者相減平方的期望值為 0（第 13 集）。
- 老師的例子【口頭】：大陸建了 500 公尺的大天線收外太空來的莫名訊號，猜外星人要說什麼。你哪知道他的載波？只能假設對方送的是穩態的，然後解回來。
- **存在**，但**不唯一**：每個人解出的 $\omega_0,A,B$ 都可能不一樣，都是對的；其中有一組是傳送端真正用的，只有傳送端知道。

**做法**：

1. 找任何一個 $Y$，使 $X,Y$ 聯合零平均 WSS 且**平衡**：$R_{YY}=R_{XX}$、$R_{XY}=-R_{YX}$（系統要穩態，一定要符合）。
2. $\omega_0$ 任意。
3. $Z=X+jY$，乘 $e^{-j\omega_0t}$，取實部就是 $A$、虛部就是 $B$。

載波猜錯也沒關係，還是有 $A,B$，只是和原來傳送的不一樣。全班 50 人可能找出 50 組 $Y$，得到的 $A,B$ 都不一樣。任何接收系統都解得出一個東西，解出來是什麼，不知道。

**Rice 最重要的問題：怎麼選一個「好」的 $Y$？** [▶ 52:44](https://youtu.be/qTKcT61ea1k?t=3164)

- 實作上合理的做法：把收到的 $X$ 經過一個**線性濾波器** $H(\omega)$ 得到 $Y$。（$Y$ 本來不要求和 $X$ 是線性關係，但接收端這樣做最合理。）
- 由 Theorem 9-4：
$$S_{YY}=S_{XX}|H|^2,\qquad S_{XY}=S_{XX}H^*.$$
  反過來 $X$ 是 $Y$ 經過 $1/H$：$S_{YX}=S_{YY}(1/H)^*=S_{XX}|H|^2/H^*=S_{XX}H$。
- 兩個條件：
  1. $S_{XX}=S_{YY}$ ⇒ $|H(\omega)|^2=1$：**全通濾波器** (all-pass filter)。
  2. $S_{XY}=-S_{YX}$ ⇒ $H^*(\omega)=-H(\omega)$。
- 設計任何濾波器都要有這兩個條件。**Hilbert 轉換**（$H=-j\,\text{sgn}\,\omega$）一定符合，但**不是唯一**。從這個角度看，Hilbert 轉換好像有實作上的意義，不只是數學上的。
- 老師最後說：還要再引進一個輔助條件，幫助推導（下一集）。

【課本補充】p. 465：$\omega_0$ 任意、$Y$ 只受 (10-130) 限制，所以表示法不唯一。問題是：所有可能的表示中有沒有最佳的？答案依最佳的準則而定。課本說：若 $Y=\hat{X}$（$X$ 的 Hilbert 轉換），(10-125) 在「**包絡的平均變化率最小**」(minimizing the average rate of variation of the envelope) 的意義下是最佳的。

---

## 9. 一頁速查表

### 調變的 WSS 條件

前提 $A,B$ 零平均、聯合 WSS：
$$X=A\cos\omega_0t-B\sin\omega_0t\ \text{WSS}\iff R_{AA}=R_{BB},\ R_{AB}=-R_{BA};\quad R_{XX}=R_{AA}\cos\omega_0\tau+R_{AB}\sin\omega_0\tau.$$
- 關鍵：積化和差後，$\cos\omega_0(2t+\tau)$、$\sin\omega_0(2t+\tau)$ 的係數必須為 0。
- 沒有前提時反例：$A=Z\sin\omega_0t$，$B=Z\cos\omega_0t$，$X\equiv0$。

### 複數表示

| | 公式 |
|---|---|
| 基頻 | $W=A+jB$ |
| 射頻 | $Z=We^{j\omega_0t}=X+jY$，$X=\text{Re}\,Z$ |
| 解調 | $A=X\cos\omega_0t+Y\sin\omega_0t$，$B=Y\cos\omega_0t-X\sin\omega_0t$ |
| 自相關 | $R_{WW}=2R_{AA}-2jR_{AB}$，$R_{ZZ}=2R_{XX}-2jR_{XY}=e^{j\omega_0\tau}R_{WW}$ |

- 一個穩態全部穩態（$A,B\leftrightarrow W\leftrightarrow Z\leftrightarrow X,Y$）。
- $R_{XX}=R_{YY}$，$R_{XY}=-R_{YX}$（$R_{XY}$ 奇）。

### 頻譜

$$S_{XX}(\omega)=\tfrac14\left[S_{WW}(\omega-\omega_0)+S_{WW}(-\omega-\omega_0)\right],\quad S_{XY}(\omega)=\tfrac j4\left[S_{WW}(\omega-\omega_0)-S_{WW}(-\omega-\omega_0)\right].$$
- $S_{XX}$ 偶、$S_{XY}$ 奇；載波不夠高時兩份會疊加（aliasing）。

### Rice 表示法

- 任何零平均 WSS 的 $X$ 都能寫成 $A\cos\omega_0t-B\sin\omega_0t$（均方），不唯一。
- $Y=h*X$ 要平衡：$|H|^2=1$ 且 $H^*=-H$；Hilbert 轉換符合。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Rice 表示法、選 $Y$ 的條件 | 下一集：輔助條件、Hilbert 轉換是最佳選擇（包絡變化率最小） |
| 單邊帶、Hilbert 轉換 | 第 17–18 集 |
| 基頻與射頻的頻譜關係、aliasing | §10-5 帶限過程與取樣（第 20 集） |
| 調變後的平穩性 | §10-4 循環平穩過程（第 19 集）：載波沒有隨機相位時不是 WSS |

---

## 附：本集一句話總結

> **在 $A,B$ 零平均聯合 WSS 的前提下，調變訊號 $A\cos\omega_0t-B\sin\omega_0t$ 是 WSS ⇔ $A,B$ 能量平衡（$R_{AA}=R_{BB}$、$R_{AB}=-R_{BA}$）；基頻與射頻透過乘複數載波再取實部連在一起，是全對稱、一穩全穩的系統；而被丟掉的虛部 $Y$，正是 Rice 表示法要選的東西——選 $Y=h*X$ 時，$h$ 必須是全通且 $H^*=-H$，Hilbert 轉換就是其中之一。**

---

## ⚠️ 待確認清單

1. [▶ 07:44](https://youtu.be/qTKcT61ea1k?t=464) 老師的反例用了哪兩個函數，逐字稿沒唸出；筆記的 $A=Z\sin\omega_0t$、$B=Z\cos\omega_0t$ 是推論的。
2. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 10-3 (1/3) 錄影逐字稿（whisper large-v3-turbo，57:56）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
