本项目用于测试downloadMiddleWare的process_request函数返回不同的对象的处理逻辑。
具体结论如下：
在process_request中当返回None的时候，则该request将继续处理下去。
如果返回Request，则会彻底终止本次Request的执行，同时重新调度新的Request的执行。
如果返回Response，则会执行相应的所有的process_response函数。优先级比该middleware低的process_response也会被执行。(对应downloadmiddlwware2中的process_response)
