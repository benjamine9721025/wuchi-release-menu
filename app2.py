import streamlit as st
import textwrap

st.set_page_config(
    page_title="37•21 慣性釋放 - 狂野互動菜單",
    layout="centered",
)

html_code = textwrap.dedent("""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>37•21 慣性釋放 - 狂野互動菜單</title>
    <style>
        /* 載入粗獷風格字體 */
        @import url('https://fonts.googleapis.com/css2?family=Anton&family=Noto+Sans+TC:wght@400;700;900&display=swap');

        :root {
            --neon-red: #ff003c;
            --neon-blue: #00f3ff;
            --warning-yellow: #f7d117;
            --dark-bg: #121212;
            --font-main: 'Noto Sans TC', sans-serif;
            --font-heading: 'Anton', 'Noto Sans TC', sans-serif;
        }

        * { box-sizing: border-box; }

        body {
            background-color: var(--dark-bg);
            /* 這裡使用半透明深色，方便內嵌在 Canva 水泥背景上 */
            background: linear-gradient(rgba(18,18,18,0.85), rgba(18,18,18,0.95));
            color: white;
            font-family: var(--font-main);
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 40px 20px;
            overflow-x: hidden;
        }

        /* --- 故障風格標題 (Glitch Effect) --- */
        .glitch-wrapper {
            text-align: center;
            margin-bottom: 30px;
        }

        .main-title {
            font-family: var(--font-heading);
            font-size: 4rem;
            font-weight: 900;
            text-transform: uppercase;
            position: relative;
            color: white;
            text-shadow: 0.05em 0 0 var(--neon-red), -0.05em -0.025em 0 var(--neon-blue);
            animation: glitch 725ms infinite;
        }

        @keyframes glitch {
            0% { text-shadow: 0.05em 0 0 var(--neon-red), -0.05em -0.025em 0 var(--neon-blue); }
            14% { text-shadow: 0.05em 0 0 var(--neon-red), -0.05em -0.025em 0 var(--neon-blue); }
            15% { text-shadow: -0.05em -0.025em 0 var(--neon-red), 0.025em 0.035em 0 var(--neon-blue); }
            49% { text-shadow: -0.05em -0.025em 0 var(--neon-red), 0.025em 0.035em 0 var(--neon-blue); }
            50% { text-shadow: 0.025em 0.05em 0 var(--neon-red), 0.05em 0 0 var(--neon-blue); }
            99% { text-shadow: 0.025em 0.05em 0 var(--neon-red), 0.05em 0 0 var(--neon-blue); }
            100% { text-shadow: -0.025em 0 0 var(--neon-red), -0.025em -0.025em 0 var(--neon-blue); }
        }

        .subtitle {
            font-size: 1.2rem;
            letter-spacing: 0.3em;
            color: var(--warning-yellow);
            margin-top: -10px;
            font-weight: 700;
        }

        /* --- 菜單網格佈局 --- */
        .menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
            width: 100%;
            max-width: 900px;
        }

        /* --- 狂野卡片樣式 --- */
        .menu-card {
            background: rgba(30, 30, 30, 0.9);
            border: 2px solid #444;
            padding: 20px;
            position: relative;
            cursor: pointer;
            transition: all 0.2s;
            /* 斜切角效果 */
            clip-path: polygon(0 0, 100% 0, 96% 100%, 0% 100%);
        }

        /* 黃黑警示條裝飾 */
        .menu-card::after {
            content: "";
            position: absolute;
            bottom: 0; left: 0; width: 100%; height: 5px;
            background: repeating-linear-gradient(45deg, var(--warning-yellow), var(--warning-yellow) 10px, #000 10px, #000 20px);
        }

        .menu-card:hover {
            border-color: var(--neon-blue);
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 0 20px rgba(0, 243, 255, 0.3);
        }

        .menu-card.active {
            border-color: var(--neon-red);
            background: rgba(255, 0, 60, 0.05);
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }

        .item-name {
            font-size: 1.5rem;
            font-weight: 900;
            color: #fff;
        }

        .item-price {
            font-family: var(--font-heading);
            font-size: 1.4rem;
            color: var(--warning-yellow);
        }

        .item-desc {
            font-size: 0.95rem;
            color: #ccc;
            line-height: 1.5;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-out;
        }

        .active .item-desc {
            max-height: 100px;
            margin-top: 15px;
            border-top: 1px solid #444;
            padding-top: 10px;
        }

        /* --- 結算區域 --- */
        .summary-box {
            margin-top: 50px;
            text-align: center;
            border-top: 2px dashed #444;
            padding-top: 30px;
            width: 100%;
        }

        .total-text {
            font-size: 1rem;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .total-amount {
            font-family: var(--font-heading);
            font-size: 3.5rem;
            color: var(--neon-red);
            text-shadow: 0 0 15px var(--neon-red);
            margin: 10px 0 30px;
        }

        /* 立即預約按鈕 */
        .cta-button {
            background: transparent;
            border: 3px solid var(--neon-red);
            color: white;
            padding: 15px 60px;
            font-size: 1.5rem;
            font-weight: 900;
            cursor: pointer;
            position: relative;
            transition: 0.3s;
            clip-path: polygon(10% 0, 100% 0, 90% 100%, 0 100%);
        }

        .cta-button:hover {
            background: var(--neon-red);
            box-shadow: 0 0 30px var(--neon-red);
            transform: scale(1.1);
        }

        /* 響應式調整 */
        @media (max-width: 600px) {
            .main-title { font-size: 2.5rem; }
            .menu-grid { grid-template-columns: 1fr; }
        }

        /* 預約表單 overlay 讓它可以置中顯示 */
        #booking-form-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(0,0,0,0.95);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
    </style>
</head>
<body>

    <div class="glitch-wrapper">
        <h1 class="main-title">37•21 慣性釋放</h1>
        <p class="subtitle">WUCHI RELEASE CENTER</p>
    </div>

    <div class="menu-grid">
        <div class="menu-card" onclick="toggleItem(this, 199)">
            <div class="card-header">
                <span class="item-name">【裂帛】撕布</span>
                <span class="item-price">$199</span>
            </div>
            <div class="item-desc">觸碰纖維斷裂的顫動，把每一絲煩惱徹底撕碎。</div>
        </div>

        <div class="menu-card" onclick="toggleItem(this, 250)">
            <div class="card-header">
                <span class="item-name">【重擊】充氣沙包</span>
                <span class="item-price">$250</span>
            </div>
            <div class="item-desc">20分鐘無差別連續攻擊，拳頭就是你最強的宣洩。</div>
        </div>

        <div class="menu-card" onclick="toggleItem(this, 299)">
            <div class="card-header">
                <span class="item-name">【入木】釘釘子</span>
                <span class="item-price">$299</span>
            </div>
            <div class="item-desc">每一槌都是力量的交響，將不滿死死釘進木頭。</div>
        </div>

        <div class="menu-card" onclick="toggleItem(this, 350)">
            <div class="card-header">
                <span class="item-name">【瓦解】砸紙箱</span>
                <span class="item-price">$350</span>
            </div>
            <div class="item-desc">純粹的破壞美學，看著巨大紙箱在你面前崩塌。</div>
        </div>
    </div>

    <!-- 結算 + 預約按鈕 + 實名制預約表單 -->
    <div class="summary-box">
        <div class="total-text">當前釋放成本估算</div>
        <div class="total-amount">NT$ <span id="price-display">0</span></div>

        <!-- 按鈕：開啟預約表單 -->
        <button id="pre-book-btn" class="cta-button" onclick="openBookingForm()">立即預約體驗</button>

        <!-- 實名制預約表單 overlay -->
        <div id="booking-form-overlay">
            <div style="background: #1a1a1a; border: 3px solid var(--neon-red); padding: 30px; width: 100%; max-width: 400px; position: relative; clip-path: polygon(0 0, 100% 5%, 100% 100%, 5% 95%);">
                <h2 style="font-family: var(--font-heading); color: var(--neon-red); margin-top: 0;">驗證身份</h2>
                <p style="color: #888; font-size: 0.8rem; margin-bottom: 20px;">※ 實名制登記，體驗現場需核對身分證件</p>

                <div style="margin-bottom: 15px;">
                    <label style="display: block; color: var(--warning-yellow); margin-bottom: 5px;">真實姓名</label>
                    <input type="text" id="user-name" placeholder="輸入姓名" style="width: 100%; background: #222; border: 1px solid #444; color: white; padding: 10px; font-size: 1rem;">
                </div>

                <div style="margin-bottom: 15px;">
                    <label style="display: block; color: var(--warning-yellow); margin-bottom: 5px;">聯絡電話</label>
                    <input type="tel" id="user-phone" placeholder="09XX-XXX-XXX" style="width: 100%; background: #222; border: 1px solid #444; color: white; padding: 10px; font-size: 1rem;">
                </div>

                <div style="margin-bottom: 25px;">
                    <label style="display: block; color: var(--warning-yellow); margin-bottom: 5px;">預約日期</label>
                    <input type="date" id="user-date" style="width: 100%; background: #222; border: 1px solid #444; color: white; padding: 10px; font-size: 1rem;">
                </div>

                <div style="display: flex; gap: 10px;">
                    <button onclick="submitBooking()" style="flex: 2; background: var(--neon-red); color: white; border: none; padding: 12px; font-weight: 900; cursor: pointer;">確認登記</button>
                    <button onclick="closeBookingForm()" style="flex: 1; background: #444; color: white; border: none; padding: 12px; cursor: pointer;">取消</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        let totalPrice = 0;
        const display = document.getElementById('price-display');

        // 切換活動項目
        function toggleItem(el, price) {
            el.classList.toggle('active');

            if (el.classList.contains('active')) {
                totalPrice += price;
            } else {
                totalPrice -= price;
            }

            // 更新金額顯示
            display.innerText = totalPrice;

            // 狂野小動效：點擊時畫面微震
            document.body.style.transform = "translate(2px, 1px)";
            setTimeout(() => { document.body.style.transform = "translate(0, 0)"; }, 50);
        }

        // 開啟預約表單
        function openBookingForm() {
            if (totalPrice === 0) {
                alert('請至少選擇一項釋放活動，否則我們無法預測你的狂野程度。');
                return;
            }
            document.getElementById('booking-form-overlay').style.display = 'flex';
        }

        // 關閉預約表單
        function closeBookingForm() {
            document.getElementById('booking-form-overlay').style.display = 'none';
        }

        // 提交預約 (實名制邏輯 + Google Form 串接 + LINE 導向)
        function submitBooking() {
            const name = document.getElementById('user-name').value.trim();
            const phone = document.getElementById('user-phone').value.trim();
            const date = document.getElementById('user-date').value;  // "YYYY-MM-DD"

            if (!name || !phone || !date) {
                alert('實名制預約失敗：請填寫完整資訊！');
                return;
            }

            // 收集已選項目與總額（如果之後想存進表單，可以加欄位）
            const selectedItems = Array.from(document.querySelectorAll('.menu-card.active .item-name'))
                                      .map(el => el.innerText)
                                      .join(', ');
            const finalSummary = `項目: ${selectedItems} | 總計: NT$ ${totalPrice}`;

            // 把日期拆成年 / 月 / 日
            const parts = date.split('-');  // ["YYYY","MM","DD"]
            const year = parts[0];
            const month = parts[1];
            const day = parts[2];

            // --- 1. GOOGLE FORM 串接設定 ---
            // 使用 formResponse 端點
            const formURL = "https://docs.google.com/forms/d/e/1FAIpQLSdaL21IrWIvdMSPHaZj6pTwLlHd769KKKOh1FJ3mMjTVeAygA/formResponse";

            const formData = new FormData();
            formData.append("entry.804859220", name);        // 姓名的 ID
            formData.append("entry.564590322", phone);       // 電話的 ID
            formData.append("entry.342289764_year", year);   // 年的 ID
            formData.append("entry.342289764_month", month); // 月的 ID
            formData.append("entry.342289764_day", day);     // 日的 ID
            // 若之後你想多存 finalSummary，可在表單加一個欄位後，解鎖這行：
            // formData.append("entry.XXXXXXXXX", finalSummary);

            // --- 2. LINE 官方帳號設定 ---
            const lineAccountURL = "https://line.me/R/ti/p/@164gjoxv";

            // 使用 AJAX 傳送資料
            fetch(formURL, {
                method: "POST",
                mode: "no-cors",
                body: formData
            }).then(() => {
                // --- 3. 成功後的跳轉邏輯 ---
                alert("【37•21 慣性釋放】\\n預約成功！資料已加密傳送至基地。\\n\\n確認後將導向 LINE 官方帳號，\\n請傳送「預約確認」與我們聯繫。");

                closeBookingForm();

                // 按下 alert 的確認後，執行跳轉
                window.location.href = lineAccountURL;

            }).catch((error) => {
                alert("傳送失敗，請檢查網路連線或聯繫店員。");
                console.error("Error!", error.message);
            });
        }
    </script>
</body>
</html>
""")

st.components.v1.html(html_code, height=900, scrolling=True)