### 证明 Approximation Error 不受影响

我们需要证明：

inf⁡f∈F∥f−f∗∥2=inf⁡f∈SGF∥f−f∗∥2\inf_{f \in \mathcal{F}} \| f - f^* \|^2 = \inf_{f \in S_{\mathscr{G}} \mathcal{F}} \| f - f^* \|^2

其中 SGS_{\mathscr{G}} 是 L2(X)L^2(\mathcal{X}) 上的正交投影算子，即对于任意 f∈L2(X)f \in L^2(\mathcal{X})，我们可以分解：

f=SGf+(I−SG)ff = S_{\mathscr{G}} f + (I - S_{\mathscr{G}}) f

其中：

- SGfS_{\mathscr{G}} f 是 ff 在 SGFS_{\mathscr{G}} \mathcal{F} 空间上的正交投影。
- (I−SG)f(I - S_{\mathscr{G}}) f 是与 SGFS_{\mathscr{G}} \mathcal{F} 正交的分量，即 ⟨SGf,(I−SG)f⟩=0\langle S_{\mathscr{G}} f, (I - S_{\mathscr{G}}) f \rangle = 0。

------

### **证明步骤**

#### **1. 误差分解**

对于任意 f∈Ff \in \mathcal{F}，由于 SGS_{\mathscr{G}} 是正交投影，我们可以将误差分解如下：

∥f−f∗∥2=∥SGf+(I−SG)f−f∗∥2.\| f - f^* \|^2 = \| S_{\mathscr{G}} f + (I - S_{\mathscr{G}}) f - f^* \|^2.

将 SGfS_{\mathscr{G}} f 与 (I−SG)f(I - S_{\mathscr{G}}) f 分开，我们得到：

∥f−f∗∥2=∥SGf−f∗+(I−SG)f∥2.\| f - f^* \|^2 = \| S_{\mathscr{G}} f - f^* + (I - S_{\mathscr{G}}) f \|^2.

由于 (I−SG)f(I - S_{\mathscr{G}}) f 与 SGFS_{\mathscr{G}} \mathcal{F} 正交，我们可以利用勾股定理展开：

∥f−f∗∥2=∥SGf−f∗∥2+∥(I−SG)f∥2.\| f - f^* \|^2 = \| S_{\mathscr{G}} f - f^* \|^2 + \| (I - S_{\mathscr{G}}) f \|^2.

#### **2. 取最小值**

由于 ∥(I−SG)f∥2≥0\| (I - S_{\mathscr{G}}) f \|^2 \geq 0，我们可以看到：

∥SGf−f∗∥2≤∥f−f∗∥2.\| S_{\mathscr{G}} f - f^* \|^2 \leq \| f - f^* \|^2.

因此，对于所有 f∈Ff \in \mathcal{F} 取最小值时，我们有：

inf⁡f∈F∥SGf−f∗∥2≤inf⁡f∈F∥f−f∗∥2.\inf_{f \in \mathcal{F}} \| S_{\mathscr{G}} f - f^* \|^2 \leq \inf_{f \in \mathcal{F}} \| f - f^* \|^2.

另一方面，对于任意 f∈Ff \in \mathcal{F}，我们可以选择 SGf∈SGFS_{\mathscr{G}} f \in S_{\mathscr{G}} \mathcal{F}，因此：

inf⁡f∈F∥f−f∗∥2≤inf⁡f∈SGF∥f−f∗∥2.\inf_{f \in \mathcal{F}} \| f - f^* \|^2 \leq \inf_{f \in S_{\mathscr{G}} \mathcal{F}} \| f - f^* \|^2.

综上，我们得出：

inf⁡f∈F∥f−f∗∥2=inf⁡f∈SGF∥f−f∗∥2.\inf_{f \in \mathcal{F}} \| f - f^* \|^2 = \inf_{f \in S_{\mathscr{G}} \mathcal{F}} \| f - f^* \|^2.

这说明**正交投影不会影响最优逼近误差**，从而完成证明。✔