# LOG
- https://www.cnblogs.com/yyds/p/6901864.html
- logging模块提供模块级别的函数记录日志
- 包括四大组件

## 1.日志相关概念
- 日志
- 日志的级别（level）
      - 不同的用户关注不同的程序信息
      - debug
      - info
      - notice
      - warning
      - error
      - critical
      - alert
      - emergency
- IO操作=>不要频繁操作
- LOG的作用
      - 调试
      - 了解软件的运行操作
      - 分析定位问题
- 日志信息
      - time
      - 地点
      - level
      - 内容
- 成熟的第三方日志
      - log4j
      - log4php
      - logging
      
## 2.logging模块
- 日志级别
      - 级别自定义(级别严重程度自上而下增加)
      - debug
      - info
      - warning
      - error
      - critical
- 初始化/写日志实例需要指定级别，只有当级别等于或者高于指定级别的时候，才会被记录
- 使用方式
      - 直接使用logging(封装了其他组件)
      - logging四大组件直接定制
      
## 2.1 logging模块级别的日志
- 使用以下几个函数
      - logging.debug(msg,*args,**kwargs)   创建一条严重级别为DEBUG的日志记录
      - logging.info(msg,*args,**kwargs)   创建一条严重级别为INFO的日志记录
      - logging.warning(msg,*args,**kwargs)   创建一条严重级别为WARNING的日志记录
      - logging.error(msg,*args,**kwargs)   创建一条严重级别为ERROR的日志记录
      - logging.critical(msg,*args,**kwargs)   创建一条严重级别为CRITICAL的日志记录
      - logging.log(level,*args,**kwargs)   创建一条严重级别LEVEL的日志记录
      - logging.basicConfig(**kwargs)  对root logger进行一次性配置
- logging.basicConfig(**kwargs)   对rootlogger进行一次性配置
      - 只在第一次调用的时候起作用
      - 不配置logger则使用默认值
            - 输出：sys.stderr(标准错误输出)
            - 级别：WARNING(低于WARNING级别的都不显示，过滤掉了)
            - 格式：level:log_name:content
      - 案例01
      - format参数(自行csdn)
      
## 2.2 logging模块的处理流程
- 四大组件
      - 日志器(Logger):产生日志的接口
      - 处理器(Handler):把产生的日志发送到相应的目的地
      - 过滤器(Filter)：更精细的控制那些日志的输出
      - 格式器(Formatter):对输出的信息进行格式化
      
- Logger
      - 产生日志
      - 操作
           Logger.setLevel()  设置日志器将会处理的日志消息的最低严重级别
           Logger.addHandle()和Logger.removeHandle() 为该日志对象添加/删除一个日志
           Logger.addFilter()和Logger.removeFilter() 为该日志添加/删除一个FILTER
           Logger.debug 产生一条debug级别的日志，同理info，warning等
           Logger.exception()  创建类似于Logging.error的日志消息
           Logger.log()  获取一个明确的日志level参数类创建一个日志记录
      - 如何得到一个logger对象
           - 实例化
           - logger.getLogger()
           
- Handler
      - 把log发送到指定位置
      - 方法
           - setLevel
           - setFormat
           - addFilter,removeFilter
      - handler是基类，不需要直接使用
- Format类
      - 直接实例化
      - 可以继承Format添加特殊内容
      - 三个参数 
          - fmt:指定消息格式化字符串
          - datefmt：指定日期格式字符串
          - style
          
- Filter类
      - 
      
      
- 综合题  见pad截屏 all_log等(较重要)