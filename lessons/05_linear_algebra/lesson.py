"""
レッスン5: 線形代数
Linear Algebra

このレッスンでは以下を学びます：
- ベクトルと行列の基本操作
- 行列の演算（積、転置、逆行列）
- 固有値と固有ベクトル
- 線形変換の可視化
- 主成分分析（PCA）の基礎
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def vector_basics():
    """ベクトルの基本"""
    print("=" * 50)
    print("1. ベクトルの基本")
    print("=" * 50)

    # ベクトルの作成
    v1 = np.array([3, 4])
    v2 = np.array([1, 2])

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")

    # ベクトルの操作
    print(f"\nベクトルの加算: v1 + v2 = {v1 + v2}")
    print(f"ベクトルの減算: v1 - v2 = {v1 - v2}")
    print(f"スカラー倍: 2 * v1 = {2 * v1}")

    # ノルム（長さ）
    print(f"\nv1のノルム（長さ）: ||v1|| = {np.linalg.norm(v1):.4f}")
    print(f"v2のノルム（長さ）: ||v2|| = {np.linalg.norm(v2):.4f}")

    # 内積
    dot_product = np.dot(v1, v2)
    print(f"\n内積: v1 · v2 = {dot_product}")

    # 角度
    cos_theta = dot_product / (np.linalg.norm(v1) * np.linalg.norm(v2))
    theta = np.arccos(cos_theta)
    print(f"v1とv2のなす角: {np.degrees(theta):.2f}°")

    # 可視化
    fig, ax = plt.subplots(figsize=(8, 8))

    # ベクトルの描画
    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1,
             color='blue', width=0.01, label='v1')
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1,
             color='red', width=0.01, label='v2')
    ax.quiver(0, 0, (v1+v2)[0], (v1+v2)[1], angles='xy', scale_units='xy', scale=1,
             color='green', width=0.01, label='v1 + v2')

    # ベクトル加算の平行四辺形
    ax.plot([0, v1[0]], [0, v1[1]], 'b--', alpha=0.3)
    ax.plot([v2[0], (v1+v2)[0]], [v2[1], (v1+v2)[1]], 'b--', alpha=0.3)
    ax.plot([v1[0], (v1+v2)[0]], [v1[1], (v1+v2)[1]], 'r--', alpha=0.3)

    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 7)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Vector Operations', fontsize=14, fontweight='bold')
    ax.legend()

    plt.savefig('../../outputs/05_vector_operations.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/05_vector_operations.png")
    plt.close()

def matrix_operations():
    """行列の基本操作"""
    print("\n" + "=" * 50)
    print("2. 行列の基本操作")
    print("=" * 50)

    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("行列 A:")
    print(A)
    print("\n行列 B:")
    print(B)

    # 行列の演算
    print("\n加算 A + B:")
    print(A + B)

    print("\n乗算 A @ B (行列積):")
    print(A @ B)

    print("\n要素ごとの積 A * B:")
    print(A * B)

    print("\n転置 A^T:")
    print(A.T)

    # 逆行列
    A_inv = np.linalg.inv(A)
    print("\n逆行列 A^(-1):")
    print(A_inv)

    print("\nA @ A^(-1) (単位行列になる):")
    print(A @ A_inv)

    # 行列式
    det_A = np.linalg.det(A)
    print(f"\n行列式 det(A) = {det_A:.4f}")

    # トレース
    trace_A = np.trace(A)
    print(f"トレース tr(A) = {trace_A:.4f}")

def linear_transformations():
    """線形変換の可視化"""
    print("\n" + "=" * 50)
    print("3. 線形変換の可視化")
    print("=" * 50)

    # 単位ベクトルと格子点
    def create_grid():
        x = np.linspace(-2, 2, 9)
        y = np.linspace(-2, 2, 9)
        points = []
        for xi in x:
            for yi in y:
                points.append([xi, yi])
        return np.array(points).T

    grid = create_grid()

    # いくつかの線形変換
    transformations = {
        'Identity': np.array([[1, 0], [0, 1]]),
        'Scaling': np.array([[2, 0], [0, 0.5]]),
        'Rotation (45°)': np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
                                     [np.sin(np.pi/4), np.cos(np.pi/4)]]),
        'Shear': np.array([[1, 0.5], [0, 1]]),
        'Reflection': np.array([[1, 0], [0, -1]])
    }

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()

    for idx, (name, T) in enumerate(transformations.items()):
        ax = axes[idx]

        # 元の格子
        ax.scatter(grid[0], grid[1], c='lightblue', s=30, alpha=0.5, label='Original')

        # 変換後の格子
        transformed = T @ grid
        ax.scatter(transformed[0], transformed[1], c='red', s=30, alpha=0.7, label='Transformed')

        # 基底ベクトル
        e1 = np.array([1, 0])
        e2 = np.array([0, 1])
        te1 = T @ e1
        te2 = T @ e2

        ax.quiver(0, 0, e1[0], e1[1], angles='xy', scale_units='xy', scale=1,
                 color='blue', width=0.01, alpha=0.5)
        ax.quiver(0, 0, e2[0], e2[1], angles='xy', scale_units='xy', scale=1,
                 color='green', width=0.01, alpha=0.5)
        ax.quiver(0, 0, te1[0], te1[1], angles='xy', scale_units='xy', scale=1,
                 color='darkblue', width=0.015)
        ax.quiver(0, 0, te2[0], te2[1], angles='xy', scale_units='xy', scale=1,
                 color='darkgreen', width=0.015)

        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
        ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
        ax.set_title(f'{name}\n{T}', fontsize=11, fontweight='bold')
        ax.legend(fontsize=8)

    # 最後のサブプロットを非表示
    axes[-1].axis('off')

    plt.tight_layout()
    plt.savefig('../../outputs/05_linear_transformations.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/05_linear_transformations.png")
    plt.close()

def eigenvalues_eigenvectors():
    """固有値と固有ベクトル"""
    print("\n" + "=" * 50)
    print("4. 固有値と固有ベクトル")
    print("=" * 50)

    A = np.array([[4, 2], [1, 3]])
    print("行列 A:")
    print(A)

    # 固有値と固有ベクトルの計算
    eigenvalues, eigenvectors = np.linalg.eig(A)

    print(f"\n固有値: {eigenvalues}")
    print("\n固有ベクトル:")
    print(eigenvectors)

    # 検証: A * v = λ * v
    print("\n検証:")
    for i in range(len(eigenvalues)):
        v = eigenvectors[:, i]
        lam = eigenvalues[i]
        Av = A @ v
        lam_v = lam * v
        print(f"\n固有値 λ{i+1} = {lam:.4f}")
        print(f"固有ベクトル v{i+1} = {v}")
        print(f"A @ v{i+1} = {Av}")
        print(f"λ{i+1} * v{i+1} = {lam_v}")
        print(f"誤差: {np.linalg.norm(Av - lam_v):.2e}")

    # 可視化
    fig, ax = plt.subplots(figsize=(10, 10))

    # 格子点
    theta = np.linspace(0, 2*np.pi, 20)
    circle = np.array([np.cos(theta), np.sin(theta)])

    # 元の円
    ax.plot(circle[0], circle[1], 'b-', alpha=0.5, linewidth=2, label='Original circle')

    # 変換後の楕円
    transformed = A @ circle
    ax.plot(transformed[0], transformed[1], 'r-', alpha=0.5, linewidth=2, label='Transformed')

    # 固有ベクトルの描画
    colors = ['green', 'purple']
    for i in range(len(eigenvalues)):
        v = eigenvectors[:, i]
        lam = eigenvalues[i]

        # 元のベクトル
        ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1,
                 color=colors[i], width=0.015, alpha=0.5)

        # 変換後のベクトル (λv)
        ax.quiver(0, 0, lam*v[0], lam*v[1], angles='xy', scale_units='xy', scale=1,
                 color=colors[i], width=0.02,
                 label=f'Eigenvector {i+1} (λ={lam:.2f})')

    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Eigenvalues and Eigenvectors', fontsize=14, fontweight='bold')
    ax.legend()

    plt.savefig('../../outputs/05_eigenvalues.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/05_eigenvalues.png")
    plt.close()

def singular_value_decomposition():
    """特異値分解（SVD）"""
    print("\n" + "=" * 50)
    print("5. 特異値分解 (SVD)")
    print("=" * 50)

    A = np.array([[3, 1, 1],
                  [-1, 3, 1]])

    print("行列 A:")
    print(A)
    print(f"形状: {A.shape}")

    # SVD
    U, S, Vt = np.linalg.svd(A)

    print(f"\nU (左特異ベクトル):\n{U}")
    print(f"形状: {U.shape}")

    print(f"\nS (特異値):\n{S}")

    print(f"\nV^T (右特異ベクトルの転置):\n{Vt}")
    print(f"形状: {Vt.shape}")

    # 再構成
    Sigma = np.zeros((A.shape[0], A.shape[1]))
    Sigma[:len(S), :len(S)] = np.diag(S)

    A_reconstructed = U @ Sigma @ Vt
    print(f"\n再構成された行列 A:")
    print(A_reconstructed)
    print(f"再構成誤差: {np.linalg.norm(A - A_reconstructed):.2e}")

def pca_example():
    """主成分分析（PCA）の基礎"""
    print("\n" + "=" * 50)
    print("6. 主成分分析（PCA）")
    print("=" * 50)

    # サンプルデータの生成
    np.random.seed(42)
    mean = [0, 0]
    cov = [[3, 1.5], [1.5, 1]]
    data = np.random.multivariate_normal(mean, cov, 300)

    print(f"データ形状: {data.shape}")
    print(f"平均: {np.mean(data, axis=0)}")
    print(f"共分散行列:\n{np.cov(data.T)}")

    # PCAの実行
    # 1. データの中心化
    data_centered = data - np.mean(data, axis=0)

    # 2. 共分散行列の計算
    cov_matrix = np.cov(data_centered.T)

    # 3. 固有値・固有ベクトルの計算
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # 固有値の降順にソート
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    print(f"\n固有値: {eigenvalues}")
    print(f"寄与率: {eigenvalues / eigenvalues.sum()}")
    print(f"累積寄与率: {np.cumsum(eigenvalues) / eigenvalues.sum()}")

    # 可視化
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 元のデータと主成分
    axes[0].scatter(data[:, 0], data[:, 1], alpha=0.5, s=20)
    axes[0].set_aspect('equal')

    # 主成分の描画
    origin = np.mean(data, axis=0)
    for i in range(2):
        vec = eigenvectors[:, i] * np.sqrt(eigenvalues[i]) * 3
        axes[0].arrow(origin[0], origin[1], vec[0], vec[1],
                     head_width=0.2, head_length=0.2, fc=f'C{i+1}', ec=f'C{i+1}',
                     linewidth=3, label=f'PC{i+1} (λ={eigenvalues[i]:.2f})')

    axes[0].grid(True, alpha=0.3)
    axes[0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[0].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[0].set_xlabel('Feature 1', fontsize=12)
    axes[0].set_ylabel('Feature 2', fontsize=12)
    axes[0].set_title('Original Data with Principal Components', fontsize=14, fontweight='bold')
    axes[0].legend()

    # 主成分空間への射影
    data_pca = data_centered @ eigenvectors
    axes[1].scatter(data_pca[:, 0], data_pca[:, 1], alpha=0.5, s=20)
    axes[1].set_aspect('equal')
    axes[1].grid(True, alpha=0.3)
    axes[1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[1].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    axes[1].set_xlabel('PC1', fontsize=12)
    axes[1].set_ylabel('PC2', fontsize=12)
    axes[1].set_title('Data in Principal Component Space', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('../../outputs/05_pca.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/05_pca.png")
    plt.close()

def main():
    """メイン実行関数"""
    print("\n" + "=" * 50)
    print("Python数学学習: レッスン5 - 線形代数")
    print("=" * 50 + "\n")

    vector_basics()
    matrix_operations()
    linear_transformations()
    eigenvalues_eigenvectors()
    singular_value_decomposition()
    pca_example()

    print("\n" + "=" * 50)
    print("レッスン5 完了!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
