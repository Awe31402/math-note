---
course: Stanford AA274A Principles of Robotic Autonomy（2019 秋）
episode: 2
lecture: Lecture 2
date: 待補
video: https://youtu.be/vEDeUdZ-jnQ
notes: 《Principles of Robot Autonomy》Robot Autonomy Software 章（書頁 15–20，PDF 頁 17–22）
---

# 第 2 集 · Lecture 2：機器人作業系統 ROS（The Robot Operating System） [▶ 影片](https://youtu.be/vEDeUdZ-jnQ)

← 上一集：[01-overview-mobile-robot-kinematics](01-overview-mobile-robot-kinematics.md) ｜ [總目錄](README.md) ｜ 下一集：[03-trajectory-optimization](03-trajectory-optimization.md) →

> **課程**：Stanford AA274A Principles of Robotic Autonomy I，2019 秋 — 第 2 集
> **講者**：Marco Pavone 開場介紹；主講是 Pavone 實驗室的資深博士生（Whisper 聽成「Pinoy」，推斷是 Benoit Landry，課本致謝有提到他）
> **來源**：YouTube 錄影逐字稿（1:14:05，Whisper `medium.en` 轉錄）＋《Principles of Robot Autonomy》Robot Autonomy Software 章
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單
>
> 照 BRIEF：本集**不抄程式碼**，程式的部分改用步驟說明；終端機指令可以列。Whisper 常把「ROS」聽成「Rust」，以下直接改回 ROS，不逐一標註。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼機器人軟體很難](#1-為什麼機器人軟體很難)
- [2. 模組化與 Pub/Sub 設計模式](#2-模組化與-pubsub-設計模式)
- [3. ROS 是什麼、為什麼這麼流行](#3-ros-是什麼為什麼這麼流行)
- [4. 一點歷史](#4-一點歷史)
- [5. 節點（node）](#5-節點node)
- [6. ROS master](#6-ros-master)
- [7. 寫一個發布者與訂閱者](#7-寫一個發布者與訂閱者)
  - [7.1 發布者（talker）](#71-發布者talker)
  - [7.2 訂閱者（listener）](#72-訂閱者listener)
  - [7.3 Demo 與命令列工具](#73-demo-與命令列工具)
- [8. Launch 檔](#8-launch-檔)
- [9. 例子：相機邊緣偵測系統與 rqt_graph](#9-例子相機邊緣偵測系統與-rqt_graph)
- [10. 開發工具：catkin 工作區與套件](#10-開發工具catkin-工作區與套件)
- [11. 其他工具：除錯、訊息定義、URDF、Gazebo](#11-其他工具除錯訊息定義urdfgazebo)
- [12. ROS 2 與課程公告](#12-ros-2-與課程公告)
- [13. 一頁速查表](#13-一頁速查表)
- [14. 與後續集數的連結](#14-與後續集數的連結)

---

## 0. 這堂課要做什麼

`【口頭】` Pavone 開場：ROS 是本課用來搭自主堆疊的軟體環境；如果你以後走機器人這行，用到 ROS 的機率非常高。熟悉 ROS 是本課主要目標之一。今天由實驗室的資深博士生講，他是「ROS 老手」。

主講者說：這堂和其他堂不一樣，**講的是軟體，不是演算法**。

| 主題 | 課本 |
|---|---|
| 為什麼機器人軟體不同 | Robot Autonomy Software 章「Why Robot Software Is Different」 |
| ROS 歷史 | 「A Brief History of ROS」 |
| 節點、訊息、topic、套件 | 「Core ROS Concepts」 |
| master、launch、catkin、URDF、Gazebo | 課本沒有（只在本集） |

---

## 1. 為什麼機器人軟體很難

[▶ 02:13](https://youtu.be/vEDeUdZ-jnQ?t=133)

`【口頭】` 講者放 DARPA 機器人挑戰賽（DARPA Robotics Challenge）的照片：一整個房間的人、至少 8 個螢幕，都在盯著一台 Atlas 人形機器人，而它只是在爬樓梯、別撞到東西。**跑一台機器人很複雜，寫跑機器人的軟體更複雜。**

本課的軟體很可能是你碰過最複雜的：不像 CS229 那種一個腳本、靠一個函式庫就跑；這裡有很多會動的零件。

【課本補充】課本列出機器人軟體的四個需求：

- **多工（multitasking）**：感測、估計、規劃、控制要同時跑，頻率還不一樣。
- **底層硬體控制**：要透過 GPIO、USB、SPI 等協定跟硬體講話，所以要支援 C++、Python 等多種語言。
- **高階物件導向抽象**：堆疊變大後需要模組化、封裝、重用。
- **社群函式庫**：不可能每個人都從頭寫所有演算法。

---

## 2. 模組化與 Pub/Sub 設計模式

[▶ 03:48](https://youtu.be/vEDeUdZ-jnQ?t=228)

對付複雜系統最常見的策略是**模組化（modularity）**：不要寫成一個大程式，拆成很多小模組。

拆的方法要遵循某個**設計模式（design pattern）**：一種一般性、可重用的解法，用來處理一直重複出現的同類問題。

本集用的是 **Pub/Sub（發布／訂閱，publish–subscribe）** 設計模式：

- 定義一些 **topic（主題）**。講者的比喻：聊天室、Slack 頻道。
- 每個模組（client）對每個 topic 可以做兩件事：
  - **發布（publish）**：在 topic 上送出訊息。
  - **訂閱（subscribe）**：「只要有人在這個 topic 上發東西，就傳給我。」
- 任何人都能發布，任何人都能訂閱（一對多、多對多都行）。

`【課堂討論】` [▶ 06:41](https://youtu.be/vEDeUdZ-jnQ?t=401) 講者問：你們每天都在用的 Pub/Sub 是什麼？學生答 Reddit 的討論串（訂閱一個串）。另一個學生開玩笑說「這堂課本身？」→ 講者：如果讓大家都講話，那倒有點像。講者心裡想的答案是**郵件列表（mailing list）**：任何人寄信到「單車社郵件列表」，所有訂閱者都會收到。

**其他設計模式**（[▶ 07:40](https://youtu.be/vEDeUdZ-jnQ?t=460)）：

- **請求／回覆（request–reply）**。
- **資料綁定（data binding）**：共用一個物件。用郵件列表的例子來說，就像走廊上一塊黑板，大家都在上面寫、也都看得到別人寫的。

> 講者：今天如果只記得一件事，就記住 **Pub/Sub 是什麼**，以及 **ROS 的核心就是 Pub/Sub 的一種實作**。語法記不住沒關係。

---

## 3. ROS 是什麼、為什麼這麼流行

[▶ 08:24](https://youtu.be/vEDeUdZ-jnQ?t=504)

**嚴格定義**：ROS 就是 Pub/Sub 設計模式的一種實作，專為機器人設計，而且懂網路（network aware，節點可以分散在不同電腦上）。

**日常用法**：大家說「我在用 ROS」，通常也包含**圍繞這個實作長出來的一整套工具和熱門套件**。

**替代品**：LCM（較輕量）、Drake（比較是替代「工具」那部分）等。

【課本補充】課本強調：ROS 名字叫作業系統，但**不是傳統意義的作業系統**，而是**中介軟體（middleware）**——一組工具、函式庫和慣例。

**為什麼業界愛用**（[▶ 10:21](https://youtu.be/vEDeUdZ-jnQ?t=621)）：不是因為比較快或有什麼魔法，理由很實際：

1. **不想重造輪子**：別人已經寫好不錯的視覺化工具，就不用花一半種子資金自己寫。
2. **成熟**：ROS 出來很久了。
3. **採用率**：很多頂尖團隊用 ROS 並開源他們的程式，你可以直接拿來用。

**為什麼這門課用它**（[▶ 11:36](https://youtu.be/vEDeUdZ-jnQ?t=696)）：

- 業界在用。就算你以後的公司不用 ROS，也幾乎一定會用很像 ROS 的東西。
- 最接近業界標準、最穩定，算是給你的「保險」。
- 網路上資源超多（書、文件），助教和講義教不到的可以自己查；其他框架沒有這麼多文件。

【課本補充】課本列出 ROS 的設計哲學：點對點（peer-to-peer）、多語言、以工具為本（tools-based）、薄（thin，核心演算法盡量寫成不依賴 ROS 的獨立函式庫）、免費開源（BSD 授權）。

---

## 4. 一點歷史

[▶ 13:01](https://youtu.be/vEDeUdZ-jnQ?t=781)

- ROS 部分源自 Stanford 的 **STAIR** 機器人計畫。
- 真正推動的是 **Willow Garage**，出資者是 Scott Hassan。Willow Garage 推出了 **PR2** 機器人（講者形容：像台冰箱、有兩隻手臂，現在看有點笨重，但當年很驚人）。講者說它雖是新創，卻幾乎像非營利組織，對社群貢獻極大。
- 現代的接班人：**OSRF**（Open Source Robotics Foundation，開源機器人基金會），在灣區，資助 ROS、Gazebo 等工具的開發。

> ⚠️ 逐字稿缺字 [▶ 13:17](https://youtu.be/vEDeUdZ-jnQ?t=797)：Whisper 寫「Scott Lassonde」，課本寫 **Scott Hassan**，依課本修正。

【課本補充】時間線：2007 年從 STAIR 出現早期版本；2009 年 ROS 0.4 搭配 PR2；2010 年 ROS 1.0；2012 年交給 OSRF；2014 年第一個長期支援版 Indigo Igloo；2017 年 OSRF 改名 Open Robotics。

`【口頭】` [▶ 14:28](https://youtu.be/vEDeUdZ-jnQ?t=868) 很多常用函式庫都有 ROS 包裝（wrapper），例如電腦視覺的 OpenCV，方便整合進 ROS。

---

## 5. 節點（node）

[▶ 14:56](https://youtu.be/vEDeUdZ-jnQ?t=896)

打開 ROS 原始碼，核心就兩樣東西：**master** 和 **節點**。

**節點**：一個做計算的**獨立行程（process）**。用 Python 的話，就是一個有 main 函式的小腳本。它是 ROS 的**基本積木**：要描述你的機器人軟體架構，列出有哪些節點就夠了。

- 節點透過 topic 互相溝通，傳的是**訊息（message）**。訊息可以代表相機影像、雷射掃描、運動控制指令、位姿估計、邊緣偵測影像……本課教的東西幾乎都有對應的 ROS 訊息型別。
- 啟動節點的指令：`rosrun <套件名> <節點名>`，例如 `rosrun my_navigation lidar_driver`。

**什麼東西可以是節點**（[▶ 18:13](https://youtu.be/vEDeUdZ-jnQ?t=1093)）：

- **感測器**：Atlas 上的魚眼相機、光達（LiDAR）、慣性測量單元（IMU）、腳底的應變規，每個都可以是一個節點。
- **致動器**：每個馬達可以是一個節點。
- **演算法**：例如一個專門用動力學模型往前模擬機器人的節點、一個跑運動規劃的節點。

`【口頭】` 很妙的是：架構圖上，「跑抽象演算法的節點」和「控制實體馬達的節點」長得幾乎一樣。ROS 讓你用同一種方式組織軟體和硬體。

**Q&A**

- `【Q&A】` [▶ 19:50](https://youtu.be/vEDeUdZ-jnQ?t=1190) 節點像獨立腳本，各跑各的，那動力學節點和感測器節點怎麼溝通、怎麼同時跑？→ 這就是 Pub/Sub 的作用。每個節點只要清楚「我訂閱什麼、我發布什麼」就能獨立跑。例如動力學模擬節點只要訂閱目前的感測量測，就能往前推預測。同步有時還是很難（某節點需要的資訊別人沒送），這是系統工程的「藝術」，但 Pub/Sub 大致有不錯的解法。
- `【Q&A】` [▶ 20:56](https://youtu.be/vEDeUdZ-jnQ?t=1256) topic 的頻率是誰決定的？ROS 有上限嗎？→ 由**每個節點自己決定**（例如「我以 1 Hz 發布」），程式裡就能設定。瓶頸通常是電腦速度或網路；講者所知 ROS 內部**沒有**節流機制。
- `【Q&A】` [▶ 21:54](https://youtu.be/vEDeUdZ-jnQ?t=1314) 投影片的架構圖裡，白框是節點、綠框是 topic 嗎？→ 不完全一一對應；白框大概是節點、藍色箭頭大概是 topic。別太認真看那張圖，重點是演算法和感測器都能是節點。

具體例子：光達節點、發布影像 topic 的相機節點、發布里程計（odometry）資料（加速度、角速度）的 IMU 節點——本課都會碰到。

---

## 6. ROS master

[▶ 23:24](https://youtu.be/vEDeUdZ-jnQ?t=1404)

master 在抽象的 Pub/Sub 設計裡**沒有對應物**，是實作時的「必要之惡」：總得有人管理聊天室／郵件列表。

- 每次啟動整個堆疊都要先啟動它。
- 它負責**協調節點**：誰發布、誰訂閱。
- 一個網路上**只需要一個** master。

**常見誤解（連資深機器人學家都會犯）**：以為訊息會經過 master。**不會。** master 只負責把發布者和訂閱者「牽線」（底層就是在兩者之間建 TCP 連線），然後就退開，讓節點直接互傳。所以期末專題如果你覺得「是 master 成了瓶頸」，那不是真正的原因。

**Q&A**

- `【Q&A】` [▶ 25:10](https://youtu.be/vEDeUdZ-jnQ?t=1510)（問題沒錄到，從回答看是在問 master 該放哪台電腦）→ 理論上放哪都行。實務上機器人常當機，所以 master **不放在機器人上**比較好，它才會一直活著，不用重啟。
- `【Q&A】` [▶ 25:47](https://youtu.be/vEDeUdZ-jnQ?t=1547) 既然 master 只負責一開始牽線，為什麼要一直跑？跑完初始化就結束不行嗎？→ 理論上可以，但很多系統的節點會在**執行中出現和消失**。例：自駕車原本在高速公路，到了停車標誌才啟動「追蹤行人」節點，這個新節點要告訴路徑規劃器附近有行人。所以需要 master 一直在。而且 ROS 沒有 master 根本不讓你跑。

【課本補充】課本另外提到 **service（服務）**：除了非同步的 topic，ROS 也支援同步的「請求–回應」，適合一次性的查詢，例如向建圖節點要一份最新地圖。

---

## 7. 寫一個發布者與訂閱者

[▶ 26:58](https://youtu.be/vEDeUdZ-jnQ?t=1618)

本課用 Python（`rospy`）。ROS 也有 C++、Julia 等介面。

發送訊息的骨架：建立發布者 → 建立訊息物件、填資料 → 用發布者發出去。發出後，所有訂閱該 topic 的節點都收得到。

### 7.1 發布者（talker）

[▶ 28:46](https://youtu.be/vEDeUdZ-jnQ?t=1726)

講者逐行講解一個叫 `talker` 的節點。步驟（不抄程式）：

1. **宣告自己是 ROS 節點**（`init_node`），名字叫 `talker`。
   - 參數 `anonymous=True`：允許多個同名節點，ROS 會在名字後面加唯一 ID。若為 False，master 會確保名字不重複；新開一個同名節點會把**舊的殺掉**。
   - 這一步同時讓節點向 master **註冊**自己。
2. **建立發布者**，給三樣東西：
   - topic 名稱：`chatter`（就是那個 Slack 頻道）。
   - 訊息型別：`String`。注意這**不是** Python 的字串，而是 ROS 標準訊息庫（`std_msgs`）的字串型別。
   - `queue_size`：網路塞住、送太快時，最多留幾則、何時開始丟舊訊息。
3. **讀參數 `rate`**（發布頻率）：向參數伺服器查名叫 `rate` 的參數，查不到就用預設值。講者比喻：像查 Python 字典，查不到就回傳預設值。
4. **建立 ROS 的 Rate 物件**，迴圈每次用它睡到下一拍。
5. **迴圈**：記一筆 log（相當於 print）→ 建立訊息、填資料 → 發布 → 睡到下一拍 → 重複。

**為什麼不用 Python 自己的計時器？**（[▶ 30:37](https://youtu.be/vEDeUdZ-jnQ?t=1837)）因為節點可能接到**模擬器**，而模擬器可能比真實時間慢或快。用 ROS 自己的時鐘，所有節點才會用同一個時間。平常 ROS 時鐘就等於牆上的時鐘。

真實系統的訊息常是有很多欄位的物件，例如 IMU 量測要填加速度計和陀螺儀的值。

**Q&A**

- `【Q&A】` [▶ 32:15](https://youtu.be/vEDeUdZ-jnQ?t=1935) 節點只用一個函式就能寫，不用寫成類別嗎？→ 這是最簡寫法。實務上講者 80% 會包一個類別，因為一個節點常常**同時**訂閱和發布：訂閱到的資料存在類別裡，再跑例如路徑規劃，然後以固定頻率發布結果。
- `【Q&A】` [▶ 33:07](https://youtu.be/vEDeUdZ-jnQ?t=1987) 固定頻率睡覺是慣例嗎？還是會用狀態機一直檢查中斷？→ 要固定頻率跑的東西就用 Rate 睡覺。有些東西只想「收到訊息才做」，例如收到一張影像就跑電腦視覺，那就是訂閱者的寫法（7.2）。期末專題的堆疊兩種都會有。
- `【Q&A】` [▶ 34:52](https://youtu.be/vEDeUdZ-jnQ?t=2092) master 在這段程式哪裡參與？→ 程式裡沒有啟動 master，要另外先啟動。`init_node` 那行在背後向 master 註冊這個節點。
- `【Q&A】` [▶ 35:28](https://youtu.be/vEDeUdZ-jnQ?t=2128) 讀 rate 參數那兩個參數是什麼？→ 見步驟 3、4。master 除了牽線，還有很多協調工作，其中一個是**儲存整個系統的參數**。

### 7.2 訂閱者（listener）

[▶ 37:34](https://youtu.be/vEDeUdZ-jnQ?t=2254)

訂閱者用**回呼函式（callback）**：收到訊息時自動呼叫的函式。講者說訂閱者其實比發布者更不好懂。步驟：

1. 宣告自己是節點（和發布者一樣——「節點都活在一個平等的世界」）。
2. **建立訂閱者**，給三樣東西：topic 名稱 `chatter`、訊息型別 `String`、收到訊息時要呼叫的回呼函式。
3. 實作回呼函式：收到訊息就把 `message.data`（裡面的字串）印出來。
4. 呼叫 `spin`：「現在原地待命；任何訂閱收到訊息，就呼叫對應的回呼。」不用自己寫迴圈。

`【口頭】` 範例裡回呼函式就叫 `callback`，講者說別學這個命名，會搞混。

**Q&A**

- `【Q&A】` [▶ 40:06](https://youtu.be/vEDeUdZ-jnQ?t=2406) 訂閱者也能設佇列嗎？→ 可以，是選用參數。一般用不到，除非頻率超高。
- `【Q&A】` [▶ 40:39](https://youtu.be/vEDeUdZ-jnQ?t=2439) 為什麼訂閱者需要佇列？→ 如果回呼要花很久，例如每則訊息是「解一個最佳化問題」要 10 分鐘，但對方每 5 分鐘就送一個，問題就會越堆越多。這種事常發生，要注意誰跟得上誰。
- `【Q&A】` [▶ 41:26](https://youtu.be/vEDeUdZ-jnQ?t=2486) 訂閱者也要向 master 註冊嗎？→ 對，`init_node` 做一次就好。這就是 ROS 節點和普通 Python 腳本的差別。
- `【Q&A】` [▶ 41:55](https://youtu.be/vEDeUdZ-jnQ?t=2515) 發布者比訂閱者快很多（例如感測資料），能只看最新的嗎？→ 可以，可以設定丟掉最舊的或其他佇列策略。ROS 2 在這方面更講究。

### 7.3 Demo 與命令列工具

[▶ 42:27](https://youtu.be/vEDeUdZ-jnQ?t=2547)

講者現場示範：

1. `roscore`：啟動 master（`roscore` 和「ROS master」基本上指同一件事）。它會印出目前的參數；這時還沒有 `rate` 參數，所以 talker 會用預設值。唯一的參數是 ROS 發行版名稱（當時課堂用 **Kinetic**）。
2. 啟動 talker：開始以 1 Hz 印出並發布訊息。
3. `rostopic list`：列出目前所有 topic，看到 `chatter`（還有 `/rosout`、`/rosout_agg`，先不管）。
4. `rostopic hz chatter`：顯示發布頻率約 1 Hz，還附標準差等統計。
5. 啟動 listener：以約 1 Hz 收到並印出 talker 的訊息。

**常用命令列工具**（[▶ 34:11](https://youtu.be/vEDeUdZ-jnQ?t=2051)）：

| 指令 | 用途 |
|---|---|
| `rostopic list` | 列出所有 topic |
| `rostopic echo <topic>` | 印出 topic 上的訊息 |
| `rostopic hz <topic>` | 量 topic 的發布頻率 |

`【口頭】` `rostopic hz` 期末超好用：「為什麼我的狀態估計全錯？」→ 一查發現光達每 100 秒才給一次量測（0.01 Hz）。

**Q&A**

- `【Q&A】` [▶ 45:36](https://youtu.be/vEDeUdZ-jnQ?t=2736)（問題沒錄到，從回答看是在問能不能直接用 Python 跑腳本而不用 `rosrun`）→ Python 兩種都行。小細節：用 `rosrun` 跑時，`print` 的輸出會被 ROS 吃掉，所以要用 ROS 的 log 方法。
- `【Q&A】` [▶ 46:43](https://youtu.be/vEDeUdZ-jnQ?t=2803)（問 log 裡的時間戳是什麼）→ 是電腦的 epoch 時間：從 1970 年 1 月 1 日起算的秒數。但機器人不在乎今天是星期二早上，在乎的是「距離上一次光達量測過了 5 秒」，所以通常看**相對時間**。

> 講者：看起來很陽春，但**這就是全部**。很複雜的系統就是由很多這種節點互傳訊息組成；作業 1 是一個節點、作業 2 是另一個，讓它們互相講話就能做出很神奇的事。

---

## 8. Launch 檔

[▶ 48:04](https://youtu.be/vEDeUdZ-jnQ?t=2884)

節點一多（talker、listener 再加 12 個），每次一個一個開很煩。**launch 檔**是一個 XML 檔，描述怎麼一次啟動整個堆疊：

- 要啟動哪些節點：節點名稱、在哪個套件、型別（就是哪個腳本）。
- 輸出要印到螢幕還是別處。
- 參數設定。例：在 launch 檔把 `rate` 設成 5，用它啟動 talker 時就會以 **5 Hz** 發布，而不是預設的 1 Hz。

理想上，期末專題最後只要在機器人上打一行 `roslaunch <套件> <launch 檔>`，所有節點就都起來了。

**Q&A**

- `【Q&A】` [▶ 55:40](https://youtu.be/vEDeUdZ-jnQ?t=3340)（問 launch 檔裡引用別的 launch 檔）→ 兩種寫法：把每個節點都列出來；或**引用別人寫好的 launch 檔**，形成階層。後者的好處：有些 launch 檔超大（例如設定 16 台相機各自的影像寬度），能直接用別人辛苦寫好的很方便；也可以覆寫它的參數。
- `【Q&A】` [▶ 57:05](https://youtu.be/vEDeUdZ-jnQ?t=3425)（問參數的作用範圍）→ 所有參數都存在 master 的同一個地方，大家都讀得到；但在某個節點裡定義的參數會加上前綴（例如 `image_view2/autosize`），算是「軟性」標示它屬於哪個節點。

---

## 9. 例子：相機邊緣偵測系統與 rqt_graph

[▶ 50:29](https://youtu.be/vEDeUdZ-jnQ?t=3029)

一個比較有趣、而且盡量**重用現成套件**的系統，共四個節點：

1. **相機驅動節點**（講者筆電的 webcam，套件 `usb_cam`）：發布原始影像 topic（`/usb_cam/image_raw`）。
2. **影像顯示節點**：訂閱原始影像，顯示出來。
3. **邊緣偵測節點**（電腦視覺演算法，本課之後會教）：**也訂閱同一個**原始影像 topic，偵測邊緣後發布到另一個 topic（邊緣偵測影像）。
4. **第二個影像顯示節點**：訂閱邊緣偵測影像，顯示出來。

一個 topic 可以被多個節點訂閱（節點 2 和 3 都聽原始影像）。

**`rqt_graph`**：ROS 工具，能自動畫出目前所有節點和 topic 的連接圖。

`【口頭】` 這就是你們之後要做的縮小版：感測器、IMU 資料、小視覺化工具、狀態估計器、路徑規劃器……

`【口頭】` 現場 demo 時相機驅動節點當掉了（「別做現場 demo，從來不會成功」），講者改成直接講這個系統的 launch 檔：其中一個節點是引用另一個套件的 launch 檔，另外三個節點直接列出。

---

## 10. 開發工具：catkin 工作區與套件

[▶ 58:18](https://youtu.be/vEDeUdZ-jnQ?t=3498)

**catkin 工作區（catkin workspace）**：看起來好像多此一舉（Python 腳本不是直接跑就好？），但 ROS 要支援 C++，而 C++ 要編譯。catkin 是編譯器的包裝，幫你整理套件，讓編譯器找得到各部分。工作區就是你電腦上的一個資料夾。

**套件（package）**：工作區裡的程式按套件組織，`rosrun <套件名> <節點名>` 的套件就是這個。

典型結構（講者說看起來太繁瑣，「怪 C++」）：

```
catkin 工作區/
└── src/
    └── 某個套件/
        ├── CMakeLists.txt、package.xml   ← 不用管
        ├── config/    設定檔
        ├── include/   C++ 標頭檔
        ├── scripts/   ← Python 節點腳本放這裡
        ├── src/       C++ 原始碼
        ├── launch/    launch 檔
        └── msg/       自訂訊息型別
```

ROS 也有工具幫你建立套件，指定套件名和相依套件。

**Q&A**

- `【Q&A】` [▶ 61:07](https://youtu.be/vEDeUdZ-jnQ?t=3667) 寫 C++ 的話，原始碼放 `src`，然後呢？→ 回到工作區最上層跑 `catkin_make`，它會找到專案並編譯。

`【口頭】` **一定會發生的坑**（[▶ 61:37](https://youtu.be/vEDeUdZ-jnQ?t=3697)）：你在 `scripts/` 放了新腳本，`rosrun` 卻說找不到。原因：**腳本沒有設成可執行**。作業會教你用一行指令修好。

- `【Q&A】` [▶ 62:15](https://youtu.be/vEDeUdZ-jnQ?t=3735) 什麼東西該算一個套件？→ 是軟體工程的決定。通常以「能力（capability）」為單位，例如一個「估計」套件，裡面有很多節點。應該是可重用、針對某種需求的一組工具。
- `【Q&A】` [▶ 63:17](https://youtu.be/vEDeUdZ-jnQ?t=3797)（問 launch 檔放哪、能不能跨套件）→ launch 檔放在套件裡，而且能**找到別的套件裡的東西**。例：一個「感測器驅動」套件只放驅動節點；「估計」套件的 launch 檔可以去啟動感測器套件裡的光達 launch 檔，再啟動自己的 EKF。

【課本補充】課本對套件的定義：一個資料夾，放相關的節點、函式庫、資料集、設定檔等，是 ROS 程式組織和散布的主要單位。

---

## 11. 其他工具：除錯、訊息定義、URDF、Gazebo

[▶ 64:32](https://youtu.be/vEDeUdZ-jnQ?t=3872)

**除錯**

- ROS 的 log 不只是 print：有一個 console GUI 能依重要程度顯示 log。DARPA 那間房裡的人大概就在看這種工具，確認「光達是不是又掛了」。
- 好好學 Python 除錯器 **pdb**，可以一行一行跑。

**訊息定義**（[▶ 65:52](https://youtu.be/vEDeUdZ-jnQ?t=3952)）：ROS 支援多種語言，所以訊息不能只是一個 Python 類別，要用**與語言無關**的語法定義（例如一個「學生」訊息有名、姓、年齡、成績欄位）。ROS 工具會自動生成 Python、C++、Java、Julia 等版本的類別。這是 Pub/Sub 的一大好處：跨語言。基本訊息型別 ROS 都已經有了。

**ROS 不只有 Pub/Sub**（[▶ 67:05](https://youtu.be/vEDeUdZ-jnQ?t=4025)）：ROS 也支援其他模式（例如 service），但講者估計 95% 的用法是 Pub/Sub，所以說「ROS 基本上就是 Pub/Sub」仍然公道。參數伺服器前面講過。

**URDF**（[▶ 67:49](https://youtu.be/vEDeUdZ-jnQ?t=4069)）：Universal Robot Description Format（通用機器人描述格式），一種 XML 檔。

- 幾乎所有機器人都能寫成**運動鏈（kinematic chain）**：一串**連桿（link）**中間接**關節（joint）**，像上臂、前臂接手肘，整體是樹狀結構。
- 把這個描述寫進 XML，就成了**可重用的機器人模型**。拿到別人機器人的 URDF，就能把它放進你的模擬、得到它的運動學、動力學。

**Gazebo**（[▶ 69:55](https://youtu.be/vEDeUdZ-jnQ?t=4195)）：模擬器，能根據 URDF 建出機器人（例如 PR2）。Gazebo 不是 ROS 的一部分（他們很在意這點），但兩者整合得很好，大家都一起用。好的模擬器有兩個價值：

1. **模擬物理**：確認控制器、路徑追蹤控制器能用。
2. **軟體環境一樣**：你的 ROS 堆疊對著模擬跑，**同樣的節點、發布同樣的訊息**，直接搬到真機器人上不用改。否則在模擬裡寫好、上真機器人又要全部重寫，模擬就沒什麼用。這能省下好幾週。

`【口頭】` 先在模擬裡跑通：模擬裡不行，真機器人上大概也不行；模擬裡行，真機器人上**可能**行。

還有 transform 函式庫（tf）等工具。資源：ROS wiki、GitHub 各套件的 README、StackOverflow、Google、助教。

---

## 12. ROS 2 與課程公告

[▶ 72:40](https://youtu.be/vEDeUdZ-jnQ?t=4360)

- ROS 從 2007 年至今十多年，最近大改版成 **ROS 2**。當時還不支援所有東西，本課為求成熟穩定，**先不用 ROS 2**，但值得關注。
- 作業 1 週五發布，下週做基本模擬和環境設定。
- 推薦 Stanford Robotics Seminar（每週五上午 11 點，1 學分，有食物，可以找研究點子和未來的指導教授）。

【課本補充】課本說明 ROS 2 的動機：ROS 1 沒有把即時保證、確定性通訊、在不可靠網路上的多機器人部署當成首要考量；ROS 2 建在 DDS（Data Distribution Service）之上，原生支援即時通訊、更好的安全性、分散式系統，以及服務品質（QoS）參數的控制。

---

## 13. 一頁速查表

### 核心概念

| 名詞 | 一句話 | 比喻 |
|---|---|---|
| Pub/Sub | 模組透過 topic 發布／訂閱訊息，彼此不需要知道對方存在 | 郵件列表 |
| topic | 有名字的訊息頻道 | Slack 頻道 |
| 節點（node） | 一個做計算的獨立行程，可以是感測器、致動器或演算法 | 一個 Python 腳本 |
| 訊息（message） | 與語言無關的資料型別，自動生成各語言的類別 | 信的內容 |
| master | 幫節點牽線、存參數；**訊息不經過它** | 郵件列表管理員 |
| service | 同步的請求–回應（課本） | 打電話問一次 |
| 參數伺服器 | master 裡存全系統參數的地方 | 字典（查不到用預設值） |
| launch 檔 | XML，一次啟動多個節點、設參數，可階層引用 | 開機腳本 |
| 套件（package） | 程式組織與重用的單位，通常一個「能力」一個 | 一個資料夾 |
| catkin 工作區 | 編譯與組織套件的資料夾 | 專案根目錄 |
| URDF | 用連桿＋關節描述機器人的 XML | 機器人的設計圖 |
| Gazebo | 和 ROS 整合的物理模擬器 | 試車場 |

### 發布者 vs. 訂閱者

| | 發布者 | 訂閱者 |
|---|---|---|
| 1 | `init_node`（同時向 master 註冊） | 同左 |
| 2 | 建立發布者：topic、型別、`queue_size` | 建立訂閱者：topic、型別、回呼函式 |
| 3 | 迴圈：建訊息 → 發布 → 用 ROS Rate 睡 | `spin`：原地等，收到就呼叫回呼 |
| 時機 | 固定頻率 | 收到訊息才做事 |

關鍵：用 **ROS 時鐘**而不是 Python 計時器，因為模擬器可能比真實時間快或慢。

### 指令

`roscore`、`rosrun <pkg> <node>`、`roslaunch <pkg> <file>`、`rostopic list / echo / hz`、`rqt_graph`、`catkin_make`

### 常見坑

1. 以為訊息經過 master（不會）。
2. `rosrun` 找不到腳本 → 腳本沒設成可執行。
3. 用 `rosrun` 時 `print` 看不到 → 改用 ROS log。
4. 回呼太慢、訊息越堆越多 → 注意佇列與頻率。
5. 狀態估計怪怪的 → 用 `rostopic hz` 查感測器頻率。

---

## 14. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 節點、topic、launch | 所有作業與期末專題 |
| 邊緣偵測節點 | 第 11 集影像處理 |
| 光達、相機、IMU 節點 | 第 8 集感測器 |
| EKF 節點、估計套件 | 第 13–16 集濾波、定位、SLAM |
| 路徑規劃節點 | 第 3–7 集軌跡最佳化與運動規劃 |
| URDF、運動鏈 | 第 1 集的完整約束（關節） |

---

## 附：本集一句話總結

> **ROS 的核心就是 Pub/Sub：把機器人軟體拆成很多節點，節點透過有名字的 topic 發布和訂閱訊息；master 只負責牽線和存參數，訊息不經過它。其他一切（launch、catkin、URDF、Gazebo）都是圍繞這個核心長出來的工具。**

---

## ⚠️ 待確認清單

1. 上課日期待補。
2. 主講者身分：Whisper 聽成「Pinoy」，依課本致謝推斷是 Benoit Landry，待確認。
3. [▶ 25:10](https://youtu.be/vEDeUdZ-jnQ?t=1510)、[▶ 45:36](https://youtu.be/vEDeUdZ-jnQ?t=2736) 兩則學生提問本身沒錄到，問題內容是從回答推測的。

---

*筆記依據「Stanford AA274A Principles of Robotic Autonomy（2019 秋）」Lecture 2 錄影逐字稿（Whisper `medium.en`，1:14:05）與《Principles of Robot Autonomy》Robot Autonomy Software 章整理。*
