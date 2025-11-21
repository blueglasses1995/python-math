"""
レッスン1: 三角関数
Trigonometric Functions

このレッスンでは以下を学びます：
- sin, cos, tan の基本
- 逆三角関数 (arcsin, arccos, arctan)
- 三角関数のグラフ
- 単位円との関係
- 三角恒等式の確認
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # GUI不要のバックエンド

# 日本語フォントの設定
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def basic_trigonometry():
    """基本的な三角関数の計算"""
    print("=" * 50)
    print("1. 基本的な三角関数")
    print("=" * 50)

    angles_deg = [0, 30, 45, 60, 90, 180, 270, 360]
    angles_rad = np.radians(angles_deg)

    print(f"{'角度(度)':>10} {'角度(ラジアン)':>15} {'sin':>10} {'cos':>10} {'tan':>10}")
    print("-" * 60)

    for deg, rad in zip(angles_deg, angles_rad):
        sin_val = np.sin(rad)
        cos_val = np.cos(rad)
        tan_val = np.tan(rad)
        print(f"{deg:>10}° {rad:>14.4f} {sin_val:>10.4f} {cos_val:>10.4f} {tan_val:>10.4f}")

def plot_trigonometric_functions():
    """三角関数のグラフを描画"""
    print("\n" + "=" * 50)
    print("2. 三角関数のグラフ")
    print("=" * 50)

    x = np.linspace(-2*np.pi, 2*np.pi, 1000)

    fig, axes = plt.subplots(3, 1, figsize=(12, 10))

    # sin(x)
    axes[0].plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
    axes[0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[0].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_ylabel('sin(x)', fontsize=12)
    axes[0].set_title('Sine Function', fontsize=14, fontweight='bold')
    axes[0].legend()
    axes[0].set_ylim(-1.5, 1.5)

    # cos(x)
    axes[1].plot(x, np.cos(x), 'r-', linewidth=2, label='cos(x)')
    axes[1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[1].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[1].grid(True, alpha=0.3)
    axes[1].set_ylabel('cos(x)', fontsize=12)
    axes[1].set_title('Cosine Function', fontsize=14, fontweight='bold')
    axes[1].legend()
    axes[1].set_ylim(-1.5, 1.5)

    # tan(x)
    axes[2].plot(x, np.tan(x), 'g-', linewidth=2, label='tan(x)')
    axes[2].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[2].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[2].grid(True, alpha=0.3)
    axes[2].set_ylabel('tan(x)', fontsize=12)
    axes[2].set_xlabel('x (radians)', fontsize=12)
    axes[2].set_title('Tangent Function', fontsize=14, fontweight='bold')
    axes[2].legend()
    axes[2].set_ylim(-5, 5)

    plt.tight_layout()
    plt.savefig('../../outputs/01_trigonometric_functions.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/01_trigonometric_functions.png")
    plt.close()

def unit_circle_visualization():
    """単位円と三角関数の関係を可視化"""
    print("\n" + "=" * 50)
    print("3. 単位円と三角関数")
    print("=" * 50)

    fig, ax = plt.subplots(figsize=(10, 10))

    # 単位円
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(np.cos(theta), np.sin(theta), 'b-', linewidth=2)

    # いくつかの角度での点を表示
    angles = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3,
              3*np.pi/4, 5*np.pi/6, np.pi, 3*np.pi/2]

    for angle in angles:
        x, y = np.cos(angle), np.sin(angle)
        ax.plot(x, y, 'ro', markersize=8)
        ax.plot([0, x], [0, y], 'r--', alpha=0.5)

        # ラベル
        angle_deg = int(np.degrees(angle))
        ax.annotate(f'{angle_deg}°', xy=(x, y), xytext=(x*1.2, y*1.2),
                   fontsize=10, ha='center')

    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('cos(theta)', fontsize=12)
    ax.set_ylabel('sin(theta)', fontsize=12)
    ax.set_title('Unit Circle and Trigonometric Functions', fontsize=14, fontweight='bold')

    plt.savefig('../../outputs/01_unit_circle.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/01_unit_circle.png")
    plt.close()

def inverse_trigonometry():
    """逆三角関数"""
    print("\n" + "=" * 50)
    print("4. 逆三角関数")
    print("=" * 50)

    values = [-1, -0.5, 0, 0.5, 1]

    print(f"{'値':>8} {'arcsin':>12} {'arccos':>12} {'arctan':>12}")
    print("-" * 50)

    for val in values:
        arcsin_val = np.arcsin(val) if -1 <= val <= 1 else np.nan
        arccos_val = np.arccos(val) if -1 <= val <= 1 else np.nan
        arctan_val = np.arctan(val)

        print(f"{val:>8.1f} {arcsin_val:>12.4f} {arccos_val:>12.4f} {arctan_val:>12.4f}")

    # 逆三角関数のグラフ
    x = np.linspace(-1, 1, 1000)
    x_tan = np.linspace(-5, 5, 1000)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # arcsin
    axes[0].plot(x, np.arcsin(x), 'b-', linewidth=2)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xlabel('x', fontsize=12)
    axes[0].set_ylabel('arcsin(x)', fontsize=12)
    axes[0].set_title('Arcsine Function', fontsize=14, fontweight='bold')
    axes[0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[0].axvline(x=0, color='k', linestyle='--', alpha=0.3)

    # arccos
    axes[1].plot(x, np.arccos(x), 'r-', linewidth=2)
    axes[1].grid(True, alpha=0.3)
    axes[1].set_xlabel('x', fontsize=12)
    axes[1].set_ylabel('arccos(x)', fontsize=12)
    axes[1].set_title('Arccosine Function', fontsize=14, fontweight='bold')
    axes[1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[1].axvline(x=0, color='k', linestyle='--', alpha=0.3)

    # arctan
    axes[2].plot(x_tan, np.arctan(x_tan), 'g-', linewidth=2)
    axes[2].grid(True, alpha=0.3)
    axes[2].set_xlabel('x', fontsize=12)
    axes[2].set_ylabel('arctan(x)', fontsize=12)
    axes[2].set_title('Arctangent Function', fontsize=14, fontweight='bold')
    axes[2].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[2].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[2].axhline(y=np.pi/2, color='r', linestyle='--', alpha=0.3, label='pi/2')
    axes[2].axhline(y=-np.pi/2, color='r', linestyle='--', alpha=0.3, label='-pi/2')
    axes[2].legend()

    plt.tight_layout()
    plt.savefig('../../outputs/01_inverse_trig.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/01_inverse_trig.png")
    plt.close()

def trigonometric_identities():
    """三角恒等式の確認"""
    print("\n" + "=" * 50)
    print("5. 三角恒等式の検証")
    print("=" * 50)

    angles = np.linspace(0, 2*np.pi, 10)

    print("\n基本恒等式: sin²(x) + cos²(x) = 1")
    print(f"{'角度(rad)':>12} {'sin²+cos²':>15} {'誤差':>15}")
    print("-" * 45)

    for angle in angles:
        identity = np.sin(angle)**2 + np.cos(angle)**2
        error = abs(identity - 1)
        print(f"{angle:>12.4f} {identity:>15.10f} {error:>15.2e}")

    print("\n\n加法定理: sin(a+b) = sin(a)cos(b) + cos(a)sin(b)")
    a, b = np.pi/3, np.pi/4
    left = np.sin(a + b)
    right = np.sin(a)*np.cos(b) + np.cos(a)*np.sin(b)
    print(f"a = π/3, b = π/4")
    print(f"左辺: sin(a+b) = {left:.10f}")
    print(f"右辺: sin(a)cos(b) + cos(a)sin(b) = {right:.10f}")
    print(f"誤差: {abs(left - right):.2e}")

def main():
    """メイン実行関数"""
    print("\n" + "=" * 50)
    print("Python数学学習: レッスン1 - 三角関数")
    print("=" * 50 + "\n")

    basic_trigonometry()
    plot_trigonometric_functions()
    unit_circle_visualization()
    inverse_trigonometry()
    trigonometric_identities()

    print("\n" + "=" * 50)
    print("レッスン1 完了!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
