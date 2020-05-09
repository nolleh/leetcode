package leetcode

import (
	"strconv"
)

func debug(desc string, datas ...int) {
    str := "("
    for i, v := range datas {
        str += strconv.Itoa(v)
        if i != len(datas)-1 {
            str += ","
        }
    }
    str += ") "
	
	panic(str + ":" + desc)
}

func debugarr(desc string, datas ...[]int) {
	str := ""
	for i, data := range datas {
		str += "data[" + strconv.Itoa(i) + "]("
		for j, v := range data {
			str += strconv.Itoa(v)
			if j != len(data)-1 {
				str += ","
			}
		}
		str += ") "
	}
	panic(str + ":" + desc)
}

func debugarr2(desc string, datas ...[][]int) {
	str := ""
	for d, data := range datas {
		str += "data[" + strconv.Itoa(d) + "](\n"
        for i := 0; i < len(data); i++ {
            for j := 0; j < len(data[i]); j++ {
                str += strconv.Itoa(data[i][j])
                if j != len(data[i])-1 {
                    str += ","
                }
            }
            str += "\n";
		}
		str += ") "
	}
	panic(str + ":" + desc)
}

func debugstr(desc string, datas ...string) {
	str := ""
	for i, data := range datas {
		str += "data[" + strconv.Itoa(i) + "]("
		str += data
		str += ") "
	}
	panic(str + ":" + desc)
}

func debugbytes(desc string, datas ...[]byte) {

	str := ""

	for d, data := range datas {
		str += "data[" + strconv.Itoa(d) + "](\n)"
		for i := 0; i < len(data); i++ {
			str += string(data[i])
		}
		str += ") "
	}
    
    panic(str)

}

type ListNode struct {
    Val int
    Next *ListNode
}

func debugNode(head *ListNode) string {
    now := head
    str := "["
    
    for now != nil {
        str += strconv.Itoa(now.Val) + ","
        now = now.Next
    }
    str += "]"
    return str
}
