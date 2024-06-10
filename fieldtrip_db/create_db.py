#create a database named fieldtrip.db
#create tables named qa, level
import sqlite3

con = sqlite3.connect('fieldtrip.db')


#用來放置題目與答案資訊的table
con.execute('''DROP TABLE IF EXISTS qa''')
# qn:question, qn_nu:qn number, ans: answer, suppl: supplement
con.execute('''CREATE TABLE IF NOT EXISTS qa\
("qn_nu" INTEGER ,
"qn_text" TEXT,
"qn_img" TEXT,
"hint_text" TEXT,
"hint_img" TEXT,
"hint_final" TEXT,
"ans_text_exact" TEXT,
"ans_text_con" TEXT,
"ans_text_multi" TEXT,
"ans_img" BOLB,
"suppl_text" TEXT,
"suppl_img" TEXT
)
''')


# 用來確認是否讀過題目和補充資料
con.execute('''DROP TABLE IF EXISTS level''')

con.execute('''CREATE TABLE IF NOT EXISTS level\
("id" TEXT,
"qn_nu" INTEGER,
"qn_read" BLOB,
"suppl_read" BLOB
)
''')


con.commit()
con.close()



