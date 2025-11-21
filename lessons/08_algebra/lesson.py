"""
レッスン8: 代数学
Algebra

このレッスンでは以下を学びます：
- 群論の基礎（群、部分群、準同型）
- 環と体
- 多項式環
- 有限体（ガロア体）
- 実務応用：暗号化、誤り訂正符号
"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import product
import matplotlib
matplotlib.use('Agg')

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def group_theory_basics():
    """群論の基礎"""
    print("=" * 50)
    print("1. 群論の基礎")
    print("=" * 50)

    print("群の定義:")
    print("集合Gと演算*について、以下の4つの公理を満たすとき(G, *)を群という")
    print("1. 閉性: a, b ∈ G ⇒ a * b ∈ G")
    print("2. 結合律: (a * b) * c = a * (b * c)")
    print("3. 単位元の存在: ∃e ∈ G s.t. a * e = e * a = a")
    print("4. 逆元の存在: ∀a ∈ G, ∃a⁻¹ ∈ G s.t. a * a⁻¹ = a⁻¹ * a = e")

    # 例1: 整数の加法群 (Z, +)
    print("\n" + "=" * 50)
    print("例1: 整数の加法群 (Z, +)")
    print("=" * 50)
    print("演算: 加法 (+)")
    print("単位元: 0")
    print("逆元: aの逆元は -a")

    a, b, c = 5, 3, -2
    print(f"\n閉性の確認: {a} + {b} = {a + b} ∈ Z")
    print(f"結合律の確認: ({a} + {b}) + {c} = {(a + b) + c}")
    print(f"               {a} + ({b} + {c}) = {a + (b + c)}")
    print(f"単位元: {a} + 0 = {a + 0}")
    print(f"逆元: {a} + ({-a}) = {a + (-a)}")

    # 例2: 剰余群 Z/nZ
    print("\n" + "=" * 50)
    print("例2: 剰余加法群 (Z/5Z, +)")
    print("=" * 50)

    n = 5
    elements = list(range(n))
    print(f"元: {elements}")
    print(f"演算: 加法 (mod {n})")

    # ケイリー表の作成
    print(f"\nケイリー表（演算表）:")
    print("  + |", " ".join(f"{i:2}" for i in elements))
    print("----+" + "---" * n)
    for i in elements:
        row = [f"{(i + j) % n:2}" for j in elements]
        print(f"{i:2}  |", " ".join(row))

    # 可視化
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # ケイリー表のヒートマップ
    cayley_table = np.array([[(i + j) % n for j in elements] for i in elements])
    im = axes[0].imshow(cayley_table, cmap='viridis', interpolation='nearest')
    axes[0].set_xticks(elements)
    axes[0].set_yticks(elements)
    axes[0].set_xlabel('j', fontsize=12)
    axes[0].set_ylabel('i', fontsize=12)
    axes[0].set_title(f'Cayley Table: (Z/{n}Z, +)', fontsize=14, fontweight='bold')

    # セルに値を表示
    for i in elements:
        for j in elements:
            axes[0].text(j, i, f'{cayley_table[i, j]}',
                        ha='center', va='center', color='white', fontweight='bold')

    plt.colorbar(im, ax=axes[0])

    # 巡回群の可視化
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(theta)
    y = np.sin(theta)

    axes[1].plot(np.cos(np.linspace(0, 2*np.pi, 100)),
                np.sin(np.linspace(0, 2*np.pi, 100)), 'k-', alpha=0.3)

    for i in range(n):
        axes[1].plot(x[i], y[i], 'ro', markersize=15)
        axes[1].annotate(f'{i}', xy=(x[i], y[i]),
                        xytext=(x[i]*1.2, y[i]*1.2),
                        fontsize=14, ha='center', fontweight='bold')

        # 矢印で次の元への移動を示す
        next_i = (i + 1) % n
        axes[1].annotate('', xy=(x[next_i], y[next_i]),
                        xytext=(x[i], y[i]),
                        arrowprops=dict(arrowstyle='->', lw=2, color='blue', alpha=0.6))

    axes[1].set_xlim(-1.5, 1.5)
    axes[1].set_ylim(-1.5, 1.5)
    axes[1].set_aspect('equal')
    axes[1].set_title(f'Cyclic Group Z/{n}Z', fontsize=14, fontweight='bold')
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../../outputs/08_group_theory.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/08_group_theory.png")
    plt.close()

def symmetric_group():
    """対称群"""
    print("\n" + "=" * 50)
    print("2. 対称群 (Symmetric Group)")
    print("=" * 50)

    print("対称群S_n: n個の元の置換全体の集合")
    print("演算: 置換の合成")

    # S_3 の例
    n = 3
    print(f"\nS_{n}の元（置換）:")

    # 置換の表現
    permutations = [
        ([0, 1, 2], "e (恒等置換)"),
        ([1, 0, 2], "(01)"),
        ([0, 2, 1], "(12)"),
        ([2, 1, 0], "(02)"),
        ([1, 2, 0], "(012)"),
        ([2, 0, 1], "(021)")
    ]

    for perm, name in permutations:
        print(f"  {name}: {[0, 1, 2]} → {perm}")

    print(f"\n|S_{n}| = {n}! = {np.math.factorial(n)}")

def rings_and_fields():
    """環と体"""
    print("\n" + "=" * 50)
    print("3. 環と体")
    print("=" * 50)

    print("環 (Ring):")
    print("- 加法について可換群")
    print("- 乗法について半群（結合律）")
    print("- 分配律が成り立つ")

    print("\n体 (Field):")
    print("- 環であって")
    print("- 乗法について（0以外が）可換群")

    print("\n例: 有理数体 Q")
    print("加法と乗法が定義され、体の公理を全て満たす")

    a, b = 2/3, 3/4
    print(f"\n{a} + {b} = {a + b}")
    print(f"{a} × {b} = {a * b}")
    print(f"{a}の加法逆元: {-a}")
    print(f"{a}の乗法逆元: {1/a}")

def polynomial_rings():
    """多項式環"""
    print("\n" + "=" * 50)
    print("4. 多項式環")
    print("=" * 50)

    print("多項式環 R[x]: 係数がRの多項式全体")
    print("演算: 多項式の加法と乗法")

    # NumPyで多項式を扱う
    print("\n例: Z[x]の多項式演算")

    # 多項式 p(x) = x^2 + 2x + 1
    p = np.poly1d([1, 2, 1])
    print(f"\np(x) = {p}")

    # 多項式 q(x) = x - 1
    q = np.poly1d([1, -1])
    print(f"q(x) = {q}")

    # 加法
    print(f"\np(x) + q(x) = {p + q}")

    # 乗法
    print(f"p(x) × q(x) = {p * q}")

    # 除法
    quotient, remainder = np.polydiv(p, q)
    print(f"\np(x) ÷ q(x):")
    print(f"  商: {np.poly1d(quotient)}")
    print(f"  余り: {np.poly1d(remainder)}")

    # 可視化
    x = np.linspace(-3, 3, 1000)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x, p(x), 'b-', linewidth=2, label='p(x) = x² + 2x + 1')
    ax.plot(x, q(x), 'r-', linewidth=2, label='q(x) = x - 1')
    ax.plot(x, (p * q)(x), 'g-', linewidth=2, label='p(x)×q(x)')

    ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='--', alpha=0.3)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Polynomial Ring Operations', fontsize=14, fontweight='bold')
    ax.legend()
    ax.set_ylim(-5, 10)

    plt.savefig('../../outputs/08_polynomial_ring.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/08_polynomial_ring.png")
    plt.close()

def finite_fields():
    """有限体（ガロア体）"""
    print("\n" + "=" * 50)
    print("5. 有限体（ガロア体）")
    print("=" * 50)

    print("有限体 GF(p): 位数pの有限体（pは素数）")
    print("元: {0, 1, 2, ..., p-1}")
    print("演算: 加法と乗法（mod p）")

    p = 7
    print(f"\n例: GF({p})")

    elements = list(range(p))
    print(f"元: {elements}")

    # 加法表
    print(f"\n加法表 (mod {p}):")
    print("  + |", " ".join(f"{i:2}" for i in elements))
    print("----+" + "---" * p)
    for i in elements:
        row = [f"{(i + j) % p:2}" for j in elements]
        print(f"{i:2}  |", " ".join(row))

    # 乗法表
    print(f"\n乗法表 (mod {p}):")
    print("  × |", " ".join(f"{i:2}" for i in elements))
    print("----+" + "---" * p)
    for i in elements:
        row = [f"{(i * j) % p:2}" for j in elements]
        print(f"{i:2}  |", " ".join(row))

    # 可視化
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 加法表
    add_table = np.array([[(i + j) % p for j in elements] for i in elements])
    im1 = axes[0].imshow(add_table, cmap='viridis', interpolation='nearest')
    axes[0].set_xticks(elements)
    axes[0].set_yticks(elements)
    axes[0].set_xlabel('j', fontsize=12)
    axes[0].set_ylabel('i', fontsize=12)
    axes[0].set_title(f'Addition Table: GF({p})', fontsize=14, fontweight='bold')

    for i in elements:
        for j in elements:
            axes[0].text(j, i, f'{add_table[i, j]}',
                        ha='center', va='center', color='white', fontweight='bold')

    plt.colorbar(im1, ax=axes[0])

    # 乗法表
    mul_table = np.array([[(i * j) % p for j in elements] for i in elements])
    im2 = axes[1].imshow(mul_table, cmap='plasma', interpolation='nearest')
    axes[1].set_xticks(elements)
    axes[1].set_yticks(elements)
    axes[1].set_xlabel('j', fontsize=12)
    axes[1].set_ylabel('i', fontsize=12)
    axes[1].set_title(f'Multiplication Table: GF({p})', fontsize=14, fontweight='bold')

    for i in elements:
        for j in elements:
            axes[1].text(j, i, f'{mul_table[i, j]}',
                        ha='center', va='center', color='white', fontweight='bold')

    plt.colorbar(im2, ax=axes[1])

    plt.tight_layout()
    plt.savefig('../../outputs/08_finite_field.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/08_finite_field.png")
    plt.close()

def cryptography_application():
    """実務応用: 暗号化"""
    print("\n" + "=" * 50)
    print("6. 実務応用: 暗号化（RSA暗号の数学）")
    print("=" * 50)

    print("RSA暗号は以下の数学的概念に基づいています：")
    print("1. 素数の性質")
    print("2. 剰余演算")
    print("3. オイラーのφ関数")
    print("4. モジュラ逆元")

    # 簡単なRSAの例
    p, q = 61, 53  # 小さい素数
    n = p * q
    phi_n = (p - 1) * (q - 1)

    print(f"\n1. 2つの素数を選ぶ: p = {p}, q = {q}")
    print(f"2. n = p × q = {n}")
    print(f"3. φ(n) = (p-1) × (q-1) = {phi_n}")

    # 公開鍵の指数 e
    e = 17  # φ(n)と互いに素
    print(f"4. 公開鍵の指数 e = {e} (φ(n)と互いに素)")

    # 秘密鍵の指数 d (e × d ≡ 1 (mod φ(n)))
    def mod_inverse(a, m):
        """拡張ユークリッドの互除法でモジュラ逆元を計算"""
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        _, x, _ = extended_gcd(a % m, m)
        return (x % m + m) % m

    d = mod_inverse(e, phi_n)
    print(f"5. 秘密鍵の指数 d = {d} (e × d ≡ 1 (mod φ(n)))")

    # 暗号化と復号化
    message = 42
    print(f"\n元のメッセージ: m = {message}")

    # 暗号化: c = m^e mod n
    ciphertext = pow(message, e, n)
    print(f"暗号化: c = {message}^{e} mod {n} = {ciphertext}")

    # 復号化: m = c^d mod n
    decrypted = pow(ciphertext, d, n)
    print(f"復号化: m = {ciphertext}^{d} mod {n} = {decrypted}")

    print(f"\n検証: 元のメッセージ = 復号化されたメッセージ? {message == decrypted}")

    print("\n暗号化プロセスの可視化...")

    # メッセージのビット表現
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 元のメッセージ
    message_bits = format(message, '08b')
    axes[0, 0].bar(range(8), [int(b) for b in message_bits], color='blue', alpha=0.7)
    axes[0, 0].set_ylim(0, 1.5)
    axes[0, 0].set_title(f'Original Message: {message} = {message_bits}b',
                        fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Bit Position')
    axes[0, 0].set_ylabel('Bit Value')
    axes[0, 0].grid(True, alpha=0.3)

    # 暗号文
    cipher_bits = format(ciphertext, '016b')
    axes[0, 1].bar(range(16), [int(b) for b in cipher_bits], color='red', alpha=0.7)
    axes[0, 1].set_ylim(0, 1.5)
    axes[0, 1].set_title(f'Ciphertext: {ciphertext}',
                        fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Bit Position')
    axes[0, 1].set_ylabel('Bit Value')
    axes[0, 1].grid(True, alpha=0.3)

    # RSA鍵生成の流れ
    axes[1, 0].text(0.5, 0.9, 'RSA Key Generation',
                   ha='center', fontsize=14, fontweight='bold',
                   transform=axes[1, 0].transAxes)

    steps = [
        f'1. Select primes: p={p}, q={q}',
        f'2. Compute n = p×q = {n}',
        f'3. Compute φ(n) = {phi_n}',
        f'4. Choose e = {e}',
        f'5. Compute d = {d}',
        f'Public key: (e={e}, n={n})',
        f'Private key: (d={d}, n={n})'
    ]

    for i, step in enumerate(steps):
        axes[1, 0].text(0.1, 0.75 - i*0.1, step,
                       fontsize=10, transform=axes[1, 0].transAxes,
                       verticalalignment='top')

    axes[1, 0].axis('off')

    # 暗号化・復号化の流れ
    axes[1, 1].text(0.5, 0.9, 'Encryption/Decryption',
                   ha='center', fontsize=14, fontweight='bold',
                   transform=axes[1, 1].transAxes)

    process = [
        f'Message: m = {message}',
        f'↓ Encrypt: c = m^e mod n',
        f'Ciphertext: c = {ciphertext}',
        f'↓ Decrypt: m = c^d mod n',
        f'Decrypted: m = {decrypted}',
        f'✓ Verified: m == decrypted'
    ]

    for i, step in enumerate(process):
        axes[1, 1].text(0.1, 0.75 - i*0.12, step,
                       fontsize=10, transform=axes[1, 1].transAxes,
                       verticalalignment='top')

    axes[1, 1].axis('off')

    plt.tight_layout()
    plt.savefig('../../outputs/08_cryptography.png', dpi=150, bbox_inches='tight')
    print("グラフを保存しました: outputs/08_cryptography.png")
    plt.close()

def error_correction_application():
    """実務応用: 誤り訂正符号"""
    print("\n" + "=" * 50)
    print("7. 実務応用: 誤り訂正符号（ハミング符号）")
    print("=" * 50)

    print("ハミング符号: データ転送時のエラーを検出・訂正")
    print("有限体上の線形代数を使用")

    print("\n(7,4)ハミング符号:")
    print("- 4ビットのデータに3ビットのパリティを追加")
    print("- 1ビットのエラーを訂正可能")

    # データビット
    data = np.array([1, 0, 1, 1])  # 4ビット
    print(f"\n元のデータ: {data}")

    # 生成行列G (4×7)
    G = np.array([
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ])

    print("\n生成行列 G:")
    print(G)

    # 符号化: c = d × G (mod 2)
    codeword = (data @ G) % 2
    print(f"\n符号語: {codeword}")

    # エラーを導入
    error_pos = 2
    received = codeword.copy()
    received[error_pos] = 1 - received[error_pos]
    print(f"\nエラー導入（位置{error_pos}）: {received}")

    # 検査行列H (3×7)
    H = np.array([
        [1, 1, 0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 1]
    ])

    print("\n検査行列 H:")
    print(H)

    # シンドローム計算: s = H × r^T (mod 2)
    syndrome = (H @ received) % 2
    print(f"\nシンドローム: {syndrome}")

    # エラー位置の特定
    syndrome_decimal = int(''.join(map(str, syndrome[::-1])), 2)
    print(f"シンドローム（10進）: {syndrome_decimal}")

    if syndrome_decimal > 0:
        print(f"エラー位置: {syndrome_decimal - 1}")
        # エラー訂正
        corrected = received.copy()
        corrected[syndrome_decimal - 1] = 1 - corrected[syndrome_decimal - 1]
        print(f"訂正後: {corrected}")
        print(f"訂正成功: {np.array_equal(corrected, codeword)}")

    # 可視化
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 元のデータ
    axes[0, 0].bar(range(len(data)), data, color='blue', alpha=0.7)
    axes[0, 0].set_ylim(0, 1.5)
    axes[0, 0].set_title('Original Data (4 bits)', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Bit Position')
    axes[0, 0].set_ylabel('Bit Value')
    axes[0, 0].grid(True, alpha=0.3)

    # 符号語
    axes[0, 1].bar(range(len(codeword)), codeword, color='green', alpha=0.7)
    axes[0, 1].set_ylim(0, 1.5)
    axes[0, 1].set_title('Codeword (7 bits)', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Bit Position')
    axes[0, 1].set_ylabel('Bit Value')
    axes[0, 1].grid(True, alpha=0.3)

    # 受信語（エラーあり）
    colors = ['red' if i == error_pos else 'orange' for i in range(len(received))]
    axes[1, 0].bar(range(len(received)), received, color=colors, alpha=0.7)
    axes[1, 0].set_ylim(0, 1.5)
    axes[1, 0].set_title(f'Received (with error at pos {error_pos})',
                        fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Bit Position')
    axes[1, 0].set_ylabel('Bit Value')
    axes[1, 0].grid(True, alpha=0.3)

    # 訂正後
    axes[1, 1].bar(range(len(corrected)), corrected, color='purple', alpha=0.7)
    axes[1, 1].set_ylim(0, 1.5)
    axes[1, 1].set_title('Corrected Codeword', fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('Bit Position')
    axes[1, 1].set_ylabel('Bit Value')
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../../outputs/08_error_correction.png', dpi=150, bbox_inches='tight')
    print("\nグラフを保存しました: outputs/08_error_correction.png")
    plt.close()

def blockchain_application():
    """実務応用: ブロックチェーンとハッシュ関数"""
    print("\n" + "=" * 50)
    print("8. 実務応用: ブロックチェーンの数学")
    print("=" * 50)

    print("ブロックチェーンで使用される代数的概念:")
    print("1. 暗号学的ハッシュ関数（一方向性関数）")
    print("2. 楕円曲線暗号（ECDSA）")
    print("3. マークル木（ハッシュ木）")

    print("\n簡易的なハッシュチェーンの例:")

    # 簡易ハッシュ関数（実際にはSHA-256などを使用）
    def simple_hash(data):
        return sum(ord(c) for c in str(data)) % 1000

    blocks = []
    prev_hash = 0

    for i in range(5):
        data = f"Block {i} data"
        block_hash = simple_hash(str(prev_hash) + data)
        blocks.append({
            'index': i,
            'data': data,
            'prev_hash': prev_hash,
            'hash': block_hash
        })
        print(f"\nブロック {i}:")
        print(f"  データ: {data}")
        print(f"  前のハッシュ: {prev_hash}")
        print(f"  ハッシュ: {block_hash}")
        prev_hash = block_hash

    print("\nチェーンの整合性:")
    for i in range(1, len(blocks)):
        is_valid = blocks[i]['prev_hash'] == blocks[i-1]['hash']
        print(f"  ブロック{i}: {'✓ 有効' if is_valid else '✗ 無効'}")

def main():
    """メイン実行関数"""
    print("\n" + "=" * 50)
    print("Python数学学習: レッスン8 - 代数学")
    print("=" * 50 + "\n")

    group_theory_basics()
    symmetric_group()
    rings_and_fields()
    polynomial_rings()
    finite_fields()
    cryptography_application()
    error_correction_application()
    blockchain_application()

    print("\n" + "=" * 50)
    print("レッスン8 完了!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
