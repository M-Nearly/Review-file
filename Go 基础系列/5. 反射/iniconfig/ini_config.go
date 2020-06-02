package main

import (
	"fmt"
	"io/ioutil"
	"reflect"
	"strconv"
	"strings"
)

// 序列化和反序列化
// 序列化数据到指定的文件

func MarshalFile(filename string, data interface{}) (err error) {
	// 1.数据的序列化
	res, err := Marshal(data)
	if err != nil {
		fmt.Println(err)
		return
	}
	// 2.将序列好的数据, 写出到 filename
	return ioutil.WriteFile(filename, res, 0666)
}

// 序列化的方法
// 传入的结构体 -> []byte
// 基本思路: 反射解析出传入的数据(各种判断). 转成[]byte
func Marshal(data interface{}) (result []byte, err error) {
	// 先获取data 的类型
	typeInfo := reflect.TypeOf(data)
	valueInfo := reflect.ValueOf(data)
	// 先判断类型
	if typeInfo.Kind() != reflect.Struct {
		return
	}

	var conf []string
	// 获取所有字段去处理
	for i := 0; i < typeInfo.NumField(); i++ {
		// 取字段
		labelField := typeInfo.Field(i)
		// 取字段的值
		labelVal := valueInfo.Field(i)

		fieldType := labelField.Type
		// 判断字段的类型
		if fieldType.Kind() != reflect.Struct {
			continue
		}
		// 拼[server] 和 [mysql]
		// 获取tag
		tagValue := labelField.Tag.Get("ini")
		if len(tagValue) == 0 {
			tagValue = labelField.Name
		}

		label := fmt.Sprintf("\n[%s]\n", tagValue)
		conf = append(conf, label)

		// 拼 k-v
		for j := 0; j < fieldType.NumField(); j++ {
			// 这里取到的是大写的field name
			keyField := fieldType.Field(j)
			// 取tag
			fieldTagVal := keyField.Tag.Get("ini")
			if len(fieldTagVal) == 0 {
				fieldTagVal = keyField.Name
			}

			// 取值
			valField := labelVal.Field(j) // valField.Interface() 取真正对应的值
			item := fmt.Sprintf("%s = %v\n", fieldTagVal, valField.Interface())
			conf = append(conf, item)

		}

	}
	// 遍历切片 转类型
	for _, val := range conf {
		result = append(result, []byte(val)...)
	}
	return
}

// 文件读取数据, 做反序列化
func UnMarshalFile(filename string, result interface{}) (err error) {
	// 1. 文件读取
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return
	}
	// 2. 反序列化
	return UnMarshal(data, result)
}

// 反序列化
// []byte -> 切片
func UnMarshal(data []byte, result interface{}) (err error) {
	// 先判断指针
	typeInfo := reflect.TypeOf(result)
	if typeInfo.Kind() != reflect.Ptr {
		return
	}
	// 判断是否是结构体
	if typeInfo.Elem().Kind() != reflect.Struct {
		return
	}
	// 转类型 按行切割
	lineArr := strings.Split(string(data), "\n")
	// 定义全局的标签名 server 和 musql
	var myFieldName string
	for _, line := range lineArr {
		//各种严谨判断 是不是空 是不是注释的
		// 处理文档注释
		line = strings.TrimSpace(line)
		if len(line) == 0 || line[0] == ';' || line[0] == '#' {
			continue
		}
		// 按照括号去判断
		if line[0] == '[' {
			// 按照大便签去处理
			myFieldName, err = MyLabel(line, typeInfo.Elem())
			if err != nil {
				return
			}
			continue

		}
		// 按照正常数据处理
		err = myField(myFieldName, line, result)
		if err != nil {
			return
		}

	}
	return

}

// 处理便签
func MyLabel(line string, typeInfo reflect.Type) (fieldName string, err error) {
	// 去字符串的头和尾
	labelName := line[1 : len(line)-1]
	// 循环去结构体找tag 对应上才能解析
	for i := 0; i < typeInfo.NumField(); i++ {
		field := typeInfo.Field(i)
		tagValue := field.Tag.Get("ini")
		// 判断tag
		if labelName == tagValue {
			fieldName = field.Name
			return
		}
	}
	return
}

// 解析属性
// 参数 大标签名 行数据 对象结构体
func myField(fileldName string, line string, result interface{}) (err error) {
	key := strings.TrimSpace(line[0:strings.Index(line, "=")])
	val := strings.TrimSpace(line[strings.Index(line, "=")+1:])

	// 解析到结构体
	//resultType := reflect.TypeOf(result)
	resultValue := reflect.ValueOf(result)
	// 拿到字段值, 这里直接设置不行,还不知道类型
	labelValue := resultValue.Elem().FieldByName(fileldName)
	// 拿到了该字段的类型
	labelType := labelValue.Type()
	// 第一次进来应该是server
	// 遍历server结构体的所有字段
	// 存放渠道的字段名
	var keyName string
	for i := 0; i < labelType.NumField(); i++ {
		// 获取结构体字段 
		field := labelType.Field(i)
		tagVal := field.Tag.Get("ini")
		if tagVal == key {
			keyName = field.Name
			break
		}

	}
	// 给字段赋值
	// 取到字段值
	filedValue := labelValue.FieldByName(keyName)
	// 修改值
	switch filedValue.Type().Kind() {
	case reflect.String:
		filedValue.SetString(val)
	case reflect.Int:
		i, err := strconv.ParseInt(val, 10, 64)
		if err != nil {
			return err
		}
		filedValue.SetInt(i)
	case reflect.Uint:
		i, err := strconv.ParseUint(val, 10, 64)
		if err != nil {
			return err
		}
		filedValue.SetUint(i)
	case reflect.Float32:
		i, err := strconv.ParseFloat(val, 64)
		if err != nil {
			return err
		}
		filedValue.SetFloat(i)
	}
	return
}
