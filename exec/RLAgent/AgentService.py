from AgentDriving import AgentDriving 
import requests
import json
import os
import sys

class AgentService():

    agent = AgentDriving()

    def networkService(self):
        url = "http://52.78.63.210:8008/darknet"
        res = requests.get(url)
        json_data = res.json()
        return json_data

    def findObjectRequest(self, obj):
        url = "http://52.78.63.210:8008/darknet/find" 
        param = {'target':obj}
        res = requests.get(url,param)
        print(res)

    def imgIdentifier(self):

        while True:

    	    # send img 
            os.system('scp -i /home/animo02/secret/soptAMSKey.pem /var/lib/motion/lastsnap.jpg ubuntu@52.78.63.210:/home/ubuntu/CNN/motion')

            # rm files
            os.system('sudo rm -rf /var/lib/motion/01-*.jpg | sudo rm -rf /var/lib/motion/*.avi')

            result = self.networkService()
            value = result['code']

            if value == 0:
                self.agent.stop()
                print("=======Find Object!========")
                return 
            elif value == -1:
                print("Network Service err")


    def mainService(self, obj):
	# auto agent playing exec
        self.agent.start()

        # notify to server what i want to find
        self.findObjectRequest(obj)

	# motion start
        os.system('sudo service motion start')

	# networkService with darknet, scp, stop agent
        self.imgIdentifier()

        # motion stop
        os.system('sudo service motion stop')


if __name__ == "__main__":
#    agent = AgentDriving()
#    agent.start()
    obj = sys.argv[1]
    print ("object = "+obj)

    agentService = AgentService()
    agentService.mainService(obj)
