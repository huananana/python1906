# jQuery

### 1.jQuery����

> jQuery���ʾ���һ����js��װ�Ŀ⣬�����װ�˺ܶ෽���Ͷ�������ҳ��������
>
> jQuery��ͨ��jQuery�������ṩ����



### 2.��ô����jQuery

1)���ص��� - ����jQuery����

2)Զ������ - `<script type="text/javascript" src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></script>`



### 3.ʹ��jQuery

```html
1.��ȡ�ڵ�
1)Ԫ��/id/���/Ⱥ��ѡ����
	$('div')
	$('#div1')
	$('#div1>p')
2)����ѡ����
	$('p+a') - a��ǩ(������p�����a��ǩ)
	$('#p1~*') - p1����(����)���ֵܱ�ǩ
	$('p:first') - ��һ��p��ǩ(last���һ��p��ǩ)
	$('div *:forst-child') - ����div�ĵ�һ���ӱ�ǩ(last-child���һ���ӱ�ǩ)
```
	2.�ڵ����
	1)�����ڵ�
		$('<p>��������</p>') - HTML����
	
	2)��ӽڵ�
		$().append() - ��jQuery�����е�������
		$().prepend() - ��jQuery�����е���ǰ���
		$().before() - ��jQuery�����ǰ�����
		$().after() - ��jQuery����ĺ������
	
	3)ɾ���ڵ�
		$().remove() - ɾ��jQuery����
		$().empty() - ɾ��jQuery����������ӽڵ�
	
	4.�����ڵ�
		$().clone(true/false) - ��ǳ����(������jQuery�е��¼�)
	1.��������
		$().text() - ��ȡ��ǩ����(��Ӳ���:'�޸�ֵ')
		$().html() - ��ȡ��ǩ����(��Ӳ���:'�޸�ֵ')
		$().val() - ��ȡvalueֵ(��Ӳ���:'�޸�ֵ')
	
		$().addClass('class') - ���class����
		$().removeClass('class') - ɾ��class����
	
	2.��ʽ����(CSS)
		$().css() - ��ȡ/������ʽ����ֵ(����:'�޸�ֵ')
		$().css({
			css���� - ���Ը�ΪCSS���շ�ʽ����(�����ſ�������ʹ��)
		})
	
	3.��ͨ����
		$('ѡ����').attr('����', '����ֵ') - ��ȡ/�޸�����ֵ(����:'������', 'ֵ')
		
	1.�¼���
		$().on('�¼�', function(){
			# �¼�����Ҫ:this,��js���͵��¼�Դ
		})
		
		$().on('�¼�', 'ѡ�����µı�ǩ����', function(){
			# �¼����԰��µı�ǩ
		})
	
	2.�¼�����
		evt.stopPropagation()  # ����ǩ��Ƕ���ӱ�ǩʱ���ӱ�ǩʱ������ӱ�ǩ�ķ�Χ���ᴥ������ǩ�ĵ���¼�
### 3.Ajaxʹ��

1.ʲô��Ajax

> asynchronization - JavaScript - xml(�첽js)
>
> Ajax����jQuery��װ��ר��������http�������ط�������python�еĵ�������requests�Ĺ���һ��

```
��ܣ�
$.ajax({
			 	url:���ݽӿڵ�ַ,
			 	type:����ʽ(get/post),
			 	data:��������/����(�ͻ��˴��ݸ�������������, ֵ�Ƕ���),
			 	success:����ɹ��Ļص�����(����),
			 	error:����ʧ�ܵĻص�����
			 })
```

ʵ����



```html
<script type="text/javascript">
	$.ajax({
        type:"get",
        url:"http://rap2api.taobao.org/app/mock/233723/shopping",
        data:{username:'С��', password:'123456'},
        success:function(result){
            console.log('����ɹ���')
            console.log(result)
            for(var goods of result.data){
                var name = goods.name
                $('#box').append($('<p>'+name+'</p>'))
                $('#box').append($('<img src="'+goods.goods_image+'" />'))

            }
        },
        error: function(){
            console.log('����ʧ��')
        }
    });
</script>

<--> ��һ�ַ�����</-->
<scipt type="text/javascript">
	$.get("http://rap2api.taobao.org/app/mock/233723/shopping", {username:'С��', password:'123456'}, function(result){	
		console.log('=====:', result)
	})
</scipt>
```