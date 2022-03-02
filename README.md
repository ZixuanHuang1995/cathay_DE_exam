# cathay_DE_exam

題目一
資料源: 內政部不動產時價登錄網 (http://plvr.land.moi.gov.tw/DownloadOpenData )
程式語言: python
1. 下載【內政部不動產時價登錄網 】中,位於【臺北市/新北市/桃園市/臺中市/高雄市】的

【不動產買賣】資料,請選擇【本期下載】。
2. 使用【pandas】套件,讀取檔名【 a_lvr_land_a 】【 b_lvr_land_a 】 【 e_lvr_land_a 】
【 f_lvr_land_a 】 【 h_lvr_land_a 】五份資料集,建立 dataframe 物件【df_a】【df_b】
【df_e】【df_f】 【df_h】 。
3. 操作 dataframe 物件,將五個物件合併成【df_all】。
4. 以下列條件從【df_all】篩選/計算出結果,並分別輸出【csv 檔案】 :
* filter_a.csv
-【主要用途】為【住家用】
-【建物型態】為【住宅大樓】
-【總樓層數】需【大於等於十三層】
* filter_b.csv
- 計算【總件數】
- 計算【總車位數】(透過交易筆棟數)
- 計算【平均總價元】
- 計算【平均車位總價元】

題目二
資料源: 591 房屋交易租屋網 (https://rent.591.com.tw/?kind=0&region=1)
程式語言: python
資料庫: MongoDB
1. 利用爬網技術取得【591房屋交易租屋網】中,位於【臺北及新北】的所有【租屋物件資料】。
2. 【租屋物件資料】至少須具有下列欄位:
- 出租者 (陳先生)
- 出租者身份 (屋主)
- 聯絡電話 (02-25569419)
- 型態 (電梯大樓)
- 現況 (獨立套房)
- 性別要求 (男女生皆可)
3. 將租屋物件資料儲存在資料庫中。
4. 【設計/建立 RESTful API】供查詢下列資訊: 【以 JSON 格式回傳,請自訂 Schema】
- 【男生可承租】且【位於新北】的租屋物件
- 以【聯絡電話】查詢租屋物件
- 所有【非屋主自行刊登】的租屋物件
- 【臺北】【屋主為女性】【姓氏為吳】所刊登的所有租屋物件
5. 請【提出或實作營運化方法/機制】,包含但不限於以下需求:
- 資料源更新機制
- 資料庫設計
- API 的效能保證
- API 的規格文件

繳交內容與方式
