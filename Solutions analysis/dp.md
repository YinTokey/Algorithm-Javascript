# 动态规划

##### 62. 不同路径
二维动态规划，可以通过画表格找到最有子结构。放上Go的实现。
```
func uniquePaths(m int, n int) int {

    opt := make([][]int,m)

    for i:=0; i < m ; i++ {
        opt[i] = make([]int,n)
        for j :=0; j< n; j++ {
            if i == 0 || j == 0 {
                opt[i][j] = 1
            } else {
                opt[i][j] = opt[i-1][j] + opt[i][j-1]
            }
        }
    }
    return opt[m-1][n-1]
}

```
利用滚动一维数组，每次都存储与更新最优解，可以把空间复杂度优化到O(n)
```
func uniquePaths(m int, n int) int {

    opt := make([]int,n)

    for i:=0; i < m ; i++ {
        for j :=0; j< n; j++ {
            if i == 0 || j == 0 {
                opt[j] = 1
            } else {
                opt[j] = opt[j-1] + opt[j]
            }
        }
    }
    return opt[n-1]
}

```
##### 63. 不同路径2
加了障碍物，需要增加一些判断。且画图领会。
```
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    n, m := len(obstacleGrid), len(obstacleGrid[0])
    opt := make([]int,m)

    if obstacleGrid[0][0] == 0 {
        opt[0] = 1
    }

    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if obstacleGrid[i][j] == 1 {
                opt[j] = 0
                continue
            } 

            if j >= 1 && obstacleGrid[i][j-1] == 0 {
                opt[j] += opt[j-1]
            }
         }
    }

    return opt[m-1]
}

```



