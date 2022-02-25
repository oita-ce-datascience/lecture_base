#pandasをインポート
import pandas as pd

#5行2列のデータフレームを作成してdfに代入。列名は出身地と性別。
df=pd.DataFrame({"出身地":["大分市","別府市","中津市","佐伯市","大分市"],"性別":["男性","女性","女性","男性","女性"]})

#printにて出力
print(df)

#先頭2行を出力
df.head(2)

#出身地が大分市のみを抽出してdf_placeに代入。
df_place=df[df["出身地"]=="大分市"]

#性別が女性を抽出してdf_fに代入。
df_f=df[df["性別"]=="女性"]

#dfに年齢という新しい列を追加。
df["年齢"]=[10,20,,40,50]

#年齢が30才以上を抽出してdf_over30に代入。
df_over30=df[df["年齢"]>=30]

#新しいデータフレームを作成してdf2に代入。
df2=pd.DataFrame({"出身地":["竹田市","国東市"],"性別":["男性","女性"],"年齢":[15,25]})

#dfとdf2を結合してdf_concatに代入。
df_concat=pd.concat([df,df2])

#新しいデータフレームを作成してdf3に代入。
df3=pd.DataFrame({"出身地":["中津市","竹田市"],"血液型":["A","O"]})

#df_concatとdf3で出身地が同じものを結合しdf_mergeに代入。
df_merge=pd.merge(df_concat,df3,on="出身地")

#df_concatの出身地に何があるかを確認
df_concat["出身地"].unique()

#df_concatの出身地は何が何個あるかを確認
df_concat["出身地"].value_counts()

#df_concatを出身地別に平均年齢、性別ごとの人数を集計
places=df_concat["出身地"].unique()
place_list=[]
age_list=[]
male_list=[]
female_list=[]

for place in places:
    choice=df_concat[df_concat["出身地"]==place]
    age=choice["年齢"].mean()
    male=choice[choice["性別"]=="男性"]["性別"].count()
    female=choice[choice["性別"]=="女性"]["性別"].count()
    place_list.append(place)
    age_list.append(age)
    male_list.append(male)
    female_list.append(female)
    df_new=pd.DataFrame({"出身地":place_list,"平均年齢":age_list,"男性の数":male_list,"女性の数":female_list})