# 1.��֧�ṹ - if���
:<<EOF
�﷨1��if
if �������
then
        ��������ִ�еĴ����
fi

�﷨2��if-else
if �������
then
        ��������ִ�еĴ����
else
        ����������ִ�еĴ����
fi

�﷨3��if-elif-else
if �������1
then
        ��������1ִ�еĴ���
elif �������2
then
        ��������2ִ�еĴ���
elif �������3
then
        ��������3ִ�еĴ���
...
else
        ����������������ִ�еĴ���
fi
EOF

printf ���������䣺
read age
if [ $age -lt 12 ]
then
        echo ��ͯ
elif [ $age -le 18 ]
then
        echo ����
elif [ $age -le 28 ]
then
        echo ����
elif [ $age -le 50 ]
then
        echo ׳��
else
        echo ����
fi

echo ====================forѭ��=======================
# 2.forѭ��
:<<EOF
�﷨��
for ���� in ����
do
        ѭ����
done
EOF

# �������ֵ
for char in "hello world��" 100 'abc'
do
        echo char:$char
done

#��������       -       forѭ����Ҫ���ڱ�������
names=(С�� С�� С�� tom bob)
for item in ${names[*]}
do
        echo name:$item
done

# 3.whileѭ��
:<<EOF
�﷨��
while �������
do
        ѭ����
done
EOF
string='hello world!'
len=${#string}
index=0
while [ $index -lt $len ]
do
        echo string:${string:$index:1}
        index=`expr $index + 1`
done

#��ϰ����100�ۼ�
index=0
num=1
while [ $indef -lt 101 ]
do
        num=`expr $sum + $num`
        index=`expr $num + 1`
done
echo num:$num
