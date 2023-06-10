node {
   def commit_id
   stage('Preparation') {
     checkout scm
   }
   
   stage('sonar-scanner') {
      def sonarqubeScannerHome = tool name: 'sonar', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
      withCredentials([string(credentialsId: 'sonar', variable: 'sonarLogin')]) {
        sh "${sonarqubeScannerHome}/bin/sonar-scanner -e -Dsonar.host.url=http://localhost:9000 -Dsonar.login=${sonarLogin} -Dsonar.projectName=flask-app -Dsonar.projectVersion=${env.BUILD_NUMBER} -Dsonar.projectKey=GS -Dsonar.sources=construct/  -Dsonar.language=python "
      }
   }
   
   stage('docker build/push') {
     docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
      def BUILD_DATE = $(date +%F-%T)
      def app = docker.build("sdousman/constructify:latest-jenkins-image-$(BUILD_DATE)", '.').push()
       
     }
   }
}
