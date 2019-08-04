pipeline{

    agent any

    stages{
        stage('SCM'){
            steps{
                echo 'SCM'
            }
        }

        stage('Dependencies'){
            steps{
                echo 'Install dependencies'
            }
        }

        stage('Test'){
            steps{
                echo 'Test'
            }
        }

        stage('Deploy'){
            steps{
                echo 'Test'
            }
        }

        stage('Email'){
            steps{
                emailext attachLog: true,
                    subject: "PIPELINE Completion ${currentBuild.result}",
                    body: "PIPELINE Completion body",
                    recipientProviders: [requestor()]
            }
        }
    }
}