node {
   def commit_id
   stage('Preparation') {
     checkout scm
   }
   
   
   stage('docker build/push') {
     docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
       def app = docker.build("sdousman/constructify:latest-jenkins", '.').push()
       
     }
   }
}
