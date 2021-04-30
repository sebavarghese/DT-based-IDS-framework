clean: 
	sudo mn -c
	sudo rm -rf DigitalTwin-SIEM-integration/src/logs/p*
	sudo rm -rf DigitalTwin-SIEM-integration/src/logs/m*
	sudo rm -rf DigitalTwin-SIEM-integration/src/logs/e*
	sudo rm -rf DigitalTwin-SIEM-integration/src/logs/u*
	sudo rm -rf DigitalTwin-SIEM-integration/src/logs/h*
	sudo rm -rf DigitalTwin-SIEM-integration/src/logs/d*
	sudo rm -rf DigitalTwin-SIEM-integration/src/pcaps
	sudo rm -rf DigitalTwin-SIEM-integration/src/trigger.txt
