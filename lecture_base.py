

#データ型の確認：整数
type(1)

#データ型の確認：浮動小数
type(1.0)

#データの確認：文字列
type("1")

#データの確認：ブーリアン型
type(True)

#intとintの足し算
1+1

#intとfloatの足し算
1+1.0

#strとstrの足し算
"出身は"+"oita"

#strとintの足し算(エラーになります)
"1+1は"+2

#1+1の計算結果をxに代入。その後、printで出力。
x=1+1
print(x)

#リスト
x_list=[1,2,3,4,5]

#fストリングス
f"計算結果は{x}です"

#if文の練習：りんごの値段と所持金によって出力結果が変わるようにする
りんごの値段=500
所持金=500

if 所持金>りんごの値段:
    print("りんごが買えました")
elif 所持金<りんごの値段:
    print("りんごが買えませんでした")
else:
    print("ぎりぎりりんごが買えました")

#for文の練習：x_list全てに対して２乗する。
for i in x_list:
    print(i**2)

#for文で1から10を出力する。range関数を使用する
for i in range(10):
    print(i+1)

#for文で1から10を2乗したものをnew_listとして作成する。
new_list=[]
for i in range(10):
    _=(i+1)**2
    new_list.append(_)

#三角形を求める関数を作成して底辺5、高さ10を計算する。計算結果をanswerという変数に代入する。
#その後fストリングスで三角形の面積は●です。という文を出力する。
def tri(base,height):
    return base*height*0.5
answer=tri(5,10)
f"三角形の面積は{answer}です。"
