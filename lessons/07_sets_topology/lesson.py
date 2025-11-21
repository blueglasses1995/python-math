"""
レッスン7: 集合と位相
Sets and Topology

このレッスンでは以下を学びます：
- 集合の基本操作
- ベン図
- 写像と関数
- 距離空間
- 開集合と閉集合
- 連続性の概念
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.patches as mpatches
import matplotlib
matplotlib.use('Agg')

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def set_operations():
    """集合の基本操作"""
    print("=" * 50)
    print("1. 集合の基本操作")
    print("=" * 50)

    # Pythonの集合を使用
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    C = {1, 2, 3}

    print(f"集合A: {A}")
    print(f"集合B: {B}")
    print(f"集合C: {C}")

    # 基本操作
    print(f"\n和集合 A ∪ B: {A | B}")
    print(f"積集合 A ∩ B: {A & B}")
    print(f"差集合 A - B: {A - B}")
    print(f"対称差 A △ B: {A ^ B}")

    # 部分集合
    print(f"\nC ⊆ A: {C.issubset(A)}")
    print(f"A ⊆ C: {A.issubset(C)}")
    print(f"C ⊂ A (真部分集合): {C < A}")

    # べき集合（2^n個の部分集合）
    def powerset(s):
        from itertools import chain, combinations
        return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

    small_set = {1, 2, 3}
    ps = powerset(small_set)
    print(f"\n{small_set} のべき集合（全{len(ps)}個の部分集合）:")
    for subset in ps:
        print(f"  {set(subset)}")

    # 直積
    D = {1, 2}
    E = {'a', 'b'}
    cartesian_product = [(d, e) for d in D for e in E]
    print(f"\n直積 D × E: {cartesian_product}")

def venn_diagrams():
    """ベン図の可視化"""
    print("\n" + "=" * 50)
    print("2. ベン図による集合の可視化")
    print("=" * 50)

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()

    # 2つの集合のベン図
    def draw_venn2(ax, title, highlight=None):
        # 円の設定
        circle1 = Circle((0.35, 0.5), 0.3, color='blue', alpha=0.3)
        circle2 = Circle((0.65, 0.5), 0.3, color='red', alpha=0.3)

        ax.add_patch(circle1)
        ax.add_patch(circle2)

        # ハイライト
        if highlight == 'union':
            circle1_h = Circle((0.35, 0.5), 0.3, color='yellow', alpha=0.5)
            circle2_h = Circle((0.65, 0.5), 0.3, color='yellow', alpha=0.5)
            ax.add_patch(circle1_h)
            ax.add_patch(circle2_h)
        elif highlight == 'intersection':
            # 交差部分のみハイライト
            theta = np.linspace(0, 2*np.pi, 100)
            x_overlap = 0.5 + 0.15 * np.cos(theta)
            y_overlap = 0.5 + 0.15 * np.sin(theta)
            ax.fill(x_overlap, y_overlap, color='yellow', alpha=0.7)
        elif highlight == 'difference':
            circle1_h = Circle((0.35, 0.5), 0.3, color='yellow', alpha=0.5)
            ax.add_patch(circle1_h)

        ax.text(0.25, 0.5, 'A', fontsize=20, fontweight='bold')
        ax.text(0.75, 0.5, 'B', fontsize=20, fontweight='bold')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(title, fontsize=12, fontweight='bold')

    # 各操作のベン図
    draw_venn2(axes[0], 'Sets A and B')
    draw_venn2(axes[1], 'Union: A ∪ B', 'union')
    draw_venn2(axes[2], 'Intersection: A ∩ B', 'intersection')
    draw_venn2(axes[3], 'Difference: A - B', 'difference')

    # 3つの集合のベン図
    def draw_venn3(ax, title):
        circle1 = Circle((0.35, 0.55), 0.25, color='blue', alpha=0.3, label='A')
        circle2 = Circle((0.65, 0.55), 0.25, color='red', alpha=0.3, label='B')
        circle3 = Circle((0.5, 0.3), 0.25, color='green', alpha=0.3, label='C')

        ax.add_patch(circle1)
        ax.add_patch(circle2)
        ax.add_patch(circle3)

        ax.text(0.25, 0.65, 'A', fontsize=16, fontweight='bold')
        ax.text(0.75, 0.65, 'B', fontsize=16, fontweight='bold')
        ax.text(0.5, 0.15, 'C', fontsize=16, fontweight='bold')

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(title, fontsize=12, fontweight='bold')

    draw_venn3(axes[4], 'Three Sets: A, B, C')

    # ド・モルガンの法則の可視化
    axes[5].text(0.5, 0.7, "De Morgan's Laws:", fontsize=14, fontweight='bold',
                ha='center', transform=axes[5].transAxes)
    axes[5].text(0.5, 0.5, "(A ∪ B)' = A' ∩ B'", fontsize=12,
                ha='center', transform=axes[5].transAxes)
    axes[5].text(0.5, 0.3, "(A ∩ B)' = A' ∪ B'", fontsize=12,
                ha='center', transform=axes[5].transAxes)
    axes[5].axis('off')

    plt.tight_layout()
    plt.savefig('../../outputs/07_venn_diagrams.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/07_venn_diagrams.png")
    plt.close()

def functions_mappings():
    """写像と関数"""
    print("\n" + "=" * 50)
    print("3. 写像と関数")
    print("=" * 50)

    # 単射、全射、全単射の例
    print("単射 (Injection): 異なる入力 → 異なる出力")
    print("  例: f(x) = 2x")

    print("\n全射 (Surjection): すべての出力が使われる")
    print("  例: f: R → R, f(x) = x³")

    print("\n全単射 (Bijection): 単射かつ全射")
    print("  例: f: R → R, f(x) = x")

    # 可視化
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 単射
    x = np.linspace(-5, 5, 100)
    axes[0, 0].plot(x, 2*x, 'b-', linewidth=2)
    axes[0, 0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[0, 0].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_xlabel('x', fontsize=12)
    axes[0, 0].set_ylabel('f(x)', fontsize=12)
    axes[0, 0].set_title('Injection: f(x) = 2x', fontsize=14, fontweight='bold')

    # 全射
    axes[0, 1].plot(x, x**3, 'r-', linewidth=2)
    axes[0, 1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[0, 1].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_xlabel('x', fontsize=12)
    axes[0, 1].set_ylabel('f(x)', fontsize=12)
    axes[0, 1].set_title('Surjection: f(x) = x³', fontsize=14, fontweight='bold')

    # 全単射
    axes[1, 0].plot(x, x, 'g-', linewidth=2)
    axes[1, 0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[1, 0].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[1, 0].plot(x, x, 'k--', alpha=0.3, label='y=x')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_xlabel('x', fontsize=12)
    axes[1, 0].set_ylabel('f(x)', fontsize=12)
    axes[1, 0].set_title('Bijection: f(x) = x', fontsize=14, fontweight='bold')
    axes[1, 0].set_aspect('equal')

    # 非単射の例
    axes[1, 1].plot(x, x**2, 'purple', linewidth=2)
    axes[1, 1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[1, 1].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].set_xlabel('x', fontsize=12)
    axes[1, 1].set_ylabel('f(x)', fontsize=12)
    axes[1, 1].set_title('Not Injective: f(x) = x² (f(-2) = f(2))',
                        fontsize=14, fontweight='bold')
    axes[1, 1].set_ylim(-1, 25)

    plt.tight_layout()
    plt.savefig('../../outputs/07_functions.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/07_functions.png")
    plt.close()

def metric_spaces():
    """距離空間"""
    print("\n" + "=" * 50)
    print("4. 距離空間")
    print("=" * 50)

    # ユークリッド距離
    p1 = np.array([1, 2])
    p2 = np.array([4, 6])

    euclidean_dist = np.linalg.norm(p2 - p1)
    manhattan_dist = np.sum(np.abs(p2 - p1))
    chebyshev_dist = np.max(np.abs(p2 - p1))

    print(f"点1: {p1}")
    print(f"点2: {p2}")
    print(f"\nユークリッド距離: {euclidean_dist:.4f}")
    print(f"マンハッタン距離: {manhattan_dist:.4f}")
    print(f"チェビシェフ距離: {chebyshev_dist:.4f}")

    # 可視化
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # ユークリッド距離
    axes[0].plot([p1[0], p2[0]], [p1[1], p2[1]], 'r-', linewidth=2,
                label=f'Euclidean: {euclidean_dist:.2f}')
    axes[0].plot(p1[0], p1[1], 'bo', markersize=10)
    axes[0].plot(p2[0], p2[1], 'go', markersize=10)
    # 距離1の円
    circle = Circle(p1, 1, fill=False, edgecolor='blue', linestyle='--', linewidth=1)
    axes[0].add_patch(circle)
    axes[0].set_aspect('equal')
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xlabel('x', fontsize=12)
    axes[0].set_ylabel('y', fontsize=12)
    axes[0].set_title('Euclidean Distance (L2)', fontsize=14, fontweight='bold')
    axes[0].legend()
    axes[0].set_xlim(-1, 6)
    axes[0].set_ylim(0, 8)

    # マンハッタン距離
    axes[1].plot([p1[0], p2[0]], [p1[1], p1[1]], 'r-', linewidth=2)
    axes[1].plot([p2[0], p2[0]], [p1[1], p2[1]], 'r-', linewidth=2,
                label=f'Manhattan: {manhattan_dist:.2f}')
    axes[1].plot(p1[0], p1[1], 'bo', markersize=10)
    axes[1].plot(p2[0], p2[1], 'go', markersize=10)
    # 距離1のダイヤモンド
    diamond = mpatches.Polygon([[p1[0]+1, p1[1]], [p1[0], p1[1]+1],
                                [p1[0]-1, p1[1]], [p1[0], p1[1]-1]],
                              fill=False, edgecolor='blue', linestyle='--', linewidth=1)
    axes[1].add_patch(diamond)
    axes[1].set_aspect('equal')
    axes[1].grid(True, alpha=0.3)
    axes[1].set_xlabel('x', fontsize=12)
    axes[1].set_ylabel('y', fontsize=12)
    axes[1].set_title('Manhattan Distance (L1)', fontsize=14, fontweight='bold')
    axes[1].legend()
    axes[1].set_xlim(-1, 6)
    axes[1].set_ylim(0, 8)

    # チェビシェフ距離
    axes[2].plot([p1[0], p2[0]], [p1[1], p2[1]], 'r-', linewidth=2,
                label=f'Chebyshev: {chebyshev_dist:.2f}')
    axes[2].plot(p1[0], p1[1], 'bo', markersize=10)
    axes[2].plot(p2[0], p2[1], 'go', markersize=10)
    # 距離1の正方形
    square = mpatches.Rectangle((p1[0]-1, p1[1]-1), 2, 2,
                                fill=False, edgecolor='blue', linestyle='--', linewidth=1)
    axes[2].add_patch(square)
    axes[2].set_aspect('equal')
    axes[2].grid(True, alpha=0.3)
    axes[2].set_xlabel('x', fontsize=12)
    axes[2].set_ylabel('y', fontsize=12)
    axes[2].set_title('Chebyshev Distance (L∞)', fontsize=14, fontweight='bold')
    axes[2].legend()
    axes[2].set_xlim(-1, 6)
    axes[2].set_ylim(0, 8)

    plt.tight_layout()
    plt.savefig('../../outputs/07_metric_spaces.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/07_metric_spaces.png")
    plt.close()

def open_closed_sets():
    """開集合と閉集合"""
    print("\n" + "=" * 50)
    print("5. 開集合と閉集合")
    print("=" * 50)

    print("開集合: 境界を含まない集合")
    print("  例: 開区間 (0, 1) = {x ∈ R | 0 < x < 1}")

    print("\n閉集合: 境界を含む集合")
    print("  例: 閉区間 [0, 1] = {x ∈ R | 0 ≤ x ≤ 1}")

    print("\n開球: B(x₀, r) = {x | d(x, x₀) < r}")
    print("閉球: B̄(x₀, r) = {x | d(x, x₀) ≤ r}")

    # 可視化
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 開区間 vs 閉区間
    x = np.linspace(-0.5, 1.5, 1000)
    axes[0, 0].axhline(y=1, color='blue', linewidth=3, label='Open: (0, 1)')
    axes[0, 0].plot([0, 1], [1, 1], 'bo', markersize=8, markerfacecolor='white',
                   markeredgewidth=2)  # 開端点
    axes[0, 0].axhline(y=0.5, color='red', linewidth=3, label='Closed: [0, 1]')
    axes[0, 0].plot([0, 1], [0.5, 0.5], 'ro', markersize=8)  # 閉端点
    axes[0, 0].set_xlim(-0.5, 1.5)
    axes[0, 0].set_ylim(0, 1.5)
    axes[0, 0].set_xlabel('x', fontsize=12)
    axes[0, 0].set_title('Open vs Closed Intervals (1D)', fontsize=14, fontweight='bold')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # 開球と閉球（2D）
    center = np.array([0, 0])
    radius = 1

    # 開球
    circle_open = Circle(center, radius, fill=True, facecolor='lightblue',
                        edgecolor='blue', linewidth=2, linestyle='--',
                        alpha=0.5, label='Open ball')
    axes[0, 1].add_patch(circle_open)
    axes[0, 1].plot(center[0], center[1], 'ko', markersize=8)

    axes[0, 1].set_xlim(-2, 2)
    axes[0, 1].set_ylim(-2, 2)
    axes[0, 1].set_aspect('equal')
    axes[0, 1].set_xlabel('x', fontsize=12)
    axes[0, 1].set_ylabel('y', fontsize=12)
    axes[0, 1].set_title('Open Ball: B(0, 1) = {x | ||x|| < 1}',
                        fontsize=14, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].legend()

    # 閉球
    circle_closed = Circle(center, radius, fill=True, facecolor='lightcoral',
                          edgecolor='red', linewidth=2,
                          alpha=0.5, label='Closed ball')
    axes[1, 0].add_patch(circle_closed)
    axes[1, 0].plot(center[0], center[1], 'ko', markersize=8)

    axes[1, 0].set_xlim(-2, 2)
    axes[1, 0].set_ylim(-2, 2)
    axes[1, 0].set_aspect('equal')
    axes[1, 0].set_xlabel('x', fontsize=12)
    axes[1, 0].set_ylabel('y', fontsize=12)
    axes[1, 0].set_title('Closed Ball: B̄(0, 1) = {x | ||x|| ≤ 1}',
                        fontsize=14, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()

    # 境界
    circle_boundary = Circle(center, radius, fill=False,
                            edgecolor='green', linewidth=3,
                            label='Boundary ∂B')
    axes[1, 1].add_patch(circle_boundary)
    axes[1, 1].plot(center[0], center[1], 'ko', markersize=8, label='Center')

    # 内部の点
    theta = np.pi/4
    interior_point = np.array([0.5*np.cos(theta), 0.5*np.sin(theta)])
    axes[1, 1].plot(interior_point[0], interior_point[1], 'bo', markersize=8,
                   label='Interior point')

    # 境界上の点
    boundary_point = np.array([np.cos(theta), np.sin(theta)])
    axes[1, 1].plot(boundary_point[0], boundary_point[1], 'go', markersize=8,
                   label='Boundary point')

    # 外部の点
    exterior_point = np.array([1.5*np.cos(theta), 1.5*np.sin(theta)])
    axes[1, 1].plot(exterior_point[0], exterior_point[1], 'ro', markersize=8,
                   label='Exterior point')

    axes[1, 1].set_xlim(-2, 2)
    axes[1, 1].set_ylim(-2, 2)
    axes[1, 1].set_aspect('equal')
    axes[1, 1].set_xlabel('x', fontsize=12)
    axes[1, 1].set_ylabel('y', fontsize=12)
    axes[1, 1].set_title('Interior, Boundary, and Exterior',
                        fontsize=14, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend()

    plt.tight_layout()
    plt.savefig('../../outputs/07_open_closed_sets.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/07_open_closed_sets.png")
    plt.close()

def continuity():
    """連続性"""
    print("\n" + "=" * 50)
    print("6. 連続性")
    print("=" * 50)

    print("連続関数: lim(x→a) f(x) = f(a)")
    print("  すべての点で極限値と関数値が一致")

    print("\n不連続関数の例:")
    print("  1. ジャンプ不連続（階段関数）")
    print("  2. 除去可能不連続")
    print("  3. 無限不連続")

    # 可視化
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    x = np.linspace(-3, 3, 1000)

    # 連続関数
    y_cont = x**2
    axes[0, 0].plot(x, y_cont, 'b-', linewidth=2)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_xlabel('x', fontsize=12)
    axes[0, 0].set_ylabel('f(x)', fontsize=12)
    axes[0, 0].set_title('Continuous: f(x) = x²', fontsize=14, fontweight='bold')

    # ジャンプ不連続（階段関数）
    x1 = np.linspace(-3, 0, 500)
    x2 = np.linspace(0, 3, 500)
    y1 = np.ones_like(x1) * (-1)
    y2 = np.ones_like(x2)

    axes[0, 1].plot(x1, y1, 'b-', linewidth=2)
    axes[0, 1].plot(x2, y2, 'b-', linewidth=2)
    axes[0, 1].plot(0, -1, 'bo', markersize=8)  # 左からの極限
    axes[0, 1].plot(0, 1, 'bo', markersize=8, markerfacecolor='white',
                   markeredgewidth=2)  # 右からの極限
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_xlabel('x', fontsize=12)
    axes[0, 1].set_ylabel('f(x)', fontsize=12)
    axes[0, 1].set_title('Jump Discontinuity (Heaviside)', fontsize=14, fontweight='bold')
    axes[0, 1].set_ylim(-2, 2)

    # 除去可能不連続
    x_removable = x[x != 0]
    y_removable = np.sin(x_removable) / x_removable
    axes[1, 0].plot(x_removable, y_removable, 'b-', linewidth=2)
    axes[1, 0].plot(0, 1, 'ro', markersize=8, markerfacecolor='white',
                   markeredgewidth=2, label='Removable')
    axes[1, 0].plot(0, 0, 'go', markersize=8, label='Actual value')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_xlabel('x', fontsize=12)
    axes[1, 0].set_ylabel('f(x)', fontsize=12)
    axes[1, 0].set_title('Removable Discontinuity: f(x) = sin(x)/x, f(0) = 0',
                        fontsize=14, fontweight='bold')
    axes[1, 0].legend()
    axes[1, 0].set_ylim(-0.5, 1.5)

    # 無限不連続
    x_inf1 = np.linspace(-3, -0.01, 500)
    x_inf2 = np.linspace(0.01, 3, 500)
    y_inf1 = 1 / x_inf1
    y_inf2 = 1 / x_inf2

    axes[1, 1].plot(x_inf1, y_inf1, 'b-', linewidth=2)
    axes[1, 1].plot(x_inf2, y_inf2, 'b-', linewidth=2)
    axes[1, 1].axvline(x=0, color='r', linestyle='--', linewidth=2,
                      label='Asymptote x=0')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].set_xlabel('x', fontsize=12)
    axes[1, 1].set_ylabel('f(x)', fontsize=12)
    axes[1, 1].set_title('Infinite Discontinuity: f(x) = 1/x',
                        fontsize=14, fontweight='bold')
    axes[1, 1].set_ylim(-10, 10)
    axes[1, 1].legend()

    plt.tight_layout()
    plt.savefig('../../outputs/07_continuity.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/07_continuity.png")
    plt.close()

def main():
    """メイン実行関数"""
    print("\n" + "=" * 50)
    print("Python数学学習: レッスン7 - 集合と位相")
    print("=" * 50 + "\n")

    set_operations()
    venn_diagrams()
    functions_mappings()
    metric_spaces()
    open_closed_sets()
    continuity()

    print("\n" + "=" * 50)
    print("レッスン7 完了!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
