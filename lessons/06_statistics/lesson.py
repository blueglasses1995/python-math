"""
レッスン6: 統計学
Statistics

このレッスンでは以下を学びます：
- 記述統計（平均、分散、標準偏差）
- 確率分布（正規分布、二項分布など）
- 中心極限定理
- 相関と回帰
- 仮説検定の基礎
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib
matplotlib.use('Agg')

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def descriptive_statistics():
    """記述統計"""
    print("=" * 50)
    print("1. 記述統計")
    print("=" * 50)

    # サンプルデータ
    np.random.seed(42)
    data = np.random.normal(100, 15, 1000)

    print(f"サンプル数: {len(data)}")
    print(f"平均: {np.mean(data):.4f}")
    print(f"中央値: {np.median(data):.4f}")
    print(f"最頻値: {stats.mode(data.round(), keepdims=True).mode[0]:.4f}")
    print(f"分散: {np.var(data, ddof=1):.4f}")
    print(f"標準偏差: {np.std(data, ddof=1):.4f}")
    print(f"最小値: {np.min(data):.4f}")
    print(f"最大値: {np.max(data):.4f}")
    print(f"範囲: {np.max(data) - np.min(data):.4f}")

    # パーセンタイル
    percentiles = [25, 50, 75]
    print(f"\nパーセンタイル:")
    for p in percentiles:
        print(f"{p}%: {np.percentile(data, p):.4f}")

    # 歪度と尖度
    print(f"\n歪度: {stats.skew(data):.4f}")
    print(f"尖度: {stats.kurtosis(data):.4f}")

    # 可視化
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # ヒストグラム
    axes[0, 0].hist(data, bins=30, edgecolor='black', alpha=0.7)
    axes[0, 0].axvline(np.mean(data), color='red', linestyle='--',
                      linewidth=2, label=f'Mean: {np.mean(data):.2f}')
    axes[0, 0].axvline(np.median(data), color='green', linestyle='--',
                      linewidth=2, label=f'Median: {np.median(data):.2f}')
    axes[0, 0].set_xlabel('Value', fontsize=12)
    axes[0, 0].set_ylabel('Frequency', fontsize=12)
    axes[0, 0].set_title('Histogram', fontsize=14, fontweight='bold')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # ボックスプロット
    axes[0, 1].boxplot(data, vert=True)
    axes[0, 1].set_ylabel('Value', fontsize=12)
    axes[0, 1].set_title('Box Plot', fontsize=14, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)

    # Q-Qプロット
    stats.probplot(data, dist="norm", plot=axes[1, 0])
    axes[1, 0].set_title('Q-Q Plot (Normal Distribution)', fontsize=14, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)

    # 累積分布
    axes[1, 1].hist(data, bins=30, cumulative=True, density=True,
                   edgecolor='black', alpha=0.7)
    axes[1, 1].set_xlabel('Value', fontsize=12)
    axes[1, 1].set_ylabel('Cumulative Probability', fontsize=12)
    axes[1, 1].set_title('Cumulative Distribution', fontsize=14, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../../outputs/06_descriptive_statistics.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/06_descriptive_statistics.png")
    plt.close()

def probability_distributions():
    """確率分布"""
    print("\n" + "=" * 50)
    print("2. 確率分布")
    print("=" * 50)

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    # 正規分布
    x = np.linspace(-5, 5, 1000)
    for mu, sigma in [(0, 1), (0, 0.5), (0, 2)]:
        y = stats.norm.pdf(x, mu, sigma)
        axes[0, 0].plot(x, y, linewidth=2, label=f'μ={mu}, σ={sigma}')
    axes[0, 0].set_xlabel('x', fontsize=12)
    axes[0, 0].set_ylabel('Probability Density', fontsize=12)
    axes[0, 0].set_title('Normal Distribution', fontsize=14, fontweight='bold')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # 二項分布
    n, p = 20, 0.5
    x_binom = np.arange(0, n+1)
    pmf = stats.binom.pmf(x_binom, n, p)
    axes[0, 1].bar(x_binom, pmf, alpha=0.7, edgecolor='black')
    axes[0, 1].set_xlabel('k', fontsize=12)
    axes[0, 1].set_ylabel('Probability', fontsize=12)
    axes[0, 1].set_title(f'Binomial Distribution (n={n}, p={p})',
                        fontsize=14, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)

    # ポアソン分布
    x_pois = np.arange(0, 20)
    for lam in [1, 4, 10]:
        pmf = stats.poisson.pmf(x_pois, lam)
        axes[0, 2].plot(x_pois, pmf, 'o-', linewidth=2, label=f'λ={lam}')
    axes[0, 2].set_xlabel('k', fontsize=12)
    axes[0, 2].set_ylabel('Probability', fontsize=12)
    axes[0, 2].set_title('Poisson Distribution', fontsize=14, fontweight='bold')
    axes[0, 2].legend()
    axes[0, 2].grid(True, alpha=0.3)

    # 指数分布
    x_exp = np.linspace(0, 5, 1000)
    for lam in [0.5, 1, 2]:
        y = stats.expon.pdf(x_exp, scale=1/lam)
        axes[1, 0].plot(x_exp, y, linewidth=2, label=f'λ={lam}')
    axes[1, 0].set_xlabel('x', fontsize=12)
    axes[1, 0].set_ylabel('Probability Density', fontsize=12)
    axes[1, 0].set_title('Exponential Distribution', fontsize=14, fontweight='bold')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)

    # t分布
    x_t = np.linspace(-4, 4, 1000)
    for df in [1, 5, 30]:
        y = stats.t.pdf(x_t, df)
        axes[1, 1].plot(x_t, y, linewidth=2, label=f'df={df}')
    # 正規分布も追加
    axes[1, 1].plot(x_t, stats.norm.pdf(x_t), 'k--', linewidth=2, label='Normal')
    axes[1, 1].set_xlabel('x', fontsize=12)
    axes[1, 1].set_ylabel('Probability Density', fontsize=12)
    axes[1, 1].set_title('t-Distribution', fontsize=14, fontweight='bold')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)

    # カイ二乗分布
    x_chi = np.linspace(0, 20, 1000)
    for df in [2, 5, 10]:
        y = stats.chi2.pdf(x_chi, df)
        axes[1, 2].plot(x_chi, y, linewidth=2, label=f'df={df}')
    axes[1, 2].set_xlabel('x', fontsize=12)
    axes[1, 2].set_ylabel('Probability Density', fontsize=12)
    axes[1, 2].set_title('Chi-Squared Distribution', fontsize=14, fontweight='bold')
    axes[1, 2].legend()
    axes[1, 2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../../outputs/06_probability_distributions.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/06_probability_distributions.png")
    plt.close()

def central_limit_theorem():
    """中心極限定理"""
    print("\n" + "=" * 50)
    print("3. 中心極限定理")
    print("=" * 50)

    np.random.seed(42)

    # 一様分布からのサンプリング
    population = np.random.uniform(0, 1, 10000)

    sample_sizes = [5, 10, 30, 100]
    n_samples = 1000

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()

    for idx, n in enumerate(sample_sizes):
        sample_means = []

        for _ in range(n_samples):
            sample = np.random.choice(population, n)
            sample_means.append(np.mean(sample))

        sample_means = np.array(sample_means)

        # ヒストグラム
        axes[idx].hist(sample_means, bins=30, density=True, alpha=0.7,
                      edgecolor='black', label='Sample means')

        # 理論的な正規分布
        mu = 0.5
        sigma = np.sqrt(1/12) / np.sqrt(n)
        x = np.linspace(sample_means.min(), sample_means.max(), 100)
        axes[idx].plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2,
                      label=f'N({mu:.2f}, {sigma:.4f})')

        axes[idx].set_xlabel('Sample Mean', fontsize=12)
        axes[idx].set_ylabel('Density', fontsize=12)
        axes[idx].set_title(f'Sample Size n = {n}', fontsize=14, fontweight='bold')
        axes[idx].legend()
        axes[idx].grid(True, alpha=0.3)

        print(f"\nサンプルサイズ n = {n}:")
        print(f"  標本平均の平均: {np.mean(sample_means):.4f}")
        print(f"  標本平均の標準偏差: {np.std(sample_means, ddof=1):.4f}")
        print(f"  理論値: {sigma:.4f}")

    plt.tight_layout()
    plt.savefig('../../outputs/06_central_limit_theorem.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/06_central_limit_theorem.png")
    plt.close()

def correlation_regression():
    """相関と回帰"""
    print("\n" + "=" * 50)
    print("4. 相関と回帰分析")
    print("=" * 50)

    np.random.seed(42)

    # サンプルデータ
    n = 100
    x = np.random.uniform(0, 10, n)
    y = 2 * x + 3 + np.random.normal(0, 2, n)

    # 相関係数
    corr_pearson = stats.pearsonr(x, y)
    corr_spearman = stats.spearmanr(x, y)

    print(f"Pearson相関係数: {corr_pearson.correlation:.4f} (p値: {corr_pearson.pvalue:.4e})")
    print(f"Spearman相関係数: {corr_spearman.correlation:.4f} (p値: {corr_spearman.pvalue:.4e})")

    # 線形回帰
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    print(f"\n線形回帰:")
    print(f"  傾き: {slope:.4f}")
    print(f"  切片: {intercept:.4f}")
    print(f"  R²値: {r_value**2:.4f}")
    print(f"  p値: {p_value:.4e}")
    print(f"  標準誤差: {std_err:.4f}")

    # 可視化
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 散布図と回帰直線
    axes[0].scatter(x, y, alpha=0.6, s=50)
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = slope * x_line + intercept
    axes[0].plot(x_line, y_line, 'r-', linewidth=2,
                label=f'y = {slope:.2f}x + {intercept:.2f} (R²={r_value**2:.3f})')
    axes[0].set_xlabel('x', fontsize=12)
    axes[0].set_ylabel('y', fontsize=12)
    axes[0].set_title('Linear Regression', fontsize=14, fontweight='bold')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # 残差プロット
    y_pred = slope * x + intercept
    residuals = y - y_pred
    axes[1].scatter(y_pred, residuals, alpha=0.6, s=50)
    axes[1].axhline(y=0, color='r', linestyle='--', linewidth=2)
    axes[1].set_xlabel('Fitted Values', fontsize=12)
    axes[1].set_ylabel('Residuals', fontsize=12)
    axes[1].set_title('Residual Plot', fontsize=14, fontweight='bold')
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../../outputs/06_regression.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/06_regression.png")
    plt.close()

def hypothesis_testing():
    """仮説検定"""
    print("\n" + "=" * 50)
    print("5. 仮説検定")
    print("=" * 50)

    np.random.seed(42)

    # 1標本t検定
    sample = np.random.normal(100, 15, 100)
    t_stat, p_value = stats.ttest_1samp(sample, 95)

    print("1標本t検定（母平均が95かどうか）:")
    print(f"  t統計量: {t_stat:.4f}")
    print(f"  p値: {p_value:.4f}")
    print(f"  結果: {'帰無仮説を棄却' if p_value < 0.05 else '帰無仮説を採択'} (α=0.05)")

    # 2標本t検定
    sample1 = np.random.normal(100, 15, 100)
    sample2 = np.random.normal(105, 15, 100)
    t_stat, p_value = stats.ttest_ind(sample1, sample2)

    print(f"\n2標本t検定（2群の平均に差があるか）:")
    print(f"  群1の平均: {np.mean(sample1):.4f}")
    print(f"  群2の平均: {np.mean(sample2):.4f}")
    print(f"  t統計量: {t_stat:.4f}")
    print(f"  p値: {p_value:.4f}")
    print(f"  結果: {'帰無仮説を棄却（差がある）' if p_value < 0.05 else '帰無仮説を採択（差がない）'} (α=0.05)")

    # カイ二乗検定
    observed = np.array([[30, 10], [20, 40]])
    chi2, p_value, dof, expected = stats.chi2_contingency(observed)

    print(f"\nカイ二乗検定（独立性の検定）:")
    print(f"  観測度数:\n{observed}")
    print(f"  期待度数:\n{expected}")
    print(f"  χ²統計量: {chi2:.4f}")
    print(f"  自由度: {dof}")
    print(f"  p値: {p_value:.4f}")
    print(f"  結果: {'独立ではない' if p_value < 0.05 else '独立である'} (α=0.05)")

    # 可視化
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # t分布と検定統計量
    df = len(sample) - 1
    x = np.linspace(-4, 4, 1000)
    axes[0, 0].plot(x, stats.t.pdf(x, df), 'b-', linewidth=2, label='t-distribution')
    axes[0, 0].axvline(t_stat, color='r', linestyle='--', linewidth=2,
                      label=f't-statistic = {t_stat:.2f}')
    axes[0, 0].fill_between(x, 0, stats.t.pdf(x, df),
                           where=(np.abs(x) >= np.abs(t_stat)),
                           alpha=0.3, color='red', label=f'p-value region')
    axes[0, 0].set_xlabel('t', fontsize=12)
    axes[0, 0].set_ylabel('Probability Density', fontsize=12)
    axes[0, 0].set_title('One-Sample t-Test', fontsize=14, fontweight='bold')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # 2群の分布
    axes[0, 1].hist(sample1, bins=20, alpha=0.6, label='Group 1', edgecolor='black')
    axes[0, 1].hist(sample2, bins=20, alpha=0.6, label='Group 2', edgecolor='black')
    axes[0, 1].axvline(np.mean(sample1), color='blue', linestyle='--', linewidth=2)
    axes[0, 1].axvline(np.mean(sample2), color='orange', linestyle='--', linewidth=2)
    axes[0, 1].set_xlabel('Value', fontsize=12)
    axes[0, 1].set_ylabel('Frequency', fontsize=12)
    axes[0, 1].set_title('Two-Sample t-Test', fontsize=14, fontweight='bold')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)

    # 信頼区間
    confidence = 0.95
    mean = np.mean(sample)
    se = stats.sem(sample)
    ci = stats.t.interval(confidence, len(sample)-1, mean, se)

    x_range = np.linspace(mean - 4*se, mean + 4*se, 1000)
    axes[1, 0].plot(x_range, stats.norm.pdf(x_range, mean, se), 'b-', linewidth=2)
    axes[1, 0].fill_between(x_range, 0, stats.norm.pdf(x_range, mean, se),
                           where=((x_range >= ci[0]) & (x_range <= ci[1])),
                           alpha=0.3, color='blue',
                           label=f'{confidence*100:.0f}% CI: [{ci[0]:.2f}, {ci[1]:.2f}]')
    axes[1, 0].axvline(mean, color='r', linestyle='--', linewidth=2, label=f'Mean: {mean:.2f}')
    axes[1, 0].set_xlabel('Value', fontsize=12)
    axes[1, 0].set_ylabel('Probability Density', fontsize=12)
    axes[1, 0].set_title('Confidence Interval', fontsize=14, fontweight='bold')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)

    # 検出力分析
    effect_sizes = np.linspace(0, 1.5, 100)
    powers = []
    for es in effect_sizes:
        power = stats.ttest_power(es, len(sample), 0.05)
        powers.append(power)

    axes[1, 1].plot(effect_sizes, powers, 'b-', linewidth=2)
    axes[1, 1].axhline(0.8, color='r', linestyle='--', linewidth=1,
                      label='80% power (conventional)')
    axes[1, 1].set_xlabel('Effect Size (Cohen\'s d)', fontsize=12)
    axes[1, 1].set_ylabel('Statistical Power', fontsize=12)
    axes[1, 1].set_title('Power Analysis', fontsize=14, fontweight='bold')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../../outputs/06_hypothesis_testing.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/06_hypothesis_testing.png")
    plt.close()

def main():
    """メイン実行関数"""
    print("\n" + "=" * 50)
    print("Python数学学習: レッスン6 - 統計学")
    print("=" * 50 + "\n")

    descriptive_statistics()
    probability_distributions()
    central_limit_theorem()
    correlation_regression()
    hypothesis_testing()

    print("\n" + "=" * 50)
    print("レッスン6 完了!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
