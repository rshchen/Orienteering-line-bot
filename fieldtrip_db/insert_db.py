#放入實際的題目到名為 level的table
import sqlite3
import os
import json
con = sqlite3.connect('fieldtrip.db')







def build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img):
	con.execute("INSERT INTO qa (qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img) values ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img))

# set the line bot Message types with qn = 0
# https://developers.line.biz/en/docs/messaging-api/message-types/
# 1: Text message, 2: Sticker message, 3: Image message
qn_nu = 0
qn_text = 1
qn_img = 3
hint_text = 1
hint_img = 3
hint_final = 1
ans_text_exact = 1
ans_text_con = 1
ans_text_multi = 1
ans_img = 3
suppl_text = 1
suppl_img = 3
build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

# qn 1

qn_nu += 1
qn_text = '請輸入班級座號姓名'
qn_img = None
hint_text = None
hint_img = None
hint_final = None
ans_text_exact = '^[1-3][0-2][0-9][0-4][0-9][\u4e00-\u9fa5][\u4e00-\u9fa5]+$'
ans_text_con = None
ans_text_multi = None
ans_img = None
suppl_text = None
suppl_img = None

build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)





#qn 2
qn_nu += 1
qn_text = '沿櫻花路前往長安國小，該校操場跑道作為避難收容處所時，最多可容納多少人數？'
qn_img = 'https://lh7-us.googleusercontent.com/XK5q7V7N72Depk26mW8drsR_EiUh52Wmu4bdAayFUvTYwBNwhq7xBkUgunm75278GaLsXUy3NPchUrH9p2m1jQCw5h5sIG9CIAbzlwj7XRFSp_Lm0eWCxajk1SYDgKACWydx1jP1H1ySc3npA6E_u6Mf5QhgHA'
hint_text = '提示：留意校門口的某處牆面'
hint_img = None
hint_final = None
ans_text_exact = '242'
ans_text_con = None
ans_text_multi = None
ans_img = None
suppl_text = '文華對面的中山國中操場，更是可以容納到1375人'
suppl_img = 'https://lh7-us.googleusercontent.com/a08YJ0ENno3IB61k3AC_r-_BDHyEvaI4WPIwe4F1hYYcmFMLFXBctIm-vNpYfyWXENfuYOKMtXRsMXq3RkmyLrjVcC5nb8YnQmbgulosWMQAOXvCJz5HjG5HNdbYSal-GqdfYb7VLnMmOJXTpKlu2Z_pid5sbA'

build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)


#qn 3
qn_nu += 1
qn_text = 'Google搜尋長安國小在民國幾年首次招生？'
qn_img = None
hint_text = '提示：長安國小官網'
hint_img = None
hint_final = None
ans_text_exact = '96'
ans_text_con = None
ans_text_multi = None
ans_img = None
suppl_text = '正確！民國96年。\n 但其實長安國小並不在大河里境內，而是與文華高中同屬何仁里哦！p.s. 文華斜對面的中山國中、大仁國小則是位在何德里。'
suppl_img = 'https://lh7-us.googleusercontent.com/ARTWvzXmPpxS0uKHhgYqYhByZdzUVSkK6O_t2kV34u02uDqc2mgiTl0tniU4z3PLarw6NUnIT3_4ayANO2sZLIVAaivbCDN1P2IJ2bR4V2G5AV1xxjtAHay3z3awVNbxBT_o82D7XAOW50z0UJDv22Zec6sfsw'

build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 4
qn_nu += 1
qn_text = '西屯路二段208巷左轉前往大河復興祠，觀察該祠日治時期地名為何？'
qn_img = None
hint_text = '提示：注意門簾的刻字'
hint_img = None
hint_final = '日治時期哦！'
ans_text_exact = None
ans_text_con = '石碑'
ans_text_multi = None
ans_img = None
suppl_text = '正確！上下石碑庄。\n 大河里在日治時期屬下石碑庄，何清科曾任當地保正，何振德是他叔叔，廖國治為上石碑人，是西屯張廖家廟早期拓墾先賢。'
suppl_img = 'https://lh7-us.googleusercontent.com/l9s48_bNFHiTrHdJu4U7UcTX8OZjsJKTdjrp-IsZZkgDUQ3LNIF6xcBTlHS_j2KFVuk18VPDSl0BzaZ8lUPiQMImpW5yfPja6E_Bf6zSou-yde90ujkfQvDNFgigkyI6PZQq50FEsoRNSwV6Wj3X5SbgTNkY1w'

build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)
#qn 5
qn_nu += 1
qn_text = '復興祠的重建金爐樂捐芳名中，哪個姓氏人數最多？'
qn_img = None
hint_text = '提示：調查看看右側的金爐'
hint_img = None
hint_final = None
ans_text_exact = '何'
ans_text_con = None
ans_text_multi = None
ans_img = None
suppl_text = '正確！何姓。\n 當我們去到一個陌生的庄頭，卻想要快速理解地方居民姓氏與頭人時，廟裡面的芳名錄與捐獻刻文能夠大大的幫助你了解一個庄頭的故事。'
suppl_img = 'https://lh7-us.googleusercontent.com/nIBBNHkB4BUL9q2vsIQTyJeRZ8OoeEAGCzlVMzSH2lqYhBI7AwO7BbOLEmhGoCkHnErG5GhIasPw1fZazN7LYN9fq3n9er8w3x_TcYU0TWtuGodC_cRCvXl_iKkxff29leq1o8IcEDTzgn3SFbzw5xqy-EHTJw'

build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 6
qn_nu += 1
qn_text = '回頭沿208巷前往下碑福德祠，找到老照片中的下碑橋位置，觀察橋右側流路今日鋪面是何種材質？'
qn_img = None
hint_text = '提示：下碑橋已不復存在，須從周圍景物推測橋的位置'
hint_img = 'https://lh7-us.googleusercontent.com/QuU6Afvc2yZQOUNNRqqRlO-UXG7PDKOWHDFxkNofBwSLDBxE5Ft0n6yGyNm_aA2eg8Y6dGJFoXvdc0Cll0hkAD3jMFjepyJjNvMzr-nph9BYFNtvAw_ItfCa8S7eZ_HiwRXSiP3VOFLcbbJWf91uFi7elGzMfQ'
hint_final = '不是指橋上哦，是橋旁邊原本的河道處'
ans_text_exact = None
ans_text_con = '水泥'
ans_text_multi = None
ans_img = None
suppl_text = '正確！水泥鋪面。\n 遺憾地，大約在2011~2015年之間，這座橋存在的痕跡已完全消失殆盡。2012年出版的《蔗糖歲月》一書中提及路面上還留有一邊的橋墩。'
suppl_img = 'https://lh7-us.googleusercontent.com/aH0jYXtQWdhCq4mLaQN-92Rsux-QNjftuR2ktpn_juxWxOLKHf3tu2Ta__UlvW454LXgZRIoUD6MKOq5q-kgbzJ0JWRsvxfpXlCxHDQqKK8rafx4AzgIZ8OUH4s7fW7iJXT3T2iQL1a1jSuqDN2Sz4L3Swf_PA'

build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 7
qn_nu += 1
qn_text = '進入下碑福德祠，圍牆上的「福德祠興建樂捐芳名」碑文人名，以哪兩個姓氏為主？（打出兩個姓氏就好）'
qn_img = 'https://lh7-us.googleusercontent.com/j0dbcQTjAM8LJnZ1O1spZmO_WgSkjDOc-AF0dMuB08lo7APCRgP8sjDlz2c3FXjNBdL8QxeN5PschOrevTksDO561g03zvtnwzgClkGB2S63mhAReoNvcH8GLMqmmJxwKeC7r3xLsmZd8tx7wEu9lsNHNO6sNQ'
hint_text = None
hint_img = None
hint_final = '兩個字'
ans_text_exact = None
ans_text_con = None
ans_text_multi = json.dumps({'何廖':0,'廖何':1})
ans_img = None
suppl_text = '正確！何姓與廖姓。\n 根據廟牆上的沿革記載，下碑福德祠建於日治時期，為地方仕紳以大時修成的小祠，而後於民國67年、民國85年二度重建後，方為今日之貌。'
suppl_img = 'https://lh7-us.googleusercontent.com/-CnNdeuJQLTE4OvgQzUUQlcXYQ-WtsBXq92CIOK1JBS12Kh56vVfpR41eALiBW3J2juvmwQZ_C51w-gzNj47pGnYPIB5LwVK740xhtCK2RdmaxpuGchsK9hM-Oqvf9U54jhapK1qMgtLIyVYoiYMTAWTOCbOiA'

build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)


#qn 8
qn_nu += 1
qn_text = '觀察廟前這段未被封蓋的溝圳，應是沿著哪間學校圍牆流經此地？'
qn_img = 'https://lh7-us.googleusercontent.com/LPxg8caS3riw8bUOHF2qNfQs0AbNHny00VMOD9L0yUMCsUMUV6zX8TM2j0w6KeR6FURGGxgayoQRiebPLh6GiYRn-h9yS6w_tJ89dTfRHluCJ7YCiLfy1db8MCmItRQm5EHx4OWbbPKxr_vc__Se5rMB25l4_g'
hint_text = '提示：留意校門口的某處牆面'
hint_img = None
hint_final = '先定位我們在哪裡，再觀察看看附近有什麼溝圳相關的圖徵'
ans_text_exact = None
ans_text_con = '葳格'
ans_text_multi = None
ans_img = None
suppl_text = '正確！葳格國際學校小學部西屯校區。\n 從大河街流經葳格國小至大河一巷的下石碑分圳的支線，曾是灌溉大河里一帶田地重要的水利設施。另外可以注意庄頭福德祠的面向，對著水流來的方向，由於水代表財富，表示財富被土地公全數留下，以象徵村莊永遠發達。'
suppl_img = None


build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)


#qn 9
qn_nu += 1
qn_text = '沿大河一巷持續前行至此社區，找到照片圓圈處的告示牌名稱。'
qn_img = 'https://lh7-us.googleusercontent.com/TxiZ00ifxMfJzeTzIQUW-G_1N9h4PUDP0RH6ovUTM6uQB4WSjcohinL2-FSW9Yp9Tl8GhkYgg9UByQHOZG5wZj2N1soh5KlSxxBIK98X-GtAFUNBgGkIW9CEj0j8PG4JuTu26RQFceZsODeD5lCR5S7l5SzyHQ'
hint_text = '提示：圓圈處告示牌哦，不是前面那棟白色大樓'
hint_img = None
hint_final = '名稱即可'
ans_text_exact = None
ans_text_con = '開放空間'
ans_text_multi = None
ans_img = None
suppl_text = '正確！開放空間標示牌。\n 開放空間是指開發業者在建築基地內，留設可連通道路並提供社會全體公眾通行或休憩的空間，相對地政府則給予開發業者增加容積作為獎勵(高一下地理：都市)'
suppl_img = 'https://lh7-us.googleusercontent.com/02LwUlE7XcdyifbSNOI9ldTmUuHZjbTj1FS7uWe_RbGFkQLYdK09IN4Lqh2aT08fB1tXbjEdt-5Q2FpUsY0YKdVgcZMTSIMvEMUMfFQ59ym_g62l6CWvajVeB2kS06a1Y87tM4JpurjPmqhau7QJJFJNHcbpJg'

build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 10
qn_nu += 1
qn_text = '沿此社區大樓的開放空間往左走至西側停車場，該停車場的名稱為何？'
qn_img = 'https://lh7-us.googleusercontent.com/H2xXnVJh2sYweKP3_04lg4PHEdYS0zaJkon5qoHx7yP6DyVSjDvOM613l4yCq6a28dTYv-pRGFz5hrWgX3kHYGD9PO1lRa4n9mqcEfVgWgK6Dr_E3GzCCcuVltYNKdKtK7Iz5hlFrlNtWFgVDVZhh1JZmFgQMw'
hint_text = None
hint_img = None
hint_final = '不要打成錯別字了哦'
ans_text_exact = None
ans_text_con = '官陂車的家'
ans_text_multi = None
ans_img = None
suppl_text = '正確！官陂車的家。\n 官陂鎮位於福建省漳州市紹安縣，西屯港尾地區的開拓者廖朝孔即為當地人。'
suppl_img = 'https://lh7-us.googleusercontent.com/yLkLRheYvTke7NjdL5ROe2N1rsZgIqCTUpjSvCJDAu9YAt-cSlcBcQ3x3Q8Qu71Mv1PHMKAxWa2LSoDJ8rH1FvBwm9mK683HJ-J-Vp-Cs-NRMWhcNvaEawroN4dCwNMS3-_S4Jwix5sqy2FsWZtKWJJ9dig0yQ'

build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 11
qn_nu += 1
qn_text = '沿大河一巷前往大何里福德祠舊址，此處今日的土地利用為何？'
qn_img = 'https://lh7-us.googleusercontent.com/LuEnEUPpq4BqGoePhXNwJk46cFVykXYeDh1CSNSSnjEnwkd03yWRXkun7k89CuHMEsdk-vxxAMWYdQg2TYYKFrG9bzTO-lPUKtDlkrQXgcp_cKmtfnP01OBOylHc7dP84ubEF_Fc_TQk2H-vFVRuu8gINP2mPA'
hint_text = '提示：你們正從照片中的前方遠處逐漸走來'
hint_img = None
hint_final = None
ans_text_exact = None
ans_text_con = '停車場'
ans_text_multi = None
ans_img = None
suppl_text = '正確！停車場。\n 此處為臺中中央公園南側停車場，東側突起小丘為水湳水資源處理中心。照片中腳踏車的位置即當年大河福德祠所在地。'
suppl_img = 'https://lh7-us.googleusercontent.com/qfMMBp0Xj1Z5ym4mRY-_0-QKrQSMxWx00ZVXQvYrP58i2SsBGm-kTPr0BF8q4Sh1jP9glDCEMb65Y0EboSct1I_CgCgbwkl11zoR5LlKhBx69khHQ8f45Hn4Az_1bIguyqxmpE4hOsJjAHDN1ieLJey1rdps-g'

build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 12
qn_nu += 1
qn_text = '沿停車場外圍道路前往大河橋旁的路口，在路口處與曾經的大河橋拍張小組合照上傳'
qn_img = None
hint_text = '是否有種我們正站在歷史洪流中的感覺？'
hint_img = 'https://lh7-us.googleusercontent.com/aGCQUCFp7wLgxOOYqoRpjFjiIHH4KIh37r-YhehGchkMoiAwoFHkqoxTbqJbotd6JB9S83fZHdJpCdQBChJW2hnkcWl34_u2cQhRBfumxn4-iYsHePA3wIdvg_hB-bXAJS-4YskILancAfXHeOgGRj9T7iN41Q'
hint_final = '趕緊交出照片吧！'
ans_text_exact = None
ans_text_con = None
ans_text_multi = None
ans_img = True
suppl_text = '2009年Google地圖的歷史街景中的大河橋。\n 畫面中左側成了惠來溪整治計畫的濕地公園，右側成了中央公園的南側停車場，今日仍能見到的只剩右方的宮廟招牌。'
suppl_img = 'https://lh7-us.googleusercontent.com/VEVoaFgKVFLQyUYByPZVH7aS776hgFPSRqaH5yuu3O6NQz8TNZQ3pxdWotJBFGZDOPbDC1MuNLi4kdK7SuUYdXyDEAzoIWrDyGx0CqtIXcbTG8rDbd-H4JmEHV4Ik8C3bKCsbHCHWj3KRlMXXkerlsggffsTuQ'
build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)


#qn 13
qn_nu += 1
qn_text = '沿溪畔步道前往河南路的中央公園陸橋，從橋上北眺，眼前這片區域可作為何種防災用途？'
qn_img = None
hint_text = '提示：地形、植生、涵管'
hint_img = None
hint_final = '真的不知道就Google搜搜看吧'
ans_text_exact = None
ans_text_con = '滯洪'
ans_text_multi = None
ans_img = None
suppl_text = '正確！滯洪池。\n 中央公園以自然的地形起伏達到滯洪效果，隨著不同的降雨量讓公園而有不同的滯洪、儲水範圍。一方面達到滯洪功能，另一方面達到基地保水的環保效果。'
suppl_img = 'https://lh7-us.googleusercontent.com/1BvEHv5lwDzfXREMTwN7C42Vnat7ioBPWMk9fAr2FVVOxnWnuzWfpzsPYyBiOZL1MJb947CDob1wjD_45iDCxPbc4C7v7wixewWUJcXhRn6s-IBgDrRpPMUKXMiRJQxvo01KhNcz7WpsAZBCKeOosaNOeMomfA'
build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 14
qn_nu += 1
qn_text = '下陸橋後右轉前往大河里福德祠現址，觀察牆上的重建基金捐款芳名錄，哪項產業的家數及捐款總額最高？'
qn_img = 'https://lh7-us.googleusercontent.com/S4m7kY7y1ccqun1uuUpaM6MI2IvY2judTIxT3791Rt2bu5go65JquvSwiEmjZQR92tDDcCy3Y4Pn0sNVyvGlm_9-e8RXCZfGrzSrwzQFXGfQ2G0kLYms80RM9SlqhMxLepMPhKTxXykUdUtpPzQo18GR-jbqpA'
hint_text = None
hint_img = None
hint_final = None
ans_text_exact = None
ans_text_con = '汽車'
ans_text_multi = None
ans_img = None
suppl_text = '正確！汽車相關產業。\n 有沒有發現對街幾乎都是汽車週邊產業。廟裡面的芳名錄與捐獻除了能幫助你了解地方居民姓氏與頭人外，亦能了解一地的產業類型結構。'
suppl_img = 'https://lh7-us.googleusercontent.com/bcWiLTFRK5SqBndb2XKBuQF93nP3Bj_KGQoeKCDEYm0E8-OGaeIhcKg65BJKiqzuWvB9mThq9svh0l3mhuUZwmkKCHdYVwomh7DvaYzOhLyvIG07vCuhtbg5SVm3ghkUHQGLG_QzkIaA5ksPmD_ljbW71OA3Jw'
build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 15
qn_nu += 1
qn_text = '沿甘河路前行直至大河街口，二側多屬哪二種土地利用型態'
qn_img = None
hint_text = '回答格式：OO區XX區'
hint_img = 'https://lh7-us.googleusercontent.com/Yj6i_HUFjbQtBJsRAPv2g-O7v2xetQfMkJK2e7L_44PTBKtPyFaYxgyJ-i7vY3Zln4f3p_bBxrtRV0XtIaoZgXZYC3NVQgzkIJcOUQDUBNoYJO3xsyiCjyipb9xFTc6m4qEMHJanUQzDTtZY1e5AjwMLCvPPLw'
hint_final = '回想一下高一下的都市土地使用分區教了什麼'
ans_text_exact = None
ans_text_con = None
ans_text_multi = json.dumps({'工業區住宅區':0,'住宅區工業區':1})
ans_img = None
suppl_text_exact = '工業區&住宅區。\n 此處屬於都市計畫工業用地中的乙種工業用地，但工廠間錯落著許多住宅，呈現住工混合的景觀。'
suppl_img = 'https://lh7-us.googleusercontent.com/JQzi38hxuG-Y7Lj1lPVkFymJ3tyH3x-OcYqaDumddtsbDEHVFaDJ5szhiI6HyYoFpbkWH1qZ1w8dGu2Dsj1A7BRRq9cZpHuHFrAd93B5pqZjKmV5r6bMmohLz9i6vy9oxlc60z2W9AMDKEUnK1qXG17tuutrMg'
build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 16
qn_nu += 1
qn_text = '右轉大河巷，找到照片中的工廠，觀察該工廠名稱後，Google查詢該工廠是何時設立。'
qn_img = None
hint_text = '建議使用「台灣公司網」或「公司登記查詢中心」查詢'
hint_img = 'https://lh7-us.googleusercontent.com/ZlkrBM2YDZoBlzXqBJf78Svo3V5LR6sKT4TnRceeVL4bS742hW7UnFcSfWlaDB69U7IBjkCNWnAhoqqIhhrzRiyewjUu9gXtZt8tzH0FDP8CKIamaX3DmI12mg6NAfZTMd9SHKJOqovYKUqfZ6XsMilQlEpRRQ'
hint_final = '西元年份'
ans_text_exact = '1992'
ans_text_con = None
ans_text_multi = None
ans_img = None
suppl_text = '正確！1992年。\n 所營事業資料：\n 1.印刷業務之經營 \n 2.文具紙張之買賣\n 3.有關前項產品之進出口貿易業務'
suppl_img = 'https://lh7-us.googleusercontent.com/EAwJuP9Nca4ThF5cc5ktCXE3807XtbIIaPGM_7pRNIurptHMqKCbcphOLznqw7-p5_1zI4VCmqEwnBaUjnoX0q2c8ccENyBid42gZPmaPJY3LsImvEgGJjS2RXIfPPzlrnogmApbo2KQDCbCwrMKB8q2Irk8Lw'
build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 17
qn_nu += 1
qn_text = '找到照片中的工廠，觀察該工廠名稱後，Google查詢該工廠是何時設立。'
qn_img = None
hint_text = '建議使用「台灣公司網」或「公司登記查詢中心」查詢'
hint_img = 'https://lh7-us.googleusercontent.com/6jTqHHyglFLxU7OqUFi0kHw4JvdxXudG-YxVjY1hTdqjn1L8-XrkkqRcJeDRCrmfeSSfuq9veokuG3o3s2FXerHdPkHI20PNzE5I3b64g3g0d0FQwkNS2JPqYZ9LPRgyy-9_JYJppLibAVIRX2BDzx116w0KLQ'
hint_final = '西元年份'
ans_text_exact = '1979'
ans_text_con = None
ans_text_multi = None
ans_img = None
suppl_text = '正確！1979年。\n 所營事業資料：以國際貿易業、竹藤製品製造業為主'
suppl_img = 'https://lh7-us.googleusercontent.com/_dPe7SHtRALXMwghAaBu3bLyV_G_6FXSciU_HG_W2Vj7033WXLN383eO2XhHkYCoE1S70KWD5y7wYdQJnaE7xVC4jZvnYLqY-vGy5BILwQrpPFMVakMOZnnlIlUkh4_2MlymviwXUCQoPQw1AdH5wFTpE3KyLQ'
build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 18
qn_nu += 1
qn_text = '前往大河街新福祠，觀察左側的沿革碑文，其在民國69年建祠時，附近可能以鐵工廠及哪種類型的工廠為主'
qn_img = None
hint_text = '提示：兩個字'
hint_img = 'https://lh7-us.googleusercontent.com/_jwsyiU_mvOtlqQSWwQrSzFy5AbwdoOsLJMtxWCbWw_Ii-rHQ1iXt3WGQIQc1aY0uTGNC2xKFg8QR1lwdgUbaiaXJLcQaf8PAXMLvOf_Oe1fDECj6d7iJuCj-1m9OFiG6ZJDCSKlOO63z4om-5Y0QtnKTpcp9A'
hint_final = '是沿革碑文，不是公告哦'
ans_text_exact = None
ans_text_con = '木業'
ans_text_multi = None
ans_img = None
suppl_text = '正確！木業及鐵工廠。\n 對照右方的民國95年環保金爐捐款名單，產業的類型在這26年間有了什麼變化？'
suppl_img = 'https://lh7-us.googleusercontent.com/XgG-TIfmfmZbBPwLnpLxqghRcbj7dr3_fQY2PHlGqdeIy9eA3WSA-fuH_HmQmSvx97jRm9vhekTQFNhSrX2ZdZdlZCtAU4epBcm5GjBSGCe1SAmWZKb_cnaP3p4pvoNWe4xORIfIaTP8q9ceewb4MYif81PUxw'
build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 19
qn_nu += 1
qn_text = '最後一站！觀察福德祠右前方路口的水池，池中有著不少的什麼？'
qn_img = None
hint_text = '提示：如果這側水池裡沒東西，那就要往右繞到文心路那側的王品專用停車場看'
hint_img = 'https://lh7-us.googleusercontent.com/4TkrHweYgmClKFNt8fJj-1DeeCmS5oEHM4XnyhGb1VoFzfkLowOoiQUIGKyxOK7MzXyto7IEzDyNSWY5VS7dlQv1U-SIv-AfeVInKVwKtiE-IQlQXHvURIxWrBahXBEjHDWeDdgBQmOJ2YEzkvuZKoAwt-fbEg'
hint_final = '呃...你/妳該不會看不出那是什麼吧'
ans_text_exact = None
ans_text_con = '鴨'
ans_text_multi = None
ans_img = None
suppl_text = '正確！鴨子。訪問文華耆老  叙文老師得知，該池原是當地木業公司的貯木池。'
suppl_img = 'https://lh7-us.googleusercontent.com/uMDmVj1lOnRBTN7XMqOHCYlXm-okmRdwUw0txdnc8F1L3OQNHYcSLam-xmhRYMNF3spYoHVIm0wuTpdvnGVIiBEzkOwuJPE6RoqIl4rA3-i8c5FjXJXie9XO6GhMM2mbzT3YeACkCK_nk7HAHS-03i0Bth1dEg'
build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)

#qn 20
qn_nu += 1
qn_text = '這是最後一關了！請說出通關密碼！'
qn_img = None
hint_text = None
hint_img = None
hint_final = '你會不會想對辛苦設計遊戲的老師說點什麼呢？'
ans_text_exact = None
ans_text_con = '謝'
ans_text_multi = None
ans_img = None
suppl_text = '好孩子，恭喜你全部破關！正所謂：懂得感恩的人最幸福！相信你之後一定會平安自在，健康幸福，後會有期^ ^'
suppl_img = None
build_qn(qn_nu, qn_text, qn_img, hint_text, hint_img, hint_final, ans_text_exact, ans_text_con,  ans_text_multi, ans_img, suppl_text,suppl_img)



con.commit()
con.close()



