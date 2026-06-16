import streamlit as st
import textwrap

st.set_page_config(
    page_title="37•21 體驗工作室 - 互動菜單",
    layout="centered",
)

html_code = textwrap.dedent("""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>37•21 體驗工作室 - 互動菜單</title>
    <style>
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

        .glitch-wrapper { text-align: center; margin-bottom: 30px; }

        .main-title { 
            font-family: var(--font-heading);
            font-size: 3.5rem;
            font-weight: 900;
            text-transform: uppercase;
            color: white;
            text-shadow: 0.05em 0 0 var(--neon-red), -0.05em -0.025em 0 var(--neon-blue);
        }

        .subtitle {
            font-size: 1.1rem;
            letter-spacing: 0.2em;
            color: var(--warning-yellow);
        }

        .menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
            width: 100%;
            max-width: 900px;
        }

        .menu-card {
            background: rgba(30, 30, 30, 0.9);
            border: 2px solid #444;
            padding: 20px;
            cursor: pointer;
            transition: all 0.2s;
            clip-path: polygon(0 0, 100% 0, 96% 100%, 0% 100%);
        }

        .menu-card:hover { border-color: var(--neon-blue); transform: translateY(-5px); }
        .menu-card.active { border-color: var(--neon-red); background: rgba(255, 0, 60, 0.05); }

        .item-name { font-size: 1.5rem; font-weight: 900; }
        .item-price { font-family: var(--font-heading); font-size: 1.4rem; color: var(--warning-yellow); }
        .item-meta { font-size: 0.85rem; color: #aaa; margin: 5px 0; }
        .item-desc { font-size: 0.9rem; color: #ccc; margin-top: 10px; border-top: 1px solid #444; padding-top: 10px; }

        .summary-box { margin-top: 40px; text-align: center; width: 100%; }
        .total-text { font-size: 1rem; color: #888; letter-spacing: 2px; }
        .total-amount { font-family: var(--font-heading); font-size: 3rem; color: var(--neon-red); margin: 10px 0; }

        .cta-button {
            background: transparent;
            border: 3px solid var(--neon-red);
            color: white;
            padding: 15px 40px;
            font-size: 1.2rem;
            font-weight: 900;
            cursor: pointer;
        }

        .cta-button:hover {
            background: var(--neon-red);
            box-shadow: 0 0 25px var(--neon-red);
        }

        #booking-form-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.95);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            padding: 20px;
            overflow-y: auto;
        }

        .booking-box {
            background: #1a1a1a;
            border: 3px solid var(--neon-red);
            padding: 30px;
            width: 100%;
            max-width: 400px;
            position: relative;
            clip-path: polygon(0 0, 100% 5%, 100% 100%, 5% 95%);
        }

        .selected-plan-box {
            margin-bottom: 15px;
            text-align: left;
            border: 1px solid #444;
            padding: 12px;
            background: #222;
        }

        .line-success-box {
            background: #1a1a1a;
            border: 3px solid var(--neon-red);
            padding: 30px;
            width: 100%;
            max-width: 460px;
            text-align: center;
            clip-path: polygon(0 0, 100% 5%, 100% 100%, 5% 95%);
        }

        .line-qr {
            background: white;
            padding: 12px;
            border-radius: 10px;
            margin: 15px auto;
            width: 240px;
            height: 240px;
        }

        .line-green-button {
            display: inline-block;
            background: #06C755;
            color: white;
            padding: 16px 28px;
            border-radius: 10px;
            font-size: 1.2rem;
            font-weight: 900;
            text-decoration: none;
            margin-top: 15px;
        }

        .desktop-line { display: block; }
        .mobile-line { display: none; }

        @media (max-width: 600px) {
            .main-title { font-size: 2.5rem; }
            .menu-grid { grid-template-columns: 1fr; }
            .desktop-line { display: none; }
            .mobile-line { display: block; }
            .line-success-box { max-width: 360px; padding: 24px; }
        }
    </style>
</head>

<body>
    <div class="glitch-wrapper">
        <h1 class="main-title">37•21 體驗工作室</h1>
        <p class="subtitle">EXPERIENCE CENTER</p>
    </div>

    <div class="menu-grid">
        <div class="menu-card" onclick="toggleItem(this, 299)">
            <div style="display:flex; justify-content:space-between;">
                <span class="item-name">創意自由拼</span>
                <span class="item-price">$299</span>
            </div>
            <div class="item-meta">時間：90 分鐘</div>
            <div class="item-desc">基礎體驗，無限使用通用積木與少量樂高。</div>
        </div>

        <div class="menu-card" onclick="toggleItem(this, 499)">
            <div style="display:flex; justify-content:space-between;">
                <span class="item-name">樂高主題特展</span>
                <span class="item-price">$499</span>
            </div>
            <div class="item-meta">時間：120 分鐘</div>
            <div class="item-desc">提供樂高限定零件、動力模組，含創作指導。</div>
        </div>

        <div class="menu-card" onclick="toggleItem(this, 550)">
            <div style="display:flex; justify-content:space-between;">
                <span class="item-name">親子共創包</span>
                <span class="item-price">$550</span>
            </div>
            <div class="item-meta">時間：120 分鐘</div>
            <div class="item-desc">雙人同行優惠，適合八德路家庭週末時光。</div>
        </div>
    </div>

    <div class="summary-box">
        <div class="total-text">目前選擇金額</div>
        <div class="total-amount">NT$ <span id="price-display">0</span></div>
        <button class="cta-button" onclick="openBookingForm()">立即預約體驗</button>

        <div id="booking-form-overlay">
            <div class="booking-box">
                <h2 style="font-family: var(--font-heading); color: var(--neon-red); margin-top: 0;">預約資料</h2>
                <p style="color: #888; font-size: 0.8rem; margin-bottom: 20px;">※ 請填寫真實資料，體驗現場將核對預約資訊</p>

                <div class="selected-plan-box">
                    <label style="display:block; color:var(--warning-yellow); margin-bottom:5px;">預約方案</label>
                    <div id="selected-plan-display" style="color:white; line-height:1.6;"></div>
                </div>

                <div style="margin-bottom: 15px; text-align:left;">
                    <label style="display: block; color: var(--warning-yellow); margin-bottom: 5px;">真實姓名</label>
                    <input type="text" id="user-name" placeholder="輸入姓名" style="width: 100%; background: #222; border: 1px solid #444; color: white; padding: 10px; font-size: 1rem;">
                </div>

                <div style="margin-bottom: 15px; text-align:left;">
                    <label style="display: block; color: var(--warning-yellow); margin-bottom: 5px;">聯絡電話</label>
                    <input type="tel" id="user-phone" placeholder="09XX-XXX-XXX" style="width: 100%; background: #222; border: 1px solid #444; color: white; padding: 10px; font-size: 1rem;">
                </div>

                <div style="margin-bottom: 25px; text-align:left;">
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

        function getSelectedItems() {
            return Array.from(document.querySelectorAll('.menu-card.active .item-name'))
                        .map(el => el.innerText)
                        .join(', ');
        }

        function toggleItem(el, price) {
            el.classList.toggle('active');
            totalPrice += el.classList.contains('active') ? price : -price;
            display.innerText = totalPrice;
        }

        function openBookingForm() {
            if (totalPrice === 0) {
                alert('請至少選擇一項體驗項目。');
                return;
            }

            const selectedItems = getSelectedItems();
            document.getElementById('selected-plan-display').innerText = selectedItems;
            document.getElementById('booking-form-overlay').style.display = 'flex';
        }

        function closeBookingForm() {
            document.getElementById('booking-form-overlay').style.display = 'none';
        }

        function submitBooking() {
            const name = document.getElementById('user-name').value.trim();
            const phone = document.getElementById('user-phone').value.trim();
            const date = document.getElementById('user-date').value;
            const selectedItems = getSelectedItems();

            if (!selectedItems) {
                alert('請至少選擇一項體驗項目。');
                return;
            }

            if (!name || !phone || !date) {
                alert('預約失敗：請填寫完整資訊！');
                return;
            }

            const finalSummary = `預約方案: ${selectedItems} | 總計: NT$ ${totalPrice}`;

            const parts = date.split('-');
            const year = parts[0];
            const month = parts[1];
            const day = parts[2];

            // Google Form 連結
            const formURL = "https://docs.google.com/forms/d/e/1FAIpQLSdaL21IrWIvdMSPHaZj6pTwLlHd769KKKOh1FJ3mMjTVeAygA/formResponse";

            const formData = new FormData();
            formData.append("entry.804859220", name);
            formData.append("entry.564590322", phone);
            formData.append("entry.342289764_year", year);
            formData.append("entry.342289764_month", month);
            formData.append("entry.342289764_day", day);

            // ★ 重要：
            // 你需要在 Google 表單新增「預約方案」欄位，
            // 然後把下面的 entry.XXXXXXXXX 改成該欄位的實際 entry ID。
            formData.append("entry.1936317149", selectedItems);

            // 官方 LINE ID：@230iknaq
            // @ 要寫成 %40
            const lineAccountURL = "https://line.me/R/ti/p/%40230iknaq";

            const lineQRURL =
                "https://api.qrserver.com/v1/create-qr-code/?size=240x240&data="
                + encodeURIComponent(lineAccountURL);

            fetch(formURL, {
                method: "POST",
                mode: "no-cors",
                body: formData
            }).then(() => {

                const overlay = document.getElementById('booking-form-overlay');

                overlay.innerHTML = `
                    <div class="line-success-box">

                        <h2 style="font-family: var(--font-heading); color: var(--neon-red);">
                            預約成功
                        </h2>

                        <p style="color:#ccc; line-height:1.8;">
                            您的預約資料已成功送出。
                        </p>

                        <p style="color:var(--warning-yellow); line-height:1.8;">
                            ${finalSummary}
                        </p>

                        <hr style="border:1px solid #444; margin:20px 0;">

                        <h3 style="color:#06C755;">
                            請加入官方 LINE 完成預約確認
                        </h3>

                        <div class="desktop-line">
                            <p style="color:#aaa;">
                                電腦版請使用手機掃描 QR Code
                            </p>

                            <img
                                class="line-qr"
                                src="${lineQRURL}"
                                alt="LINE 官方帳號 QR Code">

                            <br>

                            <a
                                class="line-green-button"
                                href="${lineAccountURL}"
                                target="_blank"
                                rel="noopener noreferrer">
                                開啟官方 LINE
                            </a>
                        </div>

                        <div class="mobile-line">
                            <p style="color:#aaa;">
                                手機版請點選下方按鈕加入官方 LINE
                            </p>

                            <a
                                class="line-green-button"
                                href="${lineAccountURL}"
                                target="_blank"
                                rel="noopener noreferrer">
                                加入官方 LINE
                            </a>
                        </div>

                        <div style="
                            margin-top:20px;
                            border:1px solid #555;
                            border-radius:10px;
                            padding:15px;
                            color:#ccc;
                            text-align:left;
                            line-height:1.8;
                            font-size:0.9rem;
                        ">

                            <b style="color:var(--warning-yellow);">
                                如果無法開啟 LINE：
                            </b>

                            <br><br>

                            ① 點選 LINE 右上角「⋯」

                            <br>

                            ② 選擇「在外部瀏覽器開啟」

                            <br>

                            ③ 再次點選加入官方 LINE

                            <br><br>

                            或直接在 LINE 搜尋：

                            <br>

                            <span style="
                                color:#06C755;
                                font-size:1.2rem;
                                font-weight:bold;
                            ">
                                @230iknaq
                            </span>

                        </div>

                    </div>
                `;

                overlay.style.display = "flex";

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
