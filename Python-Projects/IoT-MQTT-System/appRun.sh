set -x
apkName="tmp-sub.py"
logPath="/xlog_mqtt"

[ ! -d "$logPath" ] && mkdir "$logPath"

cd  /x

ndt=$(date +%Y-%m-%d_%R:%S)

python3  $apkName  1>${logPath}/http_${ndt}.log   2>${logPath}/http_${ndt}.err

