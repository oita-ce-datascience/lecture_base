import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

#身長リスト(100人分)を作成。
height_list=[]
for i in range(100):
    i=random.randint(140,190)
    height_list.append(i)

#ランダムリスト(100人分)作成。
random_list=[]
for i in range(100):
    i=random.randint(-30,30)
    random_list.append(i)

#ランダムリスト2(100人分)作成。
random_list2=[]
for i in range(100):
    i=random.randint(-10,10)
    random_list2.append(i)

#身長のデータフレーム作成。
df=pd.DataFrame({"height":height_list})

#データフレームに体重追加。式：身長-100+ランダムリスト
df["weight"]=df["height"]-100+random_list

#データフレームに握力追加。式：体重+ランダムリスト2
df["grip"]=df["weight"]+random_list2

#データフレームを説明変数(df_x)と目的変数(df_y)に分割
df_x=df.iloc[:,0:2]
df_y=df.iloc[:,-1:]

#df_xとdf_yをnumpyのarray形式へ変換。説明変数=x、目的変数=yにする。
x=df_x.values
y=df_y.values

#学習用データ=trainとテスト用データ=testに分割する。train:test=7:3。

#まずは必要なメソッドをインポート。
from sklearn.model_selection import train_test_split

#分割する。学習用説明変数=x_train、テスト用説明変数=x_test、学習用目的変数=y_train、テスト用目的変数=y_test。
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

#重回帰分析に必要なメソッドをインポートする。
from sklearn.linear_model import LinearRegression

#モデルを構築する。

#LinearRegressionのインスタンス化。
lr=LinearRegression()

#予測モデルの構築。学習用データにて学習する。
lr.fit(x_train,y_train)

#予測を行う。テスト用説明変数にてテスト用目的変数を予測する。予測結果はpredに代入する。
pred=lr.predict(x_test)

#predをdf_predとしてデータフレームに変換する。列名をpredにする
df_pred=pd.DataFrame(pred,columns=["pred"])

#df_predにy_testを追加する。列名はtargetにする。
df_pred["target"]=y_test

#df_predに残差を追加する。列名はerrorにする。
df_pred["error"]=df_pred["pred"]-df_pred["target"]

#箱ひげ図にて残差を確認する。
plt.boxplot(df_pred["error"])

#箱ひげ図にて統計量を確認する。
df_pred.describe()

#決定係数を確認する。
from sklearn.metrics import r2_score
r2_score(pred,y_test)

#MSEを確認する。
from sklearn.metrics import mean_squared_error
mean_squared_error(pred,y_test)

#RMSEを確認する。
np.sqrt(mean_squared_error(pred,y_test))

#予測と実際の値を視覚的に確認する。
plt.scatter(pred,y_test,marker="x")
plt.xlabel("predict")
plt.ylabel("grip")

# 上の図に回帰直線を描く。
poly_fit=np.polyfit(df_pred["pred"],df_pred["target"],1)
poly_1d=np.poly1d(poly_fit)
xs=np.linspace(df_pred["pred"].min(),df_pred["pred"].max())
ys=poly_1d(xs)

plt.scatter(pred,y_test,marker="x",c="black")
plt.xlabel("predict")
plt.ylabel("grip")
plt.grid()

plt.plot(xs,ys,c="green",linestyle="dashdot")