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

def vector_space_concepts():
    """ベクトル空間の詳細な概念"""
    print("\n" + "=" * 50)
    print("7. ベクトル空間の詳細")
    print("=" * 50)

    print("ベクトル空間 (Vector Space) の定義:")
    print("体F上のベクトル空間Vは、以下を満たす集合:")
    print("\n【加法に関する性質】")
    print("1. 閉性: u, v ∈ V ⇒ u + v ∈ V")
    print("2. 結合律: (u + v) + w = u + (v + w)")
    print("3. 零ベクトルの存在: ∃0 ∈ V s.t. v + 0 = v")
    print("4. 逆元の存在: ∀v ∈ V, ∃(-v) ∈ V s.t. v + (-v) = 0")
    print("5. 交換律: u + v = v + u")

    print("\n【スカラー倍に関する性質】")
    print("6. 閉性: c ∈ F, v ∈ V ⇒ cv ∈ V")
    print("7. 分配律(1): c(u + v) = cu + cv")
    print("8. 分配律(2): (c + d)v = cv + dv")
    print("9. 結合律: c(dv) = (cd)v")
    print("10. 単位元: 1v = v")

    # 例: R^2 のベクトル空間
    print("\n" + "=" * 50)
    print("例: R²のベクトル空間")
    print("=" * 50)

    v1 = np.array([2, 3])
    v2 = np.array([1, -1])
    c1, c2 = 2, -1.5

    print(f"v1 = {v1}, v2 = {v2}")
    print(f"スカラー: c1 = {c1}, c2 = {c2}")

    print(f"\n閉性の確認:")
    print(f"v1 + v2 = {v1 + v2} ∈ R²")
    print(f"c1 × v1 = {c1 * v1} ∈ R²")

    print(f"\n分配律の確認:")
    print(f"c1(v1 + v2) = {c1 * (v1 + v2)}")
    print(f"c1×v1 + c1×v2 = {c1 * v1 + c1 * v2}")

    print("\n" + "=" * 50)
    print("部分空間 (Subspace)")
    print("=" * 50)

    print("部分空間: ベクトル空間Vの部分集合Wで、以下を満たすもの:")
    print("1. 0 ∈ W (零ベクトルを含む)")
    print("2. u, v ∈ W ⇒ u + v ∈ W (加法について閉じている)")
    print("3. c ∈ F, v ∈ W ⇒ cv ∈ W (スカラー倍について閉じている)")

    # R^3の部分空間の例
    print("\n例: R³の部分空間 - xy平面")
    print("W = {(x, y, 0) | x, y ∈ R}")

    w1 = np.array([1, 2, 0])
    w2 = np.array([3, -1, 0])
    c = 2.5

    print(f"\nw1 = {w1}, w2 = {w2}")
    print(f"w1 + w2 = {w1 + w2} ∈ W (z成分が0)")
    print(f"{c} × w1 = {c * w1} ∈ W (z成分が0)")

    # 可視化
    fig = plt.figure(figsize=(14, 6))

    # 2Dベクトル空間
    ax1 = fig.add_subplot(121)

    # いくつかのベクトルをプロット
    vectors_2d = [
        ([2, 3], 'blue', 'v1'),
        ([1, -1], 'red', 'v2'),
        ([3, 2], 'green', 'v1+v2'),
        ([4, 6], 'purple', '2v1'),
    ]

    for vec, color, label in vectors_2d:
        ax1.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy', scale=1,
                  color=color, width=0.008, label=label, alpha=0.7)

    ax1.set_xlim(-2, 6)
    ax1.set_ylim(-3, 7)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax1.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('y', fontsize=12)
    ax1.set_title('Vector Space R²', fontsize=14, fontweight='bold')
    ax1.legend()

    # 3D部分空間
    ax2 = fig.add_subplot(122, projection='3d')

    # xy平面（部分空間）
    xx, yy = np.meshgrid(np.linspace(-3, 3, 10), np.linspace(-3, 3, 10))
    zz = np.zeros_like(xx)
    ax2.plot_surface(xx, yy, zz, alpha=0.3, color='cyan')

    # 部分空間内のベクトル
    vectors_3d = [
        ([2, 1, 0], 'blue'),
        ([1, 3, 0], 'red'),
        ([3, 4, 0], 'green'),
    ]

    for vec, color in vectors_3d:
        ax2.quiver(0, 0, 0, vec[0], vec[1], vec[2],
                  color=color, arrow_length_ratio=0.15, linewidth=2)

    # 部分空間外のベクトル（比較用）
    ax2.quiver(0, 0, 0, 1, 1, 2, color='orange',
              arrow_length_ratio=0.15, linewidth=2, linestyle='--')

    ax2.set_xlabel('x', fontsize=10)
    ax2.set_ylabel('y', fontsize=10)
    ax2.set_zlabel('z', fontsize=10)
    ax2.set_title('Subspace: xy-plane in R³', fontsize=14, fontweight='bold')
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-3, 3)
    ax2.set_zlim(-3, 3)

    plt.tight_layout()
    plt.savefig('../../outputs/05_vector_space.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/05_vector_space.png")
    plt.close()

    # 基底と次元
    print("\n" + "=" * 50)
    print("基底 (Basis) と次元 (Dimension)")
    print("=" * 50)

    print("基底: ベクトル空間Vの線形独立なベクトルの集合で、")
    print("      Vの任意のベクトルを線形結合で表現できるもの")

    print("\n次元: 基底のベクトルの個数")

    print("\n例: R²の標準基底")
    e1 = np.array([1, 0])
    e2 = np.array([0, 1])
    print(f"e1 = {e1}, e2 = {e2}")
    print("任意のベクトルv = [x, y]は v = x×e1 + y×e2 と表現できる")

    v = np.array([3, 5])
    print(f"\nv = {v} = {v[0]}×{e1} + {v[1]}×{e2}")

    print(f"\nR²の次元: dim(R²) = 2")

def linear_maps_detailed():
    """線形写像の詳細"""
    print("\n" + "=" * 50)
    print("8. 線形写像の詳細")
    print("=" * 50)

    print("線形写像 (Linear Map) の定義:")
    print("写像 T: V → W が線形写像 ⟺ 以下を満たす:")
    print("1. T(u + v) = T(u) + T(v) (加法の保存)")
    print("2. T(cv) = cT(v) (スカラー倍の保存)")

    print("\n" + "=" * 50)
    print("線形写像の例")
    print("=" * 50)

    # 例1: 回転
    theta = np.pi / 4  # 45度
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])

    print(f"例1: 回転変換 (45度)")
    print(f"行列表現:\n{R}")

    v1 = np.array([2, 0])
    v2 = np.array([0, 2])

    print(f"\nv1 = {v1}")
    print(f"T(v1) = {R @ v1}")

    print(f"\nv2 = {v2}")
    print(f"T(v2) = {R @ v2}")

    # 線形性の確認
    print(f"\n線形性の確認:")
    print(f"T(v1 + v2) = {R @ (v1 + v2)}")
    print(f"T(v1) + T(v2) = {R @ v1 + R @ v2}")
    print(f"一致: {np.allclose(R @ (v1 + v2), R @ v1 + R @ v2)}")

    print("\n" + "=" * 50)
    print("核 (Kernel) と像 (Image)")
    print("=" * 50)

    print("核 (Ker(T)): T(v) = 0 となるvの集合")
    print("像 (Im(T)): Tによって写される全てのベクトルの集合")

    print("\n階数定理 (Rank-Nullity Theorem):")
    print("dim(V) = dim(Ker(T)) + dim(Im(T))")
    print("       = nullity(T) + rank(T)")

    # 例: 射影
    print("\n例: R³ → R² への射影")
    P = np.array([[1, 0, 0],
                  [0, 1, 0]])

    print(f"射影行列:\n{P}")

    v3d = np.array([2, 3, 4])
    print(f"\nv = {v3d}")
    print(f"P(v) = {P @ v3d}")

    print(f"\n核: Ker(P) = {{[0, 0, z] | z ∈ R}} (z軸)")
    print(f"次元: dim(Ker(P)) = 1")

    print(f"\n像: Im(P) = R² (xy平面)")
    print(f"次元: dim(Im(P)) = 2")

    print(f"\n階数定理の確認: dim(R³) = 3 = 1 + 2 ✓")

    # 可視化
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 回転変換
    x = np.linspace(-3, 3, 20)
    y = np.linspace(-3, 3, 20)
    X, Y = np.meshgrid(x, y)

    # 元のグリッド
    for i in range(len(x)):
        axes[0].plot(X[i, :], Y[i, :], 'b-', alpha=0.3, linewidth=0.5)
        axes[0].plot(X[:, i], Y[:, i], 'b-', alpha=0.3, linewidth=0.5)

    # 変換後のグリッド
    for i in range(len(x)):
        row_transformed = R @ np.vstack([X[i, :], Y[i, :]])
        col_transformed = R @ np.vstack([X[:, i], Y[:, i]])
        axes[0].plot(row_transformed[0], row_transformed[1], 'r-', alpha=0.3, linewidth=0.5)
        axes[0].plot(col_transformed[0], col_transformed[1], 'r-', alpha=0.3, linewidth=0.5)

    # 基底ベクトル
    e1 = np.array([1, 0])
    e2 = np.array([0, 1])
    axes[0].quiver(0, 0, e1[0], e1[1], angles='xy', scale_units='xy', scale=1,
                  color='blue', width=0.01, label='Original basis')
    axes[0].quiver(0, 0, e2[0], e2[1], angles='xy', scale_units='xy', scale=1,
                  color='blue', width=0.01)

    Re1 = R @ e1
    Re2 = R @ e2
    axes[0].quiver(0, 0, Re1[0], Re1[1], angles='xy', scale_units='xy', scale=1,
                  color='red', width=0.015, label='Transformed basis')
    axes[0].quiver(0, 0, Re2[0], Re2[1], angles='xy', scale_units='xy', scale=1,
                  color='red', width=0.015)

    axes[0].set_xlim(-4, 4)
    axes[0].set_ylim(-4, 4)
    axes[0].set_aspect('equal')
    axes[0].grid(True, alpha=0.3)
    axes[0].set_title('Linear Map: Rotation (45°)', fontsize=14, fontweight='bold')
    axes[0].legend()

    # 同型写像と準同型写像
    axes[1].text(0.5, 0.95, 'Linear Map Properties', ha='center',
                fontsize=14, fontweight='bold', transform=axes[1].transAxes)

    properties = [
        "単射 (Injective / One-to-one):",
        "  T(u) = T(v) ⇒ u = v",
        "  ⟺ Ker(T) = {0}",
        "",
        "全射 (Surjective / Onto):",
        "  Im(T) = W",
        "  任意のw ∈ Wに対して、T(v) = w となるv ∈ Vが存在",
        "",
        "全単射 (Bijective):",
        "  単射 かつ 全射",
        "  ⟺ 同型写像 (Isomorphism)",
        "  ⟺ 可逆 (Invertible)",
        "",
        "準同型写像 (Homomorphism):",
        "  代数構造を保存する線形写像",
    ]

    for i, text in enumerate(properties):
        axes[1].text(0.1, 0.85 - i*0.05, text, fontsize=9,
                    transform=axes[1].transAxes, verticalalignment='top',
                    family='monospace')

    axes[1].axis('off')

    plt.tight_layout()
    plt.savefig('../../outputs/05_linear_maps.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/05_linear_maps.png")
    plt.close()

def practical_deep_learning():
    """実務応用: Deep Learning"""
    print("\n" + "=" * 50)
    print("9. 実務応用: Deep Learning での線形代数")
    print("=" * 50)

    print("ニューラルネットワークは線形代数の応用の宝庫:")

    print("\n【1. 全結合層 (Dense Layer)】")
    print("y = Wx + b")
    print("  W: 重み行列 (線形変換)")
    print("  x: 入力ベクトル")
    print("  b: バイアスベクトル (平行移動)")

    # 簡単なニューラルネットワークの例
    print("\n例: 2層ニューラルネットワーク")

    # 入力
    x = np.array([[1], [2], [3]])  # 3次元入力
    print(f"入力 x (3次元):\n{x.T}")

    # 第1層: 3 → 4
    W1 = np.random.randn(4, 3) * 0.5
    b1 = np.random.randn(4, 1) * 0.1
    z1 = W1 @ x + b1
    a1 = np.maximum(0, z1)  # ReLU活性化
    print(f"\n第1層出力 (4次元):\n{a1.T}")

    # 第2層: 4 → 2
    W2 = np.random.randn(2, 4) * 0.5
    b2 = np.random.randn(2, 1) * 0.1
    z2 = W2 @ a1 + b2
    output = 1 / (1 + np.exp(-z2))  # Sigmoid活性化
    print(f"\n第2層出力 (2次元):\n{output.T}")

    print("\n【2. バッチ処理】")
    print("行列の各列が1つのサンプルを表現")
    print("X: (features × batch_size)")
    print("Y = WX + B (複数サンプルを同時に処理)")

    batch_size = 5
    X_batch = np.random.randn(3, batch_size)
    Y_batch = W1 @ X_batch + b1
    print(f"\nバッチ入力形状: {X_batch.shape}")
    print(f"バッチ出力形状: {Y_batch.shape}")

    print("\n【3. 注意機構 (Attention Mechanism)】")
    print("Transformer等で使用される重要な概念")
    print("Attention(Q, K, V) = softmax(QK^T/√d_k)V")
    print("  Q: Query行列")
    print("  K: Key行列")
    print("  V: Value行列")

    # 簡易的な注意機構
    d_k = 4
    seq_len = 3

    Q = np.random.randn(seq_len, d_k)
    K = np.random.randn(seq_len, d_k)
    V = np.random.randn(seq_len, d_k)

    # 注意スコアの計算
    scores = Q @ K.T / np.sqrt(d_k)
    attention_weights = np.exp(scores) / np.exp(scores).sum(axis=1, keepdims=True)
    attention_output = attention_weights @ V

    print(f"\nQuery形状: {Q.shape}")
    print(f"注意重み形状: {attention_weights.shape}")
    print(f"出力形状: {attention_output.shape}")

    print("\n【4. 埋め込み (Embeddings)】")
    print("単語やトークンを高次元ベクトル空間に埋め込む")
    print("線形代数の観点: ベクトル空間内での意味の表現")

    # Word2Vec風の例
    vocab_size = 1000
    embedding_dim = 128
    E = np.random.randn(vocab_size, embedding_dim) * 0.01

    word_id = 42
    word_vector = E[word_id]
    print(f"\n語彙サイズ: {vocab_size}")
    print(f"埋め込み次元: {embedding_dim}")
    print(f"単語ベクトル形状: {word_vector.shape}")

    # コサイン類似度
    word_id2 = 100
    word_vector2 = E[word_id2]
    cosine_sim = np.dot(word_vector, word_vector2) / (
        np.linalg.norm(word_vector) * np.linalg.norm(word_vector2)
    )
    print(f"\n単語{word_id}と単語{word_id2}のコサイン類似度: {cosine_sim:.4f}")

    # 可視化
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # ニューラルネットワーク構造
    axes[0, 0].text(0.5, 0.95, 'Neural Network Architecture',
                   ha='center', fontsize=12, fontweight='bold',
                   transform=axes[0, 0].transAxes)

    layer_info = [
        "Input Layer (3)",
        "  ↓ W1 (4×3), b1 (4×1)",
        "Hidden Layer (4)",
        "  ↓ ReLU",
        "  ↓ W2 (2×4), b2 (2×1)",
        "Output Layer (2)",
        "  ↓ Sigmoid",
        "",
        "Total params:",
        f"  W1: {W1.size}",
        f"  b1: {b1.size}",
        f"  W2: {W2.size}",
        f"  b2: {b2.size}",
        f"  Total: {W1.size + b1.size + W2.size + b2.size}"
    ]

    for i, text in enumerate(layer_info):
        axes[0, 0].text(0.1, 0.85 - i*0.055, text, fontsize=9,
                       transform=axes[0, 0].transAxes, verticalalignment='top',
                       family='monospace')
    axes[0, 0].axis('off')

    # 注意機構の重み
    im = axes[0, 1].imshow(attention_weights, cmap='viridis', aspect='auto')
    axes[0, 1].set_xlabel('Key Position', fontsize=10)
    axes[0, 1].set_ylabel('Query Position', fontsize=10)
    axes[0, 1].set_title('Attention Weights', fontsize=12, fontweight='bold')
    plt.colorbar(im, ax=axes[0, 1])

    # 埋め込み空間の2D投影（t-SNEやPCAの代わりに簡易版）
    # ランダムな単語のサンプル
    n_words = 50
    sample_embeddings = E[:n_words, :2]  # 最初の2次元のみ使用

    axes[1, 0].scatter(sample_embeddings[:, 0], sample_embeddings[:, 1],
                      alpha=0.6, s=50)
    for i in range(min(10, n_words)):
        axes[1, 0].annotate(f'w{i}', xy=sample_embeddings[i],
                           xytext=(5, 5), textcoords='offset points',
                           fontsize=8, alpha=0.7)
    axes[1, 0].set_xlabel('Dimension 1', fontsize=10)
    axes[1, 0].set_ylabel('Dimension 2', fontsize=10)
    axes[1, 0].set_title('Word Embeddings (2D projection)',
                        fontsize=12, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)

    # 応用まとめ
    axes[1, 1].text(0.5, 0.95, 'Key Linear Algebra Applications in DL',
                   ha='center', fontsize=11, fontweight='bold',
                   transform=axes[1, 1].transAxes)

    applications = [
        "1. 行列積:",
        "   - 全結合層の計算",
        "   - バッチ処理",
        "",
        "2. 固有値・固有ベクトル:",
        "   - PCA (特徴量削減)",
        "   - スペクトル正規化",
        "",
        "3. SVD:",
        "   - 行列分解",
        "   - 推薦システム",
        "",
        "4. ノルム:",
        "   - L2正則化",
        "   - 勾配クリッピング",
        "",
        "5. 内積・コサイン類似度:",
        "   - 注意機構",
        "   - 類似度計算",
    ]

    for i, text in enumerate(applications):
        axes[1, 1].text(0.05, 0.88 - i*0.04, text, fontsize=8,
                       transform=axes[1, 1].transAxes, verticalalignment='top')
    axes[1, 1].axis('off')

    plt.tight_layout()
    plt.savefig('../../outputs/05_deep_learning.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/05_deep_learning.png")
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
    vector_space_concepts()
    linear_maps_detailed()
    practical_deep_learning()

    print("\n" + "=" * 50)
    print("レッスン5 完了!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
