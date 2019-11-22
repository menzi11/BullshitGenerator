package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"math/rand"
	"strings"
	"time"
	"unicode/utf8"
)

type data struct {
	Title  string   // 标题
	Famous []string // 名人名言
	Before []string // 前面垫话
	After  []string // 后面垫话
	Bosh   []string // 废话
}

var (
	数据 = func() (data data) {
		jsonData, err := ioutil.ReadFile("./data.json")
		if err != nil {
			log.Fatal(err)
		}
		err = json.Unmarshal(jsonData, &data)
		if err != nil {
			log.Fatal(err)
		}
		return
	}()
	名人名言 = 数据.Famous // a 代表前面垫话，b代表后面垫话
	前面垫话 = 数据.Before // 在名人名言前面弄点废话
	后面垫话 = 数据.After  // 在名人名言后面弄点废话
	废话   = 数据.Bosh   // 代表文章主要废话来源

	标题 = "我是谁"

	下一句废话   = 洗牌遍历(废话)
	下一句名人名言 = 洗牌遍历(名人名言)
)

const 重复度 = 2

func 洗牌遍历(列表 []string) func() string {
	var 池 []string
	for i := 0; i < 重复度; i++ {
		池 = append(池, 列表...)
	}
	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(池), func(i, j int) { 池[i], 池[j] = 池[j], 池[i] })

	索引 := 0
	return func() (val string) {
		if 索引 >= len(池) {
			索引 = 0
		}
		val = 池[索引]
		索引++
		return
	}
}

func 来点名人名言() (名人名言 string) {
	名人名言 = 下一句名人名言()
	名人名言 = strings.Replace(名人名言, "a", 前面垫话[rand.Intn(len(前面垫话))], -1)
	名人名言 = strings.Replace(名人名言, "b", 后面垫话[rand.Intn(len(后面垫话))], -1)
	return
}

func 另起一段() (newline string) {
	newline = ". "
	newline += "\r\n"
	newline += "    "
	return
}

func main() {
	fmt.Print("请输入文章主题: ")
	fmt.Scanln(&标题)
	var 文章 string
	for utf8.RuneCountInString(文章) < 6000 {
		分支 := rand.Intn(100)
		if 分支 < 5 {
			文章 += 另起一段()
		} else if 分支 < 20 {
			文章 += 来点名人名言()
		} else {
			文章 += 下一句废话()
		}
	}
	文章 = strings.Replace(文章, "x", 标题, -1)
	fmt.Println(文章)
}
