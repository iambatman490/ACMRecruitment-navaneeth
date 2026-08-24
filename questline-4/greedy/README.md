
1 Lemonade Change (LeetCode 860)
Keep track of the count of $5 and $10 bills. When a customer gives $5, increment the $5 count. When given $10, check if a $5 bill is available to give as change. When given $20, prioritize giving one $10 and one $5 bill first to preserve the more versatile $5 bills; otherwise, give three $5 bills. If neither option is possible, return `False`.
2 Assign Cookies (LeetCode 455)
 Sort both the greed factors array `g` and the cookie sizes array `s`. Use two pointers to iterate through both lists. For each cookie, check if it can satisfy the current child's greed factor. If it does, move to the next child and increment the count. Always move to the next cookie.
