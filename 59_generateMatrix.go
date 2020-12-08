type Coord struct {
    X,Y int
}

func generateMatrix(n int) [][]int {
    res := make([][]int, n)
    for i,_ := range res {
        res[i] = make([]int, n)
    }
    // 0,1,2,3 = right, down, left up
    dir     := 0
    dirMap  := map[int]Coord {
        0:Coord{0,1},
        1:Coord{1,0},
        2:Coord{0,-1},
        3:Coord{-1,0},
    }
    count   := 1
    coord   := Coord{0,0}

    updateCoord := func() {
        c := dirMap[dir]
        c.X += coord.X
        c.Y += coord.Y
        
        if c.X < 0 || c.X >= n || c.Y < 0 || c.Y >= n || res[c.X][c.Y] != 0 {
            dir = (dir+1)%4
            c = dirMap[dir]
            c.X += coord.X
            c.Y += coord.Y
            if c.X < 0 || c.X >= n || c.Y < 0 || c.Y >= n || res[c.X][c.Y] != 0 {
                return
            } else {
                coord.X = c.X
                coord.Y = c.Y
            }
        } else {
            coord.X = c.X
            coord.Y = c.Y 
        }
    } 
    
    for res[coord.X][coord.Y] == 0 {
        res[coord.X][coord.Y] = count
        count += 1

        updateCoord()
    }
    return res
}
