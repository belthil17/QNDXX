#将需要的代码复制并cd到severless文件夹
echo "开始拷贝必要文件"
sudo cp main.py ./serverless
sudo cp requirements.txt ./serverless
sudo cp cookie.txt ./serverless
cd ./serverless

#安装云函数需要的依赖库到severless文件夹
echo "开始安装所需模块"
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r ./requirements.txt -t ./

#部署至腾讯云函数
sed -i "s/.\/log.txt/..\/..\/tmp\/log.txt/g" ./main.py
echo "开始安装腾讯ServerlessFramework"
npm install -g serverless --registry=https://registry.npm.taobao.org
echo "开始部署至腾讯云函数"
sls deploy --debug

#清空文件复制的文件
echo "清空所拷贝的代码"
rm -f ./main.py
rm -f ./requirements.txt
rm -f ./cookie.txt
exit 0
