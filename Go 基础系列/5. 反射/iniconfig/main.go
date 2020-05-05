package main

import (
	"fmt"
	"io/ioutil"
)

// 解析文件

func parseFile(fielName string) {
	data, e := ioutil.ReadFile(fielName)
	if e != nil {
		return
	}

	var conf Config
	e = UnMarshal(data, &conf)
	if e != nil {
		return
	}

	fmt.Printf("反序列化成功: %#v\n", conf)

}

func parseFile2(filename string) {
	// 有一些假数据
	var conf Config
	conf.ServerConf.Ip = "127.0.0.1"
	conf.ServerConf.Port = 8000
	conf.MysqlConf.Username = "root"
	conf.MysqlConf.Port = 9000

	err := MarshalFile(filename, conf)
	if err != nil {
		return

	}

}
func main() {
	//parseFile("./config.ini")
	parseFile2("D:/my2.ini")
}
