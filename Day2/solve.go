package main

import "fmt"

func main(){
  var grid =  [][]int{}
  var row1 = []int{1,2,3}
  var row2 = []int{4,5,6}
  var row3 = []int{7,8,9}

  grid = append(grid,row1)
  grid = append(grid,row2)
  grid = append(grid,row3)
  fmt.Println(grid)
}
