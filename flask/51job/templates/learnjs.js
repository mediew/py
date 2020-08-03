// 定义多个变量，中间用；隔开
var inum = 123;
var str = '123'
// 5种基本数据：number,string,bool,undifined,null,object
var obj={
    'name':'waang',
    'age':12
}
//查看数据类型
typeof(obj);
/*
* 多行注释内容
* js中 ++相当于python中+=1
* */
// 以下是一个有参数但无返回值的参数，若已经写return则函数执行结束，后面的语句无法执行
function fn(n1,n2){
    var res = n1+n2;
    alert(n1 + n2 + '的结果是' + res)
}
fn(1,2)
//数字和字符串比较时，JavaScript自动把字符串转换成数字类型
//要求数值和类型完全相同用===，并&&, 或||，！对结果进行取反
s=90
if (s<60){
    alert('及格')
}else if(s<80){
    alert('良好')
}else{
    alert('优秀')
}
/*
使用外链式js的方法：
<script>
    function fnload(){
    var op = document.getElementById('p1');
    alert(op);
    }
    window.onload = fnload();
</script>


*/