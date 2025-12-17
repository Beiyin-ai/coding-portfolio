# -*- coding: utf-8 -*-
"""
台灣水庫水情資料擷取程式
資料來源: https://water.taiwanstat.com/
"""

import sys
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt

# --- 輔助函數 ---
def format_status(status_text):
    """
    格式化水量變化狀態
    輸入: "昨日水量下降：1.14%" 或 "昨日水量上升：0.01%"
    輸出: "-1.14%" 或 "+0.01%"
    """
    import re

    if not status_text or status_text == "狀態未知":
        return status_text

    # 提取百分比數字
    match = re.search(r'(\d+\.?\d*)%', status_text)
    if not match:
        return status_text

    percentage = match.group(1)

    # 判斷上升或下降
    if '下降' in status_text:
        return f"-{percentage}%"
    elif '上升' in status_text or '上昇' in status_text:
        return f"+{percentage}%"
    else:
        return status_text

# --- 配置與變數 ---
URL = "https://water.taiwanstat.com/"
data = []

# 設定 Chrome 瀏覽器選項
options = Options()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

# 啟動 WebDriver
try:
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
except Exception as e:
    print(f" 無法啟動 WebDriver，請檢查 ChromeDriver 是否在 PATH 中或版本是否匹配: {e}")
    sys.exit()

try:
    print(f"正在開啟網頁: {URL}...")
    driver.get(URL)

    # --- 第一層等待：確保主要內容容器載入 ---
    print(" 正在等待頁面主要內容載入...")
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.ID, 'main-content')))

    # 額外等待確保動態內容載入
    time.sleep(3)

    # --- 第二層等待：確保水庫容器都加載完成 ---
    #  修正：先等待外層容器，再找所有水庫元素
    print(" 正在等待水庫列表載入...")
    # 等待外層容器 reservoir-wrap 出現
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'reservoir-wrap')))

    # 等待所有內部的 reservoir 元素載入
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'reservoir')))

    # 再等待 2 秒確保 SVG 完全渲染
    time.sleep(2)

    # 找到所有 reservoir 元素（每個水庫一個）
    reservoirs = driver.find_elements(By.CLASS_NAME, 'reservoir')
    print(f" 成功找到 {len(reservoirs)} 個水庫資訊。開始擷取資料...")
    print()

    # --- 資料擷取迴圈 ---
    success_count = 0
    fail_count = 0

    for i, reservoir in enumerate(reservoirs):
        reservoir_name = f"第 {i+1} 個水庫"

        try:
            # 1. 滾動到該元素位置，確保元素在視窗內
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", reservoir)
            time.sleep(0.5)

            # 2. 等待關鍵元素載入（名稱和 SVG）
            WebDriverWait(reservoir, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.name h3'))
            )
            WebDriverWait(reservoir, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, 'svg'))
            )

            # 3. 擷取水庫名稱
            name = reservoir.find_element(By.CSS_SELECTOR, '.name h3').text.strip()

            # 4. 擷取蓄水百分比（從 SVG 的 text 元素中）
            # 嘗試多種方式找到百分比
            percent = None
            try:
                # 方法 1: 找尋 class 包含 'liquidFillGaugeText' 的 text 元素
                percent_element = reservoir.find_element(By.CSS_SELECTOR, 'svg text.liquidFillGaugeText')
                percent = percent_element.text.strip()
            except NoSuchElementException:
                try:
                    # 方法 2: 找尋所有 SVG text 元素，取第一個包含 % 的
                    text_elements = reservoir.find_elements(By.CSS_SELECTOR, 'svg text')
                    for elem in text_elements:
                        text = elem.text.strip()
                        if '%' in text:
                            percent = text
                            break
                except:
                    percent = "資料擷取失敗"

            if not percent:
                percent = "資料擷取失敗"

            # 5. 擷取有效蓄水量（改進版，多重備援）
            volume = None
            try:
                # 方法 1: 找 .volume h5
                volume_element = reservoir.find_element(By.CSS_SELECTOR, '.volume h5')
                volume = volume_element.text.strip()
            except NoSuchElementException:
                try:
                    # 方法 2: 找任何包含 volume 的 div
                    volume_element = reservoir.find_element(By.CSS_SELECTOR, '[class*="volume"]')
                    volume = volume_element.text.strip()
                except NoSuchElementException:
                    try:
                        # 方法 3: 從所有 h5 中找包含「蓄水量」的
                        h5_elements = reservoir.find_elements(By.TAG_NAME, 'h5')
                        for h5 in h5_elements:
                            text = h5.text.strip()
                            if '蓄水量' in text or '萬立方公尺' in text:
                                volume = text
                                break
                    except:
                        pass

            if not volume:
                volume = "資料擷取失敗"

            # 6. 擷取昨日水量變化狀態
            status_raw = None
            try:
                # state 的 class 可能是 'state red' 或 'state green' 等
                status_element = reservoir.find_element(By.CSS_SELECTOR, '[class*="state"] h5')
                status_raw = status_element.text.strip()
            except NoSuchElementException:
                try:
                    # 備援：找所有 h5 中包含「水量」的
                    h5_elements = reservoir.find_elements(By.TAG_NAME, 'h5')
                    for h5 in h5_elements:
                        text = h5.text.strip()
                        if '昨日水量' in text or '水量上升' in text or '水量下降' in text:
                            status_raw = text
                            break
                except:
                    pass

            # 格式化 status：轉換為 +/- 格式
            if status_raw:
                status = format_status(status_raw)
            else:
                status = "狀態未知"

            # 7. 擷取更新時間
            update_time_raw = None
            try:
                update_element = reservoir.find_element(By.CSS_SELECTOR, '.updateAt h5')
                update_time_raw = update_element.text.strip()
            except NoSuchElementException:
                try:
                    # 備援：找所有 h5 中包含「更新時間」的
                    h5_elements = reservoir.find_elements(By.TAG_NAME, 'h5')
                    for h5 in h5_elements:
                        text = h5.text.strip()
                        if '更新時間' in text:
                            update_time_raw = text
                            break
                except:
                    pass

            # 格式化 update_time：移除「更新時間：」前綴
            if update_time_raw:
                update_time = update_time_raw.replace('更新時間：', '').replace('更新時間:', '').strip()
            else:
                update_time = "更新時間未知"

            # 8. 將資料加入列表
            data.append({
                'name': name,
                'volume': volume,
                'percent': percent,
                'status': status,
                'update_time': update_time
            })

            success_count += 1
            print(f"    [{i+1}/{len(reservoirs)}] {name}: {percent}")

        except TimeoutException:
            fail_count += 1
            print(f"    [{i+1}/{len(reservoirs)}] {reservoir_name} 載入超時，已跳過")
            continue

        except NoSuchElementException as e:
            fail_count += 1
            print(f"    [{i+1}/{len(reservoirs)}] {reservoir_name} 找不到必要元素: {str(e)}")
            continue

        except Exception as e:
            fail_count += 1
            print(f"    [{i+1}/{len(reservoirs)}] {reservoir_name} 發生錯誤: {str(e)}")
            continue

        # 短暫延遲，避免過快請求
        time.sleep(0.3)

    print()
    print("=" * 70)
    print(f" 擷取完成統計:")
    print(f"    成功: {success_count} 個")
    print(f"    失敗: {fail_count} 個")
    print(f"    成功率: {success_count/(success_count+fail_count)*100:.1f}%")
    print("=" * 70)
    print()

    ##  第二階段：資料清洗與處理 (使用 Pandas)
    # --------------------------------------------------

    if not data:
        print(" 致命錯誤：沒有成功擷取任何資料。請檢查網頁結構或網路連線。")
        sys.exit()

    df = pd.DataFrame(data)

    # 儲存原始資料
    csv_filename = "reservoir_taiwan.csv"
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    print(f" 原始資料已儲存為 {csv_filename}")

    # 整理 'volume' 欄位（提取數字）
    df['volume_clean'] = df['volume'].str.extract(r'([\d.]+)', expand=False)
    df['volume_clean'] = pd.to_numeric(df['volume_clean'], errors='coerce')

    # 整理 'percent' 欄位（提取數字）
    df['percent_clean'] = df['percent'].str.replace('%', '', regex=False).str.strip()
    df['percent_clean'] = pd.to_numeric(df['percent_clean'], errors='coerce')

    # 顯示資料摘要
    print("\n 資料摘要:")
    print(df[['name', 'percent', 'status']].to_string(index=False))

    if df['percent_clean'].notna().any():
        print(f"\n 統計數據:")
        print(f"   平均蓄水率: {df['percent_clean'].mean():.2f}%")
        print(f"   最高蓄水率: {df['percent_clean'].max():.2f}% ({df.loc[df['percent_clean'].idxmax(), 'name']})")
        print(f"   最低蓄水率: {df['percent_clean'].min():.2f}% ({df.loc[df['percent_clean'].idxmin(), 'name']})")

    ##  第三階段：數據視覺化 (使用 Matplotlib)
    # --------------------------------------------------
    print("\n 正在生成圖表...")

    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei', 'Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False

    # 過濾掉沒有有效百分比的資料
    plot_df = df.dropna(subset=['percent_clean']).sort_values(by='percent_clean', ascending=True)

    if not plot_df.empty:
        plt.figure(figsize=(12, max(8, len(plot_df) * 0.4)))

        # 根據蓄水率設定顏色
        colors = ['red' if x < 50 else 'orange' if x < 70 else 'steelblue' for x in plot_df['percent_clean']]

        plt.barh(plot_df['name'], plot_df['percent_clean'], color=colors)
        plt.xlabel("蓄水百分比 (%)", fontsize=14)
        plt.ylabel("水庫名稱", fontsize=14)
        plt.title("台灣主要水庫即時蓄水百分比", fontsize=16, pad=20)
        plt.grid(axis='x', linestyle='--', alpha=0.7)

        # 在每個 bar 上顯示數值
        for i, (idx, row) in enumerate(plot_df.iterrows()):
            plt.text(row['percent_clean'] + 1, i, f"{row['percent_clean']:.1f}%",
                    va='center', fontsize=10)

        plt.xlim(0, 105)
        plt.tight_layout()

        chart_filename = "reservoir_percent_chart.png"
        plt.savefig(chart_filename, dpi=300, bbox_inches='tight')
        print(f" 圖表已儲存為 {chart_filename}")

        # 儲存 Excel 版本（包含完整資料）
        excel_filename = "reservoir_taiwan.xlsx"
        df.to_excel(excel_filename, index=False, engine='openpyxl')
        print(f" Excel 資料已儲存為 {excel_filename}")
    else:
        print("  沒有有效的百分比資料可以繪圖")

    print("\n 所有任務完成！")

except TimeoutException:
    print("\n 致命錯誤：網頁載入超時，無法找到水庫列表。請檢查網路連線。")
except Exception as e:
    print(f"\n 發生未預期的錯誤: {e}")
    import traceback
    print("\n詳細錯誤資訊:")
    traceback.print_exc()

finally:
    print("\n 正在關閉瀏覽器...")
    driver.quit()
    print(" 程式執行完畢。")