#!/usr/bin/env python3
"""
環境セットアップ確認スクリプト
Setup Verification Script

このスクリプトは、Python数学学習環境が正しくセットアップされているか確認します。
"""

import sys
import importlib

def check_python_version():
    """Python バージョンの確認"""
    print("=" * 60)
    print("1. Python バージョンチェック")
    print("=" * 60)

    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")

    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8以上が必要です")
        return False
    else:
        print("✅ Pythonバージョン OK")
        return True

def check_packages():
    """必要なパッケージの確認"""
    print("\n" + "=" * 60)
    print("2. 必要なパッケージのチェック")
    print("=" * 60)

    required_packages = {
        'numpy': 'NumPy',
        'scipy': 'SciPy',
        'sympy': 'SymPy',
        'matplotlib': 'Matplotlib',
        'seaborn': 'Seaborn',
        'pandas': 'Pandas',
        'statsmodels': 'StatsModels'
    }

    all_ok = True

    for package, name in required_packages.items():
        try:
            mod = importlib.import_module(package)
            version = getattr(mod, '__version__', 'unknown')
            print(f"✅ {name:15} (v{version})")
        except ImportError:
            print(f"❌ {name:15} がインストールされていません")
            all_ok = False

    return all_ok

def check_basic_functionality():
    """基本機能のチェック"""
    print("\n" + "=" * 60)
    print("3. 基本機能のチェック")
    print("=" * 60)

    try:
        import numpy as np
        import matplotlib
        matplotlib.use('Agg')  # GUI不要のバックエンド
        import matplotlib.pyplot as plt

        # NumPy の基本計算
        print("\n[NumPy テスト]")
        arr = np.array([1, 2, 3, 4, 5])
        print(f"配列: {arr}")
        print(f"平均: {np.mean(arr)}")
        print(f"標準偏差: {np.std(arr)}")
        print("✅ NumPy 計算 OK")

        # Matplotlib のグラフ生成
        print("\n[Matplotlib テスト]")
        fig, ax = plt.subplots()
        x = np.linspace(0, 2*np.pi, 100)
        ax.plot(x, np.sin(x))
        plt.savefig('test_plot.png')
        plt.close()
        print("✅ グラフ生成 OK (test_plot.png)")

        # SymPy の記号計算
        print("\n[SymPy テスト]")
        import sympy as sp
        x = sp.Symbol('x')
        expr = x**2 + 2*x + 1
        derivative = sp.diff(expr, x)
        print(f"関数: {expr}")
        print(f"導関数: {derivative}")
        print("✅ 記号計算 OK")

        # SciPy の統計計算
        print("\n[SciPy テスト]")
        from scipy import stats
        data = np.random.normal(0, 1, 100)
        mean, std = stats.norm.fit(data)
        print(f"正規分布フィッティング: 平均={mean:.4f}, 標準偏差={std:.4f}")
        print("✅ 統計計算 OK")

        return True

    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        return False

def check_directories():
    """ディレクトリ構造の確認"""
    print("\n" + "=" * 60)
    print("4. ディレクトリ構造のチェック")
    print("=" * 60)

    import os

    required_dirs = [
        'lessons/01_trigonometry',
        'lessons/02_exponential_logarithm',
        'lessons/03_complex_numbers',
        'lessons/04_calculus',
        'lessons/05_linear_algebra',
        'lessons/06_statistics',
        'lessons/07_sets_topology',
        'outputs'
    ]

    all_ok = True

    for dir_path in required_dirs:
        if os.path.isdir(dir_path):
            print(f"✅ {dir_path}")
        else:
            print(f"❌ {dir_path} が見つかりません")
            all_ok = False

    return all_ok

def test_lesson_execution():
    """レッスンファイルの実行テスト"""
    print("\n" + "=" * 60)
    print("5. レッスンファイルの存在確認")
    print("=" * 60)

    import os

    lessons = [
        'lessons/01_trigonometry/lesson.py',
        'lessons/02_exponential_logarithm/lesson.py',
        'lessons/03_complex_numbers/lesson.py',
        'lessons/04_calculus/lesson.py',
        'lessons/05_linear_algebra/lesson.py',
        'lessons/06_statistics/lesson.py',
        'lessons/07_sets_topology/lesson.py'
    ]

    all_ok = True

    for lesson in lessons:
        if os.path.isfile(lesson):
            print(f"✅ {lesson}")
        else:
            print(f"❌ {lesson} が見つかりません")
            all_ok = False

    return all_ok

def main():
    """メイン実行関数"""
    print("\n" + "=" * 60)
    print("Python数学学習環境 セットアップチェック")
    print("=" * 60 + "\n")

    results = []

    # 各チェックを実行
    results.append(("Pythonバージョン", check_python_version()))
    results.append(("パッケージ", check_packages()))
    results.append(("ディレクトリ構造", check_directories()))
    results.append(("レッスンファイル", test_lesson_execution()))
    results.append(("基本機能", check_basic_functionality()))

    # 結果のサマリー
    print("\n" + "=" * 60)
    print("チェック結果サマリー")
    print("=" * 60)

    all_passed = True
    for check_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{check_name:20} : {status}")
        if not passed:
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("✅ 全てのチェックに合格しました！")
        print("学習を始める準備ができています。")
        print("\n次のステップ:")
        print("  1. lessons/ ディレクトリ内のレッスンを順番に実行")
        print("  2. 各レッスンの README.md を読む")
        print("  3. python lesson.py を実行")
        print("  4. outputs/ ディレクトリの画像を確認")
    else:
        print("❌ いくつかのチェックに失敗しました。")
        print("上記のエラーを修正してから再度実行してください。")
        print("\n推奨される対処法:")
        print("  pip install -r requirements.txt")
    print("=" * 60 + "\n")

    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
