---
tags:
    - DIF:简单
    - 字符串
---

# 14. 最长公共前缀

从一个字符串序列中找出公共前缀最长的字符串。如果不存在公共前缀，则返回空字符串 `""`。

=== "样例 1"

    <pre>
    <code><b>输入：</b>strs = ["flower","flow","flight"]
    <b>输出：</b>"fl"</code>
    </pre>

=== "样例 2"

    <pre>
    <code><b>输入：</b>strs = ["dog","racecar","car"]
    <b>输出：</b>""
    <b>解释：</b>输入字符串中不存在公共前缀。</code>
    </pre>

=== "限制条件"

    - `1 <= strs.length <= 200`；
    - `0 <= strs[i].length <= 200`；
    - `strs[i]` 只包含小写英文字母。

## 解析

解决此题只需扫描字符串即可，可选择横向扫描字符串或者纵向扫描字符串。

- 横向扫描的思路是两两比较序列中的字符串，然后用比较后得到的最长公共前缀再去与后面的字符串比较；
- 纵向扫描的思路是逐一比较序列中每个字符串的每一位字符是否相同。

## 复杂度分析

- **时间复杂度：** $O(mn)$，$m$ 为序列中所有字符串的平均长度，$n$ 为序列中字符串的数量。
- **空间复杂度：** $O(1)$，额外使用的空间不随任务规模而改变。

## 代码

=== "Python"

    ```python
    # 本样例采用纵向扫描方式。
    def longestCommonPrefix(strs: list[str]) -> str:
        # 借助 zip 函数将列表中每个字符串的相同位字符组成元组，以便判断每一位字符是否相同。
        for i, letters in enumerate(zip(*strs)):
            if len(set(letters)) != 1:
                return strs[0][:i]
        # 如果以上流程没有找到最长公共字串，则最长公共字串一定是序列中最短的字符串。
        return min(strs, key=len)
    ```
