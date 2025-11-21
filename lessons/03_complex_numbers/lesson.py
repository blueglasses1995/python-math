"""
レッスン3: 複素数
Complex Numbers

このレッスンでは以下を学びます：
- 複素数の基本（実部・虚部）
- 複素平面（ガウス平面）
- 極形式と指数形式
- オイラーの公式
- 複素数の演算と可視化
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def complex_basics():
    """複素数の基本"""
    print("=" * 50)
    print("1. 複素数の基本")
    print("=" * 50)

    # 複素数の作成
    z1 = 3 + 4j
    z2 = complex(2, -1)
    z3 = 1 + 1j

    print(f"z1 = {z1}")
    print(f"  実部: {z1.real}")
    print(f"  虚部: {z1.imag}")
    print(f"  絶対値: {abs(z1):.4f}")
    print(f"  偏角: {np.angle(z1):.4f} rad = {np.degrees(np.angle(z1)):.2f}°")
    print(f"  共役複素数: {z1.conjugate()}")

    print(f"\nz2 = {z2}")
    print(f"  実部: {z2.real}")
    print(f"  虚部: {z2.imag}")
    print(f"  絶対値: {abs(z2):.4f}")

    print(f"\nz3 = {z3}")
    print(f"  実部: {z3.real}")
    print(f"  虚部: {z3.imag}")

    # 虚数単位
    print(f"\n虚数単位: i² = {1j * 1j}")
    print(f"i³ = {1j**3}")
    print(f"i⁴ = {1j**4}")

def complex_arithmetic():
    """複素数の演算"""
    print("\n" + "=" * 50)
    print("2. 複素数の四則演算")
    print("=" * 50)

    z1 = 3 + 4j
    z2 = 2 - 1j

    print(f"z1 = {z1}")
    print(f"z2 = {z2}\n")

    print(f"加算: z1 + z2 = {z1 + z2}")
    print(f"減算: z1 - z2 = {z1 - z2}")
    print(f"乗算: z1 * z2 = {z1 * z2}")
    print(f"除算: z1 / z2 = {z1 / z2}")
    print(f"累乗: z1² = {z1**2}")
    print(f"平方根: √z1 = {np.sqrt(z1)}")

def plot_complex_plane():
    """複素平面の可視化"""
    print("\n" + "=" * 50)
    print("3. 複素平面（ガウス平面）")
    print("=" * 50)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 複素数のプロット
    complex_numbers = [
        3 + 4j, 2 - 1j, -2 + 3j, -3 - 2j,
        1 + 1j, -1 - 1j, 4 + 0j, 0 + 3j
    ]

    for z in complex_numbers:
        axes[0].plot(z.real, z.imag, 'ro', markersize=10)
        axes[0].arrow(0, 0, z.real, z.imag, head_width=0.2, head_length=0.2,
                     fc='blue', ec='blue', alpha=0.6)
        axes[0].annotate(f'{z.real:+.0f}{z.imag:+.0f}j',
                        xy=(z.real, z.imag),
                        xytext=(z.real + 0.3, z.imag + 0.3),
                        fontsize=9)

    axes[0].axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    axes[0].axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xlabel('Real Part', fontsize=12)
    axes[0].set_ylabel('Imaginary Part', fontsize=12)
    axes[0].set_title('Complex Plane', fontsize=14, fontweight='bold')
    axes[0].set_aspect('equal')
    axes[0].set_xlim(-5, 5)
    axes[0].set_ylim(-5, 5)

    # 単位円上の複素数
    theta = np.linspace(0, 2*np.pi, 100)
    axes[1].plot(np.cos(theta), np.sin(theta), 'b-', linewidth=2, label='Unit circle')

    angles = np.linspace(0, 2*np.pi, 12, endpoint=False)
    for angle in angles:
        z = np.exp(1j * angle)
        axes[1].plot(z.real, z.imag, 'ro', markersize=8)
        axes[1].arrow(0, 0, z.real, z.imag, head_width=0.05, head_length=0.05,
                     fc='red', ec='red', alpha=0.4)
        axes[1].annotate(f'{np.degrees(angle):.0f}°',
                        xy=(z.real, z.imag),
                        xytext=(z.real*1.15, z.imag*1.15),
                        fontsize=8, ha='center')

    axes[1].axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    axes[1].axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    axes[1].grid(True, alpha=0.3)
    axes[1].set_xlabel('Real Part', fontsize=12)
    axes[1].set_ylabel('Imaginary Part', fontsize=12)
    axes[1].set_title('Unit Circle in Complex Plane', fontsize=14, fontweight='bold')
    axes[1].set_aspect('equal')
    axes[1].legend()

    plt.tight_layout()
    plt.savefig('../../outputs/03_complex_plane.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/03_complex_plane.png")
    plt.close()

def polar_form():
    """極形式と指数形式"""
    print("\n" + "=" * 50)
    print("4. 極形式と指数形式")
    print("=" * 50)

    z = 3 + 4j
    r = abs(z)
    theta = np.angle(z)

    print(f"直交形式: z = {z}")
    print(f"極形式:   z = {r:.4f} * (cos({theta:.4f}) + i*sin({theta:.4f}))")
    print(f"指数形式: z = {r:.4f} * e^(i*{theta:.4f})")
    print(f"        = {r:.4f} * e^(i*{np.degrees(theta):.2f}°)")

    # 逆変換の確認
    z_reconstructed = r * np.exp(1j * theta)
    print(f"\n極形式から直交形式への変換: {z_reconstructed}")
    print(f"誤差: {abs(z - z_reconstructed):.2e}")

    # 複数の複素数を極形式で表示
    print("\n" + "-" * 50)
    print(f"{'直交形式':>15} {'絶対値(r)':>12} {'偏角(θ)':>12} {'θ(度)':>10}")
    print("-" * 50)

    complex_nums = [1+0j, 0+1j, -1+0j, 0-1j, 1+1j, -1+1j, -1-1j, 1-1j, 3+4j]
    for z in complex_nums:
        r = abs(z)
        theta = np.angle(z)
        theta_deg = np.degrees(theta)
        print(f"{str(z):>15} {r:>12.4f} {theta:>12.4f} {theta_deg:>10.2f}°")

def eulers_formula():
    """オイラーの公式"""
    print("\n" + "=" * 50)
    print("5. オイラーの公式")
    print("=" * 50)

    print("オイラーの公式: e^(iθ) = cos(θ) + i*sin(θ)")

    angles = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]

    print(f"\n{'θ(rad)':>10} {'θ(度)':>10} {'e^(iθ)':>20} {'cos+i*sin':>20}")
    print("-" * 65)

    for theta in angles:
        exp_form = np.exp(1j * theta)
        trig_form = np.cos(theta) + 1j * np.sin(theta)
        print(f"{theta:>10.4f} {np.degrees(theta):>10.2f}° {exp_form:>20} {trig_form:>20}")

    # オイラーの等式
    print("\n" + "=" * 50)
    print("オイラーの等式: e^(iπ) + 1 = 0")
    print("=" * 50)
    result = np.exp(1j * np.pi) + 1
    print(f"e^(iπ) + 1 = {result}")
    print(f"絶対値: {abs(result):.2e}")

    # 可視化
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # オイラーの公式の可視化
    theta_range = np.linspace(0, 2*np.pi, 100)
    axes[0].plot(np.cos(theta_range), np.sin(theta_range), 'b-', linewidth=2)

    for theta in np.linspace(0, 2*np.pi, 8, endpoint=False):
        z = np.exp(1j * theta)
        axes[0].arrow(0, 0, z.real, z.imag, head_width=0.05, head_length=0.05,
                     fc='red', ec='red', alpha=0.6)
        axes[0].plot(z.real, z.imag, 'ro', markersize=8)

        # cos と sin のコンポーネントを表示
        axes[0].plot([0, z.real], [0, 0], 'g--', alpha=0.5, linewidth=1)
        axes[0].plot([z.real, z.real], [0, z.imag], 'orange', linestyle='--',
                    alpha=0.5, linewidth=1)

    axes[0].axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    axes[0].axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xlabel('Real (cos θ)', fontsize=12)
    axes[0].set_ylabel('Imaginary (sin θ)', fontsize=12)
    axes[0].set_title("Euler's Formula: e^(iθ) = cos(θ) + i*sin(θ)",
                     fontsize=14, fontweight='bold')
    axes[0].set_aspect('equal')

    # 回転の可視化
    z0 = 2 + 1j
    rotations = [np.exp(1j * angle) for angle in np.linspace(0, 2*np.pi, 8)]

    for i, rotation in enumerate(rotations):
        z_rotated = z0 * rotation
        color = plt.cm.rainbow(i / len(rotations))
        axes[1].arrow(0, 0, z_rotated.real, z_rotated.imag,
                     head_width=0.1, head_length=0.1, fc=color, ec=color, alpha=0.7)
        axes[1].plot(z_rotated.real, z_rotated.imag, 'o', color=color, markersize=8)

    axes[1].axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    axes[1].axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    axes[1].grid(True, alpha=0.3)
    axes[1].set_xlabel('Real', fontsize=12)
    axes[1].set_ylabel('Imaginary', fontsize=12)
    axes[1].set_title(f'Rotation using Complex Multiplication (z0 = {z0})',
                     fontsize=14, fontweight='bold')
    axes[1].set_aspect('equal')

    plt.tight_layout()
    plt.savefig('../../outputs/03_eulers_formula.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/03_eulers_formula.png")
    plt.close()

def complex_functions():
    """複素関数の可視化"""
    print("\n" + "=" * 50)
    print("6. 複素関数の可視化")
    print("=" * 50)

    # メッシュグリッドの作成
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j*Y

    fig, axes = plt.subplots(2, 2, figsize=(12, 12))

    # f(z) = z²
    W1 = Z**2
    im1 = axes[0, 0].imshow(np.angle(W1), extent=[-2, 2, -2, 2],
                           cmap='hsv', origin='lower')
    axes[0, 0].set_title('f(z) = z² (Phase)', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('Real', fontsize=12)
    axes[0, 0].set_ylabel('Imaginary', fontsize=12)
    plt.colorbar(im1, ax=axes[0, 0], label='Phase (rad)')

    # f(z) = e^z
    W2 = np.exp(Z)
    im2 = axes[0, 1].imshow(np.abs(W2), extent=[-2, 2, -2, 2],
                           cmap='viridis', origin='lower')
    axes[0, 1].set_title('f(z) = e^z (Magnitude)', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('Real', fontsize=12)
    axes[0, 1].set_ylabel('Imaginary', fontsize=12)
    plt.colorbar(im2, ax=axes[0, 1], label='Magnitude')

    # f(z) = 1/z
    W3 = 1 / (Z + 1e-10)  # ゼロ除算を避ける
    im3 = axes[1, 0].imshow(np.abs(W3), extent=[-2, 2, -2, 2],
                           cmap='plasma', origin='lower', vmax=5)
    axes[1, 0].set_title('f(z) = 1/z (Magnitude)', fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('Real', fontsize=12)
    axes[1, 0].set_ylabel('Imaginary', fontsize=12)
    plt.colorbar(im3, ax=axes[1, 0], label='Magnitude')

    # f(z) = sin(z)
    W4 = np.sin(Z)
    im4 = axes[1, 1].imshow(np.real(W4), extent=[-2, 2, -2, 2],
                           cmap='RdBu', origin='lower')
    axes[1, 1].set_title('f(z) = sin(z) (Real part)', fontsize=14, fontweight='bold')
    axes[1, 1].set_xlabel('Real', fontsize=12)
    axes[1, 1].set_ylabel('Imaginary', fontsize=12)
    plt.colorbar(im4, ax=axes[1, 1], label='Real value')

    plt.tight_layout()
    plt.savefig('../../outputs/03_complex_functions.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/03_complex_functions.png")
    plt.close()

def main():
    """メイン実行関数"""
    print("\n" + "=" * 50)
    print("Python数学学習: レッスン3 - 複素数")
    print("=" * 50 + "\n")

    complex_basics()
    complex_arithmetic()
    plot_complex_plane()
    polar_form()
    eulers_formula()
    complex_functions()

    print("\n" + "=" * 50)
    print("レッスン3 完了!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
