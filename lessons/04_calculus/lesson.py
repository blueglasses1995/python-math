"""
レッスン4: 微分
Calculus - Differentiation

このレッスンでは以下を学びます：
- 数値微分
- 記号微分（SymPy）
- 導関数の幾何的意味
- 偏微分
- 勾配とヘッセ行列
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import matplotlib
matplotlib.use('Agg')

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def numerical_derivative():
    """数値微分"""
    print("=" * 50)
    print("1. 数値微分")
    print("=" * 50)

    def f(x):
        return x**2

    def df_analytical(x):
        """解析的な導関数"""
        return 2*x

    def df_numerical(f, x, h=1e-5):
        """数値微分（前進差分）"""
        return (f(x + h) - f(x)) / h

    def df_central(f, x, h=1e-5):
        """中心差分"""
        return (f(x + h) - f(x - h)) / (2*h)

    x = 2.0
    print(f"関数: f(x) = x²")
    print(f"点: x = {x}")
    print(f"\n解析的導関数: f'({x}) = {df_analytical(x)}")
    print(f"数値微分(前進): f'({x}) = {df_numerical(f, x):.10f}")
    print(f"数値微分(中心): f'({x}) = {df_central(f, x):.10f}")

    # 精度の比較
    h_values = np.logspace(-10, -1, 50)
    errors_forward = []
    errors_central = []

    true_derivative = df_analytical(x)

    for h in h_values:
        error_f = abs(df_numerical(f, x, h) - true_derivative)
        error_c = abs(df_central(f, x, h) - true_derivative)
        errors_forward.append(error_f)
        errors_central.append(error_c)

    # 精度比較のグラフ
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(h_values, errors_forward, 'b-', linewidth=2, label='Forward difference')
    ax.loglog(h_values, errors_central, 'r-', linewidth=2, label='Central difference')
    ax.grid(True, alpha=0.3, which='both')
    ax.set_xlabel('Step size (h)', fontsize=12)
    ax.set_ylabel('Absolute error', fontsize=12)
    ax.set_title('Numerical Differentiation Error vs Step Size', fontsize=14, fontweight='bold')
    ax.legend()
    plt.savefig('../../outputs/04_numerical_derivative_error.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/04_numerical_derivative_error.png")
    plt.close()

def symbolic_differentiation():
    """記号微分（SymPy）"""
    print("\n" + "=" * 50)
    print("2. 記号微分（SymPy）")
    print("=" * 50)

    x = sp.Symbol('x')

    # 様々な関数の微分
    functions = [
        x**2,
        x**3 + 2*x**2 - 5*x + 3,
        sp.sin(x),
        sp.cos(x),
        sp.exp(x),
        sp.log(x),
        x * sp.sin(x),
        sp.sin(x) / x,
        sp.exp(x**2)
    ]

    print(f"{'関数 f(x)':^30} | {'導関数 f\'(x)':^30} | {'二階導関数 f\'\'(x)':^30}")
    print("-" * 95)

    for func in functions:
        df = sp.diff(func, x)
        ddf = sp.diff(func, x, 2)
        print(f"{str(func):^30} | {str(df):^30} | {str(ddf):^30}")

    # 特定の点での微分値
    print("\n" + "=" * 50)
    print("特定の点での導関数の値")
    print("=" * 50)

    f = x**3 - 3*x**2 + 2*x + 1
    df = sp.diff(f, x)

    x_vals = [-1, 0, 1, 2, 3]
    print(f"関数: f(x) = {f}")
    print(f"導関数: f'(x) = {df}")
    print(f"\n{'x':>5} {'f(x)':>15} {'f\'(x)':>15}")
    print("-" * 40)

    for x_val in x_vals:
        f_val = float(f.subs(x, x_val))
        df_val = float(df.subs(x, x_val))
        print(f"{x_val:>5} {f_val:>15.4f} {df_val:>15.4f}")

def geometric_interpretation():
    """導関数の幾何的意味"""
    print("\n" + "=" * 50)
    print("3. 導関数の幾何的意味（接線）")
    print("=" * 50)

    def f(x):
        return 0.5*x**3 - 2*x**2 + x + 2

    def df(x):
        return 1.5*x**2 - 4*x + 1

    x = np.linspace(-1, 4, 1000)
    y = f(x)

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    # 元の関数とその導関数
    axes[0, 0].plot(x, y, 'b-', linewidth=2, label='f(x)')
    axes[0, 0].plot(x, df(x), 'r-', linewidth=2, label="f'(x)")
    axes[0, 0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_xlabel('x', fontsize=12)
    axes[0, 0].set_ylabel('y', fontsize=12)
    axes[0, 0].set_title('Function and its Derivative', fontsize=14, fontweight='bold')
    axes[0, 0].legend()

    # 接線の可視化
    x_points = [0, 1, 2, 3]
    for x_point in x_points:
        y_point = f(x_point)
        slope = df(x_point)
        # 接線: y - y0 = m(x - x0)
        tangent_x = np.linspace(x_point - 0.5, x_point + 0.5, 100)
        tangent_y = slope * (tangent_x - x_point) + y_point

        axes[0, 1].plot(tangent_x, tangent_y, '--', linewidth=1.5,
                       label=f'x={x_point}, slope={slope:.2f}')
        axes[0, 1].plot(x_point, y_point, 'ro', markersize=8)

    axes[0, 1].plot(x, y, 'b-', linewidth=2, label='f(x)')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_xlabel('x', fontsize=12)
    axes[0, 1].set_ylabel('y', fontsize=12)
    axes[0, 1].set_title('Tangent Lines at Various Points', fontsize=14, fontweight='bold')
    axes[0, 1].legend()

    # 極値の検出
    # f'(x) = 0 となる点を求める
    x_sym = sp.Symbol('x')
    f_sym = 0.5*x_sym**3 - 2*x_sym**2 + x_sym + 2
    df_sym = sp.diff(f_sym, x_sym)
    critical_points = sp.solve(df_sym, x_sym)

    axes[1, 0].plot(x, y, 'b-', linewidth=2)
    for cp in critical_points:
        cp_float = float(cp)
        if -1 <= cp_float <= 4:
            axes[1, 0].plot(cp_float, f(cp_float), 'ro', markersize=10,
                          label=f'Critical point: x={cp_float:.3f}')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_xlabel('x', fontsize=12)
    axes[1, 0].set_ylabel('y', fontsize=12)
    axes[1, 0].set_title("Critical Points (f'(x) = 0)", fontsize=14, fontweight='bold')
    axes[1, 0].legend()

    print(f"臨界点（f'(x) = 0）: {[float(cp) for cp in critical_points]}")

    # 凸性（二階導関数）
    def ddf(x):
        return 3*x - 4

    axes[1, 1].plot(x, y, 'b-', linewidth=2, label='f(x)')
    axes[1, 1].plot(x, ddf(x), 'g-', linewidth=2, label="f''(x)")
    axes[1, 1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[1, 1].fill_between(x, 0, ddf(x), where=(ddf(x) > 0),
                           alpha=0.3, color='green', label='Concave up')
    axes[1, 1].fill_between(x, 0, ddf(x), where=(ddf(x) < 0),
                           alpha=0.3, color='red', label='Concave down')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].set_xlabel('x', fontsize=12)
    axes[1, 1].set_ylabel('y', fontsize=12)
    axes[1, 1].set_title('Second Derivative and Concavity', fontsize=14, fontweight='bold')
    axes[1, 1].legend()

    plt.tight_layout()
    plt.savefig('../../outputs/04_geometric_interpretation.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/04_geometric_interpretation.png")
    plt.close()

def partial_derivatives():
    """偏微分"""
    print("\n" + "=" * 50)
    print("4. 偏微分")
    print("=" * 50)

    x, y = sp.symbols('x y')

    # 多変数関数
    f = x**2 + y**2
    print(f"関数: f(x, y) = {f}")
    print(f"∂f/∂x = {sp.diff(f, x)}")
    print(f"∂f/∂y = {sp.diff(f, y)}")

    f2 = x*y**2 + sp.sin(x) + sp.exp(y)
    print(f"\n関数: f(x, y) = {f2}")
    print(f"∂f/∂x = {sp.diff(f2, x)}")
    print(f"∂f/∂y = {sp.diff(f2, y)}")

    # 二階偏微分
    print("\n" + "=" * 50)
    print("二階偏微分")
    print("=" * 50)

    f3 = x**3 * y**2 - 2*x*y + 3*y**2
    print(f"関数: f(x, y) = {f3}")
    print(f"∂²f/∂x² = {sp.diff(f3, x, 2)}")
    print(f"∂²f/∂y² = {sp.diff(f3, y, 2)}")
    print(f"∂²f/∂x∂y = {sp.diff(sp.diff(f3, x), y)}")
    print(f"∂²f/∂y∂x = {sp.diff(sp.diff(f3, y), x)}")

def gradient_visualization():
    """勾配の可視化"""
    print("\n" + "=" * 50)
    print("5. 勾配ベクトルの可視化")
    print("=" * 50)

    # 2D 関数の勾配
    def f(x, y):
        return x**2 + y**2

    def gradient_f(x, y):
        df_dx = 2*x
        df_dy = 2*y
        return df_dx, df_dy

    # メッシュグリッド
    x = np.linspace(-3, 3, 20)
    y = np.linspace(-3, 3, 20)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # 勾配
    U, V = gradient_f(X, Y)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 等高線と勾配ベクトル
    contour = axes[0].contour(X, Y, Z, levels=15, cmap='viridis')
    axes[0].clabel(contour, inline=True, fontsize=8)
    axes[0].quiver(X, Y, U, V, alpha=0.6, color='red')
    axes[0].set_xlabel('x', fontsize=12)
    axes[0].set_ylabel('y', fontsize=12)
    axes[0].set_title('Gradient Vectors: f(x,y) = x² + y²', fontsize=14, fontweight='bold')
    axes[0].set_aspect('equal')
    axes[0].grid(True, alpha=0.3)

    # 3D 表示
    from mpl_toolkits.mplot3d import Axes3D
    ax = fig.add_subplot(122, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_zlabel('f(x, y)', fontsize=12)
    ax.set_title('3D Surface', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('../../outputs/04_gradient.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/04_gradient.png")
    plt.close()

    # サドル点の例
    def f_saddle(x, y):
        return x**2 - y**2

    def gradient_f_saddle(x, y):
        return 2*x, -2*y

    Z_saddle = f_saddle(X, Y)
    U_saddle, V_saddle = gradient_f_saddle(X, Y)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    contour = axes[0].contour(X, Y, Z_saddle, levels=20, cmap='RdBu')
    axes[0].clabel(contour, inline=True, fontsize=8)
    axes[0].quiver(X, Y, U_saddle, V_saddle, alpha=0.6, color='black')
    axes[0].plot(0, 0, 'ro', markersize=10, label='Saddle point')
    axes[0].set_xlabel('x', fontsize=12)
    axes[0].set_ylabel('y', fontsize=12)
    axes[0].set_title('Gradient Vectors: f(x,y) = x² - y² (Saddle)', fontsize=14, fontweight='bold')
    axes[0].set_aspect('equal')
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()

    ax = fig.add_subplot(122, projection='3d')
    ax.plot_surface(X, Y, Z_saddle, cmap='RdBu', alpha=0.8)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_zlabel('f(x, y)', fontsize=12)
    ax.set_title('3D Surface (Saddle Point)', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('../../outputs/04_saddle_point.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/04_saddle_point.png")
    plt.close()

def main():
    """メイン実行関数"""
    print("\n" + "=" * 50)
    print("Python数学学習: レッスン4 - 微分")
    print("=" * 50 + "\n")

    numerical_derivative()
    symbolic_differentiation()
    geometric_interpretation()
    partial_derivatives()
    gradient_visualization()

    print("\n" + "=" * 50)
    print("レッスン4 完了!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
