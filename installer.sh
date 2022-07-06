curl https://dlcdn.apache.org/kafka/3.2.0/kafka_2.12-3.2.0.tgz -o ~/Downloads/kafka.tgz
mkdir -p ~/Downloads/kafka/
cd ~/Downloads/kafka
tar -xvzf ~/Downloads/kafka.tgz --strip 1
ls
ls -la
bin/zookeeper-server-start.sh config/zookeeper.properties