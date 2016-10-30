# P4 CLI connector generator
# example: ./commandSenderGenerator.sh [JSON File] [Thrift port starting point] [Number of switches]

if [ "${1}" == "" ]; then
	echo "Please input the P4 Output JSON file"; exit 0 ;
elif [ "${2}" == "" ]; then
	echo "Please input the starting port of thrift port. "; exit 0 ;
elif [ "${3}" == "" ]; then
	echo "Please input the number of switch. "; exit 0 ;
fi
rm -rf ./commandSender;
mkdir ./commandSender;
for (( i=0; i<${3}; i=i+1 ))
do
	cp ./sample.sh ./commandSender/$((${2}+${i})).sh;
	echo "\$CLI_PATH "$1" "$((${2}+${i})) >> ./commandSender/$((${2}+${i})).sh;
done
