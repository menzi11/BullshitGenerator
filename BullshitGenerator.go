package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"time"

	"github.com/urfave/cli"
)

//随便取一句 从列表当中
func PickUpOneSentence(list []string) string {
	index := RandInt(0, len(list))
	tmp := list[index]
	return tmp
}

//来点名人名言
func (this BoshJson) PickUpOneFamous() string {
	tmp := PickUpOneSentence(this.Famous)
	reg_a := regexp.MustCompile(`a`)
	reg_b := regexp.MustCompile(`b`)
	tmp = reg_a.ReplaceAllString(tmp, PickUpOneSentence(this.After))
	tmp = reg_b.ReplaceAllString(tmp, PickUpOneSentence(this.Before))
	return tmp
}

//来点废话，MainTheme是需要更换的主题
func (this BoshJson) PickupOneBosh(MainTheme string) string {
	tmp := PickUpOneSentence(this.Bosh)
	reg_x := regexp.MustCompile(`x`)
	tmp = reg_x.ReplaceAllString(tmp, MainTheme)
	return tmp
}

//增加段落
func AddNewPhrase(Content string) string {
	Content = Content + "。 "
	Content = Content + "\r\n"
	Content = Content + "    "
	return Content
}

func BullshitGenerator(c *cli.Context) error {
	var Article string = ""   //文章
	var Content string = ""   //章节
	var ContentLength int = 0 //章节长度

	//var MainTheme string = "一天掉多少根头发" //主题
	MainTheme := c.String("bush") //根据命令行传入的参数来定义主题

	var Sentence string = "" //句子
	bosh := ReadJson("data.json")
	Article = MainTheme             //文章开头为主题
	Article = AddNewPhrase(Article) //主题后，需要新建一段
	for {
		index := RandInt(0, 100) //随机取一个数，用做段落数
		if index < 5 && ContentLength > 200 {
			Content = AddNewPhrase(Content)
			Article = Article + Content
			Content = ""
		} else if index < 20 {
			Sentence = bosh.PickUpOneFamous()
			ContentLength = ContentLength + len(Sentence)
			Content = Content + Sentence

		} else {
			Sentence = bosh.PickupOneBosh(MainTheme)
			ContentLength = ContentLength + len(Sentence)
			Content = Content + Sentence
		}
		if ContentLength > 6000 { //当文章长度超过6000字时退出
			break
		}

	}
	Content = AddNewPhrase(Content)
	Article = Article + Content
	Article = Article + "\n"

	fmt.Println(Article)
	return nil
}

func main() {
	app := cli.NewApp()
	app.Name = "golang BullshitGenerator"
	app.Compiled = time.Now()
	app.Version = "1.0.0"
	app.Authors = []cli.Author{
		cli.Author{
			Name:  "Jimes Yang",
			Email: "sndnvaps@gmail.com",
		},
	}
	app.Copyright = "(c) 2019 Jimes Yang<sndnvaps@gmail.com>"
	app.Usage = "只用来生成废话文章。仅供用做娱乐，不可乱用！"
	app.Action = BullshitGenerator
	app.Flags = []cli.Flag{
		cli.StringFlag{
			Name:  "bush,b",
			Value: "一个人每天掉多少头发", //设置默认主题，当没有输入 自定义主题的时候使用
			Usage: "定义文章的主题",
		},
	}

	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}
