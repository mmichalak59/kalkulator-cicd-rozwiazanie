pipeline {
    agent any

    options {
        timeout(time: 20, unit: 'MINUTES')
    }

    environment {
        APLIKACJA = 'NarzedziaTextowe'
        WERSJA    = '1.0.0'
    }

    parameters {
        choice(
            name: 'SRODOWISKO',
            choices: ['dev', 'staging', 'prod'],
            description: 'Srodowisko docelowe'
        )
    }

    stages {
        stage('Info') {
            steps {
                echo "${env.APLIKACJA} v${env.WERSJA}"
                echo "Build: ${env.BUILD_NUMBER}"
                echo "Galaz: ${env.GIT_BRANCH}"
                echo "Srodowisko: ${params.SRODOWISKO}"
            }
        }
        stage('Instalacja zaleznosci') {
            steps {
                sh 'pip3 install -r requirements.txt --quiet'
            }
        }
        stage('Testy') {
            when {
                expression { env.GIT_BRANCH != 'origin/main' }
            }
            steps {
                sh 'python3 test_app.py'
            }
        }
        stage('Analiza jakosci') {
            parallel {
                stage('Sprawdzenie plikow') {
                    steps {
                        sh 'test -f app.py && test -f test_app.py && test -f tools.py'
                        echo 'Wymagane pliki istnieja.'
                    }
                }
                stage('Skanowanie zaleznosci') {
                    steps {
                        echo 'Skanowanie zaleznosci...'
                        sh 'pip3 show flask | grep Version'
                    }
                }
            }
        }
        stage('Wdrozenie DEV') {
            when {
                expression { params.SRODOWISKO == 'dev' }
            }
            steps {
                echo "Wdrazam ${env.APLIKACJA} v${env.WERSJA} na DEV..."
            }
        }
        stage('Zatwierdzenie') {
            when {
                expression { params.SRODOWISKO == 'prod' }
            }
            options {
                timeout(time: 5, unit: 'MINUTES')
            }
            steps {
                input message: "Wdrozyc ${env.APLIKACJA} v${env.WERSJA} na PRODUKCJE?",
                      ok: 'Tak, wdrazaj!'
            }
        }
        stage('Wdrozenie PROD') {
            when {
                expression { params.SRODOWISKO == 'prod' }
            }
            steps {
                echo "Wdrazam ${env.APLIKACJA} v${env.WERSJA} na PRODUKCJE!"
            }
        }
        stage('Uruchom aplikacje') {
            steps {
                sh 'pkill -f "python3 app.py" || true'
                sh 'JENKINS_NODE_COOKIE=dontKillMe nohup python3 app.py > app.log 2>&1 &'
                sh 'sleep 3 && curl -sf http://localhost:5000/'
                echo 'Aplikacja dziala na porcie 5000'
            }
        }
    }

    post {
        success {
            echo "Build ${env.BUILD_NUMBER}: ${env.APLIKACJA} wdrozony na ${params.SRODOWISKO}."
        }
        failure {
            echo "BLAD w buildzie ${env.BUILD_NUMBER} — sprawdz logi."
        }
        always {
            echo "Pipeline zakonczona (build ${env.BUILD_NUMBER})."
        }
    }
}
