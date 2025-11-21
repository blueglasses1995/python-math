# Python数学学習カリキュラム

Pythonで数学を学ぶための包括的な学習環境です。計算、可視化、そして理論の理解を通じて、数学の各分野を実践的に学習できます。

## 📚 カリキュラム

### レッスン1: 三角関数 (Trigonometric Functions)
- sin, cos, tan の基本と可視化
- 逆三角関数
- 単位円との関係
- 三角恒等式の検証

### レッスン2: 指数関数と対数関数 (Exponential & Logarithmic Functions)
- 自然指数関数 e^x
- 自然対数 ln(x)
- 指数・対数の法則
- 成長・減衰モデルの応用

### レッスン3: 複素数 (Complex Numbers)
- 複素平面とガウス平面
- 極形式と指数形式
- オイラーの公式
- 複素関数の可視化

### レッスン4: 微分 (Calculus - Differentiation)
- 数値微分と記号微分
- 導関数の幾何的意味
- 偏微分
- 勾配ベクトルとヘッセ行列

### レッスン5: 線形代数 (Linear Algebra)
- ベクトルと行列の演算
- 線形変換の可視化
- 固有値と固有ベクトル
- 特異値分解（SVD）
- 主成分分析（PCA）

### レッスン6: 統計学 (Statistics)
- 記述統計
- 確率分布（正規分布、二項分布など）
- 中心極限定理
- 相関と回帰分析
- 仮説検定

### レッスン7: 集合と位相 (Sets and Topology)
- 集合演算とベン図
- 写像と関数
- 距離空間
- 開集合と閉集合
- 連続性の概念

## 🚀 セットアップ

### 1. 必要な環境
- Python 3.8以上
- pip（Pythonパッケージマネージャー）

### 2. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

インストールされるパッケージ:
- `numpy`: 数値計算
- `scipy`: 科学計算
- `sympy`: 記号計算・微分
- `matplotlib`: グラフ描画
- `seaborn`: 統計的可視化
- `pandas`: データ分析
- `statsmodels`: 統計モデリング

### 3. 動作確認

```bash
python setup_check.py
```

このスクリプトで全ての必要なライブラリが正しくインストールされているか確認できます。

## 📖 学習の進め方

### 基本的な使い方

1. **各レッスンのディレクトリに移動**
   ```bash
   cd lessons/01_trigonometry
   ```

2. **レッスンのREADMEを読む**
   ```bash
   cat README.md
   ```

3. **レッスンを実行**
   ```bash
   python lesson.py
   ```

4. **生成された画像を確認**
   可視化結果は `outputs/` ディレクトリに保存されます。

### 推奨学習順序

1. **基礎編**（レッスン1-3）
   - 三角関数 → 指数・対数関数 → 複素数
   - これらは相互に関連しているため、順番に学習することをお勧めします

2. **微積分編**（レッスン4）
   - 基礎編を理解した後に進みます
   - 微分の概念は後のレッスンでも使用します

3. **応用編**（レッスン5-7）
   - 線形代数 → 統計学 → 集合と位相
   - これらは独立して学習できますが、線形代数は統計学の理解に役立ちます

### カスタマイズ

各レッスンのPythonスクリプトは編集可能です。自分で値を変更したり、新しい計算を追加して実験してみましょう。

## 📂 プロジェクト構造

```
python-math/
├── README.md                          # このファイル
├── requirements.txt                   # 依存パッケージ
├── setup_check.py                    # 環境確認スクリプト
├── lessons/                          # レッスンディレクトリ
│   ├── 01_trigonometry/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 02_exponential_logarithm/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 03_complex_numbers/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 04_calculus/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 05_linear_algebra/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 06_statistics/
│   │   ├── README.md
│   │   └── lesson.py
│   └── 07_sets_topology/
│       ├── README.md
│       └── lesson.py
└── outputs/                          # 可視化の出力先
```

## 💡 学習のヒント

1. **手を動かす**: コードを読むだけでなく、実際に実行して結果を確認しましょう

2. **パラメータを変える**: スクリプト内の値を変更して、結果がどう変わるか観察しましょう

3. **グラフを観察**: 生成されたグラフから視覚的に理解を深めましょう

4. **数式と対応付ける**: Pythonコードと数学の数式を対応付けて理解しましょう

5. **自分で拡張**: 学んだことを応用して、新しい計算や可視化を追加してみましょう

## 🔧 トラブルシューティング

### ImportError が発生する場合
```bash
pip install --upgrade -r requirements.txt
```

### グラフが表示されない場合
各レッスンでは画像ファイルとして保存されます（GUI不要）。
`outputs/` ディレクトリを確認してください。

### メモリエラーが発生する場合
一部のレッスンで大量のデータを扱います。
スクリプト内のサンプル数を減らして試してみてください。

## 📚 参考資料

### 公式ドキュメント
- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/)
- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
- [SymPy Documentation](https://docs.sympy.org/)

### オンライン教材
- [Khan Academy - Mathematics](https://www.khanacademy.org/math)
- [3Blue1Brown - YouTube](https://www.youtube.com/c/3blue1brown) (数学の可視化)
- [Wikipedia - 数学ポータル](https://ja.wikipedia.org/wiki/Portal:数学)

## 🎯 学習目標

このカリキュラムを完了することで、以下のスキルが身につきます：

- Pythonを使った数値計算と可視化
- 数学的概念のプログラミングによる実装
- データサイエンスや機械学習の基礎となる数学知識
- 理論と実践の結びつけ

## 🤝 貢献

改善提案やバグ報告は歓迎します。Issue や Pull Request をお気軽にどうぞ。

## 📝 ライセンス

このプロジェクトは教育目的で自由に使用できます。

---

**Happy Learning! 楽しい学習を！** 🎓✨
