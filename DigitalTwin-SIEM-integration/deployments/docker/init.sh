chown root $(find conf/filebeat/ conf/filebeat-es/ -name "*.yml")

echo -n "Enter the Hostname or IP Address where your elasticsearch will be deployed:"
read ip
echo "HOST_IP=$ip" > .env

docker-compose up -d

/bin/bash kbndashboard-import.sh localhost ../kibana/dashboard-siem.json
