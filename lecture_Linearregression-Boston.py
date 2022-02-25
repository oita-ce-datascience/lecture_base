#基本のライブラリ
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#前処理に必要なメソッド
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
#重回帰分析に必要なメソッド
from sklearn.linear_model import LinearRegression
#ボストンのデータを取得
from sklearn.datasets import load_boston
#load_bostonをインスタンス化
boston=load_boston()
#説明変数(x)、目的変数(y)、説明変数の名称を取得(feature_names)
x=boston.data
y=boston.target
feature_names=boston.feature_names
#データフレーム作成
df_x=pd.DataFrame(x)
df_x.columns=feature_names
df_y=pd.DataFrame(y)
df_y.columns=["target"]
df=pd.concat([df_x,df_y],axis=1)
#train(学習用データ)とtest(テストデータ)を準備
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
#LinearRegressionをインスタンス化
lr=LinearRegression()
#train(学習用データ)にて学習(モデルの作成)
lr.fit(x_train,y_train)
#テストデータを予測
pred=lr.predict(x_test)
#予測と実際のデータフレーム作成
df_pred=pd.DataFrame(pred)
df_pred.columns=["predict"]
df_true=pd.DataFrame(y_test)
df_true.columns=["true"]
df_pred_true=pd.concat([df_pred,df_true],axis=1)
df_pred_true["error"]=df_pred_true["predict"]-df_pred_true["true"]
#実際の数値と予測数値を可視化
plt.scatter(df_pred_true["predict"],df_pred_true["true"])
