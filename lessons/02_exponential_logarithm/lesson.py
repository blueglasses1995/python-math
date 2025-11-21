"""
レッスン2: 指数関数と対数関数
Exponential and Logarithmic Functions

このレッスンでは以下を学びます：
- 指数関数 e^x
- 自然対数 ln(x)
- 常用対数 log10(x)
- 指数・対数の法則
- 成長・減衰モデル
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def exponential_basics():
    """指数関数の基本"""
    print("=" * 50)
    print("1. 指数関数の基本")
    print("=" * 50)

    x_values = np.array([-2, -1, 0, 1, 2, 3, 4, 5])

    print(f"{'x':>8} {'e^x':>15} {'2^x':>15} {'10^x':>15}")
    print("-" * 55)

    for x in x_values:
        exp_e = np.exp(x)
        exp_2 = 2**x
        exp_10 = 10**x
        print(f"{x:>8} {exp_e:>15.4f} {exp_2:>15.4f} {exp_10:>15.4f}")

    print(f"\nオイラー数 e = {np.e:.10f}")

def logarithm_basics():
    """対数関数の基本"""
    print("\n" + "=" * 50)
    print("2. 対数関数の基本")
    print("=" * 50)

    x_values = np.array([0.1, 0.5, 1, 2, 5, 10, 100, 1000])

    print(f"{'x':>10} {'ln(x)':>15} {'log10(x)':>15} {'log2(x)':>15}")
    print("-" * 60)

    for x in x_values:
        ln_x = np.log(x)
        log10_x = np.log10(x)
        log2_x = np.log2(x)
        print(f"{x:>10.1f} {ln_x:>15.4f} {log10_x:>15.4f} {log2_x:>15.4f}")

def plot_exponential_functions():
    """指数関数のグラフ"""
    print("\n" + "=" * 50)
    print("3. 指数関数のグラフ")
    print("=" * 50)

    x = np.linspace(-3, 3, 1000)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # e^x
    axes[0, 0].plot(x, np.exp(x), 'b-', linewidth=2, label='e^x')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[0, 0].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[0, 0].axhline(y=1, color='r', linestyle='--', alpha=0.3)
    axes[0, 0].set_xlabel('x', fontsize=12)
    axes[0, 0].set_ylabel('e^x', fontsize=12)
    axes[0, 0].set_title('Natural Exponential Function', fontsize=14, fontweight='bold')
    axes[0, 0].legend()
    axes[0, 0].set_ylim(-1, 20)

    # 2^x, 3^x, 10^x の比較
    axes[0, 1].plot(x, 2**x, 'r-', linewidth=2, label='2^x')
    axes[0, 1].plot(x, 3**x, 'g-', linewidth=2, label='3^x')
    axes[0, 1].plot(x, np.exp(x), 'b-', linewidth=2, label='e^x')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=1, color='k', linestyle='--', alpha=0.3)
    axes[0, 1].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[0, 1].set_xlabel('x', fontsize=12)
    axes[0, 1].set_ylabel('y', fontsize=12)
    axes[0, 1].set_title('Comparison of Exponential Functions', fontsize=14, fontweight='bold')
    axes[0, 1].legend()
    axes[0, 1].set_ylim(-1, 20)

    # e^-x (減衰)
    axes[1, 0].plot(x, np.exp(-x), 'purple', linewidth=2, label='e^(-x)')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[1, 0].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[1, 0].axhline(y=1, color='r', linestyle='--', alpha=0.3)
    axes[1, 0].set_xlabel('x', fontsize=12)
    axes[1, 0].set_ylabel('e^(-x)', fontsize=12)
    axes[1, 0].set_title('Exponential Decay', fontsize=14, fontweight='bold')
    axes[1, 0].legend()
    axes[1, 0].set_ylim(-1, 20)

    # 成長と減衰の比較
    axes[1, 1].plot(x, np.exp(x), 'b-', linewidth=2, label='e^x (growth)')
    axes[1, 1].plot(x, np.exp(-x), 'r-', linewidth=2, label='e^(-x) (decay)')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=1, color='k', linestyle='--', alpha=0.3)
    axes[1, 1].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[1, 1].set_xlabel('x', fontsize=12)
    axes[1, 1].set_ylabel('y', fontsize=12)
    axes[1, 1].set_title('Growth vs Decay', fontsize=14, fontweight='bold')
    axes[1, 1].legend()
    axes[1, 1].set_ylim(-1, 20)

    plt.tight_layout()
    plt.savefig('../../outputs/02_exponential_functions.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/02_exponential_functions.png")
    plt.close()

def plot_logarithmic_functions():
    """対数関数のグラフ"""
    print("\n" + "=" * 50)
    print("4. 対数関数のグラフ")
    print("=" * 50)

    x = np.linspace(0.01, 10, 1000)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # ln(x)
    axes[0, 0].plot(x, np.log(x), 'b-', linewidth=2, label='ln(x)')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[0, 0].axvline(x=1, color='r', linestyle='--', alpha=0.3)
    axes[0, 0].set_xlabel('x', fontsize=12)
    axes[0, 0].set_ylabel('ln(x)', fontsize=12)
    axes[0, 0].set_title('Natural Logarithm', fontsize=14, fontweight='bold')
    axes[0, 0].legend()
    axes[0, 0].set_ylim(-5, 3)

    # log10(x), log2(x), ln(x) の比較
    axes[0, 1].plot(x, np.log(x), 'b-', linewidth=2, label='ln(x)')
    axes[0, 1].plot(x, np.log10(x), 'r-', linewidth=2, label='log10(x)')
    axes[0, 1].plot(x, np.log2(x), 'g-', linewidth=2, label='log2(x)')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[0, 1].axvline(x=1, color='k', linestyle='--', alpha=0.3)
    axes[0, 1].set_xlabel('x', fontsize=12)
    axes[0, 1].set_ylabel('y', fontsize=12)
    axes[0, 1].set_title('Comparison of Logarithmic Functions', fontsize=14, fontweight='bold')
    axes[0, 1].legend()
    axes[0, 1].set_ylim(-5, 3)

    # 指数関数と対数関数の逆関係
    x_exp = np.linspace(-2, 3, 100)
    axes[1, 0].plot(x_exp, np.exp(x_exp), 'b-', linewidth=2, label='y = e^x')
    axes[1, 0].plot(np.exp(x_exp), x_exp, 'r-', linewidth=2, label='y = ln(x)')
    axes[1, 0].plot([-2, 20], [-2, 20], 'k--', alpha=0.3, label='y = x')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_xlabel('x', fontsize=12)
    axes[1, 0].set_ylabel('y', fontsize=12)
    axes[1, 0].set_title('Exponential and Logarithm (Inverse Functions)',
                         fontsize=14, fontweight='bold')
    axes[1, 0].legend()
    axes[1, 0].set_xlim(-2, 20)
    axes[1, 0].set_ylim(-2, 20)
    axes[1, 0].set_aspect('equal')

    # 対数目盛
    x_range = np.logspace(-2, 3, 1000)
    axes[1, 1].semilogx(x_range, x_range, 'b-', linewidth=2, label='y = x')
    axes[1, 1].semilogx(x_range, x_range**2, 'r-', linewidth=2, label='y = x^2')
    axes[1, 1].semilogx(x_range, np.sqrt(x_range), 'g-', linewidth=2, label='y = sqrt(x)')
    axes[1, 1].grid(True, alpha=0.3, which='both')
    axes[1, 1].set_xlabel('x (log scale)', fontsize=12)
    axes[1, 1].set_ylabel('y', fontsize=12)
    axes[1, 1].set_title('Logarithmic Scale (Semi-log plot)', fontsize=14, fontweight='bold')
    axes[1, 1].legend()

    plt.tight_layout()
    plt.savefig('../../outputs/02_logarithmic_functions.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/02_logarithmic_functions.png")
    plt.close()

def exponential_logarithm_laws():
    """指数・対数の法則"""
    print("\n" + "=" * 50)
    print("5. 指数・対数の法則")
    print("=" * 50)

    a, b = 2.5, 3.7
    x, y = 1.5, 2.3

    print("指数法則:")
    print("-" * 50)
    print(f"a = {a}, b = {b}")
    print(f"e^a * e^b = e^(a+b)")
    print(f"左辺: {np.exp(a) * np.exp(b):.6f}")
    print(f"右辺: {np.exp(a + b):.6f}")
    print(f"誤差: {abs(np.exp(a) * np.exp(b) - np.exp(a + b)):.2e}")

    print(f"\n(e^a)^b = e^(a*b)")
    print(f"左辺: {np.exp(a)**b:.6f}")
    print(f"右辺: {np.exp(a * b):.6f}")
    print(f"誤差: {abs(np.exp(a)**b - np.exp(a * b)):.2e}")

    print("\n\n対数法則:")
    print("-" * 50)
    print(f"x = {x}, y = {y}")
    print(f"ln(x*y) = ln(x) + ln(y)")
    print(f"左辺: {np.log(x * y):.6f}")
    print(f"右辺: {np.log(x) + np.log(y):.6f}")
    print(f"誤差: {abs(np.log(x * y) - (np.log(x) + np.log(y))):.2e}")

    print(f"\nln(x^y) = y * ln(x)")
    print(f"左辺: {np.log(x**y):.6f}")
    print(f"右辺: {y * np.log(x):.6f}")
    print(f"誤差: {abs(np.log(x**y) - y * np.log(x)):.2e}")

    print(f"\nln(e^x) = x")
    print(f"左辺: {np.log(np.exp(x)):.6f}")
    print(f"右辺: {x:.6f}")
    print(f"誤差: {abs(np.log(np.exp(x)) - x):.2e}")

def growth_decay_models():
    """成長・減衰モデル"""
    print("\n" + "=" * 50)
    print("6. 実世界の応用: 成長・減衰モデル")
    print("=" * 50)

    t = np.linspace(0, 10, 1000)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 人口成長モデル
    P0 = 100
    r = 0.3
    P = P0 * np.exp(r * t)
    axes[0, 0].plot(t, P, 'b-', linewidth=2)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_xlabel('Time (years)', fontsize=12)
    axes[0, 0].set_ylabel('Population', fontsize=12)
    axes[0, 0].set_title(f'Population Growth: P(t) = {P0}*e^({r}*t)',
                         fontsize=14, fontweight='bold')

    # 放射性崩壊
    N0 = 1000
    lambda_decay = 0.2
    N = N0 * np.exp(-lambda_decay * t)
    axes[0, 1].plot(t, N, 'r-', linewidth=2)
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_xlabel('Time', fontsize=12)
    axes[0, 1].set_ylabel('Amount', fontsize=12)
    axes[0, 1].set_title(f'Radioactive Decay: N(t) = {N0}*e^(-{lambda_decay}*t)',
                         fontsize=14, fontweight='bold')

    # 複利計算
    principal = 1000
    rates = [0.05, 0.10, 0.15]
    for rate in rates:
        amount = principal * np.exp(rate * t)
        axes[1, 0].plot(t, amount, linewidth=2, label=f'r = {rate}')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_xlabel('Time (years)', fontsize=12)
    axes[1, 0].set_ylabel('Amount', fontsize=12)
    axes[1, 0].set_title(f'Compound Interest: A(t) = {principal}*e^(r*t)',
                         fontsize=14, fontweight='bold')
    axes[1, 0].legend()

    # 冷却の法則（ニュートンの冷却法則）
    T_env = 20
    T0 = 100
    k = 0.3
    T = T_env + (T0 - T_env) * np.exp(-k * t)
    axes[1, 1].plot(t, T, 'purple', linewidth=2)
    axes[1, 1].axhline(y=T_env, color='r', linestyle='--',
                       alpha=0.5, label=f'Environment temp = {T_env}')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].set_xlabel('Time', fontsize=12)
    axes[1, 1].set_ylabel('Temperature', fontsize=12)
    axes[1, 1].set_title(f'Cooling Law: T(t) = {T_env} + {T0-T_env}*e^(-{k}*t)',
                         fontsize=14, fontweight='bold')
    axes[1, 1].legend()

    plt.tight_layout()
    plt.savefig('../../outputs/02_growth_decay_models.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/02_growth_decay_models.png")
    plt.close()

    print("\n実世界の例:")
    print(f"1. 人口成長: 初期人口{P0}, 成長率{r}, 10年後: {P0 * np.exp(r * 10):.2f}")
    print(f"2. 放射性崩壊: 初期量{N0}, 崩壊定数{lambda_decay}, 10単位時間後: {N0 * np.exp(-lambda_decay * 10):.2f}")
    print(f"3. 複利: 元金{principal}円, 年利5%, 10年後: {principal * np.exp(0.05 * 10):.2f}円")
    print(f"4. 冷却: 初期温度{T0}°C, 環境温度{T_env}°C, 10単位時間後: {T_env + (T0 - T_env) * np.exp(-k * 10):.2f}°C")

def main():
    """メイン実行関数"""
    print("\n" + "=" * 50)
    print("Python数学学習: レッスン2 - 指数関数と対数関数")
    print("=" * 50 + "\n")

    exponential_basics()
    logarithm_basics()
    plot_exponential_functions()
    plot_logarithmic_functions()
    exponential_logarithm_laws()
    growth_decay_models()

    print("\n" + "=" * 50)
    print("レッスン2 完了!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
