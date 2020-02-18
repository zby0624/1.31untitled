# 格式化文件存储
- xml,json
- 为了解决不同设备之间信息交换的问题

# XML文件
- 参考文件
    - https://docs.python.org/3/library/xml/etree.elementtree.html
    - http://www.runoob.com/python/python-xml.html
    - https://blog.csdn.net/seetheworld518/article/details/49535285
    
- XML(extensibemarkuplanguage)  可扩展标记语言
      - 标记语言：语言中使用尖括号括起来的文本字符串标记
      - 可扩展：用户可以自己定义需要的标记
      - 例如
            <Teacher>
            自定义标记Teacher
            在两个标记之间任何内容都应该跟Teacher相关
            </Teacher>
      - 是W3C组织指定的一个标准
      - XML描述的数据本身，即数据的结构和语义
      - HTML侧重于如何显示WEB页面中的数据
      - web三剑客：HTML(页面上都有什么数据),CSS(页面数据漂亮工整),JS（数据功能，动态）

- XML文档的构成
      - 处理指令(可以认为一个文件只有一个处理指令)
          - 最多只有一行且只有第一行
          - 内容是与xml本身处理相关的声明或者指令
          - 以xml关键字开头
          - 一般用来声明XML的版本和采用的编码
            - version属性是必须的
            - encoding属性用来指出xml解释器使用的编码
      - 根元素(一个文件只有一个根元素) 
          - 在整个的xml文件中，可以把它看作一个树型文件
          - 有且只有一个  
      - 子元素
      - 属性
      - 内容
         - 表示标签存储的信息
      - 注释
         - 其说明作用的信息
         - 注释不能嵌套在标签里面
         - 只有在注释的开始和结尾使用双短横线
         - 三短横线只能出现在注释的开头，而不是注释的结尾
         
- 保留字符的组成
      - XML中使用的符号可能跟实际符号相冲突，典型的就是左右尖括号
      - 使用实体引用(entityreference)来表示保留字符
       
            <score> score&gt;80 </score>
      - 把含有保留字符的部分放在CDATA块内部，CDATA把内部信息是为不需要转义
      - 常用的许哟啊转义的保留字符和对应实体引用
           - % :&amp;
           - < :&it;
           - > :&gt;
           - ' :&apos;
           - " :&quot;
- XML标签的命名规则
      - Pascal命名法
      - 用单词表示，第一个字母大写
      - 大小写严格区分 
           
- 命令空间
      - 为了防止命名冲突
           
           <Student>
              <name>liudana</name>
              <age>21</name>
           </Student>
           <Room>
              <name>2020</name>
              <Location>1-23-110</Location>
           </Room>
           
      - 如果归并上述两个内容消息，会产生冲突
      
      - 为了避免命名冲突，需要给可能冲突的元素添加命名空间
      - xmlns:xml name space的缩写
      
                <schooler xmlns:student="http://my_student"  xmlns:room="http://my_room">
                   <student:name>liudana</student:name>
                   <age>21</age>
                   
                   <room:name>2020</room:name>
                   <location>1-23-110</location>
                   
                </schlloer>
                
# XML访问

## 读取
- XML读取分为两个主要技术：SAX,DOM
- SAX(simple API for XML):
       - 基于事情驱动的API
       - 利用SAX解析文档设计到解释器和事情处理两个部分
       - 特点
          - 快
          - 流式读取
- DOM
       - 是w3c规定的XML编程接口
       - 一个XML文件在缓存中以树形结构保存，读取
       - 用途
           - 定位浏览XML任何一个节点信息
           - 添加删除相应内容
       - minidom
           - minidom.parse(filename):加载读取的xml文件，filename可以是XML代码
           - 
       
       - etree
       
- XML文件写入
       - 更改
          - ele.set:修改属性
          - ele.append:添加子元素
          - ele.remove:删除元素
       - 生成创建
          - SubElement
          - 案例v01.py
  
  
  
       
# json
- 参考文件
      - http://www.sojson.com/
      - http://www.w3school.com.cn/json/
      - http://www.runoob.com/json/json-tutorial.html
      
- JSON(java script object notation)
- 轻量级的数据交换格式，基于ECMAScript
- json格式是一个键值对形式的数据集
      - key:字符串
      - value：字符串，数字，列表，json
      - json使用大括号包裹
      - 键值对直接用逗号隔开
          student={
            "name"："liudana",
            "age":18,
            "mobile":1552485452
          }
          
- json和python格式的对应
      - 字符串：字符串
      - 数字：数字
      - 队列：list
      - 对象：dict
      - 布尔值：布尔值(True大写)
- python for json
      - json包
      - json和python对象的转换
         - json.dumps():对数据编码，把python格式转换成json格式
         - json.loads():对数据解码，把json格式转换成python格式
      - python读取json文件
         - json.dump():把内容写入文件
         - json.load():把json文件内容读入python
         - 案例02.py
         - 案例03.py读取文件
      
      
      
      
      