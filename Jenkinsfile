node {
   def commit_id
   stage('Preparation') {
     checkout scm
                            
     commit_id = "jasjubadsojufbdsfb"
   }
   
   }
   stage('docker build/push') {
     docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
       def app = docker.build("sdousman/constructify:${commit_id}", '.').push()
       
     }
   }
}