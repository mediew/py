# xpath语法  
!['实例1'](https://raw.githubusercontent.com/mediew/pic/master/20200824114941.png)  
如上图，美国不在标签内，可以用xpath定位  
//span[./text()="制片国家/地区:"]/following::text()[1]  
> span为标签名，[]内为属性，  
