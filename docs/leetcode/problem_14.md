---
tags:
    - 难度:简单
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

## 复杂度分析

- **时间复杂度：** $O(mn)$，$m$ 为序列中所有字符串的平均长度，$n$ 为序列中字符串的数量。
- **空间复杂度：** $O(1)$，额外使用的空间不随任务规模而改变。

## 样例代码

=== "Python"

    ```python
    def longestCommonPrefix(strs: list[str]) -> str:
        for i, letters in enumerate(zip(*strs)):
            if len(set(letters)) != 1:
                return strs[0][:i]

        return min(strs, key=len)
    ```
