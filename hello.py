pipeline{
    agent any
    stages{
        stage('version'){
            steps{
                sh 'python3 --version'
            }
        }
        stage('hello uni'){
            steps{
                sh 'python3 hello.py'
            }
        }
    }
}
